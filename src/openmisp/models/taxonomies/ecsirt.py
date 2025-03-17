"""Taxonomy model for ecsirt."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EcsirtTaxonomyPredicate(str, Enum):
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


class EcsirtTaxonomyAbusiveContentEntry(str, Enum):
    SPAM = "spam"
    HARMFUL_SPEECH = "harmful-speech"
    VIOLENCE = "violence"


class EcsirtTaxonomyMaliciousCodeEntry(str, Enum):
    VIRUS = "virus"
    WORM = "worm"
    TROJAN = "trojan"
    SPYWARE = "spyware"
    DIALER = "dialer"
    ROOTKIT = "rootkit"
    MALWARE = "malware"
    BOTNET_DRONE = "botnet-drone"
    RANSOMWARE = "ransomware"
    MALWARE_CONFIGURATION = "malware-configuration"
    C_C = "c&c"


class EcsirtTaxonomyInformationGatheringEntry(str, Enum):
    SCANNER = "scanner"
    SNIFFING = "sniffing"
    SOCIAL_ENGINEERING = "social-engineering"


class EcsirtTaxonomyIntrusionAttemptsEntry(str, Enum):
    IDS_ALERT = "ids-alert"
    BRUTE_FORCE = "brute-force"
    EXPLOIT = "exploit"


class EcsirtTaxonomyIntrusionsEntry(str, Enum):
    PRIVILEGED_ACCOUNT_COMPROMISE = "privileged-account-compromise"
    UNPRIVILEGED_ACCOUNT_COMPROMISE = "unprivileged-account-compromise"
    APPLICATION_COMPROMISE = "application-compromise"
    BOT = "bot"
    DEFACEMENT = "defacement"
    COMPROMISED = "compromised"
    BACKDOOR = "backdoor"


class EcsirtTaxonomyAvailabilityEntry(str, Enum):
    DOS = "dos"
    DDOS = "ddos"
    SABOTAGE = "sabotage"
    OUTAGE = "outage"


class EcsirtTaxonomyInformationContentSecurityEntry(str, Enum):
    UNAUTHORISED_INFORMATION_ACCESS = "Unauthorised-information-access"
    UNAUTHORISED_INFORMATION_MODIFICATION = "Unauthorised-information-modification"
    DROPZONE = "dropzone"


class EcsirtTaxonomyFraudEntry(str, Enum):
    UNAUTHORIZED_USE_OF_RESOURCES = "unauthorized-use-of-resources"
    COPYRIGHT = "copyright"
    MASQUERADE = "masquerade"
    PHISHING = "phishing"


class EcsirtTaxonomyVulnerableEntry(str, Enum):
    VULNERABLE_SERVICE = "vulnerable-service"


class EcsirtTaxonomyOtherEntry(str, Enum):
    BLACKLIST = "blacklist"
    UNKNOWN = "unknown"
    OTHER = "other"


class EcsirtTaxonomyTestEntry(str, Enum):
    TEST = "test"


class EcsirtTaxonomy(BaseModel):
    """Model for the ecsirt taxonomy."""

    namespace: str = "ecsirt"
    description: str = """Incident Classification by the ecsirt.net version mkVI of 31 March 2015 enriched with IntelMQ taxonomy-type mapping."""
    version: int = 2
    exclusive: bool = False
    predicates: List[EcsirtTaxonomyPredicate] = []
    abusive_content_entries: List[EcsirtTaxonomyAbusiveContentEntry] = []
    malicious_code_entries: List[EcsirtTaxonomyMaliciousCodeEntry] = []
    information_gathering_entries: List[EcsirtTaxonomyInformationGatheringEntry] = []
    intrusion_attempts_entries: List[EcsirtTaxonomyIntrusionAttemptsEntry] = []
    intrusions_entries: List[EcsirtTaxonomyIntrusionsEntry] = []
    availability_entries: List[EcsirtTaxonomyAvailabilityEntry] = []
    information_content_security_entries: List[EcsirtTaxonomyInformationContentSecurityEntry] = []
    fraud_entries: List[EcsirtTaxonomyFraudEntry] = []
    vulnerable_entries: List[EcsirtTaxonomyVulnerableEntry] = []
    other_entries: List[EcsirtTaxonomyOtherEntry] = []
    test_entries: List[EcsirtTaxonomyTestEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
