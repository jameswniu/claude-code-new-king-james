# Chapter 07: Application State

The application state is a centralized record of the runtime configuration for the current session. It tracks the following:

- The **permission mode**: which of the five permission modes is active (default, accept edits, bypass permissions, don't ask, or plan). This governs how tool calls are authorized.
- The **plan mode flag**: a boolean indicating whether the session is currently in plan mode, where the agent designs an approach before executing.
- The **session identifier**: a unique string identifying the current conversation session.
- The **model**: the identifier of the model being used, defaulting to "claude-sonnet-4-6."
- The **fast mode flag**: a boolean indicating whether fast mode is active. Fast mode uses the same model but with faster output generation.
- The **auto-compact flag**: a boolean indicating whether automatic context compaction is enabled, defaulting to true.

This state object is consulted throughout the system whenever behavior needs to vary based on the current mode, model, or session configuration. It is mutable and updated as the user changes settings during a session (for example, toggling fast mode or entering plan mode).
