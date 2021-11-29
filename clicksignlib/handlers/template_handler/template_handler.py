from pathlib import Path

import requests
from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import BaseHandler
from clicksignlib.utils import Payload


class TemplateHandler(BaseHandler):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str = "/api/v2",
        requests_adapter=requests,
    ) -> None:
        super().__init__(
            access_token=access_token,
            environment=environment,
            api_version=api_version,
            requests_adapter=requests_adapter,
        )

    @property
    def full_endpoint(self) -> str:
        endpoint = f"{self.base_endpoint}{self._api_version}"
        endpoint = f"{endpoint}/templates?access_token={self._access_token}"
        return endpoint

    def create(self, name: str, content: bytes) -> Payload:
        request_payload = {
            "template[content]": content,
            "template[name]": name,
        }
        res = self._requests.post(url=self.full_endpoint, files=request_payload)
        return Payload(res.json(), res.status_code)

    def list(self) -> Payload:
        res = self._requests.get(self.full_endpoint)
        return Payload(res.json(), res.status_code)

    def create_from_bytes(self, file_path: str, data: bytes) -> Payload:
        filename: str = Path(file_path).name
        return self.create(filename, data)

    def create_from_file(self, file_path: str) -> Payload:
        with open(file_path, "rb") as f:
            return self.create_from_bytes(file_path, f.read())
