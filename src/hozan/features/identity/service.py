from __future__ import annotations

import secrets

from .models import Account, HozanIdentity, utcnow
from .repository import AccountRepository


class HozanIdentityService:
    def __init__(self, repository: AccountRepository) -> None:
        self.repository = repository

    async def get_or_create_account(self, *, telegram_user_id: int, name: str) -> Account:
        existing = await self.repository.get(telegram_user_id)
        if existing is not None:
            return existing

        account = Account(
            telegram_user_id=telegram_user_id,
            name=name,
            created_at=utcnow(),
        )
        await self.repository.create(account)
        identity = await self._reserve_free_identity(telegram_user_id)

        return Account(
            telegram_user_id=account.telegram_user_id,
            name=account.name,
            created_at=account.created_at,
            password_hash=account.password_hash,
            identities=(identity,),
        )

    async def _reserve_free_identity(self, account_id: int) -> HozanIdentity:
        for _ in range(32):
            value = f"#{secrets.randbelow(100_000_000):08d}"
            if await self.repository.find_identity(value) is not None:
                continue
            identity = HozanIdentity(
                value=value,
                account_id=account_id,
                free=True,
                created_at=utcnow(),
            )
            try:
                return await self.repository.add_identity(identity)
            except ValueError:
                continue
        raise RuntimeError("unable to allocate a Hozan ID")
