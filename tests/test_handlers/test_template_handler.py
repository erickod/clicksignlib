import clicksignlib


def test_ensure_TemplateHandler_can_be_imported_from_clicksignlib_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "TemplateHandler")


def test_ensure_TemplateHandler_needs_a_access_token_when_its_intantiated() -> None:
    access_token = "any valid token"
    sut = clicksignlib.handlers.TemplateHandler(access_token=access_token)
    assert sut._access_token == access_token
