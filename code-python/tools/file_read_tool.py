"""File Read tool."""
from __future__ import annotations
from pathlib import Path
from ..types.base import ToolResult

NAME = "Read"
DEFAULT_LINE_LIMIT = 2000
DESCRIPTION = """Reads a file from the local filesystem. The file_path parameter must be an absolute path.
By default reads up to 2000 lines. Can read images, PDFs, and Jupyter notebooks."""

def read_file(file_path: str, offset: int = 0, limit: int = DEFAULT_LINE_LIMIT) -> ToolResult:
    try:
        p = Path(file_path)
        if not p.exists(): return ToolResult(content=f"File not found: {file_path}", is_error=True)
        lines = p.read_text().splitlines()
        selected = lines[offset:offset + limit]
        numbered = [f"{i + offset + 1}\t{line}" for i, line in enumerate(selected)]
        return ToolResult(content="\n".join(numbered))
    except Exception as e:
        return ToolResult(content=str(e), is_error=True)
