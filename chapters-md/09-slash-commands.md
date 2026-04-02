# Chapter 09: Slash Commands

The slash command system provides a set of user-invocable actions that are triggered by typing a forward slash followed by the command name. The system surfaces forty-two primary commands.

The recognized commands are, in alphabetical order:

1. **add-dir** - Adds an additional directory to the workspace scope
2. **advisor** - Engages an advisory mode for reviewing decisions
3. **agents** - Lists or manages sub-agents
4. **branch** - Creates or switches git branches
5. **clear** - Clears the conversation history
6. **commit** - Creates a git commit from staged changes
7. **compact** - Manually triggers context compaction
8. **config** - Views or modifies configuration settings
9. **cost** - Displays the current session's token usage and cost
10. **desktop** - Manages the desktop application connection
11. **diff** - Shows git diff output
12. **doctor** - Runs diagnostics on the Claude Code installation
13. **effort** - Adjusts the reasoning effort level
14. **exit** - Ends the current session
15. **extra-usage** - Displays additional usage statistics
16. **fast** - Toggles fast mode on or off
17. **feedback** - Submits feedback to Anthropic
18. **fork** - Forks the current conversation into a new session
19. **login** - Authenticates with the Anthropic API
20. **logout** - Removes stored authentication credentials
21. **loop** - Runs a prompt or slash command on a recurring interval
22. **model** - Changes the active model
23. **permissions** - Views or modifies permission settings
24. **plan** - Enters plan mode
25. **plugin** - Manages plugins
26. **remote-control** - Starts or manages the remote control server
27. **rename** - Renames the current session
28. **resume** - Resumes a previous session
29. **review** - Initiates a code review
30. **session** - Manages session settings
31. **share** - Shares the current session transcript
32. **skills** - Lists available skills
33. **stats** - Displays session statistics
34. **status** - Shows the current system status
35. **summary** - Generates a summary of the conversation
36. **tasks** - Lists current tasks
37. **theme** - Changes the visual theme
38. **ultraplan** - Engages an intensive planning mode
39. **usage** - Displays API usage information
40. **version** - Shows the current version
41. **vim** - Toggles vim-style keybindings
42. **voice** - Toggles voice input mode

Each command is implemented as its own module\. Commands can accept arguments and may invoke tools, modify state, or produce output directly to the user.
