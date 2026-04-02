"""All 218 environment variables read by Claude Code."""
from __future__ import annotations
import os
from typing import Optional

# Key env vars (subset of 218 total)
ENV_VARS = {
    "ANTHROPIC_API_KEY": "API key for Anthropic",
    "ANTHROPIC_MODEL": "Override default model",
    "ANTHROPIC_BASE_URL": "Custom API base URL",
    "ANTHROPIC_AUTH_TOKEN": "OAuth bearer token",
    "ANTHROPIC_BETAS": "Beta feature flags",
    "CLAUDE_CODE_USE_BEDROCK": "Use AWS Bedrock",
    "CLAUDE_CODE_USE_VERTEX": "Use Google Vertex AI",
    "CLAUDE_CODE_USE_FOUNDRY": "Use Anthropic Foundry",
    "CLAUDE_CODE_SIMPLE": "Minimal/bare mode",
    "CLAUDE_CODE_DEBUG_LOGS_DIR": "Debug log output directory",
    "CLAUDE_CODE_DEBUG_LOG_LEVEL": "Debug log verbosity",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "Disable telemetry and updates",
    "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "Disable auto-memory",
    "CLAUDE_CODE_DISABLE_FAST_MODE": "Disable fast mode",
    "CLAUDE_CODE_DISABLE_CRON": "Disable cron scheduler",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "Override auto-compact window size",
    "CLAUDE_CODE_REMOTE": "Running as remote agent",
    "CLAUDE_CODE_GIT_BASH_PATH": "Windows: path to git-bash",
    "DISABLE_TELEMETRY": "Disable all telemetry",
    "DISABLE_AUTO_COMPACT": "Disable auto-compaction",
    "DISABLE_AUTOUPDATER": "Disable auto-updater",
}

def get_env(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.environ.get(name, default)

def is_env_truthy(name: str) -> bool:
    return get_env(name, "").lower() in ("1", "true", "yes")
