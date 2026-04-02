# Chapter 17: Tool Registry

The tool registry is the central catalog of all tools available to the agent. It contains thirty-eight built-in tools, each conforming to the tool contract described in Chapter 06. The complete list of registered tool names is:

1. Bash
2. Read
3. Write
4. Edit
5. Glob
6. Grep
7. Agent
8. WebFetch
9. WebSearch
10. Skill
11. ToolSearch
12. PowerShell
13. NotebookEdit
14. TaskCreate
15. TaskGet
16. TaskList
17. TaskUpdate
18. TaskOutput
19. TaskStop
20. AskUserQuestion
21. EnterPlanMode
22. ExitPlanMode
23. SendMessage
24. SendUserMessage
25. TodoWrite
26. Sleep
27. REPL
28. LSP
29. RemoteTrigger
30. EnterWorktree
31. ExitWorktree
32. ListMcpResourcesTool
33. SandboxNetworkAccess
34. TeamCreate
35. TeamDelete
36. CronCreate
37. CronDelete
38. CronList

These tools span several categories:

- **File operations**: Read, Write, Edit, Glob, Grep
- **Shell execution**: Bash, PowerShell
- **Sub-agent management**: Agent, SendMessage, SendUserMessage, TeamCreate, TeamDelete
- **Task tracking**: TaskCreate, TaskGet, TaskList, TaskUpdate, TaskOutput, TaskStop, TodoWrite
- **Planning**: EnterPlanMode, ExitPlanMode
- **Web access**: WebFetch, WebSearch
- **Scheduling**: CronCreate, CronDelete, CronList
- **Environment isolation**: EnterWorktree, ExitWorktree, SandboxNetworkAccess
- **Discovery**: ToolSearch, ListMcpResourcesTool, Skill
- **Development**: LSP, NotebookEdit, REPL
- **Remote**: RemoteTrigger
- **Interaction**: AskUserQuestion, Sleep

Not all tools are loaded into the initial system prompt. Many are deferred and loaded on demand through the ToolSearch mechanism, which keeps the initial prompt compact.
