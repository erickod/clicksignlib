# ClickSignLib - An easy way to integrate the Click Sign with your python projects
This provide integration to the Click Sign REST API on [Sanbox](https://sandbox.clicksign.com) and on [Production](https://app.clicksign.com) environments.

PS: The requests will perform asyncronoulsy and you'll get the resuls only when you call the run method.

# How to use it?

- Import the ClickSign:  ```from clicksignlib import ClickSign, run```
- Import the environments:  ```from clicksignlib.environments import SandboxEnvironment, ProductionEnvrionment```
- Create your ClickSign instance:  ```click_sign = ClickSign(access_token=<your access token>, environment=SandboxEnvironment())```

### Executing the requests
- Each request should be executed inside the run method;
- You can pass more the one request to the run method;
- You can assign requests to the variables and pass them to the run method;

## Templates
- click_sign.template.create_from_file(*, file_path: str) -> Result

- click_sign.template.create_from_bytes(*, file_path: str, data: bytes) -> Result

- click_sign.template.list() -> Result

## Documents
- click_sign.document.create_from_file(*, file_path: str, document_type: str) -> Result

- click_sign.document.create_from_bytes(*, file_path: str, document_type: str, data: bytes) -> Result

- click_sign.document.create_from_template(*, document_type: str, filename: str, template_key: str, template_data: Dict[str, Any],) -> Result

- click_sign.document.list() -> Result

- click_sign.document.detail(*, document_key: str) -> Result

- click_sign.document.delete(*, document_key: str) -> Result

- click_sign.document.finish(*, document_key: str) -> Result

- click_sign.document.cancel(*, document_key: str) -> Result

- click_sign.document.configure(*,
document_key: str,
deadline_at: Optional[datetime] = None,
auto_close: bool = True,
sequence_enabled: bool = False,
remind_interval: int = 1
) -> Result

- click_sign.document.sign_by_api(*, request_signature_key: str, secret_hmac_sha256: str) -> Result:
## Signers
import the Signers Enum: ```from clicksignlib.handlers import Auth, SignerType```
- click_sign.document.create(*,
name: str,
cpf: str = "",
birthday: str = "",
email: str = "",
phone_number: str = "",
auths: Auth = Auth.EMAIL,
notify: bool = True,
) -> Result:

- click_sign.document.add_signatory_to_document(*,
	document_key: str,
	signer_key: str,
	signer_type: SignerType,
	message: str,
	group: int = 0,
) -> Result:
## Notifications
- click_sign.notification.notify_by_email(*,
request_key: str,
message: str,
url: str = ""
) -> Result:
