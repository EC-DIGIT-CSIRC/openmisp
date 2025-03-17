"""Taxonomy model for nis2."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Nis2TaxonomyPredicate(str, Enum):
    IMPACT_SECTORS_IMPACTED = "impact-sectors-impacted"
    IMPACT_SUBSECTORS_IMPACTED = "impact-subsectors-impacted"
    IMPORTANT_ENTITIES = "important-entities"
    IMPACT_SUBSECTORS_IMPORTANT_ENTITIES = "impact-subsectors-important-entities"
    IMPACT_SEVERITY = "impact-severity"
    IMPACT_OUTLOOK = "impact-outlook"
    NATURE_ROOT_CAUSE = "nature-root-cause"
    NATURE_SEVERITY = "nature-severity"
    TEST = "test"


class Nis2TaxonomyImpactSectorsImpactedEntry(str, Enum):
    ENERGY = "energy"
    TRANSPORT = "transport"
    BANKING = "banking"
    FINANCIAL = "financial"
    HEALTH = "health"
    DRINKING_WATER = "drinking-water"
    WASTE_WATER = "waste-water"
    DIGITAL_INFRASTRUCTURE = "digital-infrastructure"
    ICT_SERVICES = "ict-services"
    PUBLIC_ADMINISTRATION = "public-administration"
    SPACE = "space"
    COURIER = "courier"
    WASTE_MANAGEMENT = "waste-management"
    CHEMICAL = "chemical"
    FOOD = "food"
    MANUFACTURING = "manufacturing"
    DIGITAL_PROVIDERS = "digital-providers"
    RESEARCH = "research"


class Nis2TaxonomyImpactSubsectorsImpactedEntry(str, Enum):
    ELECTRICITY = "electricity"
    DISTRICT_HEATING_AND_COOLING = "district-heating-and-cooling"
    OIL = "oil"
    GAS = "gas"
    HYDROGEN = "hydrogen"
    AIR = "air"
    RAIL = "rail"
    WATER = "water"
    ROAD = "road"
    BANKING_SUBSECTOR = "banking-subsector"
    FINANCIAL_SUBSECTOR = "financial-subsector"
    HEALTH_SUBSECTOR = "health-subsector"
    DRINKING_WATER_SUBSECTOR = "drinking-water-subsector"
    WASTE_WATER_SUBSECTOR = "waste-water-subsector"
    DIGITAL_INFRASTRUCTURE_SUBSECTOR = "digital-infrastructure-subsector"
    ICT_MANAGEMENT_SUBSECTOR = "ict-management-subsector"
    PUBLIC_ADMINISTRATION_SUBSECTOR = "public-administration-subsector"
    SPACE_SUBSECTOR = "space-subsector"
    COURIER_SUBSECTOR = "courier-subsector"
    WASTE_MANAGEMENT_SUBSECTOR = "waste-management-subsector"
    CHEMICAL_SUBSECTOR = "chemical-subsector"
    FOOD_SUBSECTOR = "food-subsector"
    MEDICAL_DEVICES_SUBSECTOR = "medical-devices-subsector"
    ELECTRONIC_OPTICAL_SUBSECTOR = "electronic-optical-subsector"
    ELECTRICAL_EQUIPMENT_SUBSECTOR = "electrical-equipment-subsector"
    MACHINE_TOOL_SUBSECTOR = "machine-tool-subsector"
    VEHICLE_MANUFACTURING_SUBSECTOR = "vehicle-manufacturing-subsector"
    OTHER_TRANSPORT_EQUIPMENT_SUBSECTOR = "other-transport-equipment-subsector"
    DIGITAL_PROVIDERS_SUBSECTOR = "digital-providers-subsector"
    RESEARCH_SUBSECTOR = "research-subsector"


class Nis2TaxonomyImportantEntitiesEntry(str, Enum):
    POSTAL = "postal"
    WASTE = "waste"
    CHEMICALS = "chemicals"
    MANUFACTURING = "manufacturing"
    DIGITAL = "digital"


class Nis2TaxonomyImpactSubsectorsImportantEntitiesEntry(str, Enum):
    MEDICAL_DEVICES_MANUFACTURING = "medical-devices-manufacturing"
    COMPUTER_MANUFACTURING = "computer-manufacturing"
    ELECTRICAL_EQUIPMENT_MANUFACTURING = "electrical-equipment-manufacturing"
    MACHINERY_EQUIPMENT_MANUFACTURING = "machinery-equipment-manufacturing"
    VEHICLES_TRAILERS_MANUFACTURING = "vehicles-trailers-manufacturing"
    OTHER_TRANSPORT_MANUFACTURING = "other-transport-manufacturing"


class Nis2TaxonomyImpactSeverityEntry(str, Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    WHITE = "white"


class Nis2TaxonomyImpactOutlookEntry(str, Enum):
    IMPROVING = "improving"
    STABLE = "stable"
    WORSENING = "worsening"


class Nis2TaxonomyNatureRootCauseEntry(str, Enum):
    SYSTEM_FAILURES = "system-failures"
    NATURAL_PHENOMENA = "natural-phenomena"
    HUMAN_ERRORS = "human-errors"
    MALICIOUS_ACTIONS = "malicious-actions"
    THIRD_PARTY_FAILURES = "third-party-failures"


class Nis2TaxonomyNatureSeverityEntry(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Nis2TaxonomyTestEntry(str, Enum):
    TEST = "test"


class Nis2Taxonomy(BaseModel):
    """Model for the nis2 taxonomy."""

    namespace: str = "nis2"
    description: str = """The taxonomy is meant for large scale cybersecurity incidents, as mentioned in the Commission Recommendation of 13 May 2022, also known as the provisional agreement. It has two core parts: The nature of the incident, i.e. the underlying cause, that triggered the incident, and the impact of the incident, i.e. the impact on services, in which sector(s) of economy and society."""
    version: int = 5
    exclusive: bool = False
    predicates: List[Nis2TaxonomyPredicate] = []
    impact_sectors_impacted_entries: List[Nis2TaxonomyImpactSectorsImpactedEntry] = []
    impact_subsectors_impacted_entries: List[Nis2TaxonomyImpactSubsectorsImpactedEntry] = []
    important_entities_entries: List[Nis2TaxonomyImportantEntitiesEntry] = []
    impact_subsectors_important_entities_entries: List[Nis2TaxonomyImpactSubsectorsImportantEntitiesEntry] = []
    impact_severity_entries: List[Nis2TaxonomyImpactSeverityEntry] = []
    impact_outlook_entries: List[Nis2TaxonomyImpactOutlookEntry] = []
    nature_root_cause_entries: List[Nis2TaxonomyNatureRootCauseEntry] = []
    nature_severity_entries: List[Nis2TaxonomyNatureSeverityEntry] = []
    test_entries: List[Nis2TaxonomyTestEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
