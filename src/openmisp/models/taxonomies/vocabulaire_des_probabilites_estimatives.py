"""Taxonomy model for Vocabulaire des probabilités estimatives."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class VocabulaireDesProbabilitesEstimativesTaxonomyPredicate(str, Enum):
    DEGR__DE_PROBABILIT_ = "degré-de-probabilité"


class VocabulaireDesProbabilitesEstimativesTaxonomyDegrDeProbabilitEntry(str, Enum):
    PRESQUE_AUCUNE_CHANCE = "presque-aucune-chance"
    PROBABLEMENT_PAS = "probablement-pas"
    CHANCES___PEU_PR_S_EGALES = "chances-à-peu-près-egales"
    PROBABLE = "probable"
    QUASI_CERTAINE = "quasi-certaine"


class VocabulaireDesProbabilitesEstimativesTaxonomy(BaseModel):
    """Model for the Vocabulaire des probabilités estimatives taxonomy."""

    namespace: str = "vocabulaire-des-probabilites-estimatives"
    description: str = """Ce vocabulaire attribue des valeurs en pourcentage à certains énoncés de probabilité"""
    version: int = 3
    exclusive: bool = True
    predicates: List[VocabulaireDesProbabilitesEstimativesTaxonomyPredicate] = []
    degr__de_probabilit__entries: List[VocabulaireDesProbabilitesEstimativesTaxonomyDegrDeProbabilitEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
