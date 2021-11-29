from typing import Any, Dict

import requests
from clicksignlib.environments.protocols import IEnvironment

from .document import Document


class DocumentHandler:
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str = "/api/v1",
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
        # endpoint = f"{self.base_endpoint}{self._api_version}"
        endpoint = f"{self.base_endpoint}/api/v1"
        endpoint = (
            f"{endpoint}/templates/{'{}'}/documents?access_token={self._access_token}"
        )

        return endpoint

    def create(self, document: Document) -> Any:
        print(document)
