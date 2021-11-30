from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers.mixins import EndpointMixin


class EmbeddedHandler:
    def __init__(self, *, environment: IEnvironment) -> None:
        self._environment = environment
        self._token_file = ""

    def get_widget_link(self, *, use_token: bool = False) -> str:
        if not use_token:
            return f"{self._environment.endpoint}/tokenlessWidget.js"

        return "https://raw.githubusercontent.com/clicksign/embedded/main/build/embedded.js"
