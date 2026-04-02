# Chapter 10: Hook Events

The hook system allows users to configure shell commands that execute automatically in response to specific events during a session. Eight event types are defined:

1. **PreToolUse** - Fires before a tool is executed. This allows the user to intercept, modify, or block tool calls before they take effect. A hook that returns a non-zero exit code can prevent the tool from running.

2. **PostToolUse** - Fires after a tool has successfully executed. This allows the user to log, audit, or react to completed tool operations.

3. **PostToolUseFailure** - Fires when a tool execution fails. This allows the user to handle errors, send notifications, or trigger recovery actions.

4. **Notification** - Fires when the system produces a notification for the user. This can be used to route notifications to external systems such as desktop notification daemons or messaging services.

5. **UserPromptSubmit** - Fires when the user submits a prompt. This allows pre-processing or validation of user input before it enters the conversation. Feedback from this hook is treated as coming from the user.

6. **Stop** - Fires when the agent's turn ends normally. This can trigger cleanup actions or status updates.

7. **StopFailure** - Fires when the agent's turn ends due to an error. This allows error reporting or recovery workflows.

8. **SubagentStop** - Fires when a sub-agent (spawned via the Agent tool) completes its work. This allows the parent session to react to sub-agent completion.

Hooks are configured in the user's settings file and consist of shell commands that are executed in a subprocess. The system treats hook output as user feedback, meaning that if a hook blocks an action, the agent is expected to acknowledge the blockage and adjust its approach rather than attempting workarounds.
