"""Taxonomy model for Financial."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class FinancialTaxonomyPredicate(str, Enum):
    CATEGORIES_AND_TYPES_OF_SERVICES = "categories-and-types-of-services"
    GEOGRAPHICAL_FOOTPRINT = "geographical-footprint"
    ONLINE_EXPOSITION = "online-exposition"
    PHYSICAL_PRESENCE = "physical-presence"
    SERVICES = "services"


class FinancialTaxonomyCategoriesAndTypesOfServicesEntry(str, Enum):
    BANKING = "banking"
    PRIVATE = "private"
    RETAIL = "retail"
    CUSTODIAN_BANKING = "custodian-banking"
    FINANCIAL_MARKET_INFRASTRUCTURE = "financial-market-infrastructure"
    ASSET_MANAGEMENT = "asset-management"
    IT_PROVIDER = "it-provider"
    E_MONEY_AND_PAYMENT = "e-money-and-payment"
    OTHER = "other"


class FinancialTaxonomyGeographicalFootprintEntry(str, Enum):
    CLIENT_COVERAGE_LOCAL = "client-coverage-local"
    CLIENT_COVERAGE_EU = "client-coverage-eu"
    CLIENT_COVERAGE_WORLDWIDE = "client-coverage-worldwide"
    CORPORATE_STRUCTURE_LOCAL = "corporate-structure-local"
    CORPORATE_STRUCTURE_EU = "corporate-structure-eu"
    CORPORATE_STRUCTURE_WORLDWIDE = "corporate-structure-worldwide"


class FinancialTaxonomyOnlineExpositionEntry(str, Enum):
    LIMITED = "limited"
    EXTENDED = "extended"
    CRUCIAL = "crucial"


class FinancialTaxonomyPhysicalPresenceEntry(str, Enum):
    ATM = "atm"
    POS = "pos"


class FinancialTaxonomyServicesEntry(str, Enum):
    SETTLEMENT = "settlement"
    COLLATERAL_MANAGEMENT = "collateral-management"
    LISTING_OPERATION_OF_TRADING_PLATFORM = "listing-operation-of-trading-platform"
    CREDIT_GRANTING = "credit-granting"
    DEPOSIT_MANAGEMENT = "deposit-management"
    CUSTODIAN_BANKING = "custodian-banking"
    PAYMENT_SERVICES = "payment-services"
    INVESTMENT_SERVICES = "investment-services"


class FinancialTaxonomy(BaseModel):
    """Model for the Financial taxonomy."""

    namespace: str = "financial"
    description: str = """Financial taxonomy to describe financial services, infrastructure and financial scope."""
    version: int = 7
    exclusive: bool = False
    predicates: List[FinancialTaxonomyPredicate] = []
    categories_and_types_of_services_entries: List[FinancialTaxonomyCategoriesAndTypesOfServicesEntry] = []
    geographical_footprint_entries: List[FinancialTaxonomyGeographicalFootprintEntry] = []
    online_exposition_entries: List[FinancialTaxonomyOnlineExpositionEntry] = []
    physical_presence_entries: List[FinancialTaxonomyPhysicalPresenceEntry] = []
    services_entries: List[FinancialTaxonomyServicesEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
