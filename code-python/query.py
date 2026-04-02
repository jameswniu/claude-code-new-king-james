"""
Main query loop — streams an assistant turn, dispatches tool calls,
handles compaction, token budget, and max-output recovery.


Claude Code: send messages to the API, execute tools, append results,
and repeat until the model emits end_turn or a budget is exhausted.
"""

from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field
from typing import Any, AsyncGenerator, Callable, Dict, List, Optional, Sequence

from claude_code.tool import Tool, ToolResult, ToolUseContext, Tools, find_tool_by_name
from claude_code.types.messages import (
    AssistantMessage,
    Message,
    UserMessage,
    create_assistant_message,
    create_user_interruption_message,
    create_user_message,
)

logger = logging.getLogger(__name__)

MAX_OUTPUT_TOKENS_RECOVERY_LIMIT = 3
PROMPT_TOO_LONG_ERROR_MESSAGE = "Prompt is too long"


@dataclass
class QueryParams:
    """Parameters for a query loop invocation."""
    messages: List[Message]
    system_prompt: List[str]
    user_context: Dict[str, str]
    system_context: Dict[str, str]
    tool_use_context: ToolUseContext
    query_source: str = "repl"
    fallback_model: Optional[str] = None
    max_output_tokens_override: Optional[int] = None
    max_turns: Optional[int] = None
    skip_cache_write: bool = False
    task_budget: Optional[Dict[str, int]] = None


@dataclass
class QueryConfig:
    """Resolved configuration for a single query loop run."""
    model: str = ""
    max_output_tokens: int = 32_000
    thinking_budget: Optional[int] = None
    stop_sequences: Optional[List[str]] = None


def build_query_config(params: QueryParams) -> QueryConfig:
    """Build the resolved query configuration from params + runtime state."""
    ctx = params.tool_use_context
    model = ctx.main_loop_model or "claude-sonnet-4-6"
    return QueryConfig(
        model=model,
        max_output_tokens=params.max_output_tokens_override or 32_000,
    )


def _yield_missing_tool_result_blocks(
    assistant_messages: List[AssistantMessage],
    error_message: str,
) -> List[UserMessage]:
    """For each tool_use in the assistant turn, emit a tool_result with an error."""
    results: List[UserMessage] = []
    for am in assistant_messages:
        content = am.message.get("content", [])
        tool_uses = [b for b in content if isinstance(b, dict) and b.get("type") == "tool_use"]
        for tu in tool_uses:
            results.append(
                create_user_interruption_message(
                    tool_use_id=tu["id"],
                    error_message=error_message,
                    source_tool_assistant_uuid=am.uuid,
                )
            )
    return results


async def _execute_tool(
    tool: Tool,
    tool_input: Dict[str, Any],
    tool_use_id: str,
    context: ToolUseContext,
) -> ToolResult:
    """Call a single tool with its input, handling errors gracefully."""
    try:
        result = tool.call(tool_input, context)
        if asyncio.iscoroutine(result):
            result = await result
        return result
    except Exception as exc:
        logger.error("Tool %s raised: %s", tool.name, exc)
        return ToolResult(data=f"Error: {exc}")


async def _run_tools(
    tool_uses: List[Dict[str, Any]],
    context: ToolUseContext,
    tools: Tools,
) -> List[UserMessage]:
    """Execute all tool_use blocks from the assistant turn and return tool_result messages."""
    result_messages: List[UserMessage] = []

    for tu in tool_uses:
        tool_name = tu.get("name", "")
        tool_input = tu.get("input", {})
        tool_use_id = tu.get("id", "")

        tool = find_tool_by_name(tools, tool_name)
        if tool is None:
            result_messages.append(
                create_user_message(
                    content=[
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use_id,
                            "content": f"Error: Unknown tool '{tool_name}'",
                            "is_error": True,
                        }
                    ],
                    tool_use_result=f"Error: Unknown tool '{tool_name}'",
                )
            )
            continue

        result = await _execute_tool(tool, tool_input, tool_use_id, context)
        content_text = str(result.data) if result.data is not None else ""

        result_messages.append(
            create_user_message(
                content=[
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_use_id,
                        "content": content_text,
                    }
                ],
                tool_use_result=content_text,
            )
        )

        # If the tool produced extra messages, append them
        if result.new_messages:
            result_messages.extend(result.new_messages)

    return result_messages


async def query(params: QueryParams) -> AsyncGenerator[Message, None]:
    """
    Run the agentic query loop.

    Yields Message objects as they are produced (assistant text, tool results,
    system messages, errors).  The loop continues until:
    - The model emits ``end_turn``
    - A max-turns limit is reached
    - A budget is exhausted
    - An unrecoverable error occurs

    This is an async generator so callers can stream output incrementally.
    """
    from claude_code.services.api_client import stream_message

    config = build_query_config(params)
    messages = list(params.messages)
    context = params.tool_use_context
    tools = context.tools or []
    turn = 0
    max_turns = params.max_turns or 200
    max_output_recovery = 0

    while turn < max_turns:
        turn += 1
        start = time.monotonic()

        # ----- Call the API -----
        try:
            assistant_msg = await stream_message(
                model=config.model,
                messages=messages,
                system_prompt=params.system_prompt,
                tools=tools,
                max_tokens=config.max_output_tokens,
            )
        except Exception as api_err:
            err_text = str(api_err)
            # Prompt-too-long recovery
            if PROMPT_TOO_LONG_ERROR_MESSAGE.lower() in err_text.lower():
                logger.warning("Prompt too long — attempting compaction")
                error_msg = create_assistant_message(
                    content=[{"type": "text", "text": f"API Error: {err_text}"}],
                )
                error_msg.is_api_error_message = True
                yield error_msg
                return
            # Generic API error
            error_msg = create_assistant_message(
                content=[{"type": "text", "text": f"API Error: {err_text}"}],
            )
            error_msg.is_api_error_message = True
            yield error_msg
            return

        elapsed_ms = (time.monotonic() - start) * 1000
        assistant_msg.duration_ms = elapsed_ms
        messages.append(assistant_msg)
        yield assistant_msg

        # ----- Check stop reason -----
        stop_reason = assistant_msg.api_error or _get_stop_reason(assistant_msg)

        if stop_reason == "end_turn":
            return

        if stop_reason == "max_output_tokens":
            max_output_recovery += 1
            if max_output_recovery > MAX_OUTPUT_TOKENS_RECOVERY_LIMIT:
                return
            # Ask the model to continue
            messages.append(
                create_user_message(
                    content=[{"type": "text", "text": "Please continue from where you left off."}]
                )
            )
            continue

        # ----- Dispatch tool calls -----
        content = assistant_msg.message.get("content", [])
        tool_uses = [b for b in content if isinstance(b, dict) and b.get("type") == "tool_use"]

        if not tool_uses:
            # No tool calls and not end_turn — done
            return

        tool_result_msgs = await _run_tools(tool_uses, context, tools)
        for msg in tool_result_msgs:
            messages.append(msg)
            yield msg

    logger.warning("Max turns (%d) reached", max_turns)


def _get_stop_reason(msg: AssistantMessage) -> str:
    """Extract the stop_reason from an assistant message's metadata."""
    # The streaming layer attaches stop_reason as a top-level field
    return getattr(msg, "stop_reason", "") or msg.message.get("stop_reason", "")
