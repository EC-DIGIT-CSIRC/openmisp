"""Taxonomy model for iep2-reference."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Iep2ReferenceTaxonomyPredicate(str, Enum):
    ID_REF = "id_ref"
    URL = "url"
    IEP_VERSION = "iep_version"


class Iep2ReferenceTaxonomyIdRefEntry(str, Enum):
    T__TEXT = "$text"


class Iep2ReferenceTaxonomyUrlEntry(str, Enum):
    T__TEXT = "$text"


class Iep2ReferenceTaxonomyIepVersionEntry(str, Enum):
    T_2_0 = "2.0"


class Iep2ReferenceTaxonomy(BaseModel):
    """Model for the iep2-reference taxonomy."""

    namespace: str = "iep2-reference"
    description: str = (
        """Forum of Incident Response and Security Teams (FIRST) Information Exchange Policy (IEP) v2.0 Reference"""
    )
    version: int = 1
    exclusive: bool = False
    predicates: List[Iep2ReferenceTaxonomyPredicate] = []
    id_ref_entries: List[Iep2ReferenceTaxonomyIdRefEntry] = []
    url_entries: List[Iep2ReferenceTaxonomyUrlEntry] = []
    iep_version_entries: List[Iep2ReferenceTaxonomyIepVersionEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
