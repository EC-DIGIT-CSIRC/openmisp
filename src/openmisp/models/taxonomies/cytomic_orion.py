"""Taxonomy model for cytomic-orion."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CytomicOrionTaxonomyPredicate(str, Enum):
    ACTION = "action"


class CytomicOrionTaxonomyActionEntry(str, Enum):
    UPLOAD = "upload"
    DELETE = "delete"


class CytomicOrionTaxonomy(BaseModel):
    """Model for the cytomic-orion taxonomy."""

    namespace: str = "cytomic-orion"
    description: str = """Taxonomy to describe desired actions for Cytomic Orion"""
    version: int = 1
    exclusive: bool = False
    predicates: List[CytomicOrionTaxonomyPredicate] = []
    action_entries: List[CytomicOrionTaxonomyActionEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
