"""Taxonomy model for Detection Maturity Level."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DmlTaxonomyPredicate(str, Enum):
    T_8 = "8"
    T_7 = "7"
    T_6 = "6"
    T_5 = "5"
    T_4 = "4"
    T_3 = "3"
    T_2 = "2"
    T_1 = "1"
    T_0 = "0"


class DmlTaxonomy(BaseModel):
    """Model for the Detection Maturity Level taxonomy."""

    namespace: str = "DML"
    description: str = """The Detection Maturity Level (DML) model is a capability maturity model for referencing ones maturity in detecting cyber attacks.  It's designed for organizations who perform intel-driven detection and response and who put an emphasis on having a mature detection program."""
    version: int = 1
    exclusive: bool = False
    predicates: List[DmlTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
