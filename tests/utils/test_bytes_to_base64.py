import re

import pytest
from clicksignlib.utils import bytes_to_base64

pdf = "test.pdf"
docx = "test.docx"
doc = "test.doc"
bytes_value = b"TESTING"


def test_bytes_to_base_64_returns_an_str_by_default():
    assert type(bytes_to_base64(docx, bytes_value)) is str


def test_bytes_to_base_64_returns_bytes_with_a_false_decode_value():
    assert type(bytes_to_base64(docx, bytes_value, decode="")) is bytes


@pytest.mark.parametrize("file_path", [doc, docx, pdf])
def test_bytes_to_base_64_has_the_header_in_return(file_path):
    assert re.match(
        r"^data:application/.*;base64,",
        bytes_to_base64(docx, bytes_value),
    )
