from unittest.mock import Mock

import clicksignlib
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.utils.result import Result

name = "any valid template name"
access_token = "any valid token"
api_version = "/api/v2"


def test_TemplateHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "TemplateHandler")


def test_ensure_TemplateHandler_intantiation_params() -> None:
    env = clicksignlib.environments.SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert sut.config.access_token == access_token
    assert sut.config.environment == env


def test_TemplateHandler_base_endpoint_returns_the_env_endpoint() -> None:
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    sut.base_endpoint == env.endpoint


def test_TemplateHandler_full_endpoint_return() -> None:
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    endpoint = f"{sut.base_endpoint}/{sut.config.api_version}"
    endpoint = f"{endpoint}/templates?access_token={sut.config.access_token}"
    sut.full_endpoint == endpoint


def test_TemplateHandler_create_calls_post_from_request_adapter() -> None:
    content = b""
    request = Mock()
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=request,
    )
    sut.create(name, content)
    request.post.assert_called_once()


def test_TemplateHandler_create_return_type() -> None:
    response = Mock()
    template = Mock()
    request = Mock()
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=request,
    )
    response = sut.create(name, template)
    assert type(response) is Result


def test_TemplateHandler_list_method_calls_adapter_get() -> None:
    request = Mock()
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=request,
    )
    sut.list()
    request.get.assert_called_with(sut.full_endpoint)


def test_TemplateHandler_create_from_bytes_calls_create() -> None:
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token,
        environment=SandboxEnvironment(),
        api_version=api_version,
    )
    sut.create = Mock()
    sut.create_from_bytes("test.docx", b"any bytes")
    sut.create.assert_called()
