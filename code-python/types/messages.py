"""Message types."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Literal, Optional, Union

@dataclass
class TextBlock:
    type: Literal["text"] = "text"
    text: str = ""

@dataclass
class ToolUseBlock:
    type: Literal["tool_use"] = "tool_use"
    id: str = ""
    name: str = ""
    input: dict = field(default_factory=dict)

@dataclass
class ToolResultBlock:
    type: Literal["tool_result"] = "tool_result"
    tool_use_id: str = ""
    content: Any = ""

ContentBlock = Union[TextBlock, ToolUseBlock, ToolResultBlock]

@dataclass
class UserMessage:
    role: Literal["user"] = "user"
    content: list[ContentBlock] = field(default_factory=list)

@dataclass
class AssistantMessage:
    role: Literal["assistant"] = "assistant"
    content: list[ContentBlock] = field(default_factory=list)
    id: str = ""
    model: str = ""
    usage: Optional[dict] = None

Message = Union[UserMessage, AssistantMessage]
