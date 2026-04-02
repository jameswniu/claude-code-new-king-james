"""AskUserQuestion tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "AskUserQuestion"
DESCRIPTION = """Ask the user questions during execution."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("AskUserQuestion tool execution requires runtime integration")
