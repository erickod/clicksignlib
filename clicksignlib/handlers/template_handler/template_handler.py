from pathlib import Path
from typing import Any

from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin
from clicksignlib.utils import Result


class TemplateHandler(EndpointMixin):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        requests_adapter,
        api_version: str = "/api/v2",
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

    def create(self, name: str, content: bytes) -> Result:
        request_payload = {
            "files": {
                "template[content]": content,
            },
            "data": {
                "template[name]": name,
            },
        }
        return Result(
            request_data=request_payload,
            response_data=self.config.requests.post(
                url=self.full_endpoint,
                files=request_payload["files"],
                json=request_payload["data"],
            ),
        )

    def list(self) -> Result:
        return Result(
            request_data={}, response_data=self.config.requests.get(self.full_endpoint)
        )

    def create_from_bytes(self, file_path: str, data: bytes) -> Result:
        filename: str = Path(file_path).name
        return self.create(filename, data)

    def create_from_file(self, file_path: str) -> Result:
        with open(file_path, "rb") as f:
            return self.create_from_bytes(file_path, f.read())
