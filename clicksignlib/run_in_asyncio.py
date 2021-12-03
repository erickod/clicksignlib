import asyncio
import sys
from asyncio import Future
from typing import Any, Coroutine, Dict, List, Tuple, Union

from clicksignlib.utils import Result
from clicksignlib.utils.errors import ApiError

VERSION = float(f"{sys.version_info.major}.{sys.version_info.minor}")


def wait_futures(*results: Result) -> Union[Future, Coroutine]:
    total: int = len(results)
    r2: Tuple[Any, ...] = ()
    for future in results:
        r = wait_future(future)
        if total == 1:
            return r
        r2 = r2 + (r,)
    return asyncio.gather(*r2)


async def wait_future(result: Result) -> Dict[str, Any]:
    coro = await result.response_data
    response = await coro.json()
    if coro.status_code not in [
        200,
        201,
        202,
    ]:
        raise ApiError(coro.status_code, response["errors"][0])
    return response


def run(*results: Result) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    loop = asyncio.get_event_loop()
    coro = wait_futures(*results)
    if VERSION >= 3.7:
        return asyncio.run(coro)

    return loop.run_until_complete(coro)
