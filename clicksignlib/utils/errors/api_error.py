class ApiError(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(f"Status Code {status_code}: {message}")
