import requests
from clicksignlib.environments.protocols import IEnvironment


class Template:
    def __init__(
        self,
        *,
        name: str,
        access_token: str,
        environment: IEnvironment,
        requests_adapter=requests,
    ) -> None:
        self._name = name
        self._access_token = access_token
        self._environment = environment
        self._requests = requests_adapter
        self._content: bytes = b""

    @property
    def base_endpoint(self) -> str:
        return self._environment.endpoint
