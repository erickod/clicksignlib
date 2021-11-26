from unittest.mock import Mock

from clicksignlib.handlers import Template

name = "any valid template name"
data_bytes = b"any byte value"


def test_handlers_has_a_template_package() -> None:
    import clicksignlib

    assert hasattr(clicksignlib.handlers, "Template")


def test_Template_instantiation_params() -> None:
    sut = Template(name=name)

    assert sut._name == name
    assert sut._content == b""
    assert sut._status_code == 0


def test_Template_from_bytes_is_saved_in_content_property() -> None:
    sut = Template(name=name)
    sut.from_bytes(data_bytes)

    assert sut._content == data_bytes


def test_Template_from_file_calls_from_bytes_with_right_params() -> None:
    target_file = "test.docx"

    with open("test.docx", "rb") as f:
        sut = Template(name=name)
        sut.from_bytes = Mock()
        sut.from_file(target_file)
        sut.from_bytes.assert_called_with(f.read())


def test_Template_as_dict_method_return() -> None:
    sut = Template(name=name)

    assert sut.as_dict() == {
        "template[content]": sut._content,
        "template[name]": sut._name,
    }


def test_Template_is_valid_return_true_when_everything_goes_well() -> None:
    sut = Template(name=name)
    sut.from_bytes(data_bytes)

    assert sut.is_valid()


def test_Template_is_valid_return_false_when_name_is_invalid() -> None:
    sut = Template(name=name)

    assert not sut.is_valid()


def test_Template_is_valid_return_false_when_content_is_invalid() -> None:
    sut = Template(name=name)

    assert not sut.is_valid()
