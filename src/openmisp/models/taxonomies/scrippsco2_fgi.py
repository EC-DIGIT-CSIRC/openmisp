"""Taxonomy model for scrippsco2-fgi."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Scrippsco2FgiTaxonomyPredicate(str, Enum):
    T__3 = "-3"
    T_0 = "0"
    T_3 = "3"
    T_5 = "5"
    T_6 = "6"
    T_8 = "8"
    T_9 = "9"


class Scrippsco2FgiTaxonomy(BaseModel):
    """Model for the scrippsco2-fgi taxonomy."""

    namespace: str = "scrippsco2-fgi"
    description: str = """Flags describing the sample for isotopic data (C14, O18)"""
    version: int = 1
    exclusive: bool = False
    predicates: List[Scrippsco2FgiTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
