"""Taxonomy model for action-taken."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ActionTakenTaxonomyPredicate(str, Enum):
    INFORMED_ISP_HOSTING_SERVICE_PROVIDER = "informed ISP/Hosting Service Provider"
    INFORMED_REGISTRAR = "informed Registrar"
    INFORMED_REGISTRANT = "informed Registrant"
    INFORMED_ABUSE_CONTACT__DOMAIN_ = "informed abuse-contact (domain)"
    INFORMED_ABUSE_CONTACT__IP_ = "informed abuse-contact (IP)"
    INFORMED_LEGAL_DEPARTMENT = "informed legal department"


class ActionTakenTaxonomy(BaseModel):
    """Model for the action-taken taxonomy."""

    namespace: str = "action-taken"
    description: str = """Action taken in the case of a security incident (CSIRT perspective)."""
    version: int = 2
    exclusive: bool = False
    predicates: List[ActionTakenTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
