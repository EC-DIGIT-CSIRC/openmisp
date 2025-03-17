"""Taxonomy model for scrippsco2-fgc."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Scrippsco2FgcTaxonomyPredicate(str, Enum):
    T__3 = "-3"
    T__2 = "-2"
    T__1 = "-1"
    T_0 = "0"
    T_1 = "1"
    T_2 = "2"
    T_3 = "3"
    T_4 = "4"
    T_5 = "5"
    T_6 = "6"
    T_7 = "7"
    T_8 = "8"


class Scrippsco2FgcTaxonomy(BaseModel):
    """Model for the scrippsco2-fgc taxonomy."""

    namespace: str = "scrippsco2-fgc"
    description: str = """Flags describing the sample"""
    version: int = 1
    exclusive: bool = False
    predicates: List[Scrippsco2FgcTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
