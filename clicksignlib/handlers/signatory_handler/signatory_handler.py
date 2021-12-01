from typing import Any

import requests
from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin
from clicksignlib.utils import Result

from .signer_type import SignerType


class SignatoryHandler(EndpointMixin):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str = "/api/v1",
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
        endpoint = f"{endpoint}/signers?access_token={self.config.access_token}"

        return endpoint

    def create(
        self,
        *,
        name: str,
        cpf: str,
        birthday: str,
        email: str,
        phone_number: str,
        notify: bool = True,
    ) -> Any:
        request_payload = {
            "signer": {
                "name": name,
                "email": email,
                "phone_number": phone_number,
                "auths": ["email"],
                "documentation": cpf,
                "birthday": birthday,
                "has_documentation": True,
                "selfie_enabled": False,
                "handwritten_enabled": False,
                "official_document_enabled": False,
                "liveness_enabled": False,
                "delivery": "email" if notify else None,
            }
        }
        return Result(
            request_data=request_payload,
            response_data=self.config.requests.post(
                self.full_endpoint, json=request_payload
            ),
        )

    def add_signatory_to_document(
        self,
        document_key: str,
        signer_key: str,
        signer_type: SignerType,
        message: str,
        group: int = 0,
    ) -> Any:
        endpoint: str = f"{self.config.environment.endpoint}/api/v1/lists?"
        endpoint = f"{endpoint}access_token={self.config.access_token}"
        request_payload = {
            "list": {
                "document_key": document_key,
                "signer_key": signer_key,
                "sign_as": signer_type.value,
                "message": message,
            }
        }

        if group:
            request_payload["sequence_enabled"] = True
            request_payload["group"] = group

        return Result(
            request_data=request_payload,
            response_data=self.config.requests.post(endpoint, json=request_payload),
        )
