"""Skill tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "Skill"
DESCRIPTION = """Execute a skill within the main conversation."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("Skill tool execution requires runtime integration")
