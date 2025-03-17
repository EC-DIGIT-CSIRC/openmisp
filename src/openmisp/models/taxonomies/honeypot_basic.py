"""Taxonomy model for honeypot-basic."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class HoneypotBasicTaxonomyPredicate(str, Enum):
    INTERACTION_LEVEL = "interaction-level"
    DATA_CAPTURE = "data-capture"
    CONTAINMENT = "containment"
    DISTRIBUTION_APPEARANCE = "distribution-appearance"
    COMMUNICATION_INTERFACE = "communication-interface"
    ROLE = "role"


class HoneypotBasicTaxonomyInteractionLevelEntry(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"
    ADAPTIVE = "adaptive"


class HoneypotBasicTaxonomyDataCaptureEntry(str, Enum):
    NETWORK_CAPTURE = "network-capture"
    EVENTS = "events"
    ATTACKS = "attacks"
    INTRUSIONS = "intrusions"
    NONE = "none"


class HoneypotBasicTaxonomyContainmentEntry(str, Enum):
    BLOCK = "block"
    DEFUSE = "defuse"
    SLOW_DOWN = "slow-down"
    NONE = "none"


class HoneypotBasicTaxonomyDistributionAppearanceEntry(str, Enum):
    DISTRIBUTED = "distributed"
    STAND_ALONE = "stand-alone"


class HoneypotBasicTaxonomyCommunicationInterfaceEntry(str, Enum):
    NETWORK_INTERFACE = "network-interface"
    HARDWARE_INTERFACE = "hardware-interface"
    SOFTWARE_API = "software-api"


class HoneypotBasicTaxonomyRoleEntry(str, Enum):
    SERVER = "server"
    CLIENT = "client"


class HoneypotBasicTaxonomy(BaseModel):
    """Model for the honeypot-basic taxonomy."""

    namespace: str = "honeypot-basic"
    description: str = """Updated (CIRCL, Seamus Dowling and EURECOM) from Christian Seifert, Ian Welch, Peter Komisarczuk, ‘Taxonomy of Honeypots’, Technical Report CS-TR-06/12, VICTORIA UNIVERSITY OF WELLINGTON, School of Mathematical and Computing Sciences, June 2006, http://www.mcs.vuw.ac.nz/comp/Publications/archive/CS-TR-06/CS-TR-06-12.pdf"""
    version: int = 4
    exclusive: bool = False
    predicates: List[HoneypotBasicTaxonomyPredicate] = []
    interaction_level_entries: List[HoneypotBasicTaxonomyInteractionLevelEntry] = []
    data_capture_entries: List[HoneypotBasicTaxonomyDataCaptureEntry] = []
    containment_entries: List[HoneypotBasicTaxonomyContainmentEntry] = []
    distribution_appearance_entries: List[HoneypotBasicTaxonomyDistributionAppearanceEntry] = []
    communication_interface_entries: List[HoneypotBasicTaxonomyCommunicationInterfaceEntry] = []
    role_entries: List[HoneypotBasicTaxonomyRoleEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
