import clicksignlib
import pytest
from clicksignlib.adapters import AioHttpAdapter
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.handlers import Auth, SignerType
from clicksignlib.utils.errors import InvalidParameters, RequiredParameters

env = SandboxEnvironment()
access_token: str = "899ee68c-0a4a-48dc-9331-44844203b6b4"
api_version: str = "/api/v1"


def test_BatchHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "BatchHandler")



def test_create(mock) -> None:
    sut = clicksignlib.handlers.BatchHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    sut.create(
        document_keys=["c4951f63-bee1-42c7-9bfd-4d183a248d59", "3bc71b93-4faf-4a40-b37d-abf9b04c0232"],                  
        signer_key="84053e45-247f-4260-9daf-50c7ab2944de"
    )
    mock.post.assert_called_once()
