"""Taxonomy model for PassiveTotal."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PassivetotalTaxonomyPredicate(str, Enum):
    SINKHOLED = "sinkholed"
    EVER_COMPROMISED = "ever-compromised"
    DYNAMIC_DNS = "dynamic-dns"
    CLASS = "class"


class PassivetotalTaxonomySinkholedEntry(str, Enum):
    YES = "yes"
    NO = "no"


class PassivetotalTaxonomyEverCompromisedEntry(str, Enum):
    YES = "yes"
    NO = "no"


class PassivetotalTaxonomyDynamicDnsEntry(str, Enum):
    YES = "yes"
    NO = "no"


class PassivetotalTaxonomyClassEntry(str, Enum):
    MALICIOUS = "malicious"
    SUSPICIOUS = "suspicious"
    NON_MALICIOUS = "non-malicious"
    UNKNOWN = "unknown"


class PassivetotalTaxonomy(BaseModel):
    """Model for the PassiveTotal taxonomy."""

    namespace: str = "passivetotal"
    description: str = """Tags from RiskIQ's PassiveTotal service"""
    version: int = 2
    exclusive: bool = False
    predicates: List[PassivetotalTaxonomyPredicate] = []
    sinkholed_entries: List[PassivetotalTaxonomySinkholedEntry] = []
    ever_compromised_entries: List[PassivetotalTaxonomyEverCompromisedEntry] = []
    dynamic_dns_entries: List[PassivetotalTaxonomyDynamicDnsEntry] = []
    class_entries: List[PassivetotalTaxonomyClassEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
