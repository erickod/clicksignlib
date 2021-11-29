from abc import ABC, abstractmethod

import requests
from clicksignlib.environments.protocols import IEnvironment


class Config(ABC):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        api_version: str,
        requests_adapter=requests,
    ) -> None:
        self.access_token = access_token
        self.environment = environment
        self.requests = requests_adapter
        self.api_version = api_version
