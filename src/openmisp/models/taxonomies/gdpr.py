"""Taxonomy model for gdpr."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GdprTaxonomyPredicate(str, Enum):
    SPECIAL_CATEGORIES = "special-categories"


class GdprTaxonomySpecialCategoriesEntry(str, Enum):
    RACIAL_OR_ETHNIC_ORIGIN = "racial-or-ethnic-origin"
    POLITICAL_OPINIONS = "political-opinions"
    RELIGIOUS_OR_PHILOSOPHICAL_BELIEFS = "religious-or-philosophical-beliefs"
    TRADE_UNION_MEMBERSHIP = "trade-union-membership"
    GENETIC_DATA = "genetic-data"
    BIOMETRIC_DATA = "biometric-data"
    HEALTH = "health"
    SEX_LIFE_OR_SEXUAL_ORIENTATION = "sex-life-or-sexual-orientation"


class GdprTaxonomy(BaseModel):
    """Model for the gdpr taxonomy."""

    namespace: str = "gdpr"
    description: str = """Taxonomy related to the REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation)"""
    version: int = 0
    exclusive: bool = False
    predicates: List[GdprTaxonomyPredicate] = []
    special_categories_entries: List[GdprTaxonomySpecialCategoriesEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
