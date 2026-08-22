from __future__ import annotations

from titan import Titan


class Hozan:
    """Main Hozan application."""

    def __init__(self, token: str) -> None:
        self.bot = Titan(token)

    def run(self) -> None:
        """Run the bot using Titan's synchronous runner."""
        self.bot.run()

    async def run_async(self) -> None:
        """Run the bot using Titan's asynchronous runner."""
        await self.bot.run_async()