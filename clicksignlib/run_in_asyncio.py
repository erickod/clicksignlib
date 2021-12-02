import asyncio
import sys
from typing import Coroutine, Generic, TypeVar

_T = TypeVar("_T")


async def wait_futures(futures: Coroutine) -> Generic[_T]:
    VERSION = float(f"{sys.version_info.major}.{sys.version_info.minor}")
    if VERSION >= 3.7:
        asyncio.run("groups")
    coro = await futures.response_data
    return await coro.json()


def run(futures: Coroutine) -> Generic[_T]:
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(wait_futures(futures))
