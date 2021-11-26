from typing import Any, Dict

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

    def as_dict(self) -> Dict[str, Any]:
        return {
            "template[content]": self._content,
            "template[name]": self._name,
        }

    def from_bytes(self, data: bytes) -> None:
        self._content = data

    def from_file(self, file_path: str) -> None:
        with open(file_path, "rb") as f:
            self.from_bytes(f.read())

    def is_valid(self) -> bool:
        return True
