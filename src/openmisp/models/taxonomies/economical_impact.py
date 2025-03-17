"""Taxonomy model for  Economical Impact."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EconomicalImpactTaxonomyPredicate(str, Enum):
    LOSS = "loss"
    GAIN = "gain"


class EconomicalImpactTaxonomyLossEntry(str, Enum):
    NONE = "none"
    LESS_THAN_25K_EURO = "less-than-25k-euro"
    LESS_THAN_50K_EURO = "less-than-50k-euro"
    LESS_THAN_100K_EURO = "less-than-100k-euro"
    LESS_THAN_1_M_EURO = "less-than-1M-euro"
    LESS_THAN_10_M_EURO = "less-than-10M-euro"
    LESS_THAN_100_M_EURO = "less-than-100M-euro"
    LESS_THAN_1_B_EURO = "less-than-1B-euro"
    MORE_THAN_1_B_EURO = "more-than-1B-euro"


class EconomicalImpactTaxonomyGainEntry(str, Enum):
    NONE = "none"
    LESS_THAN_25K_EUR = "less-than-25k-eur"
    LESS_THAN_50K_EURO = "less-than-50k-euro"
    LESS_THAN_100K_EURO = "less-than-100k-euro"
    LESS_THAN_1_M_EURO = "less-than-1M-euro"
    LESS_THAN_10_M_EURO = "less-than-10M-euro"
    LESS_THAN_100_M_EURO = "less-than-100M-euro"
    LESS_THAN_1_B_EURO = "less-than-1B-euro"
    MORE_THAN_1_B_EURO = "more-than-1B-euro"


class EconomicalImpactTaxonomy(BaseModel):
    """Model for the  Economical Impact taxonomy."""

    namespace: str = "economical-impact"
    description: str = """Economic impact refers to a taxonomy used to describe whether financial effects are positive or negative outcomes related to tagged information. For instance, data exfiltration loss represents a positive outcome for an adversary."""
    version: int = 5
    exclusive: bool = False
    predicates: List[EconomicalImpactTaxonomyPredicate] = []
    loss_entries: List[EconomicalImpactTaxonomyLossEntry] = []
    gain_entries: List[EconomicalImpactTaxonomyGainEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
