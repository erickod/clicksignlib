import requests

from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import (
    DocumentHandler,
    EmbeddedHandler,
    NotificationHandler,
    SignatoryHandler,
    TemplateHandler,
)
import sys
from typing import Coroutine, Generic, TypeVar
import asyncio

VERSION = float(f'{sys.version_info.major}.{sys.version_info.minor}')
_T = TypeVar("_T")


class ClickSign:
    def __init__(
            self,
            *,
            access_token: str,
            environment: IEnvironment,
            requests_adapter=requests,
    ) -> None:
        self._access_token = access_token
        self._environment = environment
        self._requests_adapter = requests_adapter
        self._config = dict(
            access_token=self._access_token,
            environment=self._environment,
            requests_adapter=self._requests_adapter,
        )

    @property
    def document(self) -> DocumentHandler:
        return DocumentHandler(**self._config)

    @property
    def template(self) -> TemplateHandler:
        return TemplateHandler(**self._config)

    @property
    def signers(self) -> SignatoryHandler:
        return SignatoryHandler(**self._config)

    @property
    def notification(self):
        return NotificationHandler(**self._config)

    @property
    def widget(self) -> EmbeddedHandler:
        return EmbeddedHandler(environment=self._config["environment"])


def run(*futures: Coroutine) -> Generic[_T]:
    groups = asyncio.gather(*futures)

    if VERSION >= 3.7:
        asyncio.run(groups)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(groups)
