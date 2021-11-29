import clicksignlib
from clicksignlib.environments import SandboxEnvironment

access_token = "any valid token"
api_version = "/api/v1"
env = SandboxEnvironment()


def test_DocumentHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "DocumentHandler")


def test_ensure_DocumentHandler_intantiation_params() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert sut._access_token == access_token
    assert sut._environment == env


def test_DocumentHandler_base_endpoint_returns_the_env_endpoint() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    sut.base_endpoint == env.endpoint


def test_DocumentHandler_full_endpoint_return() -> None:
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    endpoint = f"{sut.base_endpoint}{sut._api_version}"
    endpoint = f"{endpoint}/templates/{'{}'}/documents?access_token={sut._access_token}"
    assert sut.full_endpoint == endpoint
