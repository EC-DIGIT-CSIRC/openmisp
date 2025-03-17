"""Taxonomy model for  Distributed Denial of Service."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DdosTaxonomyPredicate(str, Enum):
    TYPE = "type"


class DdosTaxonomyTypeEntry(str, Enum):
    AMPLIFICATION_ATTACK = "amplification-attack"
    REFLECTED_SPOOFED_ATTACK = "reflected-spoofed-attack"
    SLOW_READ_ATTACK = "slow-read-attack"
    FLOODING_ATTACK = "flooding-attack"
    POST_ATTACK = "post-attack"


class DdosTaxonomy(BaseModel):
    """Model for the  Distributed Denial of Service taxonomy."""

    namespace: str = "ddos"
    description: str = """Distributed Denial of Service - or short: DDoS - taxonomy supports the description of Denial of Service attacks and especially the types they belong too."""
    version: int = 2
    exclusive: bool = False
    predicates: List[DdosTaxonomyPredicate] = []
    type_entries: List[DdosTaxonomyTypeEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
