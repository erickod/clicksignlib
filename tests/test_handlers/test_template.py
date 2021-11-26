from clicksignlib.environments import SandboxEnvironment
from clicksignlib.handlers import Template

name = "any valid template name"
access_token = "any valid access token"


def test_handlers_has_a_template_package() -> None:
    import clicksignlib

    assert hasattr(clicksignlib.handlers, "Template")


def test_Template_instantiation_params() -> None:
    env = SandboxEnvironment()
    sut = Template(name=name, access_token=access_token, environment=env)

    assert sut._name == name
    assert sut._content == b""
    assert sut._access_token == access_token
    assert sut._environment == env
    assert sut._status_code == 0
