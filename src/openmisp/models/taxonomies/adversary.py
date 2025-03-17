"""Taxonomy model for adversary."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class AdversaryTaxonomyPredicate(str, Enum):
    INFRASTRUCTURE_STATUS = "infrastructure-status"
    INFRASTRUCTURE_ACTION = "infrastructure-action"
    INFRASTRUCTURE_STATE = "infrastructure-state"
    INFRASTRUCTURE_TYPE = "infrastructure-type"


class AdversaryTaxonomyInfrastructureStatusEntry(str, Enum):
    UNKNOWN = "unknown"
    COMPROMISED = "compromised"
    OWN_AND_OPERATED = "own-and-operated"


class AdversaryTaxonomyInfrastructureActionEntry(str, Enum):
    PASSIVE_ONLY = "passive-only"
    TAKE_DOWN = "take-down"
    MONITORING_ACTIVE = "monitoring-active"
    PENDING_LAW_ENFORCEMENT_REQUEST = "pending-law-enforcement-request"
    SINKHOLED = "sinkholed"


class AdversaryTaxonomyInfrastructureStateEntry(str, Enum):
    UNKNOWN = "unknown"
    ACTIVE = "active"
    DOWN = "down"


class AdversaryTaxonomyInfrastructureTypeEntry(str, Enum):
    UNKNOWN = "unknown"
    PROXY = "proxy"
    DROP_ZONE = "drop-zone"
    EXPLOIT_DISTRIBUTION_POINT = "exploit-distribution-point"
    VPN = "vpn"
    PANEL = "panel"
    TDS = "tds"
    C2 = "c2"


class AdversaryTaxonomy(BaseModel):
    """Model for the adversary taxonomy."""

    namespace: str = "adversary"
    description: str = """An overview and description of the adversary infrastructure"""
    version: int = 6
    exclusive: bool = False
    predicates: List[AdversaryTaxonomyPredicate] = []
    infrastructure_status_entries: List[AdversaryTaxonomyInfrastructureStatusEntry] = []
    infrastructure_action_entries: List[AdversaryTaxonomyInfrastructureActionEntry] = []
    infrastructure_state_entries: List[AdversaryTaxonomyInfrastructureStateEntry] = []
    infrastructure_type_entries: List[AdversaryTaxonomyInfrastructureTypeEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
