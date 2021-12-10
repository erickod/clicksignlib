from typing import Any, Coroutine, Dict

from typing_extensions import Protocol


class IRequest(Protocol):
    async def get(self, url: str) -> Coroutine:
        pass

    async def post(self, url: str, json, files=None) -> Coroutine:
        pass

    async def put(self, url: str, json) -> Coroutine:
        pass

    async def delete(self, url: str) -> Coroutine:
        pass

    async def path(self, url: str, json) -> Coroutine:
        pass
