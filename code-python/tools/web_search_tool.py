"""WebSearch tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "WebSearch"
DESCRIPTION = """Performs a web search and returns results."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("WebSearch tool execution requires runtime integration")
