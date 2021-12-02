from typing import Any, Coroutine, Dict, Protocol


class IRequest(Protocol):
    def get(self, url: str) -> Coroutine:
        pass

    def post(self, url: str, json) -> Coroutine:
        pass

    def put(self, url: str, json) -> Coroutine:
        pass

    def delete(self, url: str) -> Coroutine:
        pass
