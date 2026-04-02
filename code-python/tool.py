"""Base Tool class."""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, AsyncIterator, Optional
from .types.base import ToolResult, ToolUseContext

class BaseTool(ABC):
    name: str
    description: str
    search_hint: str = ""
    should_defer: bool = False
    max_result_size_chars: int = 100_000

    @abstractmethod
    async def call(self, input: dict, context: ToolUseContext) -> ToolResult: ...

    def prompt_description(self) -> str:
        return self.description

    def is_read_only(self) -> bool:
        return False
