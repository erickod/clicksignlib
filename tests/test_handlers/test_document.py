from unittest.mock import Mock

from clicksignlib.handlers import Document

filename = "test.docx"
file_bytes = b"testing data"


def test_handlers_has_a_Document_class() -> None:
    import clicksignlib

    assert hasattr(clicksignlib.handlers, "Document")


def test_Document_from_bytes_method() -> None:
    sut = Document()
    sut.from_bytes(filename, file_bytes)

    assert sut._content
    assert type(sut._content) is str


def test_Document_from_file_method_calls_from_bytes() -> None:
    with open(filename, "rb") as f:
        sut = Document()
        sut.from_bytes = Mock()
        sut.from_file(filename)

        sut.from_bytes.assert_called_with(filename, f.read())


def test_Document_is_valid_method_returns_true_if_everything_goes_well() -> None:
    sut = Document()
    sut._content = file_bytes
    assert sut.is_valid()


def test_Document_is_valid_method_returns_false_if_content_is_missing() -> None:
    sut = Document()
    assert not sut.is_valid()
