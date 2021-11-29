import requests
from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import BaseHandler
from clicksignlib.utils import Payload


class SignatoryHandler(BaseHandler):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str = "/api/v1",
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
        endpoint = f"{endpoint}/signers?access_token={self._access_token}"

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
    ) -> Payload:
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
        res = self._requests.post(self.full_endpoint, json=request_payload)
        return Payload(res.json(), res.status_code)
