import clicksignlib


def test_clicksignlib_has_a_handlers_package() -> None:
    assert hasattr(clicksignlib, "handlers")


def test_clicksignlib_has_a_mixins_package() -> None:
    assert hasattr(clicksignlib.handlers, "mixins")
