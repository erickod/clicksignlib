from typing import Any, Dict


class Template:
    def __init__(
        self,
        *,
        name: str,
    ) -> None:
        self._name = name
        self._content: bytes = b""
        self._status_code: int = 0
        self._payload: Dict["str", Any] = {}

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
        return bool(self._name and self._content)
