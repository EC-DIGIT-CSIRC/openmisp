"""Taxonomy model for incident-disposition."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class IncidentDispositionTaxonomyPredicate(str, Enum):
    INCIDENT = "incident"
    NOT_AN_INCIDENT = "not-an-incident"
    DUPLICATE = "duplicate"


class IncidentDispositionTaxonomyIncidentEntry(str, Enum):
    CONFIRMED = "confirmed"
    DEFERRED = "deferred"
    UNIDENTIFIED = "unidentified"
    TRANSFERRED = "transferred"
    DISCARDED = "discarded"
    SILENTLY_DISCARDED = "silently-discarded"


class IncidentDispositionTaxonomyNotAnIncidentEntry(str, Enum):
    INSUFFICIENT_DATA = "insufficient-data"
    FAULTY_INDICATOR = "faulty-indicator"
    MISCONFIGURATION = "misconfiguration"
    SCAN_PROBE = "scan-probe"
    FAILED = "failed"
    REFUTED = "refuted"


class IncidentDispositionTaxonomyDuplicateEntry(str, Enum):
    DUPLICATE = "duplicate"


class IncidentDispositionTaxonomy(BaseModel):
    """Model for the incident-disposition taxonomy."""

    namespace: str = "incident-disposition"
    description: str = """How an incident is classified in its process to be resolved. The taxonomy is inspired from NASA Incident Response and Management Handbook. https://www.nasa.gov/pdf/589502main_ITS-HBK-2810.09-02%20%5bNASA%20Information%20Security%20Incident%20Management%5d.pdf#page=9"""
    version: int = 2
    exclusive: bool = False
    predicates: List[IncidentDispositionTaxonomyPredicate] = []
    incident_entries: List[IncidentDispositionTaxonomyIncidentEntry] = []
    not_an_incident_entries: List[IncidentDispositionTaxonomyNotAnIncidentEntry] = []
    duplicate_entries: List[IncidentDispositionTaxonomyDuplicateEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
