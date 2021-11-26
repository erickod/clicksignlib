import clicksignlib

access_token = "any valid token"
api_version = "/api/v2"


def test_TemplateHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "DocumentHandler")


def test_ensure_TemplateHandler_intantiation_params() -> None:
    env = clicksignlib.environments.SandboxEnvironment()
    sut = clicksignlib.handlers.DocumentHandler(
        access_token=access_token, environment=env, api_version=api_version
    )
    assert sut._access_token == access_token
    assert sut._environment == env
