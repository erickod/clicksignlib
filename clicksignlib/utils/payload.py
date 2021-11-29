from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Payload:
    payload: Dict["str", Any]
    status_code: int
