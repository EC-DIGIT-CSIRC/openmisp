"""Taxonomy model for Interception method."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InterceptionMethodTaxonomyPredicate(str, Enum):
    MAN_IN_THE_MIDDLE = "man-in-the-middle"
    MAN_ON_THE_SIDE = "man-on-the-side"
    PASSIVE = "passive"
    SEARCH_RESULT_POISONING = "search-result-poisoning"
    DNS = "dns"
    HOST_FILE = "host-file"
    OTHER = "other"


class InterceptionMethodTaxonomy(BaseModel):
    """Model for the Interception method taxonomy."""

    namespace: str = "interception-method"
    description: str = """The interception method used to intercept traffic."""
    version: int = 1
    exclusive: bool = False
    predicates: List[InterceptionMethodTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
