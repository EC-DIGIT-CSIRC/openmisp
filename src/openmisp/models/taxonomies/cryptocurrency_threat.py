"""Taxonomy model for cryptocurrency-threat."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CryptocurrencyThreatTaxonomyPredicate(str, Enum):
    SIM_SWAPPING = "SIM Swapping"
    CRYPTO_DUSTING = "Crypto Dusting"
    SANCTION_EVASION = "Sanction Evasion"
    NEXT_GENERATION_CRYPTO_MIXERS = "Next-Generation Crypto Mixers"
    SHADOW_MONEY_SERVICE_BUSINESSES = "Shadow Money Service Businesses"
    DATACENTER_SCALE_CRYPTO_JACKING__ = "Datacenter-Scale Crypto Jacking: "
    LIGHTNING_NETWORK_TRANSACTIONS = "Lightning Network Transactions"
    DECENTRALIZED_STABLE_COINS = "Decentralized Stable Coins"
    EMAIL_EXTORTION_AND_BOMB_THREATS = "Email Extortion and Bomb Threats"
    CRYPTO_ROBBING_RANSOMWARE = "Crypto Robbing Ransomware"
    RAG_PULL = "Rag Pull"
    PIG_BUTCHERING_SCAM = "Pig Butchering Scam"


class CryptocurrencyThreatTaxonomy(BaseModel):
    """Model for the cryptocurrency-threat taxonomy."""

    namespace: str = "cryptocurrency-threat"
    description: str = """Threats targeting cryptocurrency, based on CipherTrace report."""
    version: int = 2
    exclusive: bool = False
    predicates: List[CryptocurrencyThreatTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
