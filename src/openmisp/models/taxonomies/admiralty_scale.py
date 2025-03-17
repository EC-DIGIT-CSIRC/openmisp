"""Taxonomy model for admiralty-scale."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class AdmiraltyScaleTaxonomyPredicate(str, Enum):
    SOURCE_RELIABILITY = "source-reliability"
    INFORMATION_CREDIBILITY = "information-credibility"


class AdmiraltyScaleTaxonomySourceReliabilityEntry(str, Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"
    F = "f"
    G = "g"


class AdmiraltyScaleTaxonomyInformationCredibilityEntry(str, Enum):
    T_1 = "1"
    T_2 = "2"
    T_3 = "3"
    T_4 = "4"
    T_5 = "5"
    T_6 = "6"


class AdmiraltyScaleTaxonomy(BaseModel):
    """Model for the admiralty-scale taxonomy."""

    namespace: str = "admiralty-scale"
    description: str = """The Admiralty Scale or Ranking (also called the NATO System) is used to rank the reliability of a source and the credibility of an information. Reference based on FM 2-22.3 (FM 34-52) HUMAN INTELLIGENCE COLLECTOR OPERATIONS and NATO documents."""
    version: int = 5
    exclusive: bool = False
    predicates: List[AdmiraltyScaleTaxonomyPredicate] = []
    source_reliability_entries: List[AdmiraltyScaleTaxonomySourceReliabilityEntry] = []
    information_credibility_entries: List[AdmiraltyScaleTaxonomyInformationCredibilityEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
