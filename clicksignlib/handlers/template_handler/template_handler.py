from clicksignlib.environments.protocols import IEnvironment


class TemplateHandler:
    def __init__(self, *, access_token: str, environment: IEnvironment) -> None:
        self._access_token = access_token
        self._environment = environment
