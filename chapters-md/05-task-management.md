# Chapter 05: Task Management

The task management subsystem provides a lightweight mechanism for tracking units of work within a session. Each task is a discrete item with a description and a lifecycle.

## Task Structure

Every task carries the following attributes:

- A unique **identifier**, generated sequentially (the first task is "task_1", the second "task_2", and so on)
- A **description** in natural language
- A **status** drawn from five possible states: pending, in progress, completed, failed, or cancelled
- An optional **result** string that records the outcome when the task completes or fails
- An optional **parent identifier** linking the task to a parent task, enabling hierarchical task structures
- A list of **child identifiers** referencing sub-tasks

## Lifecycle

A task begins in the "pending" state when created. It progresses to "in progress" when work begins. From there, it may transition to "completed" (with an optional result describing the outcome), "failed" (with an error message), or "cancelled."

The completion method sets the status to "completed" and records the result. The failure method sets the status to "failed" and records the error. Cancellation is handled separately through the task manager.

## Task Manager

A central task manager maintains the collection of all tasks in a session. It provides five operations:

1. **Create**: Generates a new task with a description and optional parent reference, assigns it the next sequential identifier, and stores it.
2. **Get**: Retrieves a task by its identifier.
3. **List**: Returns all tasks in the session.
4. **Update**: Changes the status of a task by its identifier.
5. **Stop**: Cancels a task by setting its status to "cancelled."

These operations are exposed to the model through the task tools described in Chapter 23, allowing the agent to organize its own work into trackable steps that the user can monitor.
