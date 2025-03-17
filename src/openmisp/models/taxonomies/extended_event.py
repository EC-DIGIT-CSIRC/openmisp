"""Taxonomy model for extended-event."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ExtendedEventTaxonomyPredicate(str, Enum):
    COMPETITIVE_ANALYSIS = "competitive-analysis"
    EXTENDED_ANALYSIS = "extended-analysis"
    HUMAN_READABLE = "human-readable"
    CHUNKED_EVENT = "chunked-event"
    UPDATE = "update"
    COUNTER_ANALYSIS = "counter-analysis"


class ExtendedEventTaxonomyCompetitiveAnalysisEntry(str, Enum):
    DEVIL_ADVOCATE = "devil-advocate"
    ABSURD_REASONING = "absurd-reasoning"
    ROLE_PLAYING = "role-playing"
    CRYSTAL_BALL = "crystal-ball"


class ExtendedEventTaxonomyExtendedAnalysisEntry(str, Enum):
    AUTOMATIC_EXPANSION = "automatic-expansion"
    AGGRESSIVE_PIVOTING = "aggressive-pivoting"
    COMPLEMENTARY_ANALYSIS = "complementary-analysis"


class ExtendedEventTaxonomyChunkedEventEntry(str, Enum):
    TIME_BASED = "time-based"
    COUNTER_BASED = "counter-based"


class ExtendedEventTaxonomy(BaseModel):
    """Model for the extended-event taxonomy."""

    namespace: str = "extended-event"
    description: str = """Reasons why an event has been extended. This taxonomy must be used on the extended event. The competitive analysis aspect is from Psychology of Intelligence Analysis by Richard J. Heuer, Jr. ref:http://www.foo.be/docs/intelligence/PsychofIntelNew.pdf"""
    version: int = 2
    exclusive: bool = False
    predicates: List[ExtendedEventTaxonomyPredicate] = []
    competitive_analysis_entries: List[ExtendedEventTaxonomyCompetitiveAnalysisEntry] = []
    extended_analysis_entries: List[ExtendedEventTaxonomyExtendedAnalysisEntry] = []
    chunked_event_entries: List[ExtendedEventTaxonomyChunkedEventEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
