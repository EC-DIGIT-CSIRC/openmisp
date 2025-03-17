"""Taxonomy model for information-origin."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InformationOriginTaxonomyPredicate(str, Enum):
    HUMAN_GENERATED = "human-generated"
    AI_GENERATED = "AI-generated"
    UNCERTAIN_ORIGIN = "uncertain-origin"


class InformationOriginTaxonomy(BaseModel):
    """Model for the information-origin taxonomy."""

    namespace: str = "information-origin"
    description: str = """Taxonomy for tagging information by its origin: human-generated or AI-generated."""
    version: int = 2
    exclusive: bool = False
    predicates: List[InformationOriginTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
