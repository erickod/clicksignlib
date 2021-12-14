import hashlib
import hmac


def calc_hmac_sum(request_signature_key: str, secret_hmac_sha256: str) -> str:
    return hmac.new(
        secret_hmac_sha256.encode(),
        msg=request_signature_key.encode(),
        digestmod=hashlib.sha256,
    ).hexdigest()
