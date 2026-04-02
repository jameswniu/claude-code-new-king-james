"""MCP client."""
from dataclasses import dataclass
from typing import Literal, Optional

@dataclass
class MCPServer:
    name: str
    transport: Literal["stdio", "sse", "websocket"]
    status: Literal["connected", "disconnected", "error"] = "disconnected"
    instructions: Optional[str] = None
    tools: list[dict] = None
    def __post_init__(self):
        if self.tools is None: self.tools = []
