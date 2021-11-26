import requests

from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import TemplateHandler


class ClickSign:
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        requests_adapter=requests,
    ) -> None:
        self._access_token = access_token
        self._environment = environment
        self._requests_adapter = requests_adapter

    @property
    def template(self) -> TemplateHandler:
        return TemplateHandler(
            access_token=self._access_token,
            environment=self._environment,
            requests_adapter=self._requests_adapter,
            api_version="/api/v2",
        )
