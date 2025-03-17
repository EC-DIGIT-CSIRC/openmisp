"""Taxonomy model for Protocole des Feux de Circulation."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PfcTaxonomyPredicate(str, Enum):
    ROUGE = "rouge"
    AMBRE = "ambre"
    AMBRE_STRICT = "ambre+strict"
    VERT = "vert"
    LIBRE = "libre"


class PfcTaxonomy(BaseModel):
    """Model for the Protocole des Feux de Circulation taxonomy."""

    namespace: str = "pfc"
    description: str = """Le Protocole des feux de circulation (PFC) est basé sur le standard « Traffic Light Protocol (TLP) » conçu par le FIRST. Il a pour objectif d’informer sur les limites autorisées pour la diffusion des informations. Il est classé selon des codes de couleurs."""
    version: int = 1
    exclusive: bool = True
    predicates: List[PfcTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
