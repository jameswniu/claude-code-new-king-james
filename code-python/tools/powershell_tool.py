"""PowerShell tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "PowerShell"
DESCRIPTION = """Execute PowerShell commands on Windows."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("PowerShell tool execution requires runtime integration")
