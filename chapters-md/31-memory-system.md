# Chapter 31: Memory System

The memory system provides persistent storage for information that should survive across conversation sessions. It operates through two subsystems: session memory and memory extraction.

## Memory Types

The system recognizes four types of memory:

1. **User**: information about the user's role, goals, responsibilities, and knowledge. These memories help tailor future behavior to the specific user.
2. **Feedback**: guidance the user has given about how to approach work, including both corrections and confirmations of successful approaches.
3. **Project**: information about ongoing work, goals, initiatives, bugs, or incidents that is not derivable from the code or git history.
4. **Reference**: pointers to where information can be found in external systems.

## Storage Structure

Memories are stored as individual markdown files within a project-specific directory under the user's home directory, at the path "~/.claude/projects/". Each memory file has YAML frontmatter containing the memory's name, a one-line description, and its type.

The memory directory contains an index file called "MEMORY.md" that serves as a table of contents. Each entry in the index is a single line under approximately one hundred and fifty characters, formatted as a markdown link to the memory file with a brief description. The index is constrained to two hundred lines to keep it manageable.

## Memory Extraction

A memory extraction service analyzes recent messages and updates the persistent memory systems. It uses a prompt that instructs the model to analyze the most recent messages and update its persistent memory. This extraction can be triggered automatically or manually.

## Design Principles

The memory system follows several principles: memories should be organized semantically by topic rather than chronologically; memories should be updated or removed when they become outdated; duplicate memories should be avoided by checking for existing memories before writing new ones; and the index should remain concise, with detailed content stored in individual files rather than in the index itself.
