import requests
from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin


class NotificationHandler(EndpointMixin):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str = "/api/v1",
        requests_adapter=requests,
    ) -> None:
        self.config = Config(
            access_token=access_token,
            environment=environment,
            api_version=api_version,
            requests_adapter=requests_adapter,
        )

    @property
    def full_endpoint(self) -> str:
        endpoint = f"{self.base_endpoint}{self.config.api_version}"
        endpoint = f"{endpoint}/notifications?access_token={self.config.access_token}"
