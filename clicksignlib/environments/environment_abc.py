from abc import ABC


class EnvironmentABC(ABC):
    def __init__(self, title: str, endpoint: str) -> None:
        self.title = title
        self.endpoint = endpoint
