# Chapter 24: Team Tools

Three tools support the Swarm multi-agent system described in Chapter 14: TeamCreate, TeamDelete, and SendMessage.

**TeamCreate** spawns a new team of agents for parallel work. It sets up the tmux-based infrastructure and creates the initial agent processes.

**TeamDelete** tears down a team, terminating all agent processes and cleaning up the tmux sessions.

**SendMessage** is the communication primitive for agents within a team. An agent sends a message by specifying a recipient (either a specific teammate by name or the wildcard "*" for broadcasts) and the message content. This is the only way for agents to communicate with each other; direct text output is not visible to teammates.

## The Teammate Prompt

When an agent operates as part of a team, its system prompt is extended with a special addendum. This addendum instructs the agent that:

It is running as an agent in a team. To communicate with anyone on the team, it must use the SendMessage tool with the recipient's name. For team-wide broadcasts, it addresses the message to the wildcard. Simply writing a response in text is not visible to others on the team, so the SendMessage tool is mandatory for all inter-agent communication. The user interacts primarily with the team lead, and work is coordinated through the task system and teammate messaging.
