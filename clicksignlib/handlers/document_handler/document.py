import base64
from typing import Dict, Union


class Document:
    def __init__(self) -> None:
        self._content: Union[str, bytes] = b""

    def from_bytes(self, filename: str, data: bytes, decode="utf-8") -> None:
        filename = filename.lower()
        file_extension = filename.split(".")[-1]
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

    def from_file(self, filename: str) -> None:
        with open(filename, "rb") as f:
            self.from_bytes(filename, f.read())

    def is_valid(self) -> bool:
        return bool(self._content)
