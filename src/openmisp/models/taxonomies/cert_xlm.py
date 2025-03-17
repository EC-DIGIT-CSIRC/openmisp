"""Taxonomy model for CERT-XLM."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CertXlmTaxonomyPredicate(str, Enum):
    ABUSIVE_CONTENT = "abusive-content"
    MALICIOUS_CODE = "malicious-code"
    INFORMATION_GATHERING = "information-gathering"
    INTRUSION_ATTEMPTS = "intrusion-attempts"
    INTRUSION = "intrusion"
    AVAILABILITY = "availability"
    INFORMATION_CONTENT_SECURITY = "information-content-security"
    FRAUD = "fraud"
    VULNERABLE = "vulnerable"
    CONFORMITY = "conformity"
    OTHER = "other"
    TEST = "test"


class CertXlmTaxonomyAbusiveContentEntry(str, Enum):
    SPAM = "spam"
    HARMFUL_SPEECH = "harmful-speech"
    VIOLENCE = "violence"


class CertXlmTaxonomyMaliciousCodeEntry(str, Enum):
    VIRUS = "virus"
    WORM = "worm"
    RANSOMWARE = "ransomware"
    TROJAN_MALWARE = "trojan-malware"
    SPYWARE_RAT = "spyware-rat"
    DIALER = "dialer"
    ROOTKIT = "rootkit"


class CertXlmTaxonomyInformationGatheringEntry(str, Enum):
    SCANNER = "scanner"
    SNIFFING = "sniffing"
    SOCIAL_ENGINEERING = "social-engineering"


class CertXlmTaxonomyIntrusionAttemptsEntry(str, Enum):
    EXPLOIT_KNOWN_VULN = "exploit-known-vuln"
    LOGIN_ATTEMPTS = "login-attempts"
    NEW_ATTACK_SIGNATURE = "new-attack-signature"


class CertXlmTaxonomyIntrusionEntry(str, Enum):
    PRIVILEGED_ACCOUNT_COMPROMISE = "privileged-account-compromise"
    UNPRIVILEGED_ACCOUNT_COMPROMISE = "unprivileged-account-compromise"
    BOTNET_MEMBER = "botnet-member"
    DOMAIN_COMPROMISE = "domain-compromise"
    APPLICATION_COMPROMISE = "application-compromise"


class CertXlmTaxonomyAvailabilityEntry(str, Enum):
    DOS = "dos"
    DDOS = "ddos"
    SABOTAGE = "sabotage"
    OUTAGE = "outage"


class CertXlmTaxonomyInformationContentSecurityEntry(str, Enum):
    UNAUTHORISED_INFORMATION_ACCESS = "Unauthorised-information-access"
    UNAUTHORISED_INFORMATION_MODIFICATION = "Unauthorised-information-modification"


class CertXlmTaxonomyFraudEntry(str, Enum):
    COPYRIGHT = "copyright"
    MASQUERADE = "masquerade"
    PHISHING = "phishing"


class CertXlmTaxonomyVulnerableEntry(str, Enum):
    VULNERABLE_SERVICE = "vulnerable-service"


class CertXlmTaxonomyConformityEntry(str, Enum):
    REGULATOR = "regulator"
    STANDARD = "standard"
    SECURITY_POLICY = "security-policy"
    OTHER_CONFORMITY = "other-conformity"


class CertXlmTaxonomyOtherEntry(str, Enum):
    OTHER = "other"


class CertXlmTaxonomy(BaseModel):
    """Model for the CERT-XLM taxonomy."""

    namespace: str = "CERT-XLM"
    description: str = """CERT-XLM Security Incident Classification."""
    version: int = 2
    exclusive: bool = False
    predicates: List[CertXlmTaxonomyPredicate] = []
    abusive_content_entries: List[CertXlmTaxonomyAbusiveContentEntry] = []
    malicious_code_entries: List[CertXlmTaxonomyMaliciousCodeEntry] = []
    information_gathering_entries: List[CertXlmTaxonomyInformationGatheringEntry] = []
    intrusion_attempts_entries: List[CertXlmTaxonomyIntrusionAttemptsEntry] = []
    intrusion_entries: List[CertXlmTaxonomyIntrusionEntry] = []
    availability_entries: List[CertXlmTaxonomyAvailabilityEntry] = []
    information_content_security_entries: List[CertXlmTaxonomyInformationContentSecurityEntry] = []
    fraud_entries: List[CertXlmTaxonomyFraudEntry] = []
    vulnerable_entries: List[CertXlmTaxonomyVulnerableEntry] = []
    conformity_entries: List[CertXlmTaxonomyConformityEntry] = []
    other_entries: List[CertXlmTaxonomyOtherEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
