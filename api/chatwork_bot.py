"""Vercel-style handler delegating to local responder logic."""

from __future__ import annotations

from chatwork_bot.responder import build_local_response


def handler(request):  # noqa: ANN001
    message = ""
    if isinstance(request, dict):
        message = str(request.get("message", ""))
    response = build_local_response(message)
    return {"status": "ok", "response": response}
