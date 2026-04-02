# Chapter 08: Bridge System

The bridge system enables remote session management through WebSocket connections. It is the mechanism by which Claude Code can be controlled from outside the local terminal, supporting remote REPL access and session coordination.

## Transport

The bridge supports two transport mechanisms: **WebSocket** and **polling**. WebSocket is the primary transport for real-time bidirectional communication. Polling serves as a fallback for environments where persistent connections are not feasible.

## Commands

The bridge recognizes seven core commands:

1. **close**: Terminates the remote session
2. **poll**: Requests pending messages (used in polling mode)
3. **register**: Registers a new remote client with the bridge
4. **reconnect-session**: Re-establishes a previously interrupted session
5. **heartbeat**: Keeps the connection alive
6. **reconnect**: Reconnects the transport layer
7. **status**: Queries the current state of the bridge and session

## Scope

The bridge handles authentication of remote clients, message routing between the local session and remote consumers, and graceful handling of disconnections and reconnections.

The bridge provides the infrastructure for features like the desktop application's connection to a running Claude Code session and the remote control server that allows programmatic access to sessions.
