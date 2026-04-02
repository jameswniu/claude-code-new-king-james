"""Base Task class."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

@dataclass
class Task:
    id: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[str] = None
    parent_id: Optional[str] = None
    children: list[str] = field(default_factory=list)

    def complete(self, result: str = "") -> None:
        self.status = TaskStatus.COMPLETED
        self.result = result

    def fail(self, error: str = "") -> None:
        self.status = TaskStatus.FAILED
        self.result = error
