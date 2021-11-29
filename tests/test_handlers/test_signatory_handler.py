from unittest.mock import Mock

import clicksignlib
from clicksignlib.environments import SandboxEnvironment

env = SandboxEnvironment()
access_token: str = "899ee68c-0a4a-48dc-9331-44844203b6b4"
api_version: str = "/api/v1"


def test_SignatoryHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "SignatoryHandler")


def test_SignatoryHandler_intantiation_params() -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env
    )
    assert sut.config.access_token == access_token
    assert sut.config.environment == env
    assert sut.config.api_version == api_version


def test_SignatoryHandler_create_method() -> None:
    requests = Mock()
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    sut.create(
        name="Erick Duarte",
        cpf="043.149.511-41",
        email="erickduarte@companyhero.com",
        birthday="1990-10-15",
        phone_number="6198464580",
    )
    requests.post.assert_called_once()
