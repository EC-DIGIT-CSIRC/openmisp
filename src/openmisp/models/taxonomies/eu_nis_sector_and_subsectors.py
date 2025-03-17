"""Taxonomy model for eu-nis-sector-and-subsectors."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EuNisSectorAndSubsectorsTaxonomyPredicate(str, Enum):
    EU_NIS_OES = "eu-nis-oes"
    EU_NIS_OES_ENERGY = "eu-nis-oes-energy"
    EU_NIS_OES_TRANSPORT = "eu-nis-oes-transport"
    EU_NIS_OES_BANKING = "eu-nis-oes-banking"
    EU_NIS_OES_FINANCIAL = "eu-nis-oes-financial"
    EU_NIS_OES_HEALTH = "eu-nis-oes-health"
    EU_NIS_OES_WATER = "eu-nis-oes-water"
    EU_NIS_OES_DIGINFRA = "eu-nis-oes-diginfra"
    EU_NIS_DSP = "eu-nis-dsp"


class EuNisSectorAndSubsectorsTaxonomyEuNisOesEntry(str, Enum):
    ENERGY = "energy"
    TRANSPORT = "transport"
    BANKING = "banking"
    FINANCIAL = "financial"
    HEALTH = "health"
    WATER = "water"
    DIGITALINFRASTRUCTURE = "digitalinfrastructure"


class EuNisSectorAndSubsectorsTaxonomyEuNisOesEnergyEntry(str, Enum):
    ELECTRICITY_ENERGY = "electricity-energy"
    OIL_ENERGY = "oil-energy"
    GAS_ENERGY = "gas-energy"


class EuNisSectorAndSubsectorsTaxonomyEuNisOesTransportEntry(str, Enum):
    AIR_TRANSPORT = "air-transport"
    RAIL_TRANSPORT = "rail-transport"
    WATER_TRANSPORT = "water-transport"
    ROAD_TRANSPORT = "road-transport"


class EuNisSectorAndSubsectorsTaxonomyEuNisDspEntry(str, Enum):
    MARKET_DSP = "market-dsp"
    SEARCH_DSP = "search-dsp"
    CLOUD_DSP = "cloud-dsp"


class EuNisSectorAndSubsectorsTaxonomy(BaseModel):
    """Model for the eu-nis-sector-and-subsectors taxonomy."""

    namespace: str = "eu-nis-sector-and-subsectors"
    description: str = """Sectors, subsectors, and digital services as identified by the NIS Directive"""
    version: int = 1
    exclusive: bool = False
    predicates: List[EuNisSectorAndSubsectorsTaxonomyPredicate] = []
    eu_nis_oes_entries: List[EuNisSectorAndSubsectorsTaxonomyEuNisOesEntry] = []
    eu_nis_oes_energy_entries: List[EuNisSectorAndSubsectorsTaxonomyEuNisOesEnergyEntry] = []
    eu_nis_oes_transport_entries: List[EuNisSectorAndSubsectorsTaxonomyEuNisOesTransportEntry] = []
    eu_nis_dsp_entries: List[EuNisSectorAndSubsectorsTaxonomyEuNisDspEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
