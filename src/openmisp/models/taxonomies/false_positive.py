"""Taxonomy model for False positive."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class FalsePositiveTaxonomyPredicate(str, Enum):
    RISK = "risk"
    CONFIRMED = "confirmed"


class FalsePositiveTaxonomyRiskEntry(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CANNOT_BE_JUDGED = "cannot-be-judged"


class FalsePositiveTaxonomyConfirmedEntry(str, Enum):
    TRUE = "true"
    FALSE = "false"


class FalsePositiveTaxonomy(BaseModel):
    """Model for the False positive taxonomy."""

    namespace: str = "false-positive"
    description: str = """This taxonomy aims to ballpark the expected amount of false positives."""
    version: int = 7
    exclusive: bool = False
    predicates: List[FalsePositiveTaxonomyPredicate] = []
    risk_entries: List[FalsePositiveTaxonomyRiskEntry] = []
    confirmed_entries: List[FalsePositiveTaxonomyConfirmedEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
