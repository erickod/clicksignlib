from typing import Any, Dict

from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin
from clicksignlib.utils import Result
from clicksignlib.utils.errors import InvalidParameters, RequiredParameters

from .auths_type import Auth
from .signer_type import SignerType


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
        official_document_enabled: bool = False,
    ) -> Any:

        validation_rules = {
            "auths": {
                "email": {
                    "required_params": ["email"],
                    "rejected_params": [],
                },
                "api": {
                    "required_params": [
                        "email",
                        "documentation",
                        "birthday",
                    ],
                    "rejected_params": [
                        "selfie_enabled",
                        "liveness_enabled",
                    ],
                },
                "sms": {
                    "required_params": [
                        "phone_number",
                        "email",
                    ],
                    "rejected_params": [],
                },
                "whatsapp": {
                    "required_params": ["phone_number", "email"],
                    "rejected_params": [],
                },
                "pix": {
                    "required_params": [
                        "documentation",
                        "has_documentation",
                        "email",
                    ],
                    "rejected_params": [],
                },
                "icp_brasil": {
                    "required_params": ["email", "has_documentation"],
                    "rejected_params": [
                        "selfie_enabled",
                        "liveness_enabled",
                        "official_document_enabled",
                    ],
                },
            },
            "params": {
                "documentation": {
                    "required_params": ["has_documentation"],
                    "rejected_params": [],
                },
                "birthday": {
                    "required_params": ["has_documentation"],
                    "rejected_params": [],
                },
                "has_documentation": {
                    "required_params": [
                        "documentation",
                        "birthday",
                    ],
                    "rejected_params": [],
                },
            },
        }

        request_payload: Dict["str", Any] = {
            "signer": {
                "name": name,
                "auths": [auths.value],
                "official_document_enabled": official_document_enabled,
                "email": email,
                "selfie_enabled": selfie_enabled,
                "liveness_enabled": liveness_enabled,
            }
        }

        params = locals()

        for key, value in validation_rules["auths"].items():
            required_params = value["required_params"]
            rejected_params = value["rejected_params"]

            if key == auths.value:
                for param in rejected_params:
                    del request_payload["signer"][param]
                    if params[param]:
                        raise InvalidParameters(
                            f"To use {key.upper()} Auth remove the {param} param."
                        )

                for param in required_params:
                    request_payload["signer"][param] = params[param]
                    if params[param]:
                        continue
                    raise RequiredParameters(
                        f"To use {key.upper()} Auth set the {param} param."
                    )

        for key, value in validation_rules["params"].items():
            required_params = value["required_params"]
            rejected_params = value["rejected_params"]

            for param in rejected_params:
                del request_payload["signer"][param]
                if params[param]:
                    raise InvalidParameters(f"To use {key} remove the {param} param.")

            if params[key]:
                for param in required_params:
                    request_payload["signer"][param] = params[param]
                    if not params[param]:
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

    def detail(self, signer_key: str) -> Result:
        endpoint = self.full_endpoint.replace("?", f"/{signer_key}?")
        res = self.config.requests.get(endpoint)
        return Result(request_data={}, response_data=res)
