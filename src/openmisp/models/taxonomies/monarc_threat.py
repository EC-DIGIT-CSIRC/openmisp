"""Taxonomy model for MONARC Threats."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class MonarcThreatTaxonomyPredicate(str, Enum):
    COMPROMISE_OF_FUNCTIONS = "compromise-of-functions"
    UNAUTHORISED_ACTIONS = "unauthorised-actions"
    COMPROMISE_OF_INFORMATION = "compromise-of-information"
    LOSS_OF_ESSENTIAL_SERVICES = "loss-of-essential-services"
    TECHNICAL_FAILURES = "technical-failures"
    PHYSICAL_DAMAGE = "physical-damage"


class MonarcThreatTaxonomyCompromiseOfFunctionsEntry(str, Enum):
    ERROR_IN_USE = "error-in-use"
    FORGING_OF_RIGHTS = "forging-of-rights"
    EAVESDROPPING = "eavesdropping"
    DENIAL_OF_ACTIONS = "denial-of-actions"
    ABUSE_OF_RIGHTS = "abuse-of-rights"
    BREACH_OF_PERSONNEL_AVAILABILITY = "breach-of-personnel-availability"


class MonarcThreatTaxonomyUnauthorisedActionsEntry(str, Enum):
    FRAUDULENT_COPYING_OR_USE_OF_COUNTERFEIT_SOFTWARE = "fraudulent-copying-or-use-of-counterfeit-software"
    CORRUPTION_OF_DATA = "corruption-of-data"
    ILLEGAL_PROCESSING_OF_DATA = "illegal-processing-of-data"


class MonarcThreatTaxonomyCompromiseOfInformationEntry(str, Enum):
    REMOTE_SPYING = "remote-spying"
    TAMPERING_WITH_HARDWARE = "tampering-with-hardware"
    INTERCEPTION_OF_COMPROMISING_INTERFERENCE_SIGNALS = "interception-of-compromising-interference-signals"
    THEFT_OR_DESTRUCTION_OF_MEDIA_DOCUMENTS_OR_EQUIPMENT = "theft-or-destruction-of-media-documents-or-equipment"
    RETRIEVAL_OF_RECYCLED_OR_DISCARDED_MEDIA = "retrieval-of-recycled-or-discarded media"
    MALWARE_INFECTION = "malware-infection"
    DATA_FROM_UNTRUSTWORTHY_SOURCES = "data-from-untrustworthy-sources"
    DISCLOSURE = "disclosure"


class MonarcThreatTaxonomyLossOfEssentialServicesEntry(str, Enum):
    FAILURE_OF_TELECOMMUNICATION_EQUIPMENT = "failure-of-telecommunication-equipment"
    LOSS_OF_POWER_SUPPLY = "loss-of-power-supply"
    FAILURE_OF_AIR_CONDITIONING = "failure-of-air-conditioning"


class MonarcThreatTaxonomyTechnicalFailuresEntry(str, Enum):
    SOFTWARE_MALFUNCTION = "software-malfunction"
    EQUIPMENT_MALFUNCTION_OR_FAILURE = "equipment-malfunction-or-failure"
    SATURATION_OF_THE_INFORMATION_SYSTEM = "saturation-of-the-information-system"
    BREACH_OF_INFORMATION_SYSTEM_MAINTAINABILITY = "breach-of-information-system-maintainability"


class MonarcThreatTaxonomyPhysicalDamageEntry(str, Enum):
    DESTRUCTION_OF_EQUIPMENT_OR_SUPPORTS = "destruction-of-equipment-or-supports"
    FIRE = "fire"
    WATER_DAMAGE = "water-damage"
    MAJOR_ACCIDENT = "major-accident"
    POLLUTION = "pollution"
    ENVIRONMENTAL_DISASTER = "environmental-disaster"


class MonarcThreatTaxonomy(BaseModel):
    """Model for the MONARC Threats taxonomy."""

    namespace: str = "monarc-threat"
    description: str = """MONARC Threats Taxonomy"""
    version: int = 1
    exclusive: bool = False
    predicates: List[MonarcThreatTaxonomyPredicate] = []
    compromise_of_functions_entries: List[MonarcThreatTaxonomyCompromiseOfFunctionsEntry] = []
    unauthorised_actions_entries: List[MonarcThreatTaxonomyUnauthorisedActionsEntry] = []
    compromise_of_information_entries: List[MonarcThreatTaxonomyCompromiseOfInformationEntry] = []
    loss_of_essential_services_entries: List[MonarcThreatTaxonomyLossOfEssentialServicesEntry] = []
    technical_failures_entries: List[MonarcThreatTaxonomyTechnicalFailuresEntry] = []
    physical_damage_entries: List[MonarcThreatTaxonomyPhysicalDamageEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
