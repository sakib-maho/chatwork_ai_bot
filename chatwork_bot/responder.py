"""Core response helper functions for chat bot logic."""

from __future__ import annotations


def normalize_message(text: str) -> str:
    return " ".join(text.strip().split()).lower()


def build_local_response(text: str) -> str:
    cleaned = normalize_message(text)
    if "deploy" in cleaned:
        return "Deployment checklist: tests, env vars, migration status, and rollback plan."
    if "bug" in cleaned:
        return "Please share reproduction steps, expected output, and current logs."
    return "Acknowledged. I can summarize tasks, deployment notes, or bug triage details."
