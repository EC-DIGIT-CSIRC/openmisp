"""Taxonomy model for eu-marketop-and-publicadmin."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EuMarketopAndPublicadminTaxonomyPredicate(str, Enum):
    CRITICAL_INFRA_OPERATORS = "critical-infra-operators"
    INFO_SERVICES = "info-services"
    PUBLIC_ADMIN = "public-admin"


class EuMarketopAndPublicadminTaxonomyCriticalInfraOperatorsEntry(str, Enum):
    TRANSPORT = "transport"
    ENERGY = "energy"
    HEALTH = "health"
    FINANCIAL = "financial"
    BANKING = "banking"


class EuMarketopAndPublicadminTaxonomyInfoServicesEntry(str, Enum):
    E_COMMERCE = "e-commerce"
    INTERNET_PAYMENT = "internet-payment"
    CLOUD = "cloud"
    SEARCH_ENGINES = "search-engines"
    SOCNET = "socnet"
    APP_STORES = "app-stores"


class EuMarketopAndPublicadminTaxonomyPublicAdminEntry(str, Enum):
    PUBLIC_ADMIN = "public-admin"


class EuMarketopAndPublicadminTaxonomy(BaseModel):
    """Model for the eu-marketop-and-publicadmin taxonomy."""

    namespace: str = "eu-marketop-and-publicadmin"
    description: str = """Market operators and public administrations that must comply to some notifications requirements under EU NIS directive"""
    version: int = 1
    exclusive: bool = False
    predicates: List[EuMarketopAndPublicadminTaxonomyPredicate] = []
    critical_infra_operators_entries: List[EuMarketopAndPublicadminTaxonomyCriticalInfraOperatorsEntry] = []
    info_services_entries: List[EuMarketopAndPublicadminTaxonomyInfoServicesEntry] = []
    public_admin_entries: List[EuMarketopAndPublicadminTaxonomyPublicAdminEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
