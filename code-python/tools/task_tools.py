"""Task management tools."""
from __future__ import annotations
from ..types.base import ToolResult
from ..task import Task, TaskStatus

TASK_TOOL_NAMES = ["TaskCreate","TaskGet","TaskList","TaskUpdate","TaskOutput","TaskStop"]

class TaskManager:
    def __init__(self):
        self._tasks: dict[str, Task] = {}
        self._counter = 0

    def create(self, description: str, parent_id: str | None = None) -> Task:
        self._counter += 1
        task = Task(id=f"task_{self._counter}", description=description, parent_id=parent_id)
        self._tasks[task.id] = task
        return task

    def get(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def update(self, task_id: str, status: str) -> Task | None:
        task = self._tasks.get(task_id)
        if task: task.status = TaskStatus(status)
        return task

    def stop(self, task_id: str) -> Task | None:
        task = self._tasks.get(task_id)
        if task: task.status = TaskStatus.CANCELLED
        return task
