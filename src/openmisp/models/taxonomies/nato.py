"""Taxonomy model for nato."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class NatoTaxonomyPredicate(str, Enum):
    CLASSIFICATION = "classification"


class NatoTaxonomyClassificationEntry(str, Enum):
    CTS = "CTS"
    CTS_B = "CTS-B"
    NS = "NS"
    NC = "NC"
    NR = "NR"
    NU = "NU"
    CTS_A = "CTS-A"
    NS_A = "NS-A"
    NC_A = "NC-A"


class NatoTaxonomy(BaseModel):
    """Model for the nato taxonomy."""

    namespace: str = "nato"
    description: str = """NATO classification markings."""
    version: int = 2
    exclusive: bool = True
    predicates: List[NatoTaxonomyPredicate] = []
    classification_entries: List[NatoTaxonomyClassificationEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
