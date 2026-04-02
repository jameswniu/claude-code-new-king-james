# Chapter 13: Bundled Skills

The skill system provides pre-packaged capabilities that extend the agent's behavior beyond its built-in tools. Sixteen skills are bundled with the system:

1. **batch** - Processes multiple operations in a batch
2. **claudeApi** - Assists with building applications using the Claude API
3. **claudeApiContent** - Handles content-related API operations
4. **claudeInChrome** - Integrates with the Chrome browser extension for browser automation
5. **debug** - Provides enhanced debugging capabilities
6. **keybindings** - Manages keyboard shortcut configuration
7. **loop** - Runs a prompt or command on a recurring interval
8. **loremIpsum** - Generates placeholder text
9. **remember** - Saves information to persistent memory
10. **scheduleRemoteAgents** - Creates and manages scheduled remote agent triggers
11. **simplify** - Reviews code for reuse, quality, and efficiency, then fixes issues found
12. **skillify** - Converts a workflow into a reusable skill
13. **stuck** - Provides guidance when the agent or user is stuck on a problem
14. **updateConfig** - Configures the Claude Code settings via settings.json
15. **verify** - Verifies that changes work correctly
16. **verifyContent** - Verifies content integrity

Skills are invoked through the Skill tool (described in Chapter 28) using their name. When invoked, a skill expands into a specialized prompt that guides the agent's behavior for that particular capability. Skills differ from tools in that they operate at the prompt level rather than the tool level: they inject context and instructions rather than executing code directly.
