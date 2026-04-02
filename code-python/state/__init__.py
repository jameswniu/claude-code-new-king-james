"""Application state management."""
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class AppState:
    permission_mode: str = "default"
    is_plan_mode: bool = False
    session_id: str = ""
    model: str = "claude-sonnet-4-6"
    fast_mode: bool = False
    auto_compact_enabled: bool = True
