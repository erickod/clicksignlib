import requests
from clicksignlib.environments.protocols import IEnvironment


class Template:
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        requests_adapter=requests,
    ) -> None:
        self._access_token = access_token
        self._environment = environment
        self._requests = requests_adapter
