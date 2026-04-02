"""LSP tool."""
from __future__ import annotations
from ..types.base import ToolResult, ToolUseContext

NAME = "LSP"
DESCRIPTION = """Interact with Language Server Protocol servers (goToDefinition, findReferences, hover, documentSymbol, workspaceSymbol, goToImplementation, prepareCallHierarchy, incomingCalls, outgoingCalls)."""

async def call(input: dict, context: ToolUseContext) -> ToolResult:
    raise NotImplementedError("LSP tool execution requires runtime integration")
