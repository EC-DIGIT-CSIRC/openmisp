"""Taxonomy model for current-event."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CurrentEventTaxonomyPredicate(str, Enum):
    PANDEMIC = "pandemic"
    ELECTION = "election"


class CurrentEventTaxonomyPandemicEntry(str, Enum):
    SARS_COV = "sars-cov"
    COVID_19 = "covid-19"


class CurrentEventTaxonomyElectionEntry(str, Enum):
    EU_PAR_2019 = "eu-par-2019"
    US_PRES_2020 = "us-pres-2020"


class CurrentEventTaxonomy(BaseModel):
    """Model for the current-event taxonomy."""

    namespace: str = "current-event"
    description: str = """Current events - Schemes of Classification in Incident Response and Detection"""
    version: int = 1
    exclusive: bool = False
    predicates: List[CurrentEventTaxonomyPredicate] = []
    pandemic_entries: List[CurrentEventTaxonomyPandemicEntry] = []
    election_entries: List[CurrentEventTaxonomyElectionEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
