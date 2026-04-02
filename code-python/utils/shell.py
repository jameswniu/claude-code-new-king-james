"""Shell command parsing."""
from __future__ import annotations
import shlex
from typing import Optional

SHELL_OPERATORS = {"&&", "||", ";", ";;", "|", ">&", ">", ">>"}

def split_commands(command: str) -> list[str]:
    """Split a compound shell command into individual commands."""
    parts = []
    current = []
    try:
        tokens = shlex.split(command)
    except ValueError:
        return [command]
    for token in tokens:
        if token in SHELL_OPERATORS:
            if current: parts.append(" ".join(current))
            current = []
        else:
            current.append(token)
    if current: parts.append(" ".join(current))
    return parts

def get_base_command(command: str) -> Optional[str]:
    """Extract the base command (first word) from a command string."""
    stripped = command.strip()
    if not stripped: return None
    return stripped.split()[0]
