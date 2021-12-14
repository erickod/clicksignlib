from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Union

from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin
from clicksignlib.utils import Result, bytes_to_base64, calc_hmac_sum
from clicksignlib.utils.validators import UUIDValidator


class DocumentHandler(EndpointMixin):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        requests_adapter,
        api_version: str = "/api/v1",
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
        return f"{endpoint}/documents?access_token={self.config.access_token}"

    def __bytes_to_base64(
        self,
        file_path: str,
        data: bytes,
        decode="utf-8",
    ) -> Union[str, bytes]:
        return bytes_to_base64(file_path, data, decode=decode)

    def create_from_bytes(
        self,
        file_path: str,
        document_type: str,
        data: bytes,
    ) -> Result:
        filename: str = Path(file_path).name
        request_payload: Dict[str, Any] = {
            "document": {
                "path": f"/{document_type}/{filename}",
                "content_base64": self.__bytes_to_base64(file_path, data),
                # "deadline_at": "2020-01-05T14:30:59-03:00",
                "auto_close": True,
                "locale": "pt-BR",
                "sequence_enabled": False,
            }
        }

        res = self.config.requests.post(self.full_endpoint, request_payload)
        return Result(request_data=request_payload, response_data=res)

    def create_from_file(
        self,
        file_path: str,
        document_type: str,
    ) -> Result:
        with open(file_path, "rb") as f:
            return self.create_from_bytes(file_path, document_type, f.read())

    def create_from_template(
        self,
        *,
        document_type: str,
        filename: str,
        template_key: str,
        template_data: Dict[str, Any],
    ) -> Result:

        UUIDValidator(field_name="template_key").validate(template_key)

        remote_path = Path("/", document_type, filename)
        request_payload = {
            "document": {
                "path": str(remote_path),
                "template": {"data": template_data},
            }
        }
        endpoint = f"{self.base_endpoint}/api/v2"
        endpoint = f"{endpoint}/templates/{'{}'}/documents?access_token={self.config.access_token}"
        res = self.config.requests.post(
            endpoint.format(template_key), json=request_payload
        )

        return Result(request_data=request_payload, response_data=res)

    def list(self, *, page_number: int) -> Result:
        res = self.config.requests.get(url=f"{self.full_endpoint}&page={page_number}")
        return Result(request_data={}, response_data=res)

    def detail(self, *, document_key: str) -> Result:
        UUIDValidator(field_name="document_key").validate(document_key)
        endpoint = (
            f"/api/v1/documents/{document_key}?access_token={self.config.access_token}"
        )
        res = self.config.requests.get(url=f"{self.base_endpoint}{endpoint}")
        return Result(request_data={}, response_data=res)

    def delete(self, *, document_key: str) -> Result:
        UUIDValidator(field_name="document_key").validate(document_key)
        endpoint = (
            f"/api/v1/documents/{document_key}?access_token={self.config.access_token}"
        )
        res = self.config.requests.delete(url=f"{self.base_endpoint}{endpoint}")
        return Result(request_data={}, response_data=res)

    def finish(self, *, document_key: str) -> Result:
        UUIDValidator(field_name="document_key").validate(document_key)
        endpoint = f"/api/v1/documents/{document_key}/finish?access_token={self.config.access_token}"
        res = self.config.requests.patch(url=f"{self.base_endpoint}{endpoint}", json={})
        return Result(request_data={}, response_data=res)

    def cancel(self, *, document_key: str) -> Result:
        UUIDValidator(field_name="document_key").validate(document_key)
        endpoint = f"/api/v1/documents/{document_key}/cancel?access_token={self.config.access_token}"
        res = self.config.requests.patch(url=f"{self.base_endpoint}{endpoint}", json={})
        return Result(request_data={}, response_data=res)

    def configure(
        self,
        *,
        document_key: str,
        deadline_at: Optional[datetime] = None,
        auto_close: bool = True,
        sequence_enabled: bool = False,
        remind_interval: int = 1,
    ) -> Result:
        UUIDValidator(field_name="document_key").validate(document_key)
        payload = {
            "auto_close": auto_close,
            "locale": "pt-BR",
            "sequence_enabled": sequence_enabled,
            "remind_interval": remind_interval,
        }

        if deadline_at:
            payload["deadline_at"] = deadline_at.strftime("%Y-%m-%dT%H:%M:%S-03:00")

        endpoint = (
            f"/api/v1/documents/{document_key}?access_token={self.config.access_token}"
        )
        res = self.config.requests.patch(
            url=f"{self.base_endpoint}{endpoint}", json=payload
        )
        return Result(request_data={}, response_data=res)

    def sign_by_api(
        self, request_signature_key: str, secret_hmac_sha256: str
    ) -> Result:
        UUIDValidator(field_name="request_signature_key").validate(
            request_signature_key
        )
        endpoint = (
            f"{self.base_endpoint}/api/v1/sign?access_token={self.config.access_token}"
        )
        request_payload = {
            "request_signature_key": request_signature_key,
            "secret_hmac_sha256": self._calc_hmac_sum(
                request_signature_key, secret_hmac_sha256
            ),
        }
        res = self.config.requests.post(url=endpoint, json=request_payload)
        return Result(request_data=request_payload, response_data=res)

    def _calc_hmac_sum(
        self, request_signature_key: str, secret_hmac_sha256: str
    ) -> str:
        return calc_hmac_sum(request_signature_key, secret_hmac_sha256)
