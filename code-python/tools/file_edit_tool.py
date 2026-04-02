"""File Edit tool."""
from __future__ import annotations
from pathlib import Path
from ..types.base import ToolResult

NAME = "Edit"
DESCRIPTION = "Performs exact string replacements in files. The edit will FAIL if old_string is not unique."

def edit_file(file_path: str, old_string: str, new_string: str, replace_all: bool = False) -> ToolResult:
    try:
        p = Path(file_path)
        if not p.exists(): return ToolResult(content=f"File not found: {file_path}", is_error=True)
        content = p.read_text()
        count = content.count(old_string)
        if count == 0: return ToolResult(content="old_string not found in file", is_error=True)
        if count > 1 and not replace_all:
            return ToolResult(content=f"old_string found {count} times. Use replace_all=True or provide more context.", is_error=True)
        new_content = content.replace(old_string, new_string) if replace_all else content.replace(old_string, new_string, 1)
        p.write_text(new_content)
        return ToolResult(content=f"Replaced {'all occurrences' if replace_all else '1 occurrence'} in {file_path}")
    except Exception as e:
        return ToolResult(content=str(e), is_error=True)
