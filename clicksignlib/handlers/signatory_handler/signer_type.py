from enum import Enum


class SignerType(Enum):
    SIGN = "sign"
    APPROVE = "approve"
    PARTY = "party"
    WITNESS = "witness"
    INTERVENING = "intervening"
    RECEIPT = "receipt"
    ENDORSER = "endorser"
    ENDORSEE = "endorsee"
    ADMINISTRATOR = "administrator"
    GUARANTOR = "guarantor"
    TRANSFEROR = "transferor"
    TRANSFEREE = "transferee"
    CONTRACTEE = "contractee"
    CONTRACTOR = "contractor"
    JOINT_DEBTOR = "joint_debtor"
    ISSUER = "issuer"
    MANAGER = "manager"
    BUYER = "buyer"
    SELLER = "seller"
    ATTORNEY = "attorney"
    LEGAL_REPRESENTATIVE = "legal_representative"
    CO_RESPONSIBLE = "co_responsible"
    VALIDATOR = "validator"
    RATIFY = "ratify"
    LESSOR = "lessor"
    LESSEE = "lessee"
    SURETY = "surety"