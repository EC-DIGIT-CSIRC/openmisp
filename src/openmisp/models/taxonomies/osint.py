"""Taxonomy model for osint."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class OsintTaxonomyPredicate(str, Enum):
    SOURCE_TYPE = "source-type"
    LIFETIME = "lifetime"
    CERTAINTY = "certainty"


class OsintTaxonomySourceTypeEntry(str, Enum):
    BLOG_POST = "blog-post"
    MICROBLOG_POST = "microblog-post"
    TECHNICAL_REPORT = "technical-report"
    PRESENTATION = "presentation"
    NEWS_REPORT = "news-report"
    PASTIE_WEBSITE = "pastie-website"
    ELECTRONIC_FORUM = "electronic-forum"
    MAILING_LIST = "mailing-list"
    BLOCK_OR_FILTER_LIST = "block-or-filter-list"
    SOURCE_CODE_REPOSITORY = "source-code-repository"
    ACCESSIBLE_EVIDENCE = "accessible-evidence"
    EXPANSION = "expansion"
    AUTOMATIC_ANALYSIS = "automatic-analysis"
    AUTOMATIC_COLLECTION = "automatic-collection"
    MANUAL_ANALYSIS = "manual-analysis"
    MANUAL_COLLECTION = "manual-collection"
    UNKNOWN = "unknown"
    OTHER = "other"


class OsintTaxonomyLifetimeEntry(str, Enum):
    PERPETUAL = "perpetual"
    EPHEMERAL = "ephemeral"


class OsintTaxonomyCertaintyEntry(str, Enum):
    T_100 = "100"
    T_93 = "93"
    T_75 = "75"
    T_50 = "50"
    T_30 = "30"
    T_7 = "7"
    T_0 = "0"


class OsintTaxonomy(BaseModel):
    """Model for the osint taxonomy."""

    namespace: str = "osint"
    description: str = """Open Source Intelligence - Classification (MISP taxonomies)"""
    version: int = 11
    exclusive: bool = False
    predicates: List[OsintTaxonomyPredicate] = []
    source_type_entries: List[OsintTaxonomySourceTypeEntry] = []
    lifetime_entries: List[OsintTaxonomyLifetimeEntry] = []
    certainty_entries: List[OsintTaxonomyCertaintyEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
