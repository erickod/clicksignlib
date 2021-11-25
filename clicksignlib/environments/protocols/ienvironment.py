from typing_extensions import Protocol


class IEnvironment(Protocol):
    title: str
    endpoint: str
