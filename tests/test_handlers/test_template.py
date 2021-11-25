import requests
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.handlers import Template


def test_handlers_has_a_template_package() -> None:
    import clicksignlib

    assert hasattr(clicksignlib.handlers, "Template")


def test_Template_instantiation_parmas() -> None:
    access_token = "any valid access token"
    env = SandboxEnvironment()
    sut = Template(access_token=access_token, environment=env)

    assert sut._access_token == access_token
    assert sut._environment == env
    assert sut._requests == requests
