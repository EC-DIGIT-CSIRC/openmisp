"""Taxonomy model for csirt-americas."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CsirtAmericasTaxonomyPredicate(str, Enum):
    DEFACEMENT = "defacement"
    MALWARE = "malware"
    DDOS = "ddos"
    PHISHING = "phishing"
    SPAM = "spam"
    BOTNET = "botnet"
    FASTFLUX = "fastflux"
    CRYPTOJACKING = "cryptojacking"
    XSS = "xss"
    SQLI = "sqli"
    VULNERABILITY = "vulnerability"
    INFOLEAK = "infoleak"
    COMPROMISE = "compromise"
    OTHER = "other"


class CsirtAmericasTaxonomy(BaseModel):
    """Model for the csirt-americas taxonomy."""

    namespace: str = "csirt-americas"
    description: str = """Taxonomía CSIRT Américas."""
    version: int = 1
    exclusive: bool = False
    predicates: List[CsirtAmericasTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
