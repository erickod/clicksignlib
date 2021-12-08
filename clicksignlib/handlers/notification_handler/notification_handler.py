from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
from clicksignlib.handlers.mixins import EndpointMixin
from clicksignlib.utils import Result


class NotificationHandler(EndpointMixin):
    def __init__(
        self,
        *,
        access_token: str,
        environment: IEnvironment,
        requests_adapter,
        api_version: str = "/api/v1",
    ) -> None:
        self.config = Config(
            access_token=access_token,
            environment=environment,
            api_version=api_version,
            requests_adapter=requests_adapter,
        )

    @property
    def full_endpoint(self) -> str:
        endpoint = f"{self.base_endpoint}{self.config.api_version}"
        endpoint = f"{endpoint}/notifications?access_token={self.config.access_token}"
        return endpoint

    def notify_by_email(self, request_key: str, message: str, url: str = "") -> Result:
        request_payload = {
            "request_signature_key": request_key,
            "message": message,
        }
        if url:
            request_payload["url"] = url

        res = self.config.requests.post(
            url=self.full_endpoint,
            json=request_payload,
        )
        return Result(request_data=request_payload, response_data=res)
