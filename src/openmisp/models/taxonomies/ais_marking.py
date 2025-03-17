"""Taxonomy model for ais-marking."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class AisMarkingTaxonomyPredicate(str, Enum):
    TLPMARKING = "TLPMarking"
    AISCONSENT = "AISConsent"
    CISA_PROPRIETARY = "CISA_Proprietary"
    AISMARKING = "AISMarking"


class AisMarkingTaxonomyTlpmarkingEntry(str, Enum):
    WHITE = "WHITE"
    GREEN = "GREEN"
    AMBER = "AMBER"


class AisMarkingTaxonomyAisconsentEntry(str, Enum):
    EVERYONE = "EVERYONE"
    USG = "USG"
    NONE = "NONE"


class AisMarkingTaxonomyCisaProprietaryEntry(str, Enum):
    TRUE = "true"
    FALSE = "false"


class AisMarkingTaxonomyAismarkingEntry(str, Enum):
    IS_PROPRIETARY = "Is_Proprietary"
    NOT_PROPRIETARY = "Not_Proprietary"


class AisMarkingTaxonomy(BaseModel):
    """Model for the ais-marking taxonomy."""

    namespace: str = "ais-marking"
    description: str = """The AIS Marking Schema implementation is maintained by the National Cybersecurity and Communication Integration Center (NCCIC) of the U.S. Department of Homeland Security (DHS)"""
    version: int = 2
    exclusive: bool = False
    predicates: List[AisMarkingTaxonomyPredicate] = []
    tlpmarking_entries: List[AisMarkingTaxonomyTlpmarkingEntry] = []
    aisconsent_entries: List[AisMarkingTaxonomyAisconsentEntry] = []
    cisa_proprietary_entries: List[AisMarkingTaxonomyCisaProprietaryEntry] = []
    aismarking_entries: List[AisMarkingTaxonomyAismarkingEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
