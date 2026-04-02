"""Session history."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional
import json, time

@dataclass
class SessionEntry:
    session_id: str
    timestamp: float
    cwd: str
    model: str
    message_count: int = 0
    total_cost_usd: float = 0.0

@dataclass
class SessionHistory:
    entries: list[SessionEntry] = field(default_factory=list)

    def add(self, entry: SessionEntry) -> None:
        self.entries.append(entry)

    def get_recent(self, limit: int = 10) -> list[SessionEntry]:
        return sorted(self.entries, key=lambda e: e.timestamp, reverse=True)[:limit]
