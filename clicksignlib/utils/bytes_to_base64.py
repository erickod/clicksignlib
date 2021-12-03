import base64
from typing import Dict, Union


def bytes_to_base64(file_path: str, data: bytes, decode="utf-8") -> Union[str, bytes]:
    file_path = file_path.lower()
    file_extension = file_path.split(".")[-1]
    header_dict: Dict[str, str] = {
        "doc": "data:application/msword;base64,",
        "docx": "data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,",
        "pdf": "data:application/pdf;base64,",
    }
    raw_bytes = base64.b64encode(data)
    file_bytes64: Union[bytes, str] = raw_bytes
    if decode:
        return f"{header_dict[file_extension]}{raw_bytes.decode(decode)}"
    return header_dict[file_extension].encode() + file_bytes64
