"""Taxonomy model for Diamond Model for Intrusion Analysis."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DiamondModelTaxonomyPredicate(str, Enum):
    ADVERSARY = "Adversary"
    CAPABILITY = "Capability"
    INFRASTRUCTURE = "Infrastructure"
    VICTIM = "Victim"


class DiamondModelTaxonomy(BaseModel):
    """Model for the Diamond Model for Intrusion Analysis taxonomy."""

    namespace: str = "diamond-model"
    description: str = """The Diamond Model for Intrusion Analysis establishes the basic atomic element of any intrusion activity, the event, composed of four core features: adversary, infrastructure, capability, and victim."""
    version: int = 1
    exclusive: bool = False
    predicates: List[DiamondModelTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
