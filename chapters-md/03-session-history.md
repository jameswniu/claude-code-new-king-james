# Chapter 03: Session History

The session history subsystem records metadata about each conversation session for later retrieval and resumption. Each entry in the history contains:

- A unique **session identifier**
- A **timestamp** recording when the session was created or last active
- The **working directory** in which the session operated
- The **model** that was used (for example, "claude-sonnet-4-6")
- The total **message count** exchanged during the session
- The **total cost** in US dollars incurred during the session

Sessions are stored persistently and can be retrieved in reverse chronological order. When listing recent sessions, the system defaults to returning the ten most recent entries, sorted by timestamp from newest to oldest.

This history enables the user to resume prior sessions, review what work was done and at what cost, and understand their usage patterns over time. The session identifier serves as the key for locating the full transcript data stored by the session persistence layer (described in Chapter 12).
