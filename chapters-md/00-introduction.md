# Chapter 00: Introduction

Claude Code is Anthropic's official command-line interface for interacting with Claude. At the time of this description, the version under examination is 2.1.87.

The system is a large-scale agentic application comprising over sixty modules organized into a package structure. It encompasses subsystems for tool execution, session management, API communication, memory persistence, security classification, and multi-agent coordination.

The runtime is not merely a thin wrapper around an API. It is a complete agentic loop that sends messages to the Anthropic API, interprets tool-use requests from the model's responses, executes those tools locally on the user's machine, returns the results to the model, and repeats this cycle until the model signals completion or a budget is exhausted. This loop is the heart of the system and is described in detail in Chapter 04.

The production runtime encompasses the following major subsystems:

1. The query loop, which drives the agentic conversation cycle
2. A tool registry containing thirty-eight distinct tools
3. A service layer for API communication, OAuth, analytics, memory, and plugin management
4. A hook system that fires shell commands in response to eight distinct event types
5. A session persistence layer that stores transcripts as JSONL files
6. A cron scheduler for durable, recurring jobs
7. A sandbox enforcement system using platform-native isolation (Bubblewrap on Linux, Apple Sandbox on macOS)
8. A multi-agent orchestration system called "Swarm" that uses tmux for parallel agent coordination
9. A bridge system for remote session management over WebSocket
10. A skill system comprising sixteen bundled skills
11. A slash command system with forty-two recognized commands
12. A memory system with four distinct memory types and a persistent index file

Each of these subsystems is described in its own chapter.
