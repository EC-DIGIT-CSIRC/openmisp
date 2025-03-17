"""Taxonomy model for Unified Ransomware Kill Chain."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class UnifiedRansomwareKillChainTaxonomyPredicate(str, Enum):
    GAIN_ACCESS = "Gain Access"
    ESTABLISH_FOOTHOLD = "Establish Foothold"
    NETWORK_DISCOVERY = "Network Discovery"
    KEY_ASSETS_DISCOVERY = "Key Assets Discovery"
    NETWORK_PROPAGATION = "Network Propagation"
    DATA_EXFILTRATION = "Data Exfiltration"
    DEPLOYMENT_PREPARATION = "Deployment Preparation"
    RANSOMWARE_DEPLOYMENT = "Ransomware Deployment"
    EXTORTION = "Extortion"


class UnifiedRansomwareKillChainTaxonomy(BaseModel):
    """Model for the Unified Ransomware Kill Chain taxonomy."""

    namespace: str = "unified-ransomware-kill-chain"
    description: str = """The Unified Ransomware Kill Chain, a intelligence driven model developed by Oleg Skulkin, aims to track every single phase of a ransomware attack."""
    version: int = 1
    exclusive: bool = False
    predicates: List[UnifiedRansomwareKillChainTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
