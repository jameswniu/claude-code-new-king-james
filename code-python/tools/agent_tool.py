"""Agent tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "Agent"
DESCRIPTION = """Launch a new agent to handle complex, multi-step tasks autonomously."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("Agent tool execution requires runtime integration")
