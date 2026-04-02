"""Remote Trigger tool."""
from ..types.base import ToolResult
NAME = "RemoteTrigger"
DESCRIPTION = """Manage scheduled remote Claude Code agents (triggers) via the claude.ai CCR API.
Actions: list, get, create, update, run. Endpoint: /v1/code/triggers/{trigger_id}"""
