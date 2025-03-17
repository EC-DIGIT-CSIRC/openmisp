"""Taxonomy model for Deception."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DeceptionTaxonomyPredicate(str, Enum):
    SPACE = "space"
    TIME = "time"
    PARTICIPANT = "participant"
    CAUSALITY = "causality"
    QUALITY = "quality"
    ESSENCE = "essence"
    SPEECH_ACT_THEORY = "speech-act-theory"


class DeceptionTaxonomySpaceEntry(str, Enum):
    DIRECTION = "direction"
    LOCATION_AT = "location-at"
    LOCATION_FROM = "location-from"
    LOCATION_TO = "location-to"
    LOCATION_THROUGH = "location-through"
    ORIENTATION = "orientation"


class DeceptionTaxonomyTimeEntry(str, Enum):
    FREQUENCY = "frequency"
    TIME_AT = "time-at"
    TIME_FROM = "time-from"
    TIME_TO = "time-to"
    TIME_THROUGH = "time-through"


class DeceptionTaxonomyParticipantEntry(str, Enum):
    AGENT = "agent"
    BENEFICIARY = "beneficiary"
    EXPERIENCER = "experiencer"
    INSTRUMENT = "instrument"
    OBJECT = "object"
    RECIPIENT = "recipient"


class DeceptionTaxonomyCausalityEntry(str, Enum):
    CAUSE = "cause"
    CONTRADICTION = "contradiction"
    EFFECT = "effect"
    PURPOSE = "purpose"


class DeceptionTaxonomyQualityEntry(str, Enum):
    ACCOMPANIMENT = "accompaniment"
    CONTENT = "content"
    MANNER = "manner"
    MATERIAL = "material"
    MEASURE = "measure"
    ORDER = "order"
    VALUE = "value"


class DeceptionTaxonomyEssenceEntry(str, Enum):
    SUPERTYPE = "supertype"
    WHOLE = "whole"


class DeceptionTaxonomySpeechActTheoryEntry(str, Enum):
    EXTERNAL_PRECONDITION = "external-precondition"
    INTERNAL_PRECONDITION = "internal-precondition"


class DeceptionTaxonomy(BaseModel):
    """Model for the Deception taxonomy."""

    namespace: str = "deception"
    description: str = (
        """Deception is an important component of information operations, valuable for both offense and defense. """
    )
    version: int = 1
    exclusive: bool = False
    predicates: List[DeceptionTaxonomyPredicate] = []
    space_entries: List[DeceptionTaxonomySpaceEntry] = []
    time_entries: List[DeceptionTaxonomyTimeEntry] = []
    participant_entries: List[DeceptionTaxonomyParticipantEntry] = []
    causality_entries: List[DeceptionTaxonomyCausalityEntry] = []
    quality_entries: List[DeceptionTaxonomyQualityEntry] = []
    essence_entries: List[DeceptionTaxonomyEssenceEntry] = []
    speech_act_theory_entries: List[DeceptionTaxonomySpeechActTheoryEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
