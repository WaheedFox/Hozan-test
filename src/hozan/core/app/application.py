from __future__ import annotations

from titan import Titan


class Hozan:
    """Main Hozan application."""

    def __init__(self, token: str) -> None:
        self.bot = Titan(token)

    def run(self) -> None:
        self.bot.run()

    async def run_async(self) -> None:
        await self.bot.run_async()