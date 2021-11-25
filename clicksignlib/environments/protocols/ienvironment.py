from typing import Protocol


class IEnvironment(Protocol):
    title: str
    endpoint: str
