import asyncio
import sys
from asyncio import Future
from typing import Coroutine, Generic, TypeVar, Union

_T = TypeVar("_T")
VERSION = float(f"{sys.version_info.major}.{sys.version_info.minor}")


def wait_futures(*futures: Coroutine) -> Union[Future, Coroutine]:
    total = len(futures)
    r2 = ()
    for future in futures:
        r = wait_future(future)
        if total == 1:
            return r
        r2 = r2 + (r,)
    return asyncio.gather(*r2)


async def wait_future(future: Coroutine) -> Coroutine:
    coro = await future.response_data
    return await coro.json()


def run(*futures: Coroutine) -> Generic[_T]:
    loop = asyncio.get_event_loop()
    coro = wait_futures(*futures)
    if VERSION >= 3.7:
        asyncio.run(coro)

    return loop.run_until_complete(coro)
