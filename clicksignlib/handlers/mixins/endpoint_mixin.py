from abc import ABC, abstractmethod


class EndpointMixin(ABC):
    @property
    def base_endpoint(self) -> str:
        return self.config.environment.endpoint

    @abstractmethod
    def full_endpoint(self) -> str:
        pass
