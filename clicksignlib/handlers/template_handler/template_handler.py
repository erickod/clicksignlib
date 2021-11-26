import requests
from clicksignlib.environments.protocols import IEnvironment


class TemplateHandler:
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str,
        requests_adapter=requests,
    ) -> None:
        self._access_token = access_token
        self._environment = environment
        self._requests = requests_adapter
        self._api_version = api_version

    @property
    def base_endpoint(self) -> str:
        return self._environment.endpoint

    @property
    def full_endpoint(self) -> str:
        endpoint = f"{self.base_endpoint}{self._api_version}"
        endpoint = f"{endpoint}/templates?access_token={self._access_token}"
        return endpoint
