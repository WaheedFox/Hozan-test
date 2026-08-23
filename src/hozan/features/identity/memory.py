from __future__ import annotations

from .models import Account, HozanIdentity


class MemoryAccountRepository:
    def __init__(self) -> None:
        self._accounts: dict[int, Account] = {}
        self._identities: dict[str, HozanIdentity] = {}

    async def get(self, telegram_user_id: int) -> Account | None:
        return self._accounts.get(telegram_user_id)

    async def create(self, account: Account) -> Account:
        if account.telegram_user_id in self._accounts:
            raise ValueError("account already exists")
        self._accounts[account.telegram_user_id] = account
        return account

    async def add_identity(self, identity: HozanIdentity) -> HozanIdentity:
        if identity.value in self._identities:
            raise ValueError("Hozan ID already exists")
        self._identities[identity.value] = identity
        account = self._accounts.get(identity.account_id)
        if account is not None:
            self._accounts[identity.account_id] = Account(
                telegram_user_id=account.telegram_user_id,
                name=account.name,
                created_at=account.created_at,
                password_hash=account.password_hash,
                identities=(*account.identities, identity),
            )
        return identity

    async def find_identity(self, value: str) -> HozanIdentity | None:
        return self._identities.get(value)
