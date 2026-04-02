"""NotebookEdit tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "NotebookEdit"
DESCRIPTION = """Edit Jupyter notebook cells."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("NotebookEdit tool execution requires runtime integration")
