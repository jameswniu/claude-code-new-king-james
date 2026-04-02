"""Auto-dream service."""
def build_dream_prompt(memory_dir: str, transcripts_dir: str) -> str:
    return f"""# Dream: Memory Consolidation
You are performing a dream — a reflective pass over your memory files.
Memory directory: `{memory_dir}`
Session transcripts: `{transcripts_dir}`
## Phase 1 — Orient (ls memory dir, read MEMORY.md)
## Phase 2 — Gather recent signal (daily logs, drifted memories, transcript grep)
## Phase 3 — Consolidate (write/update memory files, merge, convert dates, delete contradictions)
## Phase 4 — Prune and index (update MEMORY.md, remove stale, demote verbose, resolve contradictions)"""
