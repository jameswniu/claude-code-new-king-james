"""Authentication."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import os

@dataclass
class AuthState:
    api_key: Optional[str] = None
    oauth_token: Optional[str] = None
    is_authenticated: bool = False

def get_api_key() -> Optional[str]:
    return os.environ.get("ANTHROPIC_API_KEY")

def get_auth_state() -> AuthState:
    key = get_api_key()
    return AuthState(api_key=key, is_authenticated=key is not None)

OAUTH_URLS = {
    "authorize": "https://platform.claude.com/oauth/authorize",
    "token": "https://platform.claude.com/v1/oauth/token",
    "callback": "https://platform.claude.com/oauth/code/callback",
    "client_metadata": "https://claude.ai/oauth/claude-code-client-metadata",
}
