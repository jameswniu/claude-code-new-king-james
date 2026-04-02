"""ToolSearch tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "ToolSearch"
DESCRIPTION = """Fetch full schema definitions for deferred tools."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("ToolSearch tool execution requires runtime integration")
