# Chapter 23: Task Tools

Six tools provide task management capabilities, operating on the task manager described in Chapter 05. Their names are: TaskCreate, TaskGet, TaskList, TaskUpdate, TaskOutput, and TaskStop.

**TaskCreate** creates a new task with a description and optional parent task reference. It returns the newly created task with its assigned identifier.

**TaskGet** retrieves a single task by its identifier, returning its current state including status, description, and result.

**TaskList** returns all tasks in the current session, providing an overview of what work has been planned, is in progress, or has been completed.

**TaskUpdate** changes the status of a task. The caller provides the task identifier and the new status (such as "in_progress" or "completed").

**TaskOutput** retrieves the output or result associated with a completed task.

**TaskStop** cancels a task by setting its status to "cancelled."

These tools allow the agent to organize its work into discrete, trackable steps. The model is encouraged to create tasks when working on multi-step operations, mark them as in-progress when starting, and mark them as completed when finished. This provides the user with visibility into the agent's progress.
