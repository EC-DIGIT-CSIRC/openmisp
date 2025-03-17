"""Taxonomy model for fr-classif."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class FrClassifTaxonomyPredicate(str, Enum):
    CLASSIFIEES = "classifiees"
    NON_CLASSIFIEES = "non-classifiees"
    SPECIAL_FRANCE = "special-france"


class FrClassifTaxonomyClassifieesEntry(str, Enum):
    TRES_SECRET = "TRES_SECRET"
    SECRET = "SECRET"


class FrClassifTaxonomyNonClassifieesEntry(str, Enum):
    DIFFUSION_RESTREINTE = "DIFFUSION_RESTREINTE"
    NON_PROTEGE = "NON-PROTEGE"


class FrClassifTaxonomySpecialFranceEntry(str, Enum):
    SPECIAL_FRANCE = "SPECIAL_FRANCE"


class FrClassifTaxonomy(BaseModel):
    """Model for the fr-classif taxonomy."""

    namespace: str = "fr-classif"
    description: str = """French gov information classification system"""
    version: int = 6
    exclusive: bool = False
    predicates: List[FrClassifTaxonomyPredicate] = []
    classifiees_entries: List[FrClassifTaxonomyClassifieesEntry] = []
    non_classifiees_entries: List[FrClassifTaxonomyNonClassifieesEntry] = []
    special_france_entries: List[FrClassifTaxonomySpecialFranceEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
