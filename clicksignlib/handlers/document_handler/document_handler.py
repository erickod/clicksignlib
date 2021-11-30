from pathlib import Path
from typing import Any, Dict

import requests
from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin
from clicksignlib.utils import Payload


class DocumentHandler(EndpointMixin):
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
        endpoint = f"{endpoint}/templates/{'{}'}/documents?access_token={self.config.access_token}"

        return endpoint

    def create_from_template(
        self,
        *,
        document_type: str,
        filename: str,
        template_key: str,
        template_data: Dict[str, Any],
    ) -> Payload:
        remote_path = Path("/", document_type, filename)
        request_payload = {
            "document": {
                "path": str(remote_path),
                "template": {"data": template_data},
            }
        }
        res = self.config.requests.post(
            self.full_endpoint.format(template_key), json=request_payload
        )
        return Payload(res.json(), res.status_code)
