"""Taxonomy model for organizational cyber- arm."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class OrganizationalCyberHarmTaxonomyPredicate(str, Enum):
    PHYSICAL_DIGITAL = "physical-digital"
    ECONOMIC = "economic"
    PSYCHOLOGICAL = "psychological"
    REPUTATIONAL = "reputational"
    SOCIAL_SOCIETAL = "social-societal"


class OrganizationalCyberHarmTaxonomyPhysicalDigitalEntry(str, Enum):
    DAMAGED_OR_UNAVAILABLE = "damaged-or-unavailable"
    DESTROYED = "destroyed"
    THEFT = "theft"
    COMPROMISED = "compromised"
    INFECTED = "infected"
    EXPOSED_LEAKED = "exposed-leaked"
    CORRUPTED = "corrupted"
    REDUCED_PERFORMANCE = "reduced-performance"
    BODILY_INJURY = "bodily-injury"
    PAIN = "pain"
    LOSS_OF_LIFE = "loss-of-life"
    PROSECUTION = "prosecution"
    ABUSE = "abuse"
    MISTREATMENT = "mistreatment"
    IDENTITY_THEFT = "identity-theft"


class OrganizationalCyberHarmTaxonomyEconomicEntry(str, Enum):
    DISRUPTED_OPERATIONS = "disrupted-operations"
    DISRUPTED_SALES = "disrupted-sales"
    REDUCED_CUSTOMERS = "reduced-customers"
    REDUCED_PROFITS = "reduced-profits"
    REDUCED_GROWTH = "reduced-growth"
    REDUCED_INVESTMENTS = "reduced-investments"
    FALL_IN_STOCK_PRICE = "fall-in-stock-price"
    THEFT_OF_FINANCES = "theft-of-finances"
    LOSS_OF_FINANCES = "loss-of-finances"
    REGULATORY_FINES = "regulatory-fines"
    INVESTIGATION_COSTS = "investigation-costs"
    PR_RESPONSE_COSTS = "pr-response-costs"
    COMPENSATION_PAYMENTS = "compensation-payments"
    EXTORTION_PAYMENTS = "extortion-payments"
    LOSS_OF_JOBS = "loss-of-jobs"
    SCAMMED = "scammed"


class OrganizationalCyberHarmTaxonomyPsychologicalEntry(str, Enum):
    CONFUSION = "confusion"
    DISCOMFORT = "discomfort"
    FRUSTRATION = "frustration"
    WORRY_ANXIETY = "worry-anxiety"
    FEELING_UPSET = "feeling-upset"
    DEPRESSED = "depressed"
    EMBARRASSED = "embarrassed"
    SHAMEFUL = "shameful"
    GUILTY = "guilty"
    LOSS_OF_SELF_CONFIDENCE = "loss-of-self-confidence"
    LOW_SATISFACTION = "low-satisfaction"
    NEGATIVE_CHANGES_IN_PERCEPTION = "negative-changes-in-perception"


class OrganizationalCyberHarmTaxonomyReputationalEntry(str, Enum):
    DAMAGED_PUBLIC_PERCEPTION = "damaged-public-perception"
    REDUCED_CORPORATE_GOODWILL = "reduced-corporate-goodwill"
    DAMAGED_CUSTOMER_RELATIONSHIPS = "damaged-customer-relationships"
    DAMAGED_SUPPLIER_RELATIONSHIPS = "damaged-supplier-relationships"
    REDUCED_BUSINESS_OPPORTUNITIES = "reduced-business-opportunities"
    INABILITY_TO_RECRUIT = "inability-to-recruit"
    MEDIA_SCRUTINY = "media-scrutiny"
    LOSS_OF_KEY_STAFF = "loss-of-key-staff"
    LOSS_OF_ACCREDITATIONS = "loss-of-accreditations"
    REDUCED_CREDIT_SCORES = "reduced-credit-scores"


class OrganizationalCyberHarmTaxonomySocialSocietalEntry(str, Enum):
    NEGATIVE_CHANGES_IN_PUBLIC_PERCEPTION = "negative-changes-in-public-perception"
    DISRUPTION_IN_DAILY_ACTIVITIES = "disruption-in-daily-activities"
    NEGATIVE_IMPACT_ON_NETWORK = "negative-impact-on-network"
    DROP_IN_INTERNAL_MORALE = "drop-in-internal-morale"


class OrganizationalCyberHarmTaxonomy(BaseModel):
    """Model for the organizational cyber- arm taxonomy."""

    namespace: str = "organizational-cyber-harm"
    description: str = """A taxonomy to classify organizational cyber harms based on categories like physical, economic, psychological, reputational, and social/societal impacts."""
    version: int = 1
    exclusive: bool = False
    predicates: List[OrganizationalCyberHarmTaxonomyPredicate] = []
    physical_digital_entries: List[OrganizationalCyberHarmTaxonomyPhysicalDigitalEntry] = []
    economic_entries: List[OrganizationalCyberHarmTaxonomyEconomicEntry] = []
    psychological_entries: List[OrganizationalCyberHarmTaxonomyPsychologicalEntry] = []
    reputational_entries: List[OrganizationalCyberHarmTaxonomyReputationalEntry] = []
    social_societal_entries: List[OrganizationalCyberHarmTaxonomySocialSocietalEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
