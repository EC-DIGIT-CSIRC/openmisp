"""Taxonomy model for srbcert."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class SrbcertTaxonomyPredicate(str, Enum):
    INCIDENT_TYPE = "incident-type"
    INCIDENT_CRITICALITY_LEVEL = "incident-criticality-level"


class SrbcertTaxonomyIncidentTypeEntry(str, Enum):
    VIRUS = "virus"
    WORM = "worm"
    RANSOMWARE = "ransomware"
    TROJAN = "trojan"
    SPYWARE = "spyware"
    ROOTKIT = "rootkit"
    MALWARE = "malware"
    PORT_SCANNING = "port-scanning"
    SNIFFING = "sniffing"
    SOCIAL_ENGINEERING = "social-engineering"
    DATA_BREACHES = "data-breaches"
    OTHER_TYPE_OF_INFORMATION_GATHERING = "other-type-of-information-gathering"
    PHISHING = "phishing"
    UNAUTHORIZED_USE_OF_RESOURCES = "unauthorized-use-of-resources"
    FRAUD = "fraud"
    EXPLOITING_KNOWN_VULNERABILITIES = "exploiting-known-vulnerabilities"
    BRUTE_FORCE = "brute-force"
    OTHER_TYPE_OF_INTRUSION_ATTEMPTS = "other-type-of-intrusion-attempts"
    PRIVILEGE_ACCOUNT_COMPROMISE = "privilege-account-compromise"
    UNPRIVILEGED_ACCOUNT_COMPROMISE = "unprivileged-account-compromise"
    APPLICATION_COMPROMISE = "application-compromise"
    BOTNET = "botnet"
    OTHER_TYPE_OF_INTRUSIONS = "other-type-of-intrusions"
    DOS = "dos"
    DDOS = "ddos"
    SABOTAGE = "sabotage"
    OUTAGE = "outage"
    OTHER_TYPE_OF_AVAILABILITY_INCIDENT = "other-type-of-availability-incident"
    UNAUTHORIZED_ACCESS_TO_INFORMATION = "unauthorized-access-to-information"
    UNAUTHORIZED_MODIFICATION_OF_INFORMATION = "unauthorized-modification-of-information"
    CRYPTOGRAPHIC_ATTACK = "cryptographic-attack"
    OTHER_TYPE_OF_INFORMATION_CONTENT_SECURITY_INCIDENT = "other-type-of-information-content-security-incident"
    HARDWARE_ERRORS = "hardware-errors"
    SOFTWARE_ERRORS = "software-errors"
    HARDWARE_COMPONENTS_THEFT = "hardware-components-theft"
    OTHER = "other"


class SrbcertTaxonomyIncidentCriticalityLevelEntry(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very-high"


class SrbcertTaxonomy(BaseModel):
    """Model for the srbcert taxonomy."""

    namespace: str = "srbcert"
    description: str = """SRB-CERT Taxonomy - Schemes of Classification in Incident Response and Detection"""
    version: int = 3
    exclusive: bool = False
    predicates: List[SrbcertTaxonomyPredicate] = []
    incident_type_entries: List[SrbcertTaxonomyIncidentTypeEntry] = []
    incident_criticality_level_entries: List[SrbcertTaxonomyIncidentCriticalityLevelEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
