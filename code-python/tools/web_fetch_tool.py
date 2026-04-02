"""WebFetch tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "WebFetch"
DESCRIPTION = """Fetches content from a URL, converts HTML to markdown, processes with AI."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("WebFetch tool execution requires runtime integration")
