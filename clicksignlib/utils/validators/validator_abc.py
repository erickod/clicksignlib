from abc import ABC, abstractmethod
from typing import Any
from weakref import WeakKeyDictionary


class ValidatorABC:
    """An Abstract base class to the validators descriptors"""

    def __init__(
        self,
    ):
        self._values = WeakKeyDictionary()
        # self._values = dict()
        self._field_name: str = ""

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values[instance]

    def __call__(self, value):
        self.__set__(type(value), value)
        return self.__get__(type(value), type(value))

    def validate(self, value) -> Any:
        return self.__call__(value)

    @abstractmethod
    def __set__(self, instance, value):
        raise NotImplementedError
