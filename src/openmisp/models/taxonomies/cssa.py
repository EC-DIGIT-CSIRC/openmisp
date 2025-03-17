"""Taxonomy model for cssa."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CssaTaxonomyPredicate(str, Enum):
    SHARING_CLASS = "sharing-class"
    REPORT = "report"
    ORIGIN = "origin"
    ANALYSE = "analyse"


class CssaTaxonomySharingClassEntry(str, Enum):
    HIGH_PROFILE = "high_profile"
    VETTED = "vetted"
    UNVETTED = "unvetted"


class CssaTaxonomyReportEntry(str, Enum):
    DETAILS = "details"
    LINK = "link"
    ATTACHED = "attached"


class CssaTaxonomyOriginEntry(str, Enum):
    MANUAL_INVESTIGATION = "manual_investigation"
    HONEYPOT = "honeypot"
    SANDBOX = "sandbox"
    EMAIL = "email"
    T_3RD_PARTY = "3rd-party"
    REPORT = "report"
    OTHER = "other"
    UNKNOWN = "unknown"


class CssaTaxonomy(BaseModel):
    """Model for the cssa taxonomy."""

    namespace: str = "cssa"
    description: str = """The CSSA agreed sharing taxonomy."""
    version: int = 8
    exclusive: bool = False
    predicates: List[CssaTaxonomyPredicate] = []
    sharing_class_entries: List[CssaTaxonomySharingClassEntry] = []
    report_entries: List[CssaTaxonomyReportEntry] = []
    origin_entries: List[CssaTaxonomyOriginEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
