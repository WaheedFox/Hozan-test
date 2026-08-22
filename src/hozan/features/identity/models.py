from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Account:
    """Domain model for a Hozan account."""

    telegram_user_id: int
    name: str
    hozan_id: str
    password_hash: str | None = None
