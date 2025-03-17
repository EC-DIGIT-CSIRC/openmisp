"""Taxonomy model for Access method."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class AccessMethodTaxonomyPredicate(str, Enum):
    BRUTE_FORCE = "brute-force"
    PASSWORD_GUESSING = "password-guessing"
    REMOTE_DESKTOP_APPLICATION = "remote-desktop-application"
    STOLEN_CREDENTIALS = "stolen-credentials"
    PASS_THE_HASH = "pass-the-hash"
    DEFAULT_CREDENTIALS = "default-credentials"
    SHELL = "shell"
    OTHER = "other"


class AccessMethodTaxonomy(BaseModel):
    """Model for the Access method taxonomy."""

    namespace: str = "access-method"
    description: str = """The access method used to remotely access a system."""
    version: int = 1
    exclusive: bool = False
    predicates: List[AccessMethodTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
