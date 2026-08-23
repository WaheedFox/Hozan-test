from __future__ import annotations

from titan import Titan

from hozan.core.lifecycle.runtime import Lifecycle
from hozan.features.identity import HozanIdentityService, MemoryAccountRepository
from hozan.features.registration.start import build_router


class Hozan:
    """Main Hozan application composed on top of Titan."""

    def __init__(self, token: str) -> None:
        self.bot = Titan(token)
        self.lifecycle = Lifecycle()

        self.accounts = MemoryAccountRepository()
        self.identity = HozanIdentityService(self.accounts)

        self.bot.include(build_router(self.identity))

    def run(self) -> None:
        self.bot.run()

    async def run_async(self) -> None:
        await self.bot.run_async()
