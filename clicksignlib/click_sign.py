import requests

from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import DocumentHandler, SignatoryHandler, TemplateHandler


class ClickSign:
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        requests_adapter=requests,
    ) -> None:
        self._access_token = access_token
        self._environment = environment
        self._requests_adapter = requests_adapter
        self._config = dict(
            access_token=self._access_token,
            environment=self._environment,
            requests_adapter=self._requests_adapter,
        )

    @property
    def document(self) -> DocumentHandler:
        return DocumentHandler(**self._config)

    @property
    def template(self) -> TemplateHandler:
        return TemplateHandler(**self._config)

    @property
    def signers(self) -> SignatoryHandler:
        return SignatoryHandler(**self._config)
