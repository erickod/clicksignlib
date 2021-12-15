import contextlib
import hashlib
import hmac


def calc_hmac_sum(data, secret_hmac_sha256) -> str:
    with contextlib.suppress(AttributeError):
        data = data.encode()

    with contextlib.suppress(AttributeError):
        secret_hmac_sha256 = secret_hmac_sha256.encode()

    return hmac.new(
        key=secret_hmac_sha256,
        msg=data,
        digestmod=hashlib.sha256,
    ).hexdigest()
