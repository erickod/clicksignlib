import clicksignlib
import pytest
from clicksignlib.adapters import AioHttpAdapter
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.handlers import Auth, SignerType
from clicksignlib.utils.errors import RequiredParameters

env = SandboxEnvironment()
access_token: str = "899ee68c-0a4a-48dc-9331-44844203b6b4"
api_version: str = "/api/v1"


def test_SignatoryHandler_can_be_imported_from_handlers_package() -> None:
    assert hasattr(clicksignlib.handlers, "SignatoryHandler")


def test_SignatoryHandler_intantiation_params() -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=AioHttpAdapter()
    )
    assert sut.config.access_token == access_token
    assert sut.config.environment == env
    assert sut.config.api_version == api_version


def test_SignatoryHandler_create_method(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    sut.create(
        name="João Souza Silva",
        auths=Auth.EMAIL,
        documentation="111.111.111-41",
        email="mail@mail.com",
        birthday="1990-10-15",
        phone_number="6198464580",
        has_documentation=True,
    )
    mock.post.assert_called_once()


def test_SignatoryHandler_add_signatory_to_document_calls_requests(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    sut.add_signatory_to_document(
        "document_key", "signer_key", SignerType.SURETY, "message"
    )
    mock.post.assert_called_once()


def test_create_raises_when_auth_is_api_and_no_email_is_passed(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.API,
            documentation="111.111.111-41",
            birthday="1990-10-15",
            phone_number="6198464580",
        )


def test_create_raises_when_auth_is_api_and_no_documentation_is_passed(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.API,
            email="mail@mail.com",
        )


def test_create_raises_when_auth_is_email_and_no_email_is_passed(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.EMAIL,
            documentation="111.111.111-41",
            birthday="1990-10-15",
            phone_number="6198464580",
        )


def test_create_raises_when_auth_is_sms_and_no_phone_number_is_passed(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.SMS,
            documentation="111.111.111-41",
            email="mail@mail.com",
            birthday="1990-10-15",
        )


def test_create_raises_when_auth_is_sms_and_no_email_is_passed(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.SMS,
            phone_number="111111111",
        )


def test_create_raises_when_auth_is_whatsapp_and_no_phone_number_is_passed(
    mock,
) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.WHATSAPP,
            documentation="111.111.111-41",
            email="mail@mail.com",
            birthday="1990-10-15",
        )


def test_create_raises_when_auth_is_pix_and_no_documentation_is_passed(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.PIX,
            email="mail@mail.com",
            birthday="1990-10-15",
            phone_number="6198464580",
        )


def test_create_raises_when_auth_icp_brasil_and_self_enabled_is_false(mock) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.ICP_BRASIL,
            email="mail@mail.com",
            birthday="1990-10-15",
            phone_number="6198464580",
            selfie_enabled=False,
        )


def test_create_raises_when_auth_icp_brasil_and_handwritten_enabled_is_false(
    mock,
) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.ICP_BRASIL,
            email="mail@mail.com",
            birthday="1990-10-15",
            phone_number="6198464580",
            selfie_enabled=True,
            handwritten_enabled=False,
        )


def test_create_raises_when_auth_icp_brasil_and_liveness_enabled_is_false(
    mock,
) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.ICP_BRASIL,
            email="mail@mail.com",
            birthday="1990-10-15",
            phone_number="6198464580",
            selfie_enabled=True,
            handwritten_enabled=True,
            liveness_enabled=False,
        )


def test_create_raises_when_auth_api_and_no_documentation_is_given_and_has_documentation_is_True(
    mock,
) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.API,
            email="mail@mail.com",
            birthday="1990-10-15",
            phone_number="6198464580",
            selfie_enabled=True,
            handwritten_enabled=True,
            liveness_enabled=False,
            has_documentation=True,
        )


def test_create_raises_when_auth_api_and_no_birthday_is_given_and_has_documentation_is_True(
    mock,
) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.API,
            documentation="111.111.111-41",
            email="mail@mail.com",
            phone_number="6198464580",
            selfie_enabled=True,
            handwritten_enabled=True,
            liveness_enabled=False,
            has_documentation=True,
        )


def test_create_raises_when_a_documentation_is_given_and_has_documentation_is_False(
    mock,
) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.API,
            documentation="111.111.111-41",
            email="mail@mail.com",
            phone_number="6198464580",
            selfie_enabled=True,
            handwritten_enabled=True,
            liveness_enabled=False,
            has_documentation=False,
        )


def test_create_raises_when_a_birthday_is_given_and_has_documentation_is_False(
    mock,
) -> None:
    sut = clicksignlib.handlers.SignatoryHandler(
        access_token=access_token, environment=env, requests_adapter=mock
    )
    with pytest.raises(RequiredParameters):
        sut.create(
            name="João Souza Silva",
            auths=Auth.API,
            birthday="1990-10-15",
            email="mail@mail.com",
            phone_number="6198464580",
            selfie_enabled=True,
            handwritten_enabled=True,
            liveness_enabled=False,
            has_documentation=False,
        )
