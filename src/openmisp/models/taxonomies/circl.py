"""Taxonomy model for circl."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CirclTaxonomyPredicate(str, Enum):
    INCIDENT_CLASSIFICATION = "incident-classification"
    TOPIC = "topic"
    SIGNIFICANT = "significant"


class CirclTaxonomyIncidentClassificationEntry(str, Enum):
    SPAM = "spam"
    SYSTEM_COMPROMISE = "system-compromise"
    SABOTAGE = "sabotage"
    PRIVACY_VIOLATION = "privacy-violation"
    SCAN = "scan"
    DENIAL_OF_SERVICE = "denial-of-service"
    COPYRIGHT_ISSUE = "copyright-issue"
    PHISHING = "phishing"
    WHALING = "whaling"
    SMISHING = "smishing"
    MALWARE = "malware"
    XSS = "XSS"
    VULNERABILITY = "vulnerability"
    FASTFLUX = "fastflux"
    DOMAIN_FRONTING = "domain-fronting"
    SQL_INJECTION = "sql-injection"
    INFORMATION_LEAK = "information-leak"
    SCAM = "scam"
    CRYPTOJACKING = "cryptojacking"
    LOCKER = "locker"
    SCREENLOCKER = "screenlocker"
    WIPER = "wiper"
    RANSOMWARE = "ransomware"
    SEXTORTION = "sextortion"
    SOCIAL_ENGINEERING = "social-engineering"
    GDPR_VIOLATION = "gdpr-violation"
    COVID_19 = "covid-19"


class CirclTaxonomyTopicEntry(str, Enum):
    FINANCE = "finance"
    ICT = "ict"
    INDIVIDUAL = "individual"
    INDUSTRY = "industry"
    MEDICAL = "medical"
    SERVICES = "services"
    UNDEFINED = "undefined"


class CirclTaxonomy(BaseModel):
    """Model for the circl taxonomy."""

    namespace: str = "circl"
    description: str = """CIRCL Taxonomy - Schemes of Classification in Incident Response and Detection."""
    version: int = 6
    exclusive: bool = False
    predicates: List[CirclTaxonomyPredicate] = []
    incident_classification_entries: List[CirclTaxonomyIncidentClassificationEntry] = []
    topic_entries: List[CirclTaxonomyTopicEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
