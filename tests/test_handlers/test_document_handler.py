import uuid

import clicksignlib
import pytest
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.errors import InvalidKeyError

access_token = "any valid token"
api_version = "/api/v1"
template_key = str(uuid.uuid4())
valid_template_filename = "test.docx"
invalid_template_filename = "test.ppt"
template_data = {"key": "value"}
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
    endpoint = (
        f"{endpoint}/templates/{'{}'}/documents?access_token={sut.config.access_token}"
    )
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
