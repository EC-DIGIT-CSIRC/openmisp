"""Taxonomy model for binary-class."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class BinaryClassTaxonomyPredicate(str, Enum):
    TYPE = "type"


class BinaryClassTaxonomyTypeEntry(str, Enum):
    GOOD = "good"
    MALICIOUS = "malicious"
    UNKNOWN = "unknown"


class BinaryClassTaxonomy(BaseModel):
    """Model for the binary-class taxonomy."""

    namespace: str = "binary-class"
    description: str = """Custom taxonomy for types of binary file."""
    version: int = 2
    exclusive: bool = True
    predicates: List[BinaryClassTaxonomyPredicate] = []
    type_entries: List[BinaryClassTaxonomyTypeEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
