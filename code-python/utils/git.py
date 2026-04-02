"""Git operations."""
from __future__ import annotations
import subprocess
from pathlib import Path
from typing import Optional

def is_git_repo(path: str = ".") -> bool:
    return (Path(path) / ".git").exists()

def get_branch(path: str = ".") -> Optional[str]:
    try:
        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, cwd=path)
        return result.stdout.strip() or None
    except: return None

def get_default_branch(path: str = ".") -> str:
    for name in ["main", "master", "dev"]:
        result = subprocess.run(["git", "show-ref", f"refs/heads/{name}"], capture_output=True, cwd=path)
        if result.returncode == 0: return name
    return "main"
