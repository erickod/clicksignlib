from typing import Coroutine

import httpx


class HttpxAdapter:
    async def get(self, url: str) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await client.get(url=url)

    async def post(self, url: str, json) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await client.post(url=url, json=json)

    async def put(self, url: str, json) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await client.put(url=url, json=json)

    async def delete(self, url: str) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await client.delete(url=url)
