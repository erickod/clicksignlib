from pathlib import Path
from typing import Any, Dict

import requests
from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import BaseHandler
from clicksignlib.utils import Payload


class DocumentHandler(BaseHandler):
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
        endpoint = (
            f"{endpoint}/templates/{'{}'}/documents?access_token={self._access_token}"
        )

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
        res = self._requests.post(
            self.full_endpoint.format(template_key), json=request_payload
        )
        response_payload: Dict[str, Any] = self.full_endpoint.format(template_key)
        return Payload(response_payload, res.status_code)
