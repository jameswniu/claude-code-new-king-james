"""Token estimation."""
CHARS_PER_TOKEN = 4  # rough estimate
def estimate_tokens(text: str) -> int: return len(text) // CHARS_PER_TOKEN
