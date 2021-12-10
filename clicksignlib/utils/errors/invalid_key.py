class InvalidKeyError(Exception):
    def __init__(self, target: str = "") -> None:
        erro_msg: str = "Invalid Key|ID"

        if target:
            erro_msg += " to {}".format(target)
        super().__init__(erro_msg)


class RequiredParameters(Exception):
    pass


class InvalidParameters(Exception):
    pass
