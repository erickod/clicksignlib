import contextlib
from typing import Coroutine

import aiohttp


class AioHttpAdapter:
    async def _make_async(self, data):
        setattr(data, "status_code", data.status)
        json_data = {}
        with contextlib.suppress(aiohttp.client_exceptions.ContentTypeError):
            json_data = await data.json()

        async def async_json():
            return json_data

        data.json = async_json
        return data

    async def __request(
        self, session: aiohttp.ClientSession, method: str, url: str, json, files=None
    ) -> aiohttp.ClientResponse:

        if files:
            async with session.request(
                method, url, data=dict(**files, **json)
            ) as response:
                await response.read()
                return await self._make_async(response)

        async with session.request(method, url, json=json) as response:
            await response.read()
            return await self._make_async(response)

    async def _request(
        self, method: str, url: str, json=None, files=None
    ) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await self.__request(session, method, url, json, files=files)

    def get(self, url: str) -> Coroutine:
        return self._request("GET", url)

    def post(self, url: str, json, files=None) -> Coroutine:
        return self._request("POST", url, json, files=files)

    def put(self, url: str, json) -> Coroutine:
        return self._request("PUT", url, json)

    def patch(self, url: str, json) -> Coroutine:
        return self._request("PATCH", url, {} if not json else json)

    def delete(self, url: str) -> Coroutine:
        return self._request("DELETE", url)
