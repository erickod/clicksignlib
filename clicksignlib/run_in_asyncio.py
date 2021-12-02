import asyncio
import sys
from asyncio import Future
from typing import Any, Coroutine, Generic, Tuple, TypeVar, Union

from clicksignlib.utils import Result

_T = TypeVar("_T")
VERSION = float(f"{sys.version_info.major}.{sys.version_info.minor}")


def wait_futures(*futures: Result) -> Union[Future, Coroutine]:
    total = len(futures)
    r2: Tuple[Any, ...] = ()
    for future in futures:
        r = wait_future(future)
        if total == 1:
            return r
        r2 = r2 + (r,)
    return asyncio.gather(*r2)


async def wait_future(result: Result) -> Coroutine:
    coro = await result.response_data
    if coro.status_code not in [
        200,
    ]:
        raise NotImplementedError
    return await coro.json()


def run(*results: Result) -> Generic[_T]:
    loop = asyncio.get_event_loop()
    coro = wait_futures(*results)
    if VERSION >= 3.7:
        return asyncio.run(coro)

    return loop.run_until_complete(coro)
