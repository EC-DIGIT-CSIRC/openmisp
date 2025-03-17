"""Taxonomy model for type."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class TypeTaxonomyPredicate(str, Enum):
    OSINT = "OSINT"
    SIGINT = "SIGINT"
    TECHINT = "TECHINT"
    CYBINT = "CYBINT"
    DNINT = "DNINT"
    HUMINT = "HUMINT"
    MEDINT = "MEDINT"
    GEOINT = "GEOINT"
    IMINT = "IMINT"
    MASINT = "MASINT"
    FININT = "FININT"


class TypeTaxonomy(BaseModel):
    """Model for the type taxonomy."""

    namespace: str = "type"
    description: str = """Taxonomy to describe different types of intelligence gathering discipline which can be described the origin of intelligence."""
    version: int = 1
    exclusive: bool = False
    predicates: List[TypeTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
