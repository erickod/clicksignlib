import requests
from clicksignlib.environments.protocols import IEnvironment


class Template:
    def __init__(
        self,
        *,
        name: str,
        access_token: str,
        environment: IEnvironment,
    ) -> None:
        self._name = name
        self._access_token = access_token
        self._environment = environment
        self._content: bytes = b""
        self._status_code: int = 0
