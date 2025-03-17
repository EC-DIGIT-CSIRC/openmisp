"""Taxonomy model for sentinel-threattype."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class SentinelThreattypeTaxonomyPredicate(str, Enum):
    BOTNET = "Botnet"
    C2 = "C2"
    CRYPTO_MINING = "CryptoMining"
    DARKNET = "Darknet"
    DDO_S = "DDoS"
    MALICIOUS_URL = "MaliciousUrl"
    MALWARE = "Malware"
    PHISHING = "Phishing"
    PROXY = "Proxy"
    PUA = "PUA"
    WATCH_LIST = "WatchList"


class SentinelThreattypeTaxonomy(BaseModel):
    """Model for the sentinel-threattype taxonomy."""

    namespace: str = "sentinel-threattype"
    description: str = """Sentinel indicator threat types."""
    version: int = 1
    exclusive: bool = True
    predicates: List[SentinelThreattypeTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
