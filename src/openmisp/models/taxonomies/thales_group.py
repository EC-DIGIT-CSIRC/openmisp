"""Taxonomy model for Thales Group Taxonomy."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ThalesGroupTaxonomyPredicate(str, Enum):
    DISTRIBUTION = "distribution"
    TO_BLOCK = "to_block"
    MINARM = "minarm"
    ACN = "acn"
    SIGPART = "sigpart"
    A_ISAC = "a_isac"
    INTERCERT_FRANCE = "intercert_france"
    IOC_CONFIDENCE = "ioc_confidence"
    TLP_BLACK = "tlp:black"
    WATCHER = "Watcher"


class ThalesGroupTaxonomyDistributionEntry(str, Enum):
    TEAM_EYES_ONLY = "team_eyes_only"
    LIMITED_DISTRIBUTION = "limited_distribution"
    EXTERNAL_ALLIANCES = "external_alliances"
    CUSTOMERS = "customers"


class ThalesGroupTaxonomyIocConfidenceEntry(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class ThalesGroupTaxonomy(BaseModel):
    """Model for the Thales Group Taxonomy taxonomy."""

    namespace: str = "thales_group"
    description: str = """Thales Group Taxonomy - was designed with the aim of enabling desired sharing and preventing unwanted sharing between Thales Group security communities."""
    version: int = 4
    exclusive: bool = False
    predicates: List[ThalesGroupTaxonomyPredicate] = []
    distribution_entries: List[ThalesGroupTaxonomyDistributionEntry] = []
    ioc_confidence_entries: List[ThalesGroupTaxonomyIocConfidenceEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
