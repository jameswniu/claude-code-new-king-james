# Chapter 33: Utilities

The utilities layer provides foundational functions used throughout the system. It encompasses authentication, classification, configuration, environment handling, git operations, model management, permissions, prompt assembly, sandboxing, shell operations, and telemetry.

## Authentication

The authentication utilities handle API key management and OAuth token lifecycle. They support multiple authentication methods including direct API keys, OAuth tokens from the console platform, and OAuth tokens from Claude.ai.

## Classifier

The classifier utility integrates with the security classifier described in the intelligence layer. It routes tool calls through the classification system to determine whether they should be allowed or blocked in autonomous mode.

## Configuration

The configuration utilities manage settings files, project-level configuration (CLAUDE.md files), and user-level preferences. Configuration is hierarchical: user-level settings can be overridden by project-level settings, which can be overridden by session-level settings.

## Environment

The environment utilities detect the runtime environment, including the operating system, shell type, terminal capabilities, and relevant environment variables.

## Git

The git utilities provide functions for interacting with git repositories: detecting whether a directory is a git repository, determining the current branch, finding the merge base for pull requests, and constructing git commands.

## Model Management

The model management utilities maintain the model registry. The system supports eleven model configurations, each available through four providers: first-party (Anthropic direct), Bedrock (AWS), Vertex (Google Cloud), and Foundry.

The pricing table defines per-million-token costs for each model. For Sonnet 4.6: three dollars for input, fifteen dollars for output, three dollars and seventy-five cents for cache writes, and thirty cents for cache reads. For Opus 4.6: fifteen dollars for input, seventy-five dollars for output, eighteen dollars and seventy-five cents for cache writes, and one dollar fifty for cache reads.

Context windows default to two hundred thousand tokens. Models in the 4.6 family (Opus 4.6 and Sonnet 4.6) can access a one-million-token context window if the user has feature flag access.

Output token limits vary by model. Opus 4.6 defaults to sixty-four thousand with an upper limit of one hundred and twenty-eight thousand. Sonnet 4.6 defaults to thirty-two thousand with the same upper limit. Earlier models have lower limits.

## Permissions

The permission utilities implement the five permission modes and their associated command whitelists, as described in detail in the intelligence layer.

## Prompt Assembly

The prompt assembly utilities construct the system prompt from its constituent sections: identity, system, doing tasks, executing actions, tone and style, and output efficiency.

## Sandbox

The sandbox utilities configure and invoke the platform-specific sandbox mechanisms described in Chapter 16.

## Shell

The shell utilities provide safe shell command construction and execution, including quoting, escaping, and process management.

## Telemetry

The telemetry utilities manage the collection and transmission of usage data to Anthropic, as described in detail in the intelligence layer.
