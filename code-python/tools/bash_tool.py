"""Bash tool."""
from __future__ import annotations
import asyncio, subprocess, os
from ..types.base import ToolResult, ToolUseContext

NAME = "Bash"
DESCRIPTION = "Executes a given bash command and returns its output.\n\nThe working directory persists between commands, but shell state does not."

SEARCH_COMMANDS = frozenset(["find","grep","rg","ag","ack","locate","which","whereis"])
READ_COMMANDS = frozenset(["cat","head","tail","less","more","wc","stat","file","strings","ls","tree","du","jq","awk","cut","sort","uniq","tr"])
PASSTHROUGH_COMMANDS = frozenset(["echo","printf","true","false",":"])
MUTATION_COMMANDS = frozenset(["mv","cp","rm","mkdir","rmdir","chmod","chown","chgrp","touch","ln","cd","export","unset","wait"])
ACCEPT_EDITS_ALLOWED = frozenset(["mkdir","touch","rm","rmdir","mv","cp","sed"])

async def execute(command: str, timeout_ms: int = 120000, cwd: str | None = None) -> ToolResult:
    try:
        proc = await asyncio.create_subprocess_shell(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            cwd=cwd or os.getcwd(),
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout_ms / 1000)
        output = stdout.decode() + (stderr.decode() if stderr else "")
        return ToolResult(content=output, is_error=proc.returncode != 0)
    except asyncio.TimeoutError:
        return ToolResult(content="Command timed out", is_error=True)
    except Exception as e:
        return ToolResult(content=str(e), is_error=True)
