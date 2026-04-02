"""Context management."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

@dataclass
class WorkspaceContext:
    cwd: Path = field(default_factory=Path.cwd)
    additional_dirs: list[Path] = field(default_factory=list)
    is_git_repo: bool = False
    git_branch: Optional[str] = None
    project_dir: Optional[Path] = None

    @classmethod
    def from_cwd(cls) -> "WorkspaceContext":
        cwd = Path.cwd()
        git_dir = cwd / ".git"
        return cls(cwd=cwd, is_git_repo=git_dir.exists())
