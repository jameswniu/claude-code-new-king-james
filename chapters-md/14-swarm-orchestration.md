# Chapter 14: Swarm Orchestration

The Swarm system provides multi-agent orchestration using tmux as the coordination layer. It enables multiple Claude Code agents to work in parallel on different aspects of a task, communicating through a structured messaging system.

## Architecture

The swarm is organized around two key roles:

- The **team lead**: the primary agent that coordinates work and communicates with the user. It spawns sub-agents, assigns tasks, and synthesizes results.
- The **swarm view**: a tmux-based interface that displays the activities of all agents in the swarm simultaneously.

The orchestration mode is referred to as **tmux mode**, reflecting its use of terminal multiplexing to manage parallel agent processes.

## Communication

Agents within a swarm communicate exclusively through the SendMessage tool. Direct text output from an agent is not visible to other agents or the user through the team interface. All inter-agent communication must be explicit.

An agent may send a message to a specific teammate by name, or broadcast to all teammates using the wildcard address. The system prompt for team members includes a special addendum that instructs the agent about team communication protocols:

The agent is told that it is running as part of a team, that it must use the SendMessage tool to communicate (not plain text output), that it can address messages to specific teammates by name, and that it should use team-wide broadcasts sparingly. The user interacts primarily with the team lead, and work is coordinated through the task system and teammate messaging.
