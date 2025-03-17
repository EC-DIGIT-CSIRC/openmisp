"""Taxonomy model for ioc."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class IocTaxonomyPredicate(str, Enum):
    ARTIFACT_STATE = "artifact-state"


class IocTaxonomyArtifactStateEntry(str, Enum):
    MALICIOUS = "malicious"
    NOT_MALICIOUS = "not-malicious"


class IocTaxonomy(BaseModel):
    """Model for the ioc taxonomy."""

    namespace: str = "ioc"
    description: str = """An IOC classification to facilitate automation of malicious and non malicious artifacts"""
    version: int = 2
    exclusive: bool = False
    predicates: List[IocTaxonomyPredicate] = []
    artifact_state_entries: List[IocTaxonomyArtifactStateEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
