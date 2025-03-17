"""Taxonomy model for Event Assessment."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EventAssessmentTaxonomyPredicate(str, Enum):
    ALTERNATIVE_POINTS_OF_VIEW_PROCESS = "alternative-points-of-view-process"


class EventAssessmentTaxonomyAlternativePointsOfViewProcessEntry(str, Enum):
    ANALYTIC_DEBATES_WITHIN_THE_ORGANISATION = "analytic-debates-within-the-organisation"
    DEVILS_ADVOCATES_METHODOLOGY = "devils-advocates-methodology"
    COMPETITIVE_ANALYSIS = "competitive-analysis"
    INTERDISCIPLINARY_BRAINSTORMING = "interdisciplinary-brainstorming"
    INTRA_OFFICE_PEER_REVIEW = "intra-office-peer-review"
    OUTSIDE_EXPERTISE_REVIEW = "outside-expertise-review"


class EventAssessmentTaxonomy(BaseModel):
    """Model for the Event Assessment taxonomy."""

    namespace: str = "event-assessment"
    description: str = """A series of assessment predicates describing the event assessment performed to make judgement(s) under a certain level of uncertainty."""
    version: int = 2
    exclusive: bool = False
    predicates: List[EventAssessmentTaxonomyPredicate] = []
    alternative_points_of_view_process_entries: List[EventAssessmentTaxonomyAlternativePointsOfViewProcessEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
