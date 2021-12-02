from typing import Coroutine

import httpx


class HttpxAdapter:
    def __init__(self) -> None:
        self._client = httpx.AsyncClient()

    async def get(self, url: str) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await client.get("https://axoltlapi.herokuapp.com/")

    async def post(self, url: str, json) -> Coroutine:
        return await client.get("https://axoltlapi.herokuapp.com/")

    async def put(self, url: str, json) -> Coroutine:
        return await client.get("https://axoltlapi.herokuapp.com/")

    async def delete(self, url: str) -> Coroutine:
        return await client.get("https://axoltlapi.herokuapp.com/")
