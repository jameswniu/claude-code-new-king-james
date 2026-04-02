# Chapter 15: MCP Protocol

The Model Context Protocol (MCP) subsystem manages connections to external tool servers. MCP is a protocol that allows Claude Code to discover and invoke tools provided by external servers, extending its capabilities beyond the built-in tool set.

## Server Representation

Each MCP server is represented with the following attributes:

- A **name** identifying the server
- A **transport type**: one of "stdio" (communicating via standard input/output with a local process), "sse" (Server-Sent Events over HTTP), or "websocket"
- A **status**: one of "connected," "disconnected," or "error"
- Optional **instructions**: natural language guidance from the server about how to use its tools, which is injected into the system prompt
- A list of **tools** that the server provides, each described with a name, description, and parameter schema

## Operation

When Claude Code starts, it reads the MCP server configuration from the user's settings. For each configured server, it establishes a connection using the specified transport. Once connected, it queries the server for its available tools and adds them to the tool registry alongside the built-in tools.

MCP tools are invoked through the same query loop mechanism as built-in tools. When the model requests a tool that belongs to an MCP server, the request is routed through the MCP client to the appropriate server, and the result is returned to the model in the standard tool result format.

Server instructions, when provided, are included in system reminder messages so that the model understands any special requirements or conventions for using that server's tools.
