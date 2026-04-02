"""Anthropic API client."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, AsyncIterator, Optional
from ..utils.models import MODELS, PRICING, get_context_window, get_max_output_tokens, calculate_cost

API_BASE = "https://api.anthropic.com"
API_VERSION = "2023-06-01"

@dataclass
class APIRequest:
    model: str
    messages: list[dict]
    system: str | list[str] = ""
    max_tokens: int = 32000
    tools: list[dict] = field(default_factory=list)
    stream: bool = True

@dataclass
class APIResponse:
    id: str = ""
    model: str = ""
    content: list[dict] = field(default_factory=list)
    usage: dict = field(default_factory=dict)
    stop_reason: Optional[str] = None

async def create_message(request: APIRequest, api_key: str) -> APIResponse:
    """Create a message via the Anthropic API. Requires httpx or similar."""
    raise NotImplementedError("Requires HTTP client integration (httpx/aiohttp)")
