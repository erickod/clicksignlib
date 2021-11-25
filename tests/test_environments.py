import clicksignlib


def test_enviroments_package_exists() -> None:
    assert hasattr(clicksignlib, "environments")


def test_EnviromentABC_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "EnvironmentABC")


def test_TestEnviroment_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "TestEnvironment")


def test_ProductionEnvironment_exists_in_environments_package() -> None:
    assert hasattr(clicksignlib.environments, "ProductionEnvironment")
