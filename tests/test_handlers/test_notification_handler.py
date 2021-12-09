import clicksignlib
from clicksignlib.adapters import AioHttpAdapter
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.handlers import NotificationHandler
from clicksignlib.utils.result import Result

env = SandboxEnvironment()
access_token = "any valid access token"
request_signature_key: str = "any valid request signature key"
message = "Sign this doc!"
url = "any valid url"


def test_NotificationHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "NotificationHandler")


def test_NotificationHandler_notify_by_email_returns_a_Result() -> None:
    sut = NotificationHandler(
        access_token=access_token, environment=env, requests_adapter=AioHttpAdapter()
    )
    assert (
        type(sut.notify_by_email(request_key=request_signature_key, message=message))
        is Result
    )


def test_NotificationHandler_notify_by_email_calls_post_from_request_with_right_param(mock) -> None:
    sut = NotificationHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    sut.notify_by_email(
        request_key=request_signature_key,
        message=message,
        url=url,
    )
    mock.post.assert_called_with(
        url=sut.full_endpoint,
        json={
            "request_signature_key": request_signature_key,
            "message": message,
            "url": url,
        },
    )


def test_NotificationHandler_notify_by_email_Result_data(mock) -> None:
    sut = NotificationHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    result = sut.notify_by_email(
        request_key=request_signature_key,
        message=message,
        url=url,
    )

    assert result.request_data
    assert result.response_data


def test_ensure_notify_by_email_has_no_url_in_payload_when_it_doesnt_was_passed(mock) -> None:
    sut = NotificationHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    result = sut.notify_by_email(
        request_key=request_signature_key,
        message=message,
        url=url,
    )

    assert not hasattr(result.request_data, "url")
