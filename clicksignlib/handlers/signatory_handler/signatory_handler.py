from typing import Any, Dict

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
        auths: Auth,
        documentation: str = "",
        birthday: str = "",
        email: str = "",
        phone_number: str = "",
        notify: bool = True,
        selfie_enabled: bool = False,
        handwritten_enabled: bool = True,
        liveness_enabled: bool = False,
        has_documentation: bool = False,
    ) -> Any:

        validators = {
            "auths": {
                "email": {"required_params": ["email"]},
                "api": {"required_params": ["email", "documentation", "birthday"]},
                "sms": {"required_params": ["phone_number", "email"]},
                "whatsapp": {"required_params": ["phone_number"]},
                "pix": {"required_params": ["documentation"]},
                "icpbrasil": {
                    "required_params": [
                        "selfie_enabled",
                        "handwritten_enabled",
                        "liveness_enabled",
                    ]
                },
            },
            "params": {
                "documentation": {"required_params": ["has_documentation"]},
                "birthday": {"required_params": ["has_documentation"]},
                "has_documentation": {"required_params": ["documentation", "birthday"]},
            },
        }

        request_payload: Dict["str", Any] = {
            "signer": {
                "name": name,
                "auths": [auths.value],
                "official_document_enabled": False,
                "email": email,
            }
        }

        params = locals()

        for key, value in validators["auths"].items():
            required_params = value["required_params"]
            if key == auths.value:
                for param in required_params:
                    request_payload["signer"][param] = params[param]
                    if params[param]:
                        continue
                    raise RequiredParameters(
                        f"To use {key.upper()} Auth set the {param} param."
                    )

        for key, value in validators["params"].items():
            required_params = value["required_params"]
            if params[key]:
                for param in required_params:
                    request_payload["signer"][param] = params[param]
                    if params[param]:
                        continue
                    raise RequiredParameters(f"To use {key} set the {param} param.")

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
        request_payload: Dict["str", Any] = {
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
            response_data=self.config.requests.post(
                endpoint,
                json=request_payload,
            ),
        )
