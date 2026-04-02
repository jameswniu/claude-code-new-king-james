# Chapter 27: Worktree Tools

Two tools manage git worktree isolation: EnterWorktree and ExitWorktree.

**EnterWorktree** creates an isolated git worktree inside the ".claude/worktrees/" directory with a new branch based on the current HEAD. This gives the agent an isolated copy of the repository where it can make changes without affecting the user's working directory. The tool is only used when the user explicitly requests worktree isolation.

**ExitWorktree** leaves the worktree. It offers two actions:

- **"keep"**: leaves the worktree on disk so the user can review or continue with its changes later
- **"remove"**: deletes the worktree and its associated branch entirely

Worktrees are particularly useful for Agent tool invocations where the sub-agent needs to make experimental changes without risking conflicts with the parent session's working directory. They provide a form of filesystem-level isolation that complements the sandbox enforcement described in Chapter 16.
