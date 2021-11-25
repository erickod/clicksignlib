from abc import ABC


class EnvironmentABC(ABC):
    def __init__(self, title: str, endpoint: str) -> None:
        self.title = title
        self.endpoint = endpoint

    def is_valid(self):
        required_class_variables = ["title", "endpoint"]
        for var in required_class_variables:
            if not getattr(self, var):
                raise NotImplementedError(
                    f"Provide a value to the `{var}` attributte in the {self.__class__.__name__} class"
                )
