from enum import Enum, EnumMeta


class AuthMeta(EnumMeta):
    def __getitem__(self, key):
        return self.__dict__[key.upper()]

    def __contains__(self, member) -> bool:
        return member.upper() in self.__dict__.keys()


class Auth(Enum, metaclass=AuthMeta):
    EMAIL = "email"
    SMS = "sms"
    WHATSAPP = "whatsapp"
    PIX = "pix"
    API = "api"
    ICP_BRASIL = "icp_brasil"
