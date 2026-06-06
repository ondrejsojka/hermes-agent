"""Cursor Agent API transport."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from agent.transports.base import ProviderTransport
from agent.transports.types import NormalizedResponse


class CursorAgentTransport(ProviderTransport):
    @property
    def api_mode(self) -> str:
        return "cursor_agent"

    def convert_messages(self, messages: List[Dict[str, Any]], **kwargs) -> Any:
        return messages

    def convert_tools(self, tools: List[Dict[str, Any]]) -> Any:
        return tools

    def build_kwargs(
        self,
        model: str,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        **params,
    ) -> Dict[str, Any]:
        kwargs: Dict[str, Any] = {"model": model, "messages": messages}
        if tools is not None:
            kwargs["tools"] = tools
        return kwargs

    def normalize_response(self, response: Any, **kwargs) -> Any:
        return response

    def validate_response(self, response: Any) -> bool:
        return response is not None and hasattr(response, "choices") and bool(response.choices)


from agent.transports import register_transport  # noqa: E402

register_transport("cursor_agent", CursorAgentTransport)
