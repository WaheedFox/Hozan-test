from __future__ import annotations

from titan import Router, Titan

from hozan.core.lifecycle.runtime import Lifecycle


class TelegramApplication:
    """Hozan's Telegram integration boundary around Titan.

    This class owns the Titan application and is the only place where the
    Hozan application composes Telegram-specific routers and execution.
    """

    def __init__(self, token: str) -> None:
        self.bot = Titan(token)

    def include(self, router: Router) -> None:
        """Register a Hozan Telegram router with Titan."""
        self.bot.include(router)

    def run(self) -> None:
        """Run Titan's synchronous Telegram lifecycle."""
        self.bot.run()

    async def start(self, lifecycle: Lifecycle) -> None:
        """Start Titan's asynchronous Telegram lifecycle."""
        await self.bot.run_async()

    async def stop(self, lifecycle: Lifecycle) -> None:
        """Stop the Telegram integration.

        Titan owns the polling lifecycle, so there is no additional stop
        operation to perform here yet.
        """
        return None
