# Chapter 29: Services Overview

The services layer provides the infrastructure that supports the query loop and tools. It comprises several subsystems.

## API Client

The API client communicates with the Anthropic API. It constructs requests containing the model identifier, message history, system prompt, tool definitions, maximum output tokens, and a streaming flag. Requests are sent to the base URL "https://api.anthropic.com" using API version "2023-06-01."

Each response from the API contains an identifier, the model used, the content blocks (text and tool use), usage statistics (input tokens, output tokens, cache read tokens, cache write tokens), and a stop reason.

The API client uses the model registry and pricing tables (described in Chapter 33) to calculate costs for each call.

## OAuth Service

The OAuth service handles authentication with Anthropic's platform. It uses the following endpoints:

- Authorization (console): "https://platform.claude.com/oauth/authorize"
- Authorization (Claude.ai): "https://claude.com/cai/oauth/authorize"
- Token exchange: "https://platform.claude.com/v1/oauth/token"
- Callback: "https://platform.claude.com/oauth/code/callback"
- Client metadata: "https://claude.ai/oauth/claude-code-client-metadata"

## Analytics

The analytics service integrates with GrowthBook for feature flags and experiment tracking. It uses the SDK client key "sdk-zAZezfDKGoZuXXKe" and communicates with the API host at "https://api.anthropic.com/." The service name is "claude-code" and the logger name is "com.anthropic.claude_code.events."

The following API endpoints are used for various analytics and operational purposes:

- Messages: "https://api.anthropic.com/v1/messages"
- Feedback: "https://api.anthropic.com/api/claude_cli_feedback"
- Metrics: "https://api.anthropic.com/api/claude_code/metrics"
- Transcripts: "https://api.anthropic.com/api/claude_code_shared_session_transcripts"
- MCP registry: "https://api.anthropic.com/mcp-registry/v0/servers"

Staging environments use separate endpoints at "staging.ant.dev" and "api-staging.anthropic.com."

## MCP Client

The MCP client manages connections to external MCP servers, as described in Chapter 15.

## Plugin Management

The plugin system supports two package formats: ".mcpb" and ".dxt". Plugins can be sourced from five locations: GitHub repositories, git subdirectories, package registries, direct URLs, and package managers. The plugin manager handles discovery, installation, and lifecycle management of these extensions.

## Token Estimation

A simple token estimation service approximates token counts by dividing the character count by four. This rough estimate (four characters per token) is used for quick calculations when exact tokenization is not needed, such as estimating whether compaction will be necessary.
