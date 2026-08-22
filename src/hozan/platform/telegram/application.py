from __future__ import annotations

from hozan.core.lifecycle.runtime import Lifecycle


class TelegramApplication:
    """Thin Hozan adapter around Titan.

    Hozan composes Titan instead of duplicating Telegram transport,
    routing, context, or framework lifecycle machinery.
    """

    def __init__(self, token: str) -> None:
        from titan import Titan

        self.bot = Titan(token)

    async def start(self, lifecycle: Lifecycle) -> None:
        await self.bot.run_async()

    async def stop(self, lifecycle: Lifecycle) -> None:
        return None
