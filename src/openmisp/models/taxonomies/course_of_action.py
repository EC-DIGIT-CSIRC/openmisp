"""Taxonomy model for Courses of Action."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CourseOfActionTaxonomyPredicate(str, Enum):
    PASSIVE = "passive"
    ACTIVE = "active"


class CourseOfActionTaxonomyPassiveEntry(str, Enum):
    DISCOVER = "discover"
    NODISCOVER = "nodiscover"
    DETECT = "detect"


class CourseOfActionTaxonomyActiveEntry(str, Enum):
    DENY = "deny"
    DISRUPT = "disrupt"
    DEGRADE = "degrade"
    DECEIVE = "deceive"
    DESTROY = "destroy"


class CourseOfActionTaxonomy(BaseModel):
    """Model for the Courses of Action taxonomy."""

    namespace: str = "course-of-action"
    description: str = """A Course Of Action analysis considers six potential courses of action for the development of a cyber security capability."""
    version: int = 3
    exclusive: bool = False
    predicates: List[CourseOfActionTaxonomyPredicate] = []
    passive_entries: List[CourseOfActionTaxonomyPassiveEntry] = []
    active_entries: List[CourseOfActionTaxonomyActiveEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
