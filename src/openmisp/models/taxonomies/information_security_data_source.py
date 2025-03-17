"""Taxonomy model for information-security-data-source."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InformationSecurityDataSourceTaxonomyPredicate(str, Enum):
    TYPE_OF_INFORMATION = "type-of-information"
    ORIGINALITY = "originality"
    TIMELINESS_SHARING_BEHAVIOR = "timeliness-sharing-behavior"
    INTEGRABILITY_FORMAT = "integrability-format"
    INTEGRABILITY_INTERFACE = "integrability-interface"
    TRUSTWORTHINESS_CREDITABILILY = "trustworthiness-creditabilily"
    TRUSTWORTHINESS_TRACEABILITY = "trustworthiness-traceability"
    TRUSTWORTHINESS_FEEDBACK_MECHANISM = "trustworthiness-feedback-mechanism"
    TYPE_OF_SOURCE = "type-of-source"


class InformationSecurityDataSourceTaxonomyTypeOfInformationEntry(str, Enum):
    VULNERABILITY = "vulnerability"
    THREAT = "threat"
    COUNTERMEASURE = "countermeasure"
    ATTACK = "attack"
    RISK = "risk"
    ASSET = "asset"


class InformationSecurityDataSourceTaxonomyOriginalityEntry(str, Enum):
    ORIGINAL_SOURCE = "original-source"
    SECONDARY_SOURCE = "secondary-source"


class InformationSecurityDataSourceTaxonomyTimelinessSharingBehaviorEntry(str, Enum):
    ROUTINE_SHARING = "routine-sharing"
    INCIDENT_SPECIFIC = "incident-specific"


class InformationSecurityDataSourceTaxonomyIntegrabilityFormatEntry(str, Enum):
    STRUCTURED = "structured"
    UNSTRUCTURED = "unstructured"


class InformationSecurityDataSourceTaxonomyIntegrabilityInterfaceEntry(str, Enum):
    NO_INTERFACE = "no-interface"
    API = "api"
    RSS_FEEDS = "rss-feeds"
    EXPORT = "export"


class InformationSecurityDataSourceTaxonomyTrustworthinessCreditabililyEntry(str, Enum):
    VENDOR = "vendor"
    GOVERNMENT = "government"
    SECURITY_EXPERT = "security-expert"
    NORMAL_USER = "normal-user"


class InformationSecurityDataSourceTaxonomyTrustworthinessTraceabilityEntry(str, Enum):
    YES = "yes"
    NO = "no"


class InformationSecurityDataSourceTaxonomyTrustworthinessFeedbackMechanismEntry(str, Enum):
    YES = "yes"
    NO = "no"


class InformationSecurityDataSourceTaxonomyTypeOfSourceEntry(str, Enum):
    NEWS_WEBSITE = "news-website"
    EXPERT_BLOG = "expert-blog"
    SECURITY_PRODUCT_VENDOR_WEBSITE = "security-product-vendor-website"
    VULNERABILITY_DATABASE = "vulnerability-database"
    MAILING_LIST_ARCHIVE = "mailing-list-archive"
    SOCIAL_NETWORK = "social-network"
    STREAMING_PORTAL = "streaming-portal"
    FORUM = "forum"
    OTHER = "other"


class InformationSecurityDataSourceTaxonomy(BaseModel):
    """Model for the information-security-data-source taxonomy."""

    namespace: str = "information-security-data-source"
    description: str = """Taxonomy to classify the information security data sources."""
    version: int = 1
    exclusive: bool = False
    predicates: List[InformationSecurityDataSourceTaxonomyPredicate] = []
    type_of_information_entries: List[InformationSecurityDataSourceTaxonomyTypeOfInformationEntry] = []
    originality_entries: List[InformationSecurityDataSourceTaxonomyOriginalityEntry] = []
    timeliness_sharing_behavior_entries: List[InformationSecurityDataSourceTaxonomyTimelinessSharingBehaviorEntry] = []
    integrability_format_entries: List[InformationSecurityDataSourceTaxonomyIntegrabilityFormatEntry] = []
    integrability_interface_entries: List[InformationSecurityDataSourceTaxonomyIntegrabilityInterfaceEntry] = []
    trustworthiness_creditabilily_entries: List[
        InformationSecurityDataSourceTaxonomyTrustworthinessCreditabililyEntry
    ] = []
    trustworthiness_traceability_entries: List[
        InformationSecurityDataSourceTaxonomyTrustworthinessTraceabilityEntry
    ] = []
    trustworthiness_feedback_mechanism_entries: List[
        InformationSecurityDataSourceTaxonomyTrustworthinessFeedbackMechanismEntry
    ] = []
    type_of_source_entries: List[InformationSecurityDataSourceTaxonomyTypeOfSourceEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
