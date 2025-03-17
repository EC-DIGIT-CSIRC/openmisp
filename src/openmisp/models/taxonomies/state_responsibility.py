"""Taxonomy model for The Spectrum of State Responsibility."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class StateResponsibilityTaxonomyPredicate(str, Enum):
    STATE_PROHIBITED_ = "state-prohibited."
    STATE_PROHIBITED_BUT_INADEQUATE_ = "state-prohibited-but-inadequate."
    STATE_IGNORED = "state-ignored"
    STATE_ENCOURAGED = "state-encouraged"
    STATE_SHAPED = "state-shaped"
    STATE_COORDINATED = "state-coordinated"
    STATE_ORDERED = "state-ordered"
    STATE_ROGUE_CONDUCTED = "state-rogue-conducted"
    STATE_EXECUTED = "state-executed"
    STATE_INTEGRATED = "state-integrated"


class StateResponsibilityTaxonomy(BaseModel):
    """Model for the The Spectrum of State Responsibility taxonomy."""

    namespace: str = "state-responsibility"
    description: str = """A spectrum of state responsibility to more directly tie the goals of attribution to the needs of policymakers."""
    version: int = 1
    exclusive: bool = False
    predicates: List[StateResponsibilityTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
