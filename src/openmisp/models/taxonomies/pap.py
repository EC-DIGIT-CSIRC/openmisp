"""Taxonomy model for Permissible Actions Protocol."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PapTaxonomyPredicate(str, Enum):
    RED = "RED"
    AMBER = "AMBER"
    GREEN = "GREEN"
    CLEAR = "CLEAR"
    WHITE = "WHITE"


class PapTaxonomy(BaseModel):
    """Model for the Permissible Actions Protocol taxonomy."""

    namespace: str = "PAP"
    description: str = """The Permissible Actions Protocol - or short: PAP - was designed to indicate how the received information can be used."""
    version: int = 3
    exclusive: bool = True
    predicates: List[PapTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
