# Chapter 06: Tool Architecture

Every tool in Claude Code conforms to a common contract that defines how tools are discovered, described, invoked, and how their results are returned.

## The Tool Contract

Each tool declares the following properties:

- A **name**: a short, unique identifier (such as "Bash", "Read", "Edit", or "Agent")
- A **description**: a natural language explanation of what the tool does, which is included in the system prompt sent to the model
- A **search hint**: an optional string that helps the ToolSearch mechanism find the tool when it is deferred (not loaded into the initial prompt)
- A **deferral flag**: a boolean indicating whether the tool's full schema should be omitted from the initial prompt and loaded on demand via ToolSearch
- A **maximum result size**: the upper limit on the number of characters a tool result may contain, defaulting to one hundred thousand characters

Every tool must implement a **call** method that accepts a dictionary of input parameters and a tool use context, and returns a tool result. This method may be asynchronous.

Tools may optionally provide a **prompt description** method that returns a customized version of their description for inclusion in the system prompt. They may also declare whether they are **read-only**, meaning they do not modify any state on the user's system.

## Tool Results

A tool result contains:

- A **type** field, always set to "tool_result"
- A **tool use identifier** linking the result back to the specific tool call that produced it
- A **content** string containing the output
- An **error flag** indicating whether the result represents a failure

## Tool Use Context

The tool use context is the shared state object that is passed to every tool call. It contains the session's configuration options, available tools, permission settings, and any other runtime state that tools may need to consult.

## Design Philosophy

The tool architecture follows a uniform interface pattern. Every tool, regardless of complexity, presents the same shape to the query loop: name, description, call method, result. This allows the query loop to dispatch tool calls generically without special-casing any particular tool. The deferral mechanism (ToolSearch) allows the system to keep the initial prompt compact by omitting tool schemas that are rarely needed, loading them on demand when the model requests them.
