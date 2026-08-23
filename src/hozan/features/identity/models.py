from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True, slots=True)
class HozanIdentity:
    value: str
    account_id: int
    free: bool
    created_at: datetime


@dataclass(frozen=True, slots=True)
class Account:
    telegram_user_id: int
    name: str
    created_at: datetime
    password_hash: str | None = None
    identities: tuple[HozanIdentity, ...] = ()

    @property
    def free_identity(self) -> HozanIdentity | None:
        return next((item for item in self.identities if item.free), None)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)
