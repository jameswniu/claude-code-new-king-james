"""Glob tool."""
from __future__ import annotations
from pathlib import Path
from ..types.base import ToolResult

NAME = "Glob"
DESCRIPTION = "Fast file pattern matching tool. Supports glob patterns like '**/*.js'."

def glob_files(pattern: str, path: str = ".") -> ToolResult:
    try:
        matches = sorted(Path(path).glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)
        return ToolResult(content="\n".join(str(m) for m in matches[:250]))
    except Exception as e:
        return ToolResult(content=str(e), is_error=True)
