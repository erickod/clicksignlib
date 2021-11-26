import clicksignlib
from clicksignlib.environments import SandboxEnvironment

name = "any valid template name"
access_token = "any valid token"
api_version = "/api/v2"


def test_ensure_TemplateHandler_can_be_imported_from_clicksignlib_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "TemplateHandler")


def test_ensure_TemplateHandler_intantiation_params() -> None:
    env = clicksignlib.environments.SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert sut._access_token == access_token
    assert sut._environment == env


def test_TemplateHandler_base_endpoint_returns_the_env_endpoint_() -> None:
    env = SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    sut.base_endpoint == env.endpoint
