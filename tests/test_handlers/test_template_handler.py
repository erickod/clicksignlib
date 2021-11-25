import clicksignlib


def test_ensure_TemplateHandler_can_be_imported_from_clicksignlib_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "TemplateHandler")


def test_ensure_TemplateHandler_intantiation_params() -> None:
    access_token = "any valid token"
    env = clicksignlib.environments.SandboxEnvironment()
    sut = clicksignlib.handlers.TemplateHandler(
        access_token=access_token, environment=env
    )
    assert sut._access_token == access_token
    assert sut._environment == env
