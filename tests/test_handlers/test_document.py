def test_handlers_has_a_Document_class() -> None:
    import clicksignlib

    assert hasattr(clicksignlib.handlers, "Document")
