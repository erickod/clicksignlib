from .environment_abc import EnvironmentABC


class SandboxEnvironment(EnvironmentABC):
    def __init__(
        self,
        title: str = "Sandbox Environment",
        endpoint: str = "https://sandbox.clicksign.com",
    ) -> None:
        super().__init__(title, endpoint)
