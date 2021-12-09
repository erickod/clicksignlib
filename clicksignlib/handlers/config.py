from abc import ABC, abstractmethod

from clicksignlib.environments.protocols import IEnvironment


class Config(ABC):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        requests_adapter,
        api_version: str,
    ) -> None:
        self.access_token = access_token
        self.environment = environment
        self.requests = requests_adapter
        self.api_version = api_version
