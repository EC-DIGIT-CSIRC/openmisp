"""Taxonomy model for dhs-ciip-sectors."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DhsCiipSectorsTaxonomyPredicate(str, Enum):
    DHS_CRITICAL_SECTORS = "DHS-critical-sectors"
    SECTOR = "sector"


class DhsCiipSectorsTaxonomyDhsCriticalSectorsEntry(str, Enum):
    CHEMICAL = "chemical"
    COMMERCIAL_FACILITIES = "commercial-facilities"
    COMMUNICATIONS = "communications"
    CRITICAL_MANUFACTURING = "critical-manufacturing"
    DAMS = "dams"
    DIB = "dib"
    EMERGENCY_SERVICES = "emergency-services"
    ENERGY = "energy"
    FINANCIAL_SERVICES = "financial-services"
    FOOD_AGRICULTURE = "food-agriculture"
    GOVERNMENT_FACILITIES = "government-facilities"
    HEALTHCARE_PUBLIC = "healthcare-public"
    IT = "it"
    NUCLEAR = "nuclear"
    TRANSPORT = "transport"
    WATER = "water"


class DhsCiipSectorsTaxonomy(BaseModel):
    """Model for the dhs-ciip-sectors taxonomy."""

    namespace: str = "dhs-ciip-sectors"
    description: str = """DHS critical sectors as in https://www.dhs.gov/critical-infrastructure-sectors"""
    version: int = 2
    exclusive: bool = False
    predicates: List[DhsCiipSectorsTaxonomyPredicate] = []
    dhs_critical_sectors_entries: List[DhsCiipSectorsTaxonomyDhsCriticalSectorsEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
