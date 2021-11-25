import clicksignlib
import pytest
from clicksignlib.environments import EnvironmentABC, ProductionEnvironment


def test_enviroments_package_exists() -> None:
    assert hasattr(clicksignlib, "environments")


def test_EnviromentABC_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "EnvironmentABC")


def test_TestEnviroment_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "TestEnvironment")


def test_ProductionEnvironment_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "ProductionEnvironment")


def test_EnvironmentABC_raises_on_calling_is_valid() -> None:
    with pytest.raises(NotImplementedError):
        sut = EnvironmentABC(title="", endpoint="")
        sut.is_valid()


def test_ProductionEnvironment_default_instantiation_params() -> None:
    sut = ProductionEnvironment()
    assert sut.title == "Production Environment"
    assert sut.endpoint == "https://app.clicksign.com"
