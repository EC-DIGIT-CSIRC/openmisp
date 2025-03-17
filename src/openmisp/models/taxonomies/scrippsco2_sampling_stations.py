"""Taxonomy model for scrippsco2-sampling-stations."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Scrippsco2SamplingStationsTaxonomyPredicate(str, Enum):
    ALT = "ALT"
    PTB = "PTB"
    STP = "STP"
    LJO = "LJO"
    BCS = "BCS"
    MLO = "MLO"
    KUM = "KUM"
    CHR = "CHR"
    SAM = "SAM"
    KER = "KER"
    NZD = "NZD"
    PSA = "PSA"
    SPO = "SPO"


class Scrippsco2SamplingStationsTaxonomy(BaseModel):
    """Model for the scrippsco2-sampling-stations taxonomy."""

    namespace: str = "scrippsco2-sampling-stations"
    description: str = """Sampling stations of the Scripps CO2 Program"""
    version: int = 1
    exclusive: bool = False
    predicates: List[Scrippsco2SamplingStationsTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
