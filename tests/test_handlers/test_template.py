import clicksignlib


def test_handlers_has_a_template_package() -> None:
    assert hasattr(clicksignlib.handlers, "Template")
