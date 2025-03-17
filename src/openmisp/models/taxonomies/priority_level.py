"""Taxonomy model for priority-level."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PriorityLevelTaxonomyPredicate(str, Enum):
    EMERGENCY = "emergency"
    SEVERE = "severe"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    BASELINE_MINOR = "baseline-minor"
    BASELINE_NEGLIGIBLE = "baseline-negligible"


class PriorityLevelTaxonomy(BaseModel):
    """Model for the priority-level taxonomy."""

    namespace: str = "priority-level"
    description: str = """After an incident is scored, it is assigned a priority level. The six levels listed below are aligned with NCCIC, DHS, and the CISS to help provide a common lexicon when discussing incidents. This priority assignment drives NCCIC urgency, pre-approved incident response offerings, reporting requirements, and recommendations for leadership escalation. Generally, incident priority distribution should follow a similar pattern to the graph below. Based on https://www.cisa.gov/news-events/news/cisa-national-cyber-incident-scoring-system-nciss."""
    version: int = 2
    exclusive: bool = True
    predicates: List[PriorityLevelTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
