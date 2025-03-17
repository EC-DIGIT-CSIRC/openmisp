"""Taxonomy model for Domain-Generation Algorithms."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DgaTaxonomyPredicate(str, Enum):
    GENERATION_SCHEME = "generation-scheme"
    SEEDING = "seeding"


class DgaTaxonomyGenerationSchemeEntry(str, Enum):
    ARITHMETIC = "arithmetic"
    HASH = "hash"
    WORDLIST = "wordlist"
    PERMUTATION = "permutation"


class DgaTaxonomySeedingEntry(str, Enum):
    TIME_DEPENDENT = "time-dependent"
    TIME_INDEPENDENT = "time-independent"
    DETERMINISTIC = "deterministic"
    NON_DETERMINISTIC = "non-deterministic"


class DgaTaxonomy(BaseModel):
    """Model for the Domain-Generation Algorithms taxonomy."""

    namespace: str = "dga"
    description: str = """A taxonomy to describe domain-generation algorithms often called DGA. Ref: A Comprehensive Measurement Study of Domain Generating Malware Daniel Plohmann and others."""
    version: int = 2
    exclusive: bool = False
    predicates: List[DgaTaxonomyPredicate] = []
    generation_scheme_entries: List[DgaTaxonomyGenerationSchemeEntry] = []
    seeding_entries: List[DgaTaxonomySeedingEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
