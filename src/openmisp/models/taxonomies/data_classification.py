"""Taxonomy model for Data Classification."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DataClassificationTaxonomyPredicate(str, Enum):
    REGULATED_DATA = "regulated-data"
    COMMERCIALLY_CONFIDENTIAL_INFORMATION = "commercially-confidential-information"
    FINANCIALLY_SENSITIVE_INFORMATION = "financially-sensitive-information"
    VALUATION_SENSITIVE_INFORMATION = "valuation-sensitive-information"
    SENSITIVE_INFORMATION = "sensitive-information"


class DataClassificationTaxonomy(BaseModel):
    """Model for the Data Classification taxonomy."""

    namespace: str = "data-classification"
    description: str = """Data classification for data potentially at risk of exfiltration based on table 2.1 of Solving Cyber Risk book."""
    version: int = 1
    exclusive: bool = False
    predicates: List[DataClassificationTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
