"""Taxonomy model for gsma-attack-category."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GsmaAttackCategoryTaxonomyPredicate(str, Enum):
    DENIAL_OF_SERVICE = "denial-of-service"
    EXPLOIT_ATTACK = "exploit-attack"
    INFORMATION_GATHERING = "information-gathering"
    INSIDER_ATTACK = "insider-attack"
    INTERCEPTION_ATTACK = "interception-attack"
    MANIPULATION_ATTACK = "manipulation-attack"
    PHYSICAL_ATTACK = "physical-attack"
    SPOOFING = "spoofing"


class GsmaAttackCategoryTaxonomy(BaseModel):
    """Model for the gsma-attack-category taxonomy."""

    namespace: str = "gsma-attack-category"
    description: str = (
        """Taxonomy used by GSMA for their information sharing program with telco describing the attack categories"""
    )
    version: int = 1
    exclusive: bool = False
    predicates: List[GsmaAttackCategoryTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
