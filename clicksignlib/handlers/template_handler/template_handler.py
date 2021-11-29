from typing import Any

import requests
from clicksignlib.environments.protocols import IEnvironment


class TemplateHandler:
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str = "/api/v2",
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

    def create(self, template) -> Any:
        data = template.as_dict()
        response = self._requests.post(url=self.full_endpoint, files=data)
        template._status_code = response.status_code
        template._payload = response.json()
        return template

    def list(self) -> Any:
        return self._requests.get(self.full_endpoint).json()
