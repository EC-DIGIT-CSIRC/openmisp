"""Taxonomy model for  Universal Cybersecurity Resource Catalogue."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CycatTaxonomyPredicate(str, Enum):
    TYPE = "type"
    SCOPE = "scope"


class CycatTaxonomyTypeEntry(str, Enum):
    TOOL = "tool"
    PLAYBOOK = "playbook"
    TAXONOMY = "taxonomy"
    RULE = "rule"
    NOTEBOOK = "notebook"
    VULNERABILITY = "vulnerability"
    PROOF_OF_CONCEPT = "proof-of-concept"
    FINGERPRINT = "fingerprint"
    MITIGATION = "mitigation"
    DATASET = "dataset"


class CycatTaxonomyScopeEntry(str, Enum):
    IDENTIFY = "identify"
    PROTECT = "protect"
    DETECT = "detect"
    RESPOND = "respond"
    RECOVER = "recover"
    EXPLOIT = "exploit"
    INVESTIGATE = "investigate"
    TRAIN = "train"
    TEST = "test"


class CycatTaxonomy(BaseModel):
    """Model for the  Universal Cybersecurity Resource Catalogue taxonomy."""

    namespace: str = "cycat"
    description: str = """Taxonomy used by CyCAT, the Universal Cybersecurity Resource Catalogue, to categorize the namespaces it supports and uses."""
    version: int = 1
    exclusive: bool = False
    predicates: List[CycatTaxonomyPredicate] = []
    type_entries: List[CycatTaxonomyTypeEntry] = []
    scope_entries: List[CycatTaxonomyScopeEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
