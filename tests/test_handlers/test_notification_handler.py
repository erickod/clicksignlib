from unittest.mock import Mock

import clicksignlib
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.handlers import NotificationHandler
from clicksignlib.utils.result import Result

env = SandboxEnvironment()


def test_NotificationHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "NotificationHandler")


def test_NotificationHandler_notify_by_email_returns_a_Result() -> None:
    request_signature_key: str = "any valid request signature key"
    message = "Sign this doc!"

    sut = NotificationHandler(access_token="any valid access token", environment=env)
    assert (
        type(sut.notify_by_email(request_key=request_signature_key, message=message))
        is Result
    )
