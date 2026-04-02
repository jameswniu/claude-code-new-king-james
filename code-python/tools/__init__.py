"""Tool registry. All 38 tools from Claude Code."""
from typing import Type
TOOL_NAMES = [
    "Bash","Read","Write","Edit","Glob","Grep","Agent","WebFetch","WebSearch",
    "Skill","ToolSearch","PowerShell","NotebookEdit","TaskCreate","TaskGet",
    "TaskList","TaskUpdate","TaskOutput","TaskStop","AskUserQuestion",
    "EnterPlanMode","ExitPlanMode","SendMessage","SendUserMessage","TodoWrite",
    "Sleep","REPL","LSP","RemoteTrigger","EnterWorktree","ExitWorktree",
    "ListMcpResourcesTool","SandboxNetworkAccess","TeamCreate","TeamDelete",
    "CronCreate","CronDelete","CronList",
]
