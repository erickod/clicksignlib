from unittest.mock import Mock

from clicksignlib import ClickSign, __version__
from clicksignlib.environments import SandboxEnvironment


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_clicksignlib_has_a_ClickSign_class_to_import() -> None:
    from clicksignlib import ClickSign

    assert ClickSign


def test_ClickSign_instantiation_params() -> None:
    access_token = "any valid token"
    env = SandboxEnvironment()
    requests = Mock()

    sut = ClickSign(
        access_token=access_token, environment=env, requests_adapter=requests
    )
    assert sut._access_token == access_token
    assert sut._environment == env
    assert sut._requests_adapter == requests
