# Chapter 21: Agent Tool

The Agent tool launches new sub-agents to handle complex, multi-step tasks autonomously. Each sub-agent is a separate instance of the Claude Code runtime that operates independently from the parent session.

When the model invokes the Agent tool, it provides a prompt describing the task for the sub-agent to perform. The sub-agent is spawned as a new process, executes its task using whatever tools are available to it, and returns a single result message to the parent session when complete.

Sub-agents are valuable for:

- Parallelizing independent research or exploration tasks
- Isolating complex operations from the main conversation context
- Protecting the parent session's context window from being consumed by verbose intermediate results

The Agent tool is one of the most frequently invoked tools in complex workflows. The model may launch multiple agents simultaneously when tasks are independent, sending all spawn requests in a single response to maximize parallelism.

Sub-agents can be configured with different types (such as "Explore" for codebase exploration, "Plan" for architectural design, or "general-purpose" for broad tasks). Each agent type may have access to a different subset of tools.

The completion of a sub-agent fires the SubagentStop hook event (described in Chapter 10), allowing the parent session to react to the sub-agent's completion.
