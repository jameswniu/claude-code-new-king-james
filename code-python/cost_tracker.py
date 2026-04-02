"""Cost tracking."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class SessionCost:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0
    total_usd: float = 0.0
    api_calls: int = 0

    def add_usage(self, usage: dict, cost_usd: float) -> None:
        self.input_tokens += usage.get("input_tokens", 0)
        self.output_tokens += usage.get("output_tokens", 0)
        self.cache_read_tokens += usage.get("cache_read_input_tokens", 0)
        self.cache_write_tokens += usage.get("cache_creation_input_tokens", 0)
        self.total_usd += cost_usd
        self.api_calls += 1

    def format_cost(self) -> str:
        if self.total_usd >= 1: return f"${self.total_usd:.2f}"
        return f"${self.total_usd:.4f}"
