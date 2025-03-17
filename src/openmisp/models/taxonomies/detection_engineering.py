"""Taxonomy model for Detection engineering."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DetectionEngineeringTaxonomyPredicate(str, Enum):
    PATTERN_MATCHING = "pattern-matching"


class DetectionEngineeringTaxonomyPatternMatchingEntry(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class DetectionEngineeringTaxonomy(BaseModel):
    """Model for the Detection engineering taxonomy."""

    namespace: str = "detection-engineering"
    description: str = """Taxonomy related to detection engineering techniques"""
    version: int = 1
    exclusive: bool = False
    predicates: List[DetectionEngineeringTaxonomyPredicate] = []
    pattern_matching_entries: List[DetectionEngineeringTaxonomyPatternMatchingEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
