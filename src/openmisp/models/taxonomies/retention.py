"""Taxonomy model for retention."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class RetentionTaxonomyPredicate(str, Enum):
    EXPIRED = "expired"
    T_1D = "1d"
    T_2D = "2d"
    T_7D = "7d"
    T_2W = "2w"
    T_1M = "1m"
    T_2M = "2m"
    T_3M = "3m"
    T_6M = "6m"
    T_1Y = "1y"
    T_10Y = "10y"


class RetentionTaxonomy(BaseModel):
    """Model for the retention taxonomy."""

    namespace: str = "retention"
    description: str = """Add a retention time to events to automatically remove the IDS-flag on ip-dst or ip-src attributes. We calculate the time elapsed based on the date of the event. Supported time units are: d(ays), w(eeks), m(onths), y(ears). The numerical_value is just for sorting in the web-interface and is not used for calculations."""
    version: int = 4
    exclusive: bool = True
    predicates: List[RetentionTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
