"""Taxonomy model for de-vs."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DeVsTaxonomyPredicate(str, Enum):
    EINSTUFUNG = "Einstufung"
    SCHUTZWORT = "Schutzwort"


class DeVsTaxonomyEinstufungEntry(str, Enum):
    STRENG_GEHEIM = "STRENG GEHEIM"
    GEHEIM = "GEHEIM"
    VS_VERTRAULICH = "VS-VERTRAULICH"
    VS_NF_D = "VS-NfD"


class DeVsTaxonomySchutzwortEntry(str, Enum):
    DUMMY = "Dummy"


class DeVsTaxonomy(BaseModel):
    """Model for the de-vs taxonomy."""

    namespace: str = "de-vs"
    description: str = """German (DE) Government classification markings (VS)."""
    version: int = 1
    exclusive: bool = False
    predicates: List[DeVsTaxonomyPredicate] = []
    einstufung_entries: List[DeVsTaxonomyEinstufungEntry] = []
    schutzwort_entries: List[DeVsTaxonomySchutzwortEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
