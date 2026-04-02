"""Grep tool."""
from __future__ import annotations
import subprocess
from ..types.base import ToolResult

NAME = "Grep"
DESCRIPTION = "A powerful search tool built on ripgrep. Supports full regex syntax."

def grep(pattern: str, path: str = ".", glob_filter: str | None = None,
         output_mode: str = "files_with_matches", head_limit: int = 250,
         case_insensitive: bool = False) -> ToolResult:
    cmd = ["rg", pattern, path]
    if output_mode == "files_with_matches": cmd.append("-l")
    elif output_mode == "count": cmd.append("-c")
    if glob_filter: cmd.extend(["--glob", glob_filter])
    if case_insensitive: cmd.append("-i")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        lines = result.stdout.strip().split("\n")[:head_limit]
        return ToolResult(content="\n".join(lines))
    except FileNotFoundError:
        return ToolResult(content="ripgrep (rg) not found. Install it or use the bundled version.", is_error=True)
    except Exception as e:
        return ToolResult(content=str(e), is_error=True)
