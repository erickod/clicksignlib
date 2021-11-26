from pathlib import Path
from typing import Any, Dict


class Template:
    def __init__(self) -> None:
        self._path = ""
        self._content: bytes = b""
        self._status_code: int = 0
        self._payload: Dict["str", Any] = {}

    def as_dict(self) -> Dict[str, Any]:
        return {
            "template[content]": self._content,
            "template[name]": self.name,
        }

    def from_bytes(self, file_path: str, data: bytes) -> None:
        self._path = file_path
        self._content = data

    def from_file(self, file_path: str) -> None:
        with open(file_path, "rb") as f:
            self.from_bytes(f.read())

    def is_valid(self) -> bool:
        if not bool(self.name and self._content):
            raise ValueError("call from_bytes or from_file before call is_valid")
        return True

    @property
    def name(self) -> str:
        if self._path:
            return Path(self._path).name
        return ""
