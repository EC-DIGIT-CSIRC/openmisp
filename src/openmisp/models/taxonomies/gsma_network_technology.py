"""Taxonomy model for gsma-network-technology."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GsmaNetworkTechnologyTaxonomyPredicate(str, Enum):
    USER = "user"
    APPLICATIONS = "applications"
    END_DEVICES_AND_COMPONENTS = "end-devices-and-components"
    SERVICES = "services"
    RADIO_ACCESS_NETWORK = "radio-access-network"
    SUPPORT_AND_PROVISIONING_SYSTEMS = "support-and-provisioning-systems"
    INTERCONNECTS = "interconnects"
    CORE = "core"
    SIM_SECURE_ELEMENT_MODULES = "sim-secure-element-modules"


class GsmaNetworkTechnologyTaxonomyEndDevicesAndComponentsEntry(str, Enum):
    MS = "ms"
    MOBILE_EQUIPMENT_RADIO = "mobile-equipment-radio"


class GsmaNetworkTechnologyTaxonomy(BaseModel):
    """Model for the gsma-network-technology taxonomy."""

    namespace: str = "gsma-network-technology"
    description: str = """Taxonomy used by GSMA for their information sharing program with telco describing the types of infrastructure. WiP"""
    version: int = 3
    exclusive: bool = False
    predicates: List[GsmaNetworkTechnologyTaxonomyPredicate] = []
    end_devices_and_components_entries: List[GsmaNetworkTechnologyTaxonomyEndDevicesAndComponentsEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
