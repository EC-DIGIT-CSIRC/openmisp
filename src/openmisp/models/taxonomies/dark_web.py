"""Taxonomy model for Dark Web."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DarkWebTaxonomyPredicate(str, Enum):
    TOPIC = "topic"
    MOTIVATION = "motivation"
    STRUCTURE = "structure"
    SERVICE = "service"
    CONTENT = "content"


class DarkWebTaxonomyTopicEntry(str, Enum):
    DRUGS_NARCOTICS = "drugs-narcotics"
    ELECTRONICS = "electronics"
    FINANCE = "finance"
    FINANCE_CRYPTO = "finance-crypto"
    CREDIT_CARD = "credit-card"
    CASH_IN = "cash-in"
    CASH_OUT = "cash-out"
    ESCROW = "escrow"
    HACKING = "hacking"
    IDENTIFICATION_CREDENTIALS = "identification-credentials"
    INTELLECTUAL_PROPERTY_COPYRIGHT_MATERIALS = "intellectual-property-copyright-materials"
    PORNOGRAPHY_ADULT = "pornography-adult"
    PORNOGRAPHY_CHILD_EXPLOITATION = "pornography-child-exploitation"
    PORNOGRAPHY_ILLICIT_OR_ILLEGAL = "pornography-illicit-or-illegal"
    SEARCH_ENGINE_INDEX = "search-engine-index"
    UNCLEAR = "unclear"
    EXTREMISM = "extremism"
    VIOLENCE = "violence"
    WEAPONS = "weapons"
    SOFTWARES = "softwares"
    COUNTERFEIT_MATERIALS = "counterfeit-materials"
    GAMBLING = "gambling"
    LIBRARY = "library"
    OTHER_NOT_ILLEGAL = "other-not-illegal"
    LEGITIMATE = "legitimate"
    CHAT = "chat"
    MIXER = "mixer"
    MYSTERY_BOX = "mystery-box"
    ANONYMIZER = "anonymizer"
    VPN_PROVIDER = "vpn-provider"
    EMAIL_PROVIDER = "email-provider"
    PONIES = "ponies"
    GAMES = "games"
    PARODY = "parody"
    WHISTLEBLOWER = "whistleblower"
    RANSOMWARE_GROUP = "ransomware-group"
    HITMAN = "hitman"
    DIRECTORY_PROVIDER = "directory-provider"


class DarkWebTaxonomyMotivationEntry(str, Enum):
    EDUCATION_TRAINING = "education-training"
    WIKI = "wiki"
    FORUM = "forum"
    FILE_SHARING = "file-sharing"
    HOSTING = "hosting"
    DDOS_SERVICES = "ddos-services"
    GENERAL = "general"
    INFORMATION_SHARING_REPORTAGE = "information-sharing-reportage"
    SCAM = "scam"
    POLITICAL_SPEECH = "political-speech"
    CONSPIRATIONIST = "conspirationist"
    HATE_SPEECH = "hate-speech"
    RELIGIOUS = "religious"
    MARKETPLACE_FOR_SALE = "marketplace-for-sale"
    SMUGGLING = "smuggling"
    RECRUITMENT_ADVOCACY = "recruitment-advocacy"
    SYSTEM_PLACEHOLDER = "system-placeholder"
    UNCLEAR = "unclear"


class DarkWebTaxonomyStructureEntry(str, Enum):
    INCOMPLETE = "incomplete"
    CAPTCHA = "captcha"
    LOGIN_FORMS = "login-forms"
    CONTACT_FORMS = "contact-forms"
    ENCRYPTION_KEYS = "encryption-keys"
    POLICE_NOTICE = "police-notice"
    LEGAL_STATEMENT = "legal-statement"
    TEST = "test"
    VIDEOS = "videos"
    RANSOMWARE_POST = "ransomware-post"
    UNCLEAR = "unclear"


class DarkWebTaxonomyServiceEntry(str, Enum):
    URL = "url"
    CONTENT_TYPE = "content-type"
    PATH = "path"
    DETECTION_DATE = "detection-date"
    NETWORK_PROTOCOL = "network-protocol"
    PORT = "port"
    NETWORK = "network"
    FOUND_AT = "found-at"


class DarkWebTaxonomyContentEntry(str, Enum):
    SHA1SUM = "sha1sum"
    SHA256SUM = "sha256sum"
    SSDEEP = "ssdeep"
    LANGUAGE = "language"
    HTML = "html"
    CSS = "css"
    TEXT = "text"
    PAGE_TITLE = "page-title"
    PHONE_NUMBER = "phone-number"
    CREDIT_CARD = "creditCard"
    EMAIL = "email"
    PGP_PUBLIC_KEY_BLOCK = "pgp-public-key-block"
    COUNTRY = "country"
    COMPANY_NAME = "company-name"
    COMPANY_LINK = "company-link"
    VICTIM_ADDRESS = "victim-address"
    VICTIM_TLD = "victim-TLD"


class DarkWebTaxonomy(BaseModel):
    """Model for the Dark Web taxonomy."""

    namespace: str = "dark-web"
    description: str = """Criminal motivation and content detection the dark web: A categorisation model for law enforcement. ref: Janis Dalins, Campbell Wilson, Mark Carman. Taxonomy updated by MISP Project and extended by the JRC (Joint Research Centre) of the European Commission."""
    version: int = 9
    exclusive: bool = False
    predicates: List[DarkWebTaxonomyPredicate] = []
    topic_entries: List[DarkWebTaxonomyTopicEntry] = []
    motivation_entries: List[DarkWebTaxonomyMotivationEntry] = []
    structure_entries: List[DarkWebTaxonomyStructureEntry] = []
    service_entries: List[DarkWebTaxonomyServiceEntry] = []
    content_entries: List[DarkWebTaxonomyContentEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
