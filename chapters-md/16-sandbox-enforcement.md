# Chapter 16: Sandbox Enforcement

The sandbox enforcement subsystem restricts the agent's ability to interact with the host system, providing an isolation boundary that limits the blast radius of tool execution.

## Platform-Specific Implementation

The sandbox uses platform-native isolation mechanisms:

- On **Linux**, the system uses **Bubblewrap** (bwrap), a lightweight sandboxing tool that creates restricted namespaces for processes. Bubblewrap can limit filesystem access, network access, and process visibility.

- On **macOS**, the system uses the **Apple Sandbox** (sandbox-exec), the operating system's built-in application sandboxing framework. This provides fine-grained control over file system access, network operations, and inter-process communication.

## Purpose

The sandbox serves as a defense-in-depth measure. Even if the security classifier (described in the intelligence layer) approves a tool call, the sandbox provides an additional layer of protection by restricting what that tool call can actually access on the host system. This is particularly important for the Bash tool, which executes arbitrary shell commands and could potentially access or modify anything on the system without sandboxing.

The sandbox configuration is adjusted based on the permission mode and the specific tool being executed. Read-only tools may run with minimal sandbox restrictions, while tools that modify the filesystem or execute shell commands operate within tighter constraints.
