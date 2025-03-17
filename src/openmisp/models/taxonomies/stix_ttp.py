"""Taxonomy model for STIX TTP."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class StixTtpTaxonomyPredicate(str, Enum):
    VICTIM_TARGETING = "victim-targeting"


class StixTtpTaxonomyVictimTargetingEntry(str, Enum):
    BUSINESS_PROFESSIONAL_SECTOR = "business-professional-sector"
    RETAIL_SECTOR = "retail-sector"
    FINANCIAL_SECTOR = "financial-sector"
    MEDIA_ENTERTAINMENT_SECTOR = "media-entertainment-sector"
    CONSTRUCTION_ENGINEERING_SECTOR = "construction-engineering-sector"
    GOVERNMENT_INTERNATIONAL_ORGANIZATIONS_SECTOR = "government-international-organizations-sector"
    LEGAL_SECTOR = "legal-sector"
    HIGHTECH_IT_SECTOR = "hightech-it-sector"
    HEALTHCARE_SECTOR = "healthcare-sector"
    TRANSPORTATION_SECTOR = "transportation-sector"
    AEROSPACE_DEFENCE_SECTOR = "aerospace-defence-sector"
    ENERGY_SECTOR = "energy-sector"
    FOOD_SECTOR = "food-sector"
    NATURAL_RESOURCES_SECTOR = "natural-resources-sector"
    OTHER_SECTOR = "other-sector"
    CORPORATE_EMPLOYEE_INFORMATION = "corporate-employee-information"
    CUSTOMER_PII = "customer-pii"
    EMAIL_LISTS_ARCHIVES = "email-lists-archives"
    FINANCIAL_DATA = "financial-data"
    INTELLECTUAL_PROPERTY = "intellectual-property"
    MOBILE_PHONE_CONTACTS = "mobile-phone-contacts"
    USER_CREDENTIALS = "user-credentials"
    AUTHENTIFICATION_COOKIES = "authentification-cookies"


class StixTtpTaxonomy(BaseModel):
    """Model for the STIX TTP taxonomy."""

    namespace: str = "stix-ttp"
    description: str = """TTPs are representations of the behavior or modus operandi of cyber adversaries."""
    version: int = 1
    exclusive: bool = False
    predicates: List[StixTtpTaxonomyPredicate] = []
    victim_targeting_entries: List[StixTtpTaxonomyVictimTargetingEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
