import uuid
from unittest.mock import Mock

import clicksignlib
import pytest
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.utils import Result
from clicksignlib.utils.errors import InvalidKeyError

access_token = "any valid token"
api_version = "/api/v1"
template_key = str(uuid.uuid4())
valid_template_filename = "test.docx"
invalid_template_filename = "test.ppt"
template_data = {"key": "value"}
document_key = "cf89212c-68d8-4cdc-a7aa-c42a194798f3"
env = SandboxEnvironment()


def test_DocumentHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "DocumentHandler")


def test_ensure_DocumentHandler_intantiation_params() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert sut.config.access_token == access_token
    assert sut.config.environment == env


def test_DocumentHandler_base_endpoint_returns_the_env_endpoint() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    sut.base_endpoint == env.endpoint


def test_DocumentHandler_full_endpoint_return() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    endpoint = f"{sut.base_endpoint}{sut.config.api_version}"
    endpoint = f"{endpoint}/documents?access_token={sut.config.access_token}"
    assert sut.full_endpoint == endpoint


def test_DocumentHandler_create_from_template() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    result = sut.create_from_template(
        document_type="Contratos",
        filename=valid_template_filename,
        template_key=template_key,
        template_data=template_data,
    )

    assert type(result)


def test_DocumentHandler_raises_when_create_from_template_receives_an_invalid_key() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )

    with pytest.raises(InvalidKeyError):
        sut.create_from_template(
            document_type="Contratos",
            filename=valid_template_filename,
            template_key="invalid key",
            template_data=template_data,
        )


def test_DocumentHandler_list_returns_a_Result():
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )

    assert type(sut.list(page_number=1)) is Result


@pytest.mark.parametrize("page_number", [1, 10, 15, 150])
def test_DocumentHandler_list_calls_get_from_adapter_with_right_params(page_number):
    adapter = Mock()
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=adapter,
    )
    sut.list(page_number=page_number)
    endpoint = (
        f"/api/v1/documents?access_token={sut.config.access_token}&page={page_number}"
    )
    adapter.get.assert_called_with(url=f"{sut.base_endpoint}{endpoint}")


def test_DocumentHandler_detail_returns_a_Result():
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )

    assert type(sut.detail(document_key=document_key)) is Result


def test_DocumentHandler_create_from_bytes_returns_a_Result() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert type(sut.create_from_bytes("test.docx", "test", data=b"any bytes")) is Result


def test_finish_document_returns_a_Result() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert type(sut.finish(document_key=document_key)) is Result


def test_finish_document_calls_patch_from_request_adapter() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=Mock(),
    )
    sut.finish(document_key=document_key)
    sut.config.requests.patch.assert_called_with(
        url=f"{sut.base_endpoint}/api/v1/documents/{document_key}/finish?access_token={access_token}",
        json={},
    )


def test_cancel_document_returns_a_Result() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert type(sut.cancel(document_key=document_key)) is Result


def test_cancel_document_calls_patch_from_request_adapter() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=Mock(),
    )
    sut.cancel(document_key=document_key)
    sut.config.requests.patch.assert_called_with(
        url=f"{sut.base_endpoint}/api/v1/documents/{document_key}/cancel?access_token={access_token}",
        json={},
    )


def test_delete_document_returns_a_Result() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert type(sut.delete(document_key=document_key)) is Result


def test_delete_calls_patch_from_request_adapter() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=Mock(),
    )
    sut.delete(document_key=document_key)
    sut.config.requests.delete.assert_called_with(
        url=f"{sut.base_endpoint}/api/v1/documents/{document_key}?access_token={access_token}"
    )


def test_configure_document_returns_a_Result() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert type(sut.configure(document_key=document_key)) is Result
