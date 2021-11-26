from clicksignlib.handlers import Document


def test_handlers_has_a_Document_class() -> None:
    import clicksignlib

    assert hasattr(clicksignlib.handlers, "Document")


def test_Document_from_bytes_method() -> None:
    file_bytes = b"testing data"
    filename = "test.test.docx"
    sut = Document()
    sut.from_bytes(filename, file_bytes)

    assert sut._content
    assert type(sut._content) is str
