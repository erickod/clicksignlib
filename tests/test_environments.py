import clicksignlib
import pytest
from clicksignlib.environments import (
    EnvironmentABC,
    ProductionEnvironment,
    SandboxEnvironment,
)


def test_enviroments_package_exists() -> None:
    assert hasattr(clicksignlib, "environments")


def test_EnviromentABC_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "EnvironmentABC")


def test_TestEnviroment_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "SandboxEnvironment")


def test_ProductionEnvironment_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "ProductionEnvironment")


def test_ProductionEnvironment_default_instantiation_params() -> None:
    sut = ProductionEnvironment()
    assert sut.title == "Production Environment"
    assert sut.endpoint == "https://app.clicksign.com"


def test_TestEnvironment_default_instantiation_params() -> None:
    sut = SandboxEnvironment()
    assert sut.title == "Sandbox Environment"
    assert sut.endpoint == "https://sandbox.clicksign.com"
