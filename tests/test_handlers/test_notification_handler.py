from unittest.mock import Mock

import clicksignlib
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.utils.result import Result


def test_NotificationHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "NotificationHandler")
