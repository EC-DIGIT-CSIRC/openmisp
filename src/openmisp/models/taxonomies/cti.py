"""Taxonomy model for cti."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CtiTaxonomyPredicate(str, Enum):
    PLANNING = "planning"
    COLLECTION = "collection"
    PROCESSING_AND_ANALYSIS = "processing-and-analysis"
    DISSEMINATION_DONE = "dissemination-done"
    FEEDBACK_RECEIVED = "feedback-received"
    FEEDBACK_PENDING = "feedback-pending"


class CtiTaxonomy(BaseModel):
    """Model for the cti taxonomy."""

    namespace: str = "cti"
    description: str = """Cyber Threat Intelligence cycle to control workflow state of your process."""
    version: int = 1
    exclusive: bool = False
    predicates: List[CtiTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
