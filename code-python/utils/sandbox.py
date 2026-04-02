"""Sandbox configuration."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import platform

@dataclass
class SandboxConfig:
    enabled: bool = True
    fs_read_deny_only: list[str] = field(default_factory=list)
    fs_read_allow_within_deny: list[str] = field(default_factory=list)
    fs_write_allow_only: list[str] = field(default_factory=list)
    fs_write_deny_within_allow: list[str] = field(default_factory=list)
    allow_unix_sockets: list[str] = field(default_factory=list)
    ignore_violations: dict[str, list[str]] = field(default_factory=dict)
    allow_unsandboxed_commands: bool = True

def get_sandbox_backend() -> str:
    system = platform.system()
    if system == "Linux": return "bubblewrap"
    if system == "Darwin": return "apple_sandbox"
    return "none"
