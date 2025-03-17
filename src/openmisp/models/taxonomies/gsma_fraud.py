"""Taxonomy model for gsma-fraud."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GsmaFraudTaxonomyPredicate(str, Enum):
    TECHNICAL = "technical"
    SUBSCRIPTION = "subscription"
    DISTRIBUTION = "distribution"
    BUSINESS = "business"
    PREPAID = "prepaid"


class GsmaFraudTaxonomyTechnicalEntry(str, Enum):
    MAILBOX_HACKING = "mailbox-hacking"
    IMEI_REPROGRAMMING = "imei-reprogramming"
    CALL_FORWARDING_FRAUD = "call-forwarding-fraud"
    CALL_CONFERENCE = "call-conference"
    HLR_TAMPERING = "hlr-tampering"
    SIM_CARD_CLONING = "sim-card-cloning"
    FALSE_BASE_STATION_ATTACK = "false-base-station-attack"
    SPAMMING = "spamming"
    PHISHING_PHARMING = "phishing-pharming"
    MOBILE_MALWARE = "mobile-malware"
    FRAUD_RISKS_ASSOCIATED_WITH_VOICE_OVER_IP_SERVICES = "fraud-risks-associated-with-voice-over-ip-services"
    PBX_HACKING = "pbx-hacking"
    FRAUD_RISKS_ASSOCIATED_WITH_M2M_SERVICES = "fraud-risks-associated-with-m2m-services"
    DATA_CHARING_BYPASS = "data-charing-bypass"


class GsmaFraudTaxonomySubscriptionEntry(str, Enum):
    SUBSCRIPTION_FRAUD = "subscription-fraud"
    PROXY_FRAUD = "proxy-fraud"
    ACCOUNT_TAKEOVER = "account-takeover"
    CALL_SELLING = "call-selling"
    DIRECT_DEBIT_FRAUD = "direct-debit-fraud"
    CREDIT_CARD_FRAUD = "credit-card-fraud"
    CREDIT_CARD_NOT_PRESENT_TRANSACTIONS = "credit-card-not-present-transactions"
    CHEQUE_FRAUD = "cheque-fraud"


class GsmaFraudTaxonomyDistributionEntry(str, Enum):
    DEALER_FRAUD = "dealer-fraud"
    FALSE_AGENT = "false-agent"
    THEFT_AND_HANDLING_STOLEN_GOODS = "theft-and-handling-stolen-goods"
    HANDSET_SUBSIDY_LOSS = "handset-subsidy-loss"
    REMOTE_ORDER_FRAUD = "remote-order-fraud"


class GsmaFraudTaxonomyBusinessEntry(str, Enum):
    PREMIUM_RATE = "premium-rate"
    ROAMING_FRAUD = "roaming-fraud"
    INTERNATIONAL_REVENUE_SHARE_FRAUD = "international-revenue-share-fraud"
    INBOUND_ROAMING_FRAUD_RISK_TO_VPMN = "inbound-roaming-fraud-risk-to-vpmn"
    INTERCONNECT_ABUSE = "interconnect-abuse"
    REFILING = "refiling"
    MOBILE_TO_FIXED_NETWORK_GATEWAY_ABUSE = "mobile-to-fixed-network-gateway-abuse"
    FALSE_ANSWER_FALSE_RING = "false-answer-false-ring"
    SOCIAL_ENGINEERING = "social-engineering"
    INTERNAL_FRAUD = "internal-fraud"
    NORMAL_BUSINESS_FRAUD_CRIME = "normal-business-fraud-crime"
    BRAND_NAME_LOGO_ABUSE = "brand-name-logo-abuse"
    M_COMMERCE_PROVIDER_CONTENT_FRAUD = "m-commerce-provider-content-fraud"
    M_COMMERCE_PROVIDER_PRS_FRAUD = "m-commerce-provider-prs-fraud"
    CONTENT_THEFT = "content-theft"
    WANGIRI = "wangiri"
    AIRTIME_RESELLER_FRAUD = "airtime-reseller-fraud"


class GsmaFraudTaxonomyPrepaidEntry(str, Enum):
    SERVICES_FRAUD = "services-fraud"
    HLR_PROFILE_MANIPULATION = "hlr-profile-manipulation"
    MANUAL_RECHARGING = "manual-recharging"
    GENERATION_OF_ABUSIVE_CREDITS = "generation-of-abusive-credits"
    SCARTCH_CARD_ABUSE = "scartch-card-abuse"


class GsmaFraudTaxonomy(BaseModel):
    """Model for the gsma-fraud taxonomy."""

    namespace: str = "gsma-fraud"
    description: str = """Taxonomy used by GSMA for their information sharing program with telco describing the various aspects of fraud"""
    version: int = 1
    exclusive: bool = False
    predicates: List[GsmaFraudTaxonomyPredicate] = []
    technical_entries: List[GsmaFraudTaxonomyTechnicalEntry] = []
    subscription_entries: List[GsmaFraudTaxonomySubscriptionEntry] = []
    distribution_entries: List[GsmaFraudTaxonomyDistributionEntry] = []
    business_entries: List[GsmaFraudTaxonomyBusinessEntry] = []
    prepaid_entries: List[GsmaFraudTaxonomyPrepaidEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
