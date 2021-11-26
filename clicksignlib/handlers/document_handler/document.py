import base64
from pathlib import Path
from typing import Any, Dict, Union


class Document:
    def __init__(self) -> None:
        self._path: str = ""
        self._content: Union[str, bytes, Dict[str, Any]] = b""
        self._status_code: int = 0

    def from_bytes(self, file_path: str, data: bytes, decode="utf-8") -> None:
        self._path = file_path.lower()
        file_extension = self._path.split(".")[-1]
        header_dict: Dict[str, str] = {
            "doc": "data:application/msword;base64,",
            "docx": "data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,",
            "pdf": "data:application/pdf;base64,",
        }
        raw_bytes = base64.b64encode(data)
        file_bytes64: Union[bytes, str] = raw_bytes
        if decode:
            file_bytes64 = raw_bytes.decode(decode)
        self._content = f"{header_dict[file_extension]}{file_bytes64}"

    def from_dict(self, file_path: str, data: Dict[str, Any]) -> None:
        self._path = file_path
        self._content = data

    def from_file(self, file_path: str) -> None:
        with open(file_path, "rb") as f:
            self.from_bytes(file_path, f.read())

    def is_valid(self) -> bool:
        if not bool(self.name and self._content):
            raise ValueError("call from_bytes or from_file before call is_valid")
        return True

    @property
    def name(self) -> str:
        if self._path:
            return Path(self._path).name
        return ""
