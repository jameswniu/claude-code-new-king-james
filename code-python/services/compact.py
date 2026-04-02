"""Compaction engine."""
WARNING_OFFSET = 20_000; ERROR_OFFSET = 13_000; BLOCKING_OFFSET = 3_000
MAX_CONSECUTIVE_FAILURES = 3
COMPACTION_PROMPT = """Your task is to create a detailed summary of the conversation so far, paying close attention to the user's explicit requests and your previous actions.
This summary should be thorough in capturing technical details, code patterns, and architectural decisions.

Your summary should include: 1. Primary Request and Intent, 2. Key Technical Concepts, 3. Files and Code Sections, 4. Errors and fixes, 5. Problem Solving, 6. All user messages, 7. Pending Tasks, 8. Current Work, 9. Optional Next Step."""

def should_auto_compact(tokens: int, window: int) -> bool:
    return tokens >= (window - WARNING_OFFSET)
