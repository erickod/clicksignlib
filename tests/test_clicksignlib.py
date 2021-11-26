from unittest.mock import Mock

from clicksignlib import ClickSign, __version__
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.handlers import DocumentHandler, TemplateHandler

access_token = "any valid token"
env = SandboxEnvironment()


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_clicksignlib_has_a_ClickSign_class_to_import() -> None:
    from clicksignlib import ClickSign

    assert ClickSign


def test_ClickSign_instantiation_params() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert sut._access_token == access_token
    assert sut._environment == env
    assert sut._requests_adapter == requests


def test_clickSign_template_property() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert isinstance(sut.template, TemplateHandler)


def test_clickSign_document_property() -> None:
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert isinstance(sut.document, DocumentHandler)
