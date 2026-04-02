"""Analytics / GrowthBook / telemetry."""
GROWTHBOOK_SDK_CLIENT_KEY = "sdk-zAZezfDKGoZuXXKe"
GROWTHBOOK_API_HOST = "https://api.anthropic.com/"
SERVICE_NAME = "claude-code"
LOGGER_NAME = "com.anthropic.claude_code.events"
API_ENDPOINTS = {
    "messages": "https://api.anthropic.com/v1/messages",
    "feedback": "https://api.anthropic.com/api/claude_cli_feedback",
    "metrics": "https://api.anthropic.com/api/claude_code/metrics",
    "transcripts": "https://api.anthropic.com/api/claude_code_shared_session_transcripts",
    "mcp_registry": "https://api.anthropic.com/mcp-registry/v0/servers",
}
STAGING = {"ant_dev": "staging.ant.dev", "anthropic": "api-staging.anthropic.com"}
