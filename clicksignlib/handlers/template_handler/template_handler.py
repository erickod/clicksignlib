from pathlib import Path
from typing import Any

import requests
from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin


class TemplateHandler(EndpointMixin):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str = "/api/v2",
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
        endpoint = f"{endpoint}/templates?access_token={self.config.access_token}"
        return endpoint

    def create(self, name: str, content: bytes) -> Any:
        return self.config.requests.post(
            url=self.full_endpoint,
            files={
                "template[content]": content,
            },
            data={
                "template[name]": name,
            },
        )

    def list(self) -> Any:
        return self.config.requests.get(self.full_endpoint)

    def create_from_bytes(self, file_path: str, data: bytes) -> Any:
        filename: str = Path(file_path).name
        return self.create(filename, data)

    def create_from_file(self, file_path: str) -> Any:
        with open(file_path, "rb") as f:
            return self.create_from_bytes(file_path, f.read())
