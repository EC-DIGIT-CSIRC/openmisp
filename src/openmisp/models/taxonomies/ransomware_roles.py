"""Taxonomy model for Ransomware Actor Roles."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class RansomwareRolesTaxonomyPredicate(str, Enum):
    T_1___INITIAL_ACCESS_BROKER = "1 - Initial Access Broker"
    T_2___RANSOMWARE_AFFILIATE = "2 - Ransomware Affiliate"
    T_3___DATA_MANAGER = "3 - Data Manager"
    T_4___RANSOMWARE_OPERATOR = "4 - Ransomware Operator"
    T_5___NEGOTIATOR = "5 - Negotiator"
    T_6___CHASER = "6 - Chaser"
    T_7___ACCOUNTANT = "7 - Accountant"


class RansomwareRolesTaxonomy(BaseModel):
    """Model for the Ransomware Actor Roles taxonomy."""

    namespace: str = "ransomware-roles"
    description: str = """The seven roles seen in most ransomware incidents."""
    version: int = 1
    exclusive: bool = False
    predicates: List[RansomwareRolesTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
