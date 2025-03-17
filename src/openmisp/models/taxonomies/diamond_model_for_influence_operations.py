"""Taxonomy model for The Diamond Model for Influence Operations Analysis."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DiamondModelForInfluenceOperationsTaxonomyPredicate(str, Enum):
    INFLUENCER = "Influencer"
    CAPABILITIES = "Capabilities"
    INFRASTRUCTURE = "Infrastructure"
    AUDIENCE = "Audience"
    NARRATIVE = "Narrative"


class DiamondModelForInfluenceOperationsTaxonomy(BaseModel):
    """Model for the The Diamond Model for Influence Operations Analysis taxonomy."""

    namespace: str = "diamond-model-for-influence-operations"
    description: str = """The diamond model for influence operations analysis is a framework that leads analysts and researchers toward a comprehensive understanding of a malign influence campaign by addressing the socio-political, technical, and psychological aspects of the campaign. The diamond model for influence operations analysis consists of 5 components: 4 corners and a core element. The 4 corners are divided into 2 axes: influencer and audience on the socio-political axis, capabilities and infrastructure on the technical axis. Narrative makes up the core of the diamond."""
    version: int = 1
    exclusive: bool = False
    predicates: List[DiamondModelForInfluenceOperationsTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
