from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Awaitable, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class Lifecycle:
    """Per-run lifecycle state.

    This object is deliberately short-lived. It must never become global
    mutable state or permanent application state.
    """

    _tasks: set[asyncio.Task] = field(default_factory=set)

    def track(self, awaitable: Awaitable[T], *, name: str | None = None) -> asyncio.Task[T]:
        task = asyncio.create_task(awaitable, name=name)
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)
        return task

    async def drain(self) -> None:
        tasks = tuple(self._tasks)
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    async def cancel(self) -> None:
        tasks = tuple(self._tasks)
        for task in tasks:
            if not task.done():
                task.cancel()
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
