"""Taxonomy model for pandemic."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PandemicTaxonomyPredicate(str, Enum):
    COVID_19 = "covid-19"


class PandemicTaxonomyCovid19Entry(str, Enum):
    HEALTH = "health"
    CYBER = "cyber"
    DISINFORMATION = "disinformation"
    GEOSTRATEGY = "geostrategy"


class PandemicTaxonomy(BaseModel):
    """Model for the pandemic taxonomy."""

    namespace: str = "pandemic"
    description: str = """Pandemic"""
    version: int = 4
    exclusive: bool = False
    predicates: List[PandemicTaxonomyPredicate] = []
    covid_19_entries: List[PandemicTaxonomyCovid19Entry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
