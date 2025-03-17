"""Taxonomy model for phishing."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PhishingTaxonomyPredicate(str, Enum):
    TECHNIQUES = "techniques"
    DISTRIBUTION = "distribution"
    REPORT_TYPE = "report-type"
    REPORT_ORIGIN = "report-origin"
    ACTION = "action"
    STATE = "state"
    PSYCHOLOGICAL_ACCEPTABILITY = "psychological-acceptability"
    PRINCIPLE_OF_PERSUASION = "principle-of-persuasion"


class PhishingTaxonomyTechniquesEntry(str, Enum):
    FAKE_WEBSITE = "fake-website"
    EMAIL_SPOOFING = "email-spoofing"
    CLONE_PHISHING = "clone-phishing"
    VOICE_PHISHING = "voice-phishing"
    SEARCH_ENGINES_ABUSE = "search-engines-abuse"
    SMS_PHISHING = "sms-phishing"
    BUSINESS_EMAIL_COMPROMISE = "business email compromise"


class PhishingTaxonomyDistributionEntry(str, Enum):
    SPEAR_PHISHING = "spear-phishing"
    BULK_PHISHING = "bulk-phishing"
    WHALING = "whaling"


class PhishingTaxonomyReportTypeEntry(str, Enum):
    MANUAL_REPORTING = "manual-reporting"
    AUTOMATIC_REPORTING = "automatic-reporting"


class PhishingTaxonomyReportOriginEntry(str, Enum):
    URL_ABUSE = "url-abuse"
    LOOKYLOO = "lookyloo"
    PHISHTANK = "phishtank"
    SPAMBEE = "spambee"


class PhishingTaxonomyActionEntry(str, Enum):
    TAKE_DOWN = "take-down"
    PENDING_LAW_ENFORCEMENT_REQUEST = "pending-law-enforcement-request"
    PENDING_DISPUTE_RESOLUTION = "pending-dispute-resolution"


class PhishingTaxonomyStateEntry(str, Enum):
    UNKNOWN = "unknown"
    ACTIVE = "active"
    DOWN = "down"


class PhishingTaxonomyPsychologicalAcceptabilityEntry(str, Enum):
    UNKNOWN = "unknown"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class PhishingTaxonomyPrincipleOfPersuasionEntry(str, Enum):
    AUTHORITY = "authority"
    SOCIAL_PROOF = "social-proof"
    LIKING_SIMILARITY_DECEPTION = "liking-similarity-deception"
    COMMITMENT_RECIPROCATION_CONSISTENCY = "commitment-reciprocation-consistency"
    DISTRACTION = "distraction"


class PhishingTaxonomy(BaseModel):
    """Model for the phishing taxonomy."""

    namespace: str = "phishing"
    description: str = (
        """Taxonomy to classify phishing attacks including techniques, collection mechanisms and analysis status."""
    )
    version: int = 5
    exclusive: bool = False
    predicates: List[PhishingTaxonomyPredicate] = []
    techniques_entries: List[PhishingTaxonomyTechniquesEntry] = []
    distribution_entries: List[PhishingTaxonomyDistributionEntry] = []
    report_type_entries: List[PhishingTaxonomyReportTypeEntry] = []
    report_origin_entries: List[PhishingTaxonomyReportOriginEntry] = []
    action_entries: List[PhishingTaxonomyActionEntry] = []
    state_entries: List[PhishingTaxonomyStateEntry] = []
    psychological_acceptability_entries: List[PhishingTaxonomyPsychologicalAcceptabilityEntry] = []
    principle_of_persuasion_entries: List[PhishingTaxonomyPrincipleOfPersuasionEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
