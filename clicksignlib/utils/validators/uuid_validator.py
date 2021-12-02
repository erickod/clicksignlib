import uuid
from typing import Optional, Union
from weakref import WeakKeyDictionary

from clicksignlib.utils.errors import InvalidKeyError

from .validator_abc import ValidatorABC


class UUIDValidator(ValidatorABC):
    """Perform UUID validations"""

    def __init__(
        self,
        field_name: str = "",
    ):
        super().__init__()

        self._field_name = field_name

    def __set__(self, instance, value):
        try:
            uuid.UUID(value)
        except ValueError:
            raise InvalidKeyError(target=self._field_name)
        self._values[instance] = value
