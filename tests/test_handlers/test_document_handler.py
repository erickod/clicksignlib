import clicksignlib


def test_TemplateHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "DocumentHandler")
