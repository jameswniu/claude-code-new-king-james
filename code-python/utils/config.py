"""Settings configuration."""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional
import json

SETTINGS_SCOPES = ["user", "project", "enterprise"]
USER_SETTINGS_PATH = Path.home() / ".claude" / "settings.json"
PROJECT_SETTINGS_PATH = Path(".claude") / "settings.json"

@dataclass
class Settings:
    permissions_mode: str = "default"
    auto_compact_enabled: bool = True
    auto_memory_enabled: bool = True
    custom_api_key: Optional[str] = None
    model: Optional[str] = None
    fast_mode: bool = False
    hooks: dict = field(default_factory=dict)
    allowed_tools: list[str] = field(default_factory=list)
    denied_tools: list[str] = field(default_factory=list)

    @classmethod
    def load(cls, path: Path | None = None) -> "Settings":
        target = path or USER_SETTINGS_PATH
        if not target.exists(): return cls()
        try:
            data = json.loads(target.read_text())
            return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
        except: return cls()
