"""Core types."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Literal, Optional, Protocol, runtime_checkable

@dataclass
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_creation_input_tokens: int = 0
    cache_read_input_tokens: int = 0
    server_tool_use: Optional[dict] = None
    service_tier: Optional[str] = None

@dataclass
class ToolResult:
    type: Literal["tool_result"] = "tool_result"
    tool_use_id: str = ""
    content: str = ""
    is_error: bool = False

@dataclass
class ToolUseContext:
    options: dict = field(default_factory=dict)
    messages: list = field(default_factory=list)

@runtime_checkable
class Tool(Protocol):
    name: str
    description: str
    async def call(self, input: dict, context: ToolUseContext) -> ToolResult: ...

@dataclass
class AgentDefinition:
    agent_type: str
    when_to_use: str
    model: str = "inherit"
    tools: list[str] = field(default_factory=lambda: ["*"])
    disallowed_tools: list[str] = field(default_factory=list)
    source: str = "built-in"
    omit_claude_md: bool = False
    def get_system_prompt(self, **kwargs) -> str: return ""
