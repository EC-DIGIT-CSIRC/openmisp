"""Taxonomy model for Indicators of Trust."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class TrustTaxonomyPredicate(str, Enum):
    TRUST = "trust"
    FREQUENCY = "frequency"
    VALID = "valid"


class TrustTaxonomyTrustEntry(str, Enum):
    UNKNOWN = "unknown"
    NONE = "none"
    PARTIAL = "partial"
    RELATIONSHIP = "relationship"
    FULL = "full"


class TrustTaxonomyFrequencyEntry(str, Enum):
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"


class TrustTaxonomyValidEntry(str, Enum):
    TRUE = "true"
    FALSE = "false"


class TrustTaxonomy(BaseModel):
    """Model for the Indicators of Trust taxonomy."""

    namespace: str = "trust"
    description: str = """The Indicator of Trust provides insight about data on what can be trusted and known as a good actor. Similar to a whitelist but on steroids, reusing features one would use with Indicators of Compromise, but to filter out what is known to be good."""
    version: int = 1
    exclusive: bool = True
    predicates: List[TrustTaxonomyPredicate] = []
    trust_entries: List[TrustTaxonomyTrustEntry] = []
    frequency_entries: List[TrustTaxonomyFrequencyEntry] = []
    valid_entries: List[TrustTaxonomyValidEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
