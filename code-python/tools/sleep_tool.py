"""Sleep tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "Sleep"
DESCRIPTION = """Pause execution for a specified duration."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("Sleep tool execution requires runtime integration")
