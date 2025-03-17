"""Taxonomy model for flesch-reading-ease."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class FleschReadingEaseTaxonomyPredicate(str, Enum):
    SCORE = "score"


class FleschReadingEaseTaxonomyScoreEntry(str, Enum):
    T_90_100 = "90-100"
    T_80_89 = "80-89"
    T_70_79 = "70-79"
    T_60_69 = "60-69"
    T_50_59 = "50-59"
    T_30_49 = "30-49"
    T_0_29 = "0-29"


class FleschReadingEaseTaxonomy(BaseModel):
    """Model for the flesch-reading-ease taxonomy."""

    namespace: str = "flesch-reading-ease"
    description: str = """Flesch Reading Ease is a revised system for determining the comprehension difficulty of written material. The scoring of the flesh score can have a maximum of 121.22 and there is no limit on how low a score can be (negative score are valid)."""
    version: int = 2
    exclusive: bool = True
    predicates: List[FleschReadingEaseTaxonomyPredicate] = []
    score_entries: List[FleschReadingEaseTaxonomyScoreEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
