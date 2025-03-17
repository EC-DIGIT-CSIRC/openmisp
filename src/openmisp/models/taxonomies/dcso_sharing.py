"""Taxonomy model for dcso-sharing."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DcsoSharingTaxonomyPredicate(str, Enum):
    EVENT_TYPE = "event-type"


class DcsoSharingTaxonomyEventTypeEntry(str, Enum):
    OBSERVATION = "Observation"
    INCIDENT = "Incident"
    REPORT = "Report"
    ANALYSIS = "Analysis"
    COLLECTION = "Collection"


class DcsoSharingTaxonomy(BaseModel):
    """Model for the dcso-sharing taxonomy."""

    namespace: str = "dcso-sharing"
    description: str = """Taxonomy defined in the DCSO MISP Event Guide. It provides guidance for the creation and consumption of MISP events in a way that minimises the extra effort for the sending party, while enhancing the usefulness for receiving parties."""
    version: int = 1
    exclusive: bool = False
    predicates: List[DcsoSharingTaxonomyPredicate] = []
    event_type_entries: List[DcsoSharingTaxonomyEventTypeEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
