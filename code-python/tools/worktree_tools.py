"""Worktree tools."""
from ..types.base import ToolResult
ENTER_NAME = "EnterWorktree"
EXIT_NAME = "ExitWorktree"
ENTER_DESCRIPTION = """Use this tool ONLY when the user explicitly asks to work in a worktree.
Creates an isolated git worktree inside .claude/worktrees/ with a new branch based on HEAD."""
EXIT_DESCRIPTION = """Exit a worktree. Actions: "keep" (leave on disk) or "remove" (delete worktree and branch)."""
