"""Taxonomy model for euci."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EuciTaxonomyPredicate(str, Enum):
    TS_UE_EU_TS = "TS-UE/EU-TS"
    S_UE_EU_S = "S-UE/EU-S"
    C_UE_EU_C = "C-UE/EU-C"
    R_UE_EU_R = "R-UE/EU-R"


class EuciTaxonomy(BaseModel):
    """Model for the euci taxonomy."""

    namespace: str = "euci"
    description: str = """EU classified information (EUCI) means any information or material designated by a EU security classification, the unauthorised disclosure of which could cause varying degrees of prejudice to the interests of the European Union or of one or more of the Member States."""
    version: int = 3
    exclusive: bool = True
    predicates: List[EuciTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
