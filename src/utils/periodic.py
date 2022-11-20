import asyncio
from contextlib import suppress


class Periodic:
    def __init__(self, func, time, *args, **kwargs):
        self.func = func
        self.time = time
        self.is_started = False
        self._task = None
        self.args = args
        self.kwargs = kwargs

    async def start(self):
        if not self.is_started:
            self.is_started = True
            self._task = asyncio.ensure_future(self._run())

    async def stop(self):
        if self.is_started:
            self.is_started = False
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task

    async def _run(self):
        while True:
            await self.func(*self.args, **self.kwargs)
            await asyncio.sleep(self.time)

