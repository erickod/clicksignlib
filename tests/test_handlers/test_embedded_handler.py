import pytest
from clicksignlib.environments import ProductionEnvironment, SandboxEnvironment
from clicksignlib.handlers import EmbeddedHandler

sanbox_env = SandboxEnvironment()
prod_env = ProductionEnvironment()


@pytest.mark.parametrize("environment", [sanbox_env, prod_env])
def test_EmbeddedHandler_get_widget_link_is_using_Environment_with_false_use_token(
    environment,
) -> None:
    sut = EmbeddedHandler(environment=environment)
    assert environment.endpoint in sut.get_widget_link()


def test_EmbeddedHandler_get_widget_link_return_when_using_true_use_token() -> None:
    sut = EmbeddedHandler(environment=sanbox_env)
    assert "embedded.js" in sut.get_widget_link(use_token=True)
