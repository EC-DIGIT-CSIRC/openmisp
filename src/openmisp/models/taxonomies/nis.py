"""Taxonomy model for nis."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class NisTaxonomyPredicate(str, Enum):
    IMPACT_SECTORS_IMPACTED = "impact-sectors-impacted"
    IMPACT_SEVERITY = "impact-severity"
    IMPACT_OUTLOOK = "impact-outlook"
    NATURE_ROOT_CAUSE = "nature-root-cause"
    NATURE_SEVERITY = "nature-severity"
    TEST = "test"


class NisTaxonomyImpactSectorsImpactedEntry(str, Enum):
    ENERGY = "energy"
    TRANSPORT = "transport"
    BANKING = "banking"
    FINANCIAL = "financial"
    HEALTH = "health"
    DRINKING_WATER = "drinking-water"
    DIGITAL_INFRASTRUCTURE = "digital-infrastructure"
    COMMUNICATIONS = "communications"
    DIGITAL_SERVICES = "digital-services"
    TRUST_AND_IDENTIFICATION_SERVICES = "trust-and-identification-services"
    GOVERNMENT = "government"


class NisTaxonomyImpactSeverityEntry(str, Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    WHITE = "white"


class NisTaxonomyImpactOutlookEntry(str, Enum):
    IMPROVING = "improving"
    STABLE = "stable"
    WORSENING = "worsening"


class NisTaxonomyNatureRootCauseEntry(str, Enum):
    SYSTEM_FAILURES = "system-failures"
    NATURAL_PHENOMENA = "natural-phenomena"
    HUMAN_ERRORS = "human-errors"
    MALICIOUS_ACTIONS = "malicious-actions"
    THIRD_PARTY_FAILURES = "third-party-failures"


class NisTaxonomyNatureSeverityEntry(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class NisTaxonomyTestEntry(str, Enum):
    TEST = "test"


class NisTaxonomy(BaseModel):
    """Model for the nis taxonomy."""

    namespace: str = "nis"
    description: str = """The taxonomy is meant for large scale cybersecurity incidents, as mentioned in the Commission Recommendation of 13 September 2017, also known as the blueprint. It has two core parts: The nature of the incident, i.e. the underlying cause, that triggered the incident, and the impact of the incident, i.e. the impact on services, in which sector(s) of economy and society."""
    version: int = 2
    exclusive: bool = False
    predicates: List[NisTaxonomyPredicate] = []
    impact_sectors_impacted_entries: List[NisTaxonomyImpactSectorsImpactedEntry] = []
    impact_severity_entries: List[NisTaxonomyImpactSeverityEntry] = []
    impact_outlook_entries: List[NisTaxonomyImpactOutlookEntry] = []
    nature_root_cause_entries: List[NisTaxonomyNatureRootCauseEntry] = []
    nature_severity_entries: List[NisTaxonomyNatureSeverityEntry] = []
    test_entries: List[NisTaxonomyTestEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
