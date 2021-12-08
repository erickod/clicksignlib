from typing import Any

from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin
from clicksignlib.utils import Result
from clicksignlib.utils.errors import RequiredParameters

from .signer_type import Auth, SignerType


class SignatoryHandler(EndpointMixin):
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
        return f"{endpoint}/signers?access_token={self.config.access_token}"

    def create(
        self,
        *,
        name: str,
        cpf: str = "",
        birthday: str = "",
        email: str = "",
        phone_number: str = "",
        auths: Auth = Auth.EMAIL,
        notify: bool = True,
        handwritten_enabled: bool = True,
    ) -> Any:

        if auths in (Auth.EMAIL, Auth.API) and not email:
            raise RequiredParameters(
                "email field is required if auths equal to EMAIL or API."
            )

        if auths in (Auth.WHATSAPP, Auth.SMS) and not phone_number:
            raise RequiredParameters(
                "phone_number field is required if auths equal to SMS."
            )

        request_payload = {
            "signer": {
                "name": name,
                "phone_number": phone_number,
                "auths": [auths.value],
                "selfie_enabled": False,
                "handwritten_enabled": handwritten_enabled,
                "official_document_enabled": False,
                "liveness_enabled": False,
                "delivery": "email" if notify else None,
            }
        }
        if email:
            request_payload["signer"]["email"] = email
            request_payload["signer"]["auths"].append("email")

        if birthday:
            request_payload["signer"]["birthday"] = birthday

        if cpf:
            request_payload["signer"]["documentation"] = cpf
            request_payload["signer"]["has_documentation"] = True

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
    ) -> Result:
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
