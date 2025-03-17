"""Taxonomy model for infoleak."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InfoleakTaxonomyPredicate(str, Enum):
    AUTOMATIC_DETECTION = "automatic-detection"
    ANALYST_DETECTION = "analyst-detection"
    CONFIRMED = "confirmed"
    SOURCE = "source"
    SUBMISSION = "submission"
    OUTPUT_FORMAT = "output-format"
    CERTAINTY = "certainty"


class InfoleakTaxonomyAutomaticDetectionEntry(str, Enum):
    CREDENTIAL = "credential"
    CREDIT_CARD = "credit-card"
    IBAN = "iban"
    IP = "ip"
    MAIL = "mail"
    PHONE_NUMBER = "phone-number"
    API_KEY = "api-key"
    GOOGLE_API_KEY = "google-api-key"
    AWS_KEY = "aws-key"
    PRIVATE_KEY = "private-key"
    ENCRYPTED_PRIVATE_KEY = "encrypted-private-key"
    PRIVATE_SSH_KEY = "private-ssh-key"
    PRIVATE_STATIC_KEY = "private-static-key"
    VPN_STATIC_KEY = "vpn-static-key"
    PGP_MESSAGE = "pgp-message"
    PGP_PUBLIC_KEY_BLOCK = "pgp-public-key-block"
    PGP_SIGNATURE = "pgp-signature"
    PGP_PRIVATE_KEY = "pgp-private-key"
    CERTIFICATE = "certificate"
    RSA_PRIVATE_KEY = "rsa-private-key"
    DSA_PRIVATE_KEY = "dsa-private-key"
    EC_PRIVATE_KEY = "ec-private-key"
    PUBLIC_KEY = "public-key"
    BASE64 = "base64"
    BINARY = "binary"
    HEXADECIMAL = "hexadecimal"
    BITCOIN_ADDRESS = "bitcoin-address"
    BITCOIN_PRIVATE_KEY = "bitcoin-private-key"
    CVE = "cve"
    ONION = "onion"
    BARCODE = "barcode"
    QRCODE = "qrcode"
    SQL_INJECTION = "sql-injection"


class InfoleakTaxonomyAnalystDetectionEntry(str, Enum):
    CREDENTIAL = "credential"
    CREDIT_CARD = "credit-card"
    IBAN = "iban"
    IP = "ip"
    MAIL = "mail"
    PHONE_NUMBER = "phone-number"
    API_KEY = "api-key"
    GOOGLE_API_KEY = "google-api-key"
    AWS_KEY = "aws-key"
    PRIVATE_KEY = "private-key"
    ENCRYPTED_PRIVATE_KEY = "encrypted-private-key"
    PRIVATE_SSH_KEY = "private-ssh-key"
    PRIVATE_STATIC_KEY = "private-static-key"
    VPN_STATIC_KEY = "vpn-static-key"
    PGP_MESSAGE = "pgp-message"
    PGP_PUBLIC_KEY_BLOCK = "pgp-public-key-block"
    PGP_SIGNATURE = "pgp-signature"
    PGP_PRIVATE_KEY = "pgp-private-key"
    CERTIFICATE = "certificate"
    RSA_PRIVATE_KEY = "rsa-private-key"
    DSA_PRIVATE_KEY = "dsa-private-key"
    EC_PRIVATE_KEY = "ec-private-key"
    PUBLIC_KEY = "public-key"
    BASE64 = "base64"
    BINARY = "binary"
    HEXADECIMAL = "hexadecimal"
    BITCOIN_ADDRESS = "bitcoin-address"
    BITCOIN_PRIVATE_KEY = "bitcoin-private-key"
    CVE = "cve"
    ONION = "onion"
    BARCODE = "barcode"
    QRCODE = "qrcode"
    SQL_INJECTION = "sql-injection"


class InfoleakTaxonomyConfirmedEntry(str, Enum):
    FALSE_POSITIVE = "false-positive"
    FALSE_NEGATIVE = "false-negative"
    TRUE_POSITIVE = "true-positive"
    TRUE_NEGATIVE = "true-negative"


class InfoleakTaxonomySourceEntry(str, Enum):
    PUBLIC_WEBSITE = "public-website"
    PASTIE_WEBSITE = "pastie-website"
    ELECTRONIC_FORUM = "electronic-forum"
    MAILING_LIST = "mailing-list"
    SOURCE_CODE_REPOSITORY = "source-code-repository"
    AUTOMATIC_COLLECTION = "automatic-collection"
    MANUAL_ANALYSIS = "manual-analysis"
    UNKNOWN = "unknown"
    OTHER = "other"


class InfoleakTaxonomySubmissionEntry(str, Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    CRAWLER = "crawler"


class InfoleakTaxonomyOutputFormatEntry(str, Enum):
    AIL_DAILY = "ail-daily"
    AIL_WEEKLY = "ail-weekly"
    AIL_MONTHLY = "ail-monthly"


class InfoleakTaxonomyCertaintyEntry(str, Enum):
    T_100 = "100"
    T_93 = "93"
    T_75 = "75"
    T_50 = "50"
    T_30 = "30"
    T_7 = "7"
    T_0 = "0"


class InfoleakTaxonomy(BaseModel):
    """Model for the infoleak taxonomy."""

    namespace: str = "infoleak"
    description: str = """A taxonomy describing information leaks and especially information classified as being potentially leaked. The taxonomy is based on the work by CIRCL on the AIL framework. The taxonomy aim is to be used at large to improve classification of leaked information."""
    version: int = 10
    exclusive: bool = False
    predicates: List[InfoleakTaxonomyPredicate] = []
    automatic_detection_entries: List[InfoleakTaxonomyAutomaticDetectionEntry] = []
    analyst_detection_entries: List[InfoleakTaxonomyAnalystDetectionEntry] = []
    confirmed_entries: List[InfoleakTaxonomyConfirmedEntry] = []
    source_entries: List[InfoleakTaxonomySourceEntry] = []
    submission_entries: List[InfoleakTaxonomySubmissionEntry] = []
    output_format_entries: List[InfoleakTaxonomyOutputFormatEntry] = []
    certainty_entries: List[InfoleakTaxonomyCertaintyEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
