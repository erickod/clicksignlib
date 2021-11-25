import clicksignlib


def test_enviroments_package_exists() -> None:
    assert hasattr(clicksignlib, "environments")
