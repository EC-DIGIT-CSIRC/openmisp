"""Taxonomy model for rsit."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class RsitTaxonomyPredicate(str, Enum):
    ABUSIVE_CONTENT = "abusive-content"
    MALICIOUS_CODE = "malicious-code"
    INFORMATION_GATHERING = "information-gathering"
    INTRUSION_ATTEMPTS = "intrusion-attempts"
    INTRUSIONS = "intrusions"
    AVAILABILITY = "availability"
    INFORMATION_CONTENT_SECURITY = "information-content-security"
    FRAUD = "fraud"
    VULNERABLE = "vulnerable"
    OTHER = "other"
    TEST = "test"


class RsitTaxonomyAbusiveContentEntry(str, Enum):
    SPAM = "spam"
    HARMFUL_SPEECH = "harmful-speech"
    VIOLENCE = "violence"


class RsitTaxonomyMaliciousCodeEntry(str, Enum):
    INFECTED_SYSTEM = "infected-system"
    C2_SERVER = "c2-server"
    MALWARE_DISTRIBUTION = "malware-distribution"
    MALWARE_CONFIGURATION = "malware-configuration"


class RsitTaxonomyInformationGatheringEntry(str, Enum):
    SCANNER = "scanner"
    SNIFFING = "sniffing"
    SOCIAL_ENGINEERING = "social-engineering"


class RsitTaxonomyIntrusionAttemptsEntry(str, Enum):
    IDS_ALERT = "ids-alert"
    BRUTE_FORCE = "brute-force"
    EXPLOIT = "exploit"


class RsitTaxonomyIntrusionsEntry(str, Enum):
    PRIVILEGED_ACCOUNT_COMPROMISE = "privileged-account-compromise"
    UNPRIVILEGED_ACCOUNT_COMPROMISE = "unprivileged-account-compromise"
    APPLICATION_COMPROMISE = "application-compromise"
    SYSTEM_COMPROMISE = "system-compromise"
    BURGLARY = "burglary"


class RsitTaxonomyAvailabilityEntry(str, Enum):
    DOS = "dos"
    DDOS = "ddos"
    MISCONFIGURATION = "misconfiguration"
    SABOTAGE = "sabotage"
    OUTAGE = "outage"


class RsitTaxonomyInformationContentSecurityEntry(str, Enum):
    UNAUTHORISED_INFORMATION_ACCESS = "unauthorised-information-access"
    UNAUTHORISED_INFORMATION_MODIFICATION = "unauthorised-information-modification"
    DATA_LOSS = "data-loss"
    DATA_LEAK = "data-leak"


class RsitTaxonomyFraudEntry(str, Enum):
    UNAUTHORISED_USE_OF_RESOURCES = "unauthorised-use-of-resources"
    COPYRIGHT = "copyright"
    MASQUERADE = "masquerade"
    PHISHING = "phishing"


class RsitTaxonomyVulnerableEntry(str, Enum):
    WEAK_CRYPTO = "weak-crypto"
    DDOS_AMPLIFIER = "ddos-amplifier"
    POTENTIALLY_UNWANTED_ACCESSIBLE = "potentially-unwanted-accessible"
    INFORMATION_DISCLOSURE = "information-disclosure"
    VULNERABLE_SYSTEM = "vulnerable-system"


class RsitTaxonomyOtherEntry(str, Enum):
    OTHER = "other"
    UNDETERMINED = "undetermined"


class RsitTaxonomyTestEntry(str, Enum):
    TEST = "test"


class RsitTaxonomy(BaseModel):
    """Model for the rsit taxonomy."""

    namespace: str = "rsit"
    description: str = """Reference Security Incident Classification Taxonomy"""
    version: int = 1003
    exclusive: bool = False
    predicates: List[RsitTaxonomyPredicate] = []
    abusive_content_entries: List[RsitTaxonomyAbusiveContentEntry] = []
    malicious_code_entries: List[RsitTaxonomyMaliciousCodeEntry] = []
    information_gathering_entries: List[RsitTaxonomyInformationGatheringEntry] = []
    intrusion_attempts_entries: List[RsitTaxonomyIntrusionAttemptsEntry] = []
    intrusions_entries: List[RsitTaxonomyIntrusionsEntry] = []
    availability_entries: List[RsitTaxonomyAvailabilityEntry] = []
    information_content_security_entries: List[RsitTaxonomyInformationContentSecurityEntry] = []
    fraud_entries: List[RsitTaxonomyFraudEntry] = []
    vulnerable_entries: List[RsitTaxonomyVulnerableEntry] = []
    other_entries: List[RsitTaxonomyOtherEntry] = []
    test_entries: List[RsitTaxonomyTestEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
