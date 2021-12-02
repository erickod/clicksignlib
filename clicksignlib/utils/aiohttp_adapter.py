from typing import Coroutine
import aiohttp


class AioHttpAdapter:

    @staticmethod
    async def __request(session: aiohttp.ClientSession, method: str, url: str, json) -> aiohttp.ClientResponse:
        async with session.request(method, url, json=json) as response:
            return response

    async def _request(self, method: str, url: str, json=None) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await self.__request(session, method, url, json)

    def get(self, url: str) -> Coroutine:
        return self._request('GET', url)

    def post(self, url: str, json) -> Coroutine:
        return self._request('POST', url, json)

    def put(self, url: str, json) -> Coroutine:
        return self._request('PUT', url, json)

    def delete(self, url: str) -> Coroutine:
        return self._request('DELETE', url)
