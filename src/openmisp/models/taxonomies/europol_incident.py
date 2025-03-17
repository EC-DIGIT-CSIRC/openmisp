"""Taxonomy model for Europol class of incidents taxonomy."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EuropolIncidentTaxonomyPredicate(str, Enum):
    MALWARE = "malware"
    AVAILABILITY = "availability"
    INFORMATION_GATHERING = "information-gathering"
    INTRUSION_ATTEMPT = "intrusion-attempt"
    INTRUSION = "intrusion"
    INFORMATION_SECURITY = "information-security"
    FRAUD = "fraud"
    ABUSIVE_CONTENT = "abusive-content"
    OTHER = "other"


class EuropolIncidentTaxonomyMalwareEntry(str, Enum):
    INFECTION = "infection"
    DISTRIBUTION = "distribution"
    C_C = "c&c"
    UNDETERMINED = "undetermined"


class EuropolIncidentTaxonomyAvailabilityEntry(str, Enum):
    DOS_DDOS = "dos-ddos"
    SABOTAGE = "sabotage"


class EuropolIncidentTaxonomyInformationGatheringEntry(str, Enum):
    SCANNING = "scanning"
    SNIFFING = "sniffing"
    PHISHING = "phishing"


class EuropolIncidentTaxonomyIntrusionAttemptEntry(str, Enum):
    EXPLOITATION_VULNERABILITY = "exploitation-vulnerability"
    LOGIN_ATTEMPT = "login-attempt"


class EuropolIncidentTaxonomyIntrusionEntry(str, Enum):
    EXPLOITATION_VULNERABILITY = "exploitation-vulnerability"
    COMPROMISING_ACCOUNT = "compromising-account"


class EuropolIncidentTaxonomyInformationSecurityEntry(str, Enum):
    UNAUTHORIZED_ACCESS = "unauthorized-access"
    UNAUTHORIZED_MODIFICATION = "unauthorized-modification"


class EuropolIncidentTaxonomyFraudEntry(str, Enum):
    ILLEGITIMATE_USE_RESOURCES = "illegitimate-use-resources"
    ILLEGITIMATE_USE_NAME = "illegitimate-use-name"


class EuropolIncidentTaxonomyAbusiveContentEntry(str, Enum):
    SPAM = "spam"
    COPYRIGHT = "copyright"
    CONTENT_FORBIDDEN_BY_LAW = "content-forbidden-by-law"


class EuropolIncidentTaxonomyOtherEntry(str, Enum):
    OTHER = "other"


class EuropolIncidentTaxonomy(BaseModel):
    """Model for the Europol class of incidents taxonomy taxonomy."""

    namespace: str = "europol-incident"
    description: str = """This taxonomy was designed to describe the type of incidents by class."""
    version: int = 1
    exclusive: bool = False
    predicates: List[EuropolIncidentTaxonomyPredicate] = []
    malware_entries: List[EuropolIncidentTaxonomyMalwareEntry] = []
    availability_entries: List[EuropolIncidentTaxonomyAvailabilityEntry] = []
    information_gathering_entries: List[EuropolIncidentTaxonomyInformationGatheringEntry] = []
    intrusion_attempt_entries: List[EuropolIncidentTaxonomyIntrusionAttemptEntry] = []
    intrusion_entries: List[EuropolIncidentTaxonomyIntrusionEntry] = []
    information_security_entries: List[EuropolIncidentTaxonomyInformationSecurityEntry] = []
    fraud_entries: List[EuropolIncidentTaxonomyFraudEntry] = []
    abusive_content_entries: List[EuropolIncidentTaxonomyAbusiveContentEntry] = []
    other_entries: List[EuropolIncidentTaxonomyOtherEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
