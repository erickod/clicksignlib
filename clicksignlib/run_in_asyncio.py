import asyncio
import sys
from asyncio import Future
from typing import Any, Coroutine, Dict, List, Tuple, Union

from clicksignlib.utils import Result
from clicksignlib.utils.errors import ApiError

VERSION = float(f"{sys.version_info.major}.{sys.version_info.minor}")


def wait_futures(*results: Result, raises: bool) -> Union[Future, Coroutine]:
    total: int = len(results)
    r2: Tuple[Any, ...] = ()
    for future in results:
        r = wait_future(future, raises=raises)
        if total == 1:
            return r
        r2 = r2 + (r,)
    return asyncio.gather(*r2)


async def wait_future(result: Result, raises: bool = False) -> Dict[str, Any]:
    coro = await result.response_data
    response = await coro.json()
    if (
        coro.status_code
        not in [
            200,
            201,
            202,
        ]
        and raises
    ):
        try:
            raise ApiError(coro.status_code, response["errors"])
        except KeyError:
            raise ApiError(coro.status_code, "No errors message")
    return response


def run(
    *results: Result, raises: bool = True
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    if VERSION >= 3.7:
        return asyncio.run(wait_futures(*results, raises=raises))
    coro = wait_futures(*results, raises=raises)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)
