from .environment_abc import EnvironmentABC


class TestEnvironment(EnvironmentABC):
    def __init__(
        self,
        title: str = "Test Environment",
        endpoint: str = "https://sandbox.clicksign.com",
    ) -> None:
        super().__init__(title, endpoint)
