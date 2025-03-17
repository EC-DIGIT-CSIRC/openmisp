"""Taxonomy model for fpf."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class FpfTaxonomyPredicate(str, Enum):
    DEGREES_OF_IDENTIFIABILITY = "degrees-of-identifiability"
    PSEUDONYMOUS_DATA = "pseudonymous-data"
    DE_IDENTIFIED_DATA = "de-identified-data"
    ANONYMOUS_DATA = "anonymous-data"


class FpfTaxonomyDegreesOfIdentifiabilityEntry(str, Enum):
    EXPLICITLY_PERSONAL = "explicitly-personal"
    POTENTIALLY_IDENTIFIABLE = "potentially-identifiable"
    NOT_READILY_IDENTIFIABLE = "not-readily-identifiable"


class FpfTaxonomyPseudonymousDataEntry(str, Enum):
    KEY_CODED = "key-coded"
    PSEUDONYMOUS = "pseudonymous"
    PROTECTED_PSEUDONYMOUS = "protected-pseudonymous"


class FpfTaxonomyDeIdentifiedDataEntry(str, Enum):
    DE_IDENTIFIED = "de-identified"
    PROTECTED_DE_IDENTIFIED = "protected-de-identified"


class FpfTaxonomyAnonymousDataEntry(str, Enum):
    ANONYMOUS = "anonymous"
    AGGREGATED_ANONYMOUS = "aggregated-anonymous"


class FpfTaxonomy(BaseModel):
    """Model for the fpf taxonomy."""

    namespace: str = "fpf"
    description: str = """The Future of Privacy Forum (FPF) [visual guide to practical de-identification](https://fpf.org/2016/04/25/a-visual-guide-to-practical-data-de-identification/) taxonomy is used to evaluate the degree of identifiability of personal data and the types of pseudonymous data, de-identified data and anonymous data. The work of FPF is licensed under a creative commons attribution 4.0 international license."""
    version: int = 0
    exclusive: bool = False
    predicates: List[FpfTaxonomyPredicate] = []
    degrees_of_identifiability_entries: List[FpfTaxonomyDegreesOfIdentifiabilityEntry] = []
    pseudonymous_data_entries: List[FpfTaxonomyPseudonymousDataEntry] = []
    de_identified_data_entries: List[FpfTaxonomyDeIdentifiedDataEntry] = []
    anonymous_data_entries: List[FpfTaxonomyAnonymousDataEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
