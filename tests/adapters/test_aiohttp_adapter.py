import asyncio
from typing import Any
from unittest.mock import MagicMock, Mock

import asynctest
from clicksignlib.adapters import AioHttpAdapter

url = "https://example.com"
post_method = "post"
json = {"key": "value"}
files = {"fkey": "fvalue"}


def test_AioHttpAdapter_is_calling_session__request_with_right_params_when_no_file_is_passed():
    sut = AioHttpAdapter()
    FakeResponse = asynctest.CoroutineMock
    FakeResponse.read = asynctest.CoroutineMock()
    FakeResponse.status = 200
    FakeResponse.json = asynctest.CoroutineMock()
    session = asynctest.CoroutineMock()
    session.request().__aenter__.return_value = FakeResponse()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        sut._AioHttpAdapter__request(
            session,
            post_method,
            url,
            json,
            files=None,
        )
    )

    session.request.assert_called_with(post_method, url, json=json)


def test_AioHttpAdapter_is_calling_session__request_with_right_params_when_a_file_is_passed():
    sut = AioHttpAdapter()
    FakeResponse = asynctest.CoroutineMock
    FakeResponse.read = asynctest.CoroutineMock()
    FakeResponse.status = 200
    FakeResponse.json = asynctest.CoroutineMock()
    session = asynctest.CoroutineMock()
    session.request().__aenter__.return_value = FakeResponse()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        sut._AioHttpAdapter__request(
            session,
            post_method,
            url,
            json,
            files=files,
        )
    )

    session.request.assert_called_with(
        post_method,
        url,
        data=dict(**files, **json),
    )


def test_AioHttpAdapter_post_is_calling_request_with_right_params(mock):
    sut = AioHttpAdapter()
    sut._request = mock

    sut.post(url, json)
    sut._request.assert_called_with("POST", url, json, files=None)


def test_AioHttpAdapter_get_is_calling_request_with_right_params(mock):
    sut = AioHttpAdapter()
    sut._request = mock

    sut.get(url)
    sut._request.assert_called_with("GET", url)


def test_AioHttpAdapter_put_is_calling_request_with_right_params(mock):
    sut = AioHttpAdapter()
    sut._request = mock

    sut.put(url, json=json)
    sut._request.assert_called_with("PUT", url, json)


def test_AioHttpAdapter_patch_is_calling_request_with_right_params(mock):
    sut = AioHttpAdapter()
    sut._request = mock

    sut.patch(url, json)
    sut._request.assert_called_with("PATCH", url, json)


def test_AioHttpAdapter_delete_is_calling_request_with_right_params(mock):
    sut = AioHttpAdapter()
    sut._request = mock

    sut.delete(url)
    sut._request.assert_called_with("DELETE", url)
