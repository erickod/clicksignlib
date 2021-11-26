from unittest.mock import Mock

import clicksignlib
from clicksignlib.environments import SandboxEnvironment

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
    assert sut._access_token == access_token
    assert sut._environment == env


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
    endpoint = f"{sut.base_endpoint}/{sut._api_version}"
    endpoint = f"{endpoint}/templates?access_token={sut._access_token}"
    sut.full_endpoint == endpoint


def test_TemplateHandler_create_calls_as_dict_from_template() -> None:
    template = Mock()
    request = Mock()
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=request,
    )
    sut.create(template)
    template.as_dict.assert_called_once()


def test_TemplateHandler_create_calls_post_from_request_adapter() -> None:
    template = Mock()
    template.as_dict.return_value = {}
    request = Mock()
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=request,
    )
    sut.create(template)
    request.post.assert_called_with(
        url=sut.full_endpoint,
        files=template.as_dict(),
    )


def test_TemplateHandler_create_return() -> None:
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"key": "value"}
    template = Mock()
    template.as_dict.return_value = {}
    request = Mock()
    request.post.return_value = response
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token,
        environment=env,
        api_version=api_version,
        requests_adapter=request,
    )
    template = sut.create(template)
    assert template._status_code == response.status_code
    assert template._payload == response.json()
