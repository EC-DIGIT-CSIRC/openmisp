"""Taxonomy model for Cyber Kill Chain."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class KillChainTaxonomyPredicate(str, Enum):
    RECONNAISSANCE = "Reconnaissance"
    WEAPONIZATION = "Weaponization"
    DELIVERY = "Delivery"
    EXPLOITATION = "Exploitation"
    INSTALLATION = "Installation"
    COMMAND_AND_CONTROL = "Command and Control"
    ACTIONS_ON_OBJECTIVES = "Actions on Objectives"


class KillChainTaxonomy(BaseModel):
    """Model for the Cyber Kill Chain taxonomy."""

    namespace: str = "kill-chain"
    description: str = """The Cyber Kill Chain, a phase-based model developed by Lockheed Martin, aims to help categorise and identify the stage of an attack."""
    version: int = 2
    exclusive: bool = False
    predicates: List[KillChainTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
