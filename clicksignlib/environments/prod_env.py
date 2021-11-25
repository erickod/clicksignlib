from .environment_abc import EnvironmentABC


class ProductionEnvironment(EnvironmentABC):
    def __init__(
        self,
        title: str = "Production Environment",
        endpoint: str = "https://app.clicksign.com",
    ) -> None:
        super().__init__(title, endpoint)
