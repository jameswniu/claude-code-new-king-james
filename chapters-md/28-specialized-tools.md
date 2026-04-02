# Chapter 28: Specialized Tools

This chapter describes the remaining tools that do not warrant individual chapters.

## LSP Tool

The LSP (Language Server Protocol) tool provides code intelligence by communicating with language servers. It supports nine operations: go to definition, find references, hover (documentation lookup), document symbols, workspace symbols, go to implementation, prepare call hierarchy, incoming calls, and outgoing calls. These operations enable the agent to navigate codebases with the same precision that a human developer gets from an IDE.

## NotebookEdit Tool

The NotebookEdit tool modifies Jupyter notebook cells. It allows the agent to edit code cells, markdown cells, and other cell types within ".ipynb" files without having to understand or manipulate the raw JSON structure of the notebook format.

## PowerShell Tool

The PowerShell tool executes PowerShell commands on Windows systems. It is the Windows counterpart to the Bash tool, providing shell execution for Windows-native operations.

## Skill Tool

The Skill tool executes a skill within the main conversation. When invoked with a skill name, it expands the skill's prompt and injects it into the conversation, effectively activating a specialized behavior mode. Skills are listed in Chapter 13.

## ToolSearch Tool

The ToolSearch tool fetches full schema definitions for deferred tools. Many tools are not included in the initial system prompt to keep it compact. When the model needs to use a deferred tool, it first calls ToolSearch to load the tool's complete parameter schema, after which the tool can be invoked normally. ToolSearch accepts queries in several forms: exact selection by name, keyword search, or name-required search with ranking.

## Sleep Tool

The Sleep tool pauses execution for a specified duration. It is used when the agent needs to wait for an external process to complete or for a timed interval to pass.

## RemoteTrigger Tool

The RemoteTrigger tool manages scheduled remote Claude Code agents (called "triggers") through the claude.ai API. It supports five actions: listing existing triggers, getting details of a specific trigger, creating a new trigger, updating an existing trigger, and running a trigger immediately. The endpoint for these operations is "/v1/code/triggers/" followed by the trigger identifier.

## ListMcpResourcesTool

This tool lists the resources available from connected MCP servers, allowing the agent to discover what data and capabilities are provided by external tool servers.

## SandboxNetworkAccess Tool

This tool manages network access within the sandbox environment, allowing controlled access to network resources when the sandbox would otherwise restrict it.
