import asyncio
from unittest.mock import MagicMock, Mock

import pytest
from clicksignlib import ClickSign, __version__, wait_future
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.handlers import (
    DocumentHandler,
    EmbeddedHandler,
    NotificationHandler,
    SignatoryHandler,
    TemplateHandler,
)
from clicksignlib.utils.errors import ApiError

access_token = "any valid token"
env = SandboxEnvironment()


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_clicksignlib_has_a_ClickSign_class_to_import() -> None:
    from clicksignlib import ClickSign

    assert ClickSign


def test_ClickSign_instantiation_params() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert sut._access_token == access_token
    assert sut._environment == env
    assert sut._requests_adapter == requests


def test_clickSign_template_property() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert isinstance(sut.template, TemplateHandler)


def test_clickSign_document_property() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert isinstance(sut.document, DocumentHandler)


def test_clickSign_signers_property() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert isinstance(sut.signers, SignatoryHandler)


def test_clickSign_notification_property() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert isinstance(sut.notification, NotificationHandler)


def test_clickSign_widget_property() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert isinstance(sut.widget, EmbeddedHandler)


@pytest.mark.parametrize("status_code", [400, 403, 404, 500])
def test_Clicksign_wait_future_method_raises_when_status_code_is_not_acceptable(
    status_code,
):
    async def json():
        json = MagicMock()
        json["errors"] = ["Test Error"]
        return json

    async def make_response():

        response_data = Mock()
        response_data.status_code = status_code
        response_data.json = json
        return response_data

    result = Mock()
    result.response_data = make_response()

    with pytest.raises(ApiError):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(wait_future(result))
