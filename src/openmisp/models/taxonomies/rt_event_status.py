"""Taxonomy model for rt_event_status."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class RtEventStatusTaxonomyPredicate(str, Enum):
    EVENT_STATUS = "event-status"


class RtEventStatusTaxonomyEventStatusEntry(str, Enum):
    NEW = "new"
    OPEN = "open"
    STALLED = "stalled"
    REJECTED = "rejected"
    RESOLVED = "resolved"
    DELETED = "deleted"


class RtEventStatusTaxonomy(BaseModel):
    """Model for the rt_event_status taxonomy."""

    namespace: str = "rt_event_status"
    description: str = """Status of events used in Request Tracker."""
    version: int = 2
    exclusive: bool = True
    predicates: List[RtEventStatusTaxonomyPredicate] = []
    event_status_entries: List[RtEventStatusTaxonomyEventStatusEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
