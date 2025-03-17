"""Taxonomy model for tor."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class TorTaxonomyPredicate(str, Enum):
    TOR_RELAY_TYPE = "tor-relay-type"


class TorTaxonomyTorRelayTypeEntry(str, Enum):
    ENTRY_GUARD_RELAY = "entry-guard-relay"
    MIDDLE_RELAY = "middle-relay"
    EXIT_RELAY = "exit-relay"
    BRIDGE_RELAY = "bridge-relay"


class TorTaxonomy(BaseModel):
    """Model for the tor taxonomy."""

    namespace: str = "tor"
    description: str = """Taxonomy to describe Tor network infrastructure"""
    version: int = 1
    exclusive: bool = False
    predicates: List[TorTaxonomyPredicate] = []
    tor_relay_type_entries: List[TorTaxonomyTorRelayTypeEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
