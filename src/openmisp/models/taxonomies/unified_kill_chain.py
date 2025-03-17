"""Taxonomy model for Unified Kill Chain."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class UnifiedKillChainTaxonomyPredicate(str, Enum):
    INITIAL_FOOTHOLD = "Initial Foothold"
    NETWORK_PROPAGATION = "Network Propagation"
    ACTION_ON_OBJECTIVES = "Action on Objectives"


class UnifiedKillChainTaxonomyInitialFootholdEntry(str, Enum):
    RECONNAISSANCE = "reconnaissance"
    WEAPONIZATION = "weaponization"
    DELIVERY = "delivery"
    SOCIAL_ENGINEERING = "social-engineering"
    EXPLOITATION = "exploitation"
    PERSISTENCE = "persistence"
    DEFENSE_EVASION = "defense-evasion"
    COMMAND_CONTROL = "command-control"


class UnifiedKillChainTaxonomyNetworkPropagationEntry(str, Enum):
    PIVOTING = "pivoting"
    DISCOVERY = "discovery"
    PRIVILEGE_ESCALATION = "privilege-escalation"
    EXECUTION = "execution"
    CREDENTIAL_ACCESS = "credential-access"
    LATERAL_MOVEMENT = "lateral-movement"


class UnifiedKillChainTaxonomyActionOnObjectivesEntry(str, Enum):
    ACCESS = "access"
    COLLECTION = "collection"
    EXFILTRATION = "exfiltration"
    IMPACT = "impact"
    OBJECTIVES = "objectives"


class UnifiedKillChainTaxonomy(BaseModel):
    """Model for the Unified Kill Chain taxonomy."""

    namespace: str = "unified-kill-chain"
    description: str = """The Unified Kill Chain is a refinement to the Kill Chain."""
    version: int = 1
    exclusive: bool = False
    predicates: List[UnifiedKillChainTaxonomyPredicate] = []
    initial_foothold_entries: List[UnifiedKillChainTaxonomyInitialFootholdEntry] = []
    network_propagation_entries: List[UnifiedKillChainTaxonomyNetworkPropagationEntry] = []
    action_on_objectives_entries: List[UnifiedKillChainTaxonomyActionOnObjectivesEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
