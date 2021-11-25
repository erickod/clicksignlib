from abc import ABC


class EnvironmentABC(ABC):
    title: str
    endpoint: str

    def is_valid(self):
        required_class_variables = ["title", "endpoint"]
        for var in required_class_variables:
            if not hasattr(self, var):
                raise NotImplementedError(
                    f"Provide a value to the `{var}` attributte in the {self.__class__.__name__} class"
                )
