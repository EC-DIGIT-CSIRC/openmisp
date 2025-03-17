"""Taxonomy model for Approved category of action."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ApprovedCategoryOfActionTaxonomyPredicate(str, Enum):
    CAT1 = "cat1"
    CAT2 = "cat2"
    CAT3 = "cat3"
    CAT4 = "cat4"
    CAT5 = "cat5"
    CAT6 = "cat6"


class ApprovedCategoryOfActionTaxonomy(BaseModel):
    """Model for the Approved category of action taxonomy."""

    namespace: str = "approved-category-of-action"
    description: str = """A pre-approved category of action for indicators being shared with partners (MIMIC)."""
    version: int = 1
    exclusive: bool = False
    predicates: List[ApprovedCategoryOfActionTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
