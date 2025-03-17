"""Taxonomy model for event-classification."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EventClassificationTaxonomyPredicate(str, Enum):
    EVENT_CLASS = "event-class"


class EventClassificationTaxonomyEventClassEntry(str, Enum):
    INCIDENT_REPORT = "incident_report"
    INCIDENT = "incident"
    INVESTIGATION = "investigation"
    COUNTERMEASURE = "countermeasure"
    GENERAL = "general"
    EXERCISE = "exercise"


class EventClassificationTaxonomy(BaseModel):
    """Model for the event-classification taxonomy."""

    namespace: str = "event-classification"
    description: str = """Classification of events as seen in tools such as RT/IR, MISP and other"""
    version: int = 1
    exclusive: bool = False
    predicates: List[EventClassificationTaxonomyPredicate] = []
    event_class_entries: List[EventClassificationTaxonomyEventClassEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
