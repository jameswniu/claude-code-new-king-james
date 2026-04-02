"""Session memory."""
from pathlib import Path
MEMORY_TYPES = ["user", "feedback", "project", "reference"]
DEFAULT_MEMORY_DIR = Path.home() / ".claude" / "projects"
MEMORY_INDEX_FILE = "MEMORY.md"
MAX_INDEX_LINES = 200
