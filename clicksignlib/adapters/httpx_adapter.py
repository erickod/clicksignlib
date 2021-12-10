import contextlib
import json
from typing import Coroutine

import httpx


class HttpxAdapter:
    async def _make_async(self, data):
        json_data = {}
        with contextlib.suppress(json.decoder.JSONDecodeError):
            json_data = data.json()

        async def async_json():
            return json_data

        data.json = async_json
        return data

    async def get(self, url: str) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await self._make_async(await client.get(url=url))

    async def post(self, url: str, json, files=None) -> Coroutine:
        async with httpx.AsyncClient() as client:
            if files:
                return await self._make_async(
                    await client.post(
                        url=url,
                        data=json,
                        files=files,
                    )
                )
            return await self._make_async(
                await client.post(url=url, json=json, files=files)
            )

    async def put(self, url: str, json) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await self._make_async(await client.put(url=url, json=json))

    async def delete(self, url: str) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await self._make_async(await client.delete(url=url))

    async def patch(self, url: str, json) -> Coroutine:
        async with httpx.AsyncClient() as client:
            return await self._make_async(await client.patch(url=url, json=json))
