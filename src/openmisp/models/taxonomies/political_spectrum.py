"""Taxonomy model for Political Spectrum."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PoliticalSpectrumTaxonomyPredicate(str, Enum):
    IDEOLOGY = "ideology"
    LEFT_RIGHT_SPECTRUM = "left-right-spectrum"


class PoliticalSpectrumTaxonomyIdeologyEntry(str, Enum):
    AGRARIANISM = "agrarianism"
    ANARCHISM = "anarchism"
    CENTRISM = "centrism"
    CHRISTIAN_DEMOCRACY = "christian-democracy"
    COMMUNISM = "communism"
    CONSERVATISM = "conservatism"
    DEMOCRATIC_SOCIALISM = "democratic-socialism"
    FASCISM = "fascism"
    FEMINISM = "feminism"
    GREEN_POLITICS = "green-politics"
    ISLAMISM = "islamism"
    LIBERALISM = "liberalism"
    LIBERTARIANISM = "libertarianism"
    MONARCHISM = "monarchism"
    PACIFISM = "pacifism"
    SOCIAL_DEMOCRACY = "social-democracy"
    SOCIALISM = "socialism"


class PoliticalSpectrumTaxonomyLeftRightSpectrumEntry(str, Enum):
    FAR_LEFT = "far-left"
    CENTRE_LEFT = "centre-left"
    RADICAL_CENTRE = "radical-centre"
    CENTRE_RIGHT = "centre-right"
    FAR_RIGHT = "far-right"


class PoliticalSpectrumTaxonomy(BaseModel):
    """Model for the Political Spectrum taxonomy."""

    namespace: str = "political-spectrum"
    description: str = """A political spectrum is a system to characterize and classify different political positions in relation to one another."""
    version: int = 1
    exclusive: bool = False
    predicates: List[PoliticalSpectrumTaxonomyPredicate] = []
    ideology_entries: List[PoliticalSpectrumTaxonomyIdeologyEntry] = []
    left_right_spectrum_entries: List[PoliticalSpectrumTaxonomyLeftRightSpectrumEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
