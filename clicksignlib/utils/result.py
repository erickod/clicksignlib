from typing import Any, Dict


class Result:
    def __init__(
        self,
        *,
        request_data: Dict[str, Any],
        response_data: Any,
    ) -> None:
        self.request_data = request_data
        self.response_data = response_data
