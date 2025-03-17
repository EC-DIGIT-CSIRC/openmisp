"""Taxonomy model for PyOTI Enrichment."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PyotiTaxonomyPredicate(str, Enum):
    CHECKDMARC = "checkdmarc"
    DISPOSABLE_EMAIL = "disposable-email"
    EMAILREPIO = "emailrepio"
    IRIS_INVESTIGATE = "iris-investigate"
    VIRUSTOTAL = "virustotal"
    CIRCL_HASHLOOKUP = "circl-hashlookup"
    REPUTATION_BLOCK_LIST = "reputation-block-list"
    ABUSEIPDB = "abuseipdb"
    GREYNOISE_RIOT = "greynoise-riot"
    GOOGLESAFEBROWSING = "googlesafebrowsing"


class PyotiTaxonomyCheckdmarcEntry(str, Enum):
    SPOOFABLE = "spoofable"


class PyotiTaxonomyEmailrepioEntry(str, Enum):
    SPOOFABLE = "spoofable"
    SUSPICIOUS = "suspicious"
    BLACKLISTED = "blacklisted"
    MALICIOUS_ACTIVITY = "malicious-activity"
    MALICIOUS_ACTIVITY_RECENT = "malicious-activity-recent"
    CREDENTIALS_LEAKED = "credentials-leaked"
    CREDENTIALS_LEAKED_RECENT = "credentials-leaked-recent"
    REPUTATION_HIGH = "reputation-high"
    REPUTATION_MEDIUM = "reputation-medium"
    REPUTATION_LOW = "reputation-low"
    SUSPICIOUS_TLD = "suspicious-tld"
    SPAM = "spam"


class PyotiTaxonomyIrisInvestigateEntry(str, Enum):
    HIGH = "high"
    MEDIUM_HIGH = "medium-high"
    MEDIUM = "medium"
    LOW = "low"


class PyotiTaxonomyVirustotalEntry(str, Enum):
    KNOWN_DISTRIBUTOR = "known-distributor"
    VALID_SIGNATURE = "valid-signature"
    INVALID_SIGNATURE = "invalid-signature"


class PyotiTaxonomyCirclHashlookupEntry(str, Enum):
    HIGH_TRUST = "high-trust"
    MEDIUM_HIGH_TRUST = "medium-high-trust"
    MEDIUM_TRUST = "medium-trust"
    LOW_TRUST = "low-trust"


class PyotiTaxonomyReputationBlockListEntry(str, Enum):
    BARRACUDACENTRAL_BRBL = "barracudacentral-brbl"
    SPAMCOP_SCBL = "spamcop-scbl"
    SPAMHAUS_SBL = "spamhaus-sbl"
    SPAMHAUS_XBL = "spamhaus-xbl"
    SPAMHAUS_PBL = "spamhaus-pbl"
    SPAMHAUS_CSS = "spamhaus-css"
    SPAMHAUS_DROP = "spamhaus-drop"
    SPAMHAUS_SPAM = "spamhaus-spam"
    SPAMHAUS_PHISH = "spamhaus-phish"
    SPAMHAUS_MALWARE = "spamhaus-malware"
    SPAMHAUS_BOTNET_C2 = "spamhaus-botnet-c2"
    SPAMHAUS_ABUSED_LEGIT_SPAM = "spamhaus-abused-legit-spam"
    SPAMHAUS_ABUSED_SPAMMED_REDIRECTOR = "spamhaus-abused-spammed-redirector"
    SPAMHAUS_ABUSED_LEGIT_PHISH = "spamhaus-abused-legit-phish"
    SPAMHAUS_ABUSED_LEGIT_MALWARE = "spamhaus-abused-legit-malware"
    SPAMHAUS_ABUSED_LEGIT_BOTNET_C2 = "spamhaus-abused-legit-botnet-c2"
    SURBL_PHISH = "surbl-phish"
    SURBL_MALWARE = "surbl-malware"
    SURBL_SPAM = "surbl-spam"
    SURBL_ABUSED_LEGIT = "surbl-abused-legit"
    URIBL_BLACK = "uribl-black"
    URIBL_GREY = "uribl-grey"
    URIBL_RED = "uribl-red"
    URIBL_MULTI = "uribl-multi"


class PyotiTaxonomyAbuseipdbEntry(str, Enum):
    HIGH = "high"
    MEDIUM_HIGH = "medium-high"
    MEDIUM = "medium"
    LOW = "low"


class PyotiTaxonomyGreynoiseRiotEntry(str, Enum):
    TRUST_LEVEL_1 = "trust-level-1"
    TRUST_LEVEL_2 = "trust-level-2"


class PyotiTaxonomyGooglesafebrowsingEntry(str, Enum):
    MALWARE = "malware"
    SOCIAL_ENGINEERING = "social-engineering"
    UNWANTED_SOFTWARE = "unwanted-software"
    POTENTIALLY_HARMFUL_APPLICATION = "potentially-harmful-application"
    UNSPECIFIED = "unspecified"


class PyotiTaxonomy(BaseModel):
    """Model for the PyOTI Enrichment taxonomy."""

    namespace: str = "pyoti"
    description: str = """PyOTI automated enrichment schemes for point in time classification of indicators."""
    version: int = 3
    exclusive: bool = False
    predicates: List[PyotiTaxonomyPredicate] = []
    checkdmarc_entries: List[PyotiTaxonomyCheckdmarcEntry] = []
    emailrepio_entries: List[PyotiTaxonomyEmailrepioEntry] = []
    iris_investigate_entries: List[PyotiTaxonomyIrisInvestigateEntry] = []
    virustotal_entries: List[PyotiTaxonomyVirustotalEntry] = []
    circl_hashlookup_entries: List[PyotiTaxonomyCirclHashlookupEntry] = []
    reputation_block_list_entries: List[PyotiTaxonomyReputationBlockListEntry] = []
    abuseipdb_entries: List[PyotiTaxonomyAbuseipdbEntry] = []
    greynoise_riot_entries: List[PyotiTaxonomyGreynoiseRiotEntry] = []
    googlesafebrowsing_entries: List[PyotiTaxonomyGooglesafebrowsingEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
