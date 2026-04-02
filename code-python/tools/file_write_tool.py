"""File Write tool."""
from __future__ import annotations
from pathlib import Path
from ..types.base import ToolResult

NAME = "Write"
DESCRIPTION = "Writes a file to the local filesystem. Overwrites existing files. You MUST Read first before writing to an existing file."

def write_file(file_path: str, content: str) -> ToolResult:
    try:
        p = Path(file_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return ToolResult(content=f"Successfully wrote {len(content)} bytes to {file_path}")
    except Exception as e:
        return ToolResult(content=str(e), is_error=True)
