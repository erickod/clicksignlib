class TemplateHandler:
    def __init__(self, *, access_token: str, environment: str) -> None:
        self._access_token = access_token
        self._environment = environment
