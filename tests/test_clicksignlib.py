import clicksignlib


def test_version() -> None:
    assert clicksignlib.__version__ == "0.1.0"


def test_clicksignlib_has_a_ClickSign_class_to_import() -> None:
    from clicksignlib import ClickSign
