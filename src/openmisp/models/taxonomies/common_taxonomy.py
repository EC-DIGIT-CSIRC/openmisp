"""Taxonomy model for common-taxonomy."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CommonTaxonomyTaxonomyPredicate(str, Enum):
    MALWARE = "malware"
    AVAILABILITY = "availability"
    INFORMATION_GATHERING = "information-gathering"
    INTRUSION_ATTEMPT = "intrusion-attempt"
    INTRUSION = "intrusion"
    INFORMATION_SECURITY = "information-security"
    FRAUD = "fraud"
    ABUSIVE_CONTENT = "abusive-content"
    OTHER = "other"


class CommonTaxonomyTaxonomyMalwareEntry(str, Enum):
    INFECTION = "infection"
    DISTRIBUTION = "distribution"
    COMMAND_AND_CONTROL = "command-and-control"
    MALICIOUS_CONNECTION = "malicious-connection"


class CommonTaxonomyTaxonomyAvailabilityEntry(str, Enum):
    DOS_DDOS = "dos-ddos"
    SABOTAGE = "sabotage"


class CommonTaxonomyTaxonomyInformationGatheringEntry(str, Enum):
    SCANNING = "scanning"
    SNIFFING = "sniffing"
    PHISHING = "phishing"


class CommonTaxonomyTaxonomyIntrusionAttemptEntry(str, Enum):
    VULNERABILITY_EXPLOITATION_ATTEMPT = "vulnerability-exploitation-attempt"
    LOGIN_ATTEMPT = "login-attempt"


class CommonTaxonomyTaxonomyIntrusionEntry(str, Enum):
    VULNERABILITY_EXPLOITATION = "vulnerability-exploitation"
    ACCOUNT_COMPROMISE = "account-compromise"


class CommonTaxonomyTaxonomyInformationSecurityEntry(str, Enum):
    UNAUTHORISED_ACCESS = "unauthorised-access"
    UNAUTHORISED_MODIFICATION_OR_DELETION = "unauthorised-modification-or-deletion"


class CommonTaxonomyTaxonomyFraudEntry(str, Enum):
    RESOURCES_MISUSE = "resources-misuse"
    FALSE_REPRESENTATION = "false-representation"


class CommonTaxonomyTaxonomyAbusiveContentEntry(str, Enum):
    SPAM = "spam"
    COPYRIGHT = "copyright"
    CSE_RACISM_VIOLENCE_INCITEMENT = "cse-racism-violence-incitement"


class CommonTaxonomyTaxonomyOtherEntry(str, Enum):
    UNCLASSIFIED_INCIDENT = "unclassified-incident"
    UNDETERMINED_INCIDENT = "undetermined-incident"


class CommonTaxonomyTaxonomy(BaseModel):
    """Model for the common-taxonomy taxonomy."""

    namespace: str = "common-taxonomy"
    description: str = """Common Taxonomy for Law enforcement and CSIRTs"""
    version: int = 3
    exclusive: bool = False
    predicates: List[CommonTaxonomyTaxonomyPredicate] = []
    malware_entries: List[CommonTaxonomyTaxonomyMalwareEntry] = []
    availability_entries: List[CommonTaxonomyTaxonomyAvailabilityEntry] = []
    information_gathering_entries: List[CommonTaxonomyTaxonomyInformationGatheringEntry] = []
    intrusion_attempt_entries: List[CommonTaxonomyTaxonomyIntrusionAttemptEntry] = []
    intrusion_entries: List[CommonTaxonomyTaxonomyIntrusionEntry] = []
    information_security_entries: List[CommonTaxonomyTaxonomyInformationSecurityEntry] = []
    fraud_entries: List[CommonTaxonomyTaxonomyFraudEntry] = []
    abusive_content_entries: List[CommonTaxonomyTaxonomyAbusiveContentEntry] = []
    other_entries: List[CommonTaxonomyTaxonomyOtherEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
