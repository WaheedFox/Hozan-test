from __future__ import annotations

from hozan.core.lifecycle.runtime import Lifecycle
from hozan.features.identity import HozanIdentityService, MemoryAccountRepository
from hozan.features.registration.start import build_router
from hozan.platform.telegram.application import TelegramApplication


class Hozan:
    """Main Hozan application composed above the Telegram boundary."""

    def __init__(self, token: str) -> None:
        self.telegram = TelegramApplication(token)
        self.lifecycle = Lifecycle()

        self.accounts = MemoryAccountRepository()
        self.identity = HozanIdentityService(self.accounts)

        self.telegram.include(build_router(self.identity))

    @property
    def bot(self):
        """Expose Titan for backwards compatibility with existing callers."""
        return self.telegram.bot

    def run(self) -> None:
        self.telegram.run()

    async def run_async(self) -> None:
        await self.telegram.start(self.lifecycle)
