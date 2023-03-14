from clicksignlib.handlers.mixins import EndpointMixin
from clicksignlib.environments.protocols import IEnvironment
from clicksignlib.handlers import Config
import typing
from clicksignlib.utils import Result

class BatchHandler(EndpointMixin):
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
        endpoint = f"{endpoint}/batches?access_token={self.config.access_token}"
        return endpoint
    

    def create(self, document_keys: typing.List[str], signer_key: str, summary: bool=True) -> Result:
        request_payload = {
            "batch": {
                "signer_key": signer_key,
                "document_keys": document_keys,
                "summary": summary
                }
        }
        res = self.config.requests.post(url=self.full_endpoint, json=request_payload)
        return Result(request_data=request_payload, response_data=res)