"""Taxonomy model for Europol type of events taxonomy."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EuropolEventTaxonomyPredicate(str, Enum):
    INFECTED_BY_KNOWN_MALWARE = "infected-by-known-malware"
    DISSEMINATION_MALWARE_EMAIL = "dissemination-malware-email"
    HOSTING_MALWARE_WEBPAGE = "hosting-malware-webpage"
    C_C_SERVER_HOSTING = "c&c-server-hosting"
    WORM_SPREADING = "worm-spreading"
    CONNECTION_MALWARE_PORT = "connection-malware-port"
    CONNECTION_MALWARE_SYSTEM = "connection-malware-system"
    FLOOD = "flood"
    EXPLOIT_TOOL_EXHAUSTING_RESOURCES = "exploit-tool-exhausting-resources"
    PACKET_FLOOD = "packet-flood"
    EXPLOIT_FRAMEWORK_EXHAUSTING_RESOURCES = "exploit-framework-exhausting-resources"
    VANDALISM = "vandalism"
    DISRUPTION_DATA_TRANSMISSION = "disruption-data-transmission"
    SYSTEM_PROBE = "system-probe"
    NETWORK_SCANNING = "network-scanning"
    DNS_ZONE_TRANSFER = "dns-zone-transfer"
    WIRETAPPING = "wiretapping"
    DISSEMINATION_PHISHING_EMAILS = "dissemination-phishing-emails"
    HOSTING_PHISHING_SITES = "hosting-phishing-sites"
    AGGREGATION_INFORMATION_PHISHING_SCHEMES = "aggregation-information-phishing-schemes"
    EXPLOIT_ATTEMPT = "exploit-attempt"
    SQL_INJECTION_ATTEMPT = "sql-injection-attempt"
    XSS_ATTEMPT = "xss-attempt"
    FILE_INCLUSION_ATTEMPT = "file-inclusion-attempt"
    BRUTE_FORCE_ATTEMPT = "brute-force-attempt"
    PASSWORD_CRACKING_ATTEMPT = "password-cracking-attempt"
    DICTIONARY_ATTACK_ATTEMPT = "dictionary-attack-attempt"
    EXPLOIT = "exploit"
    SQL_INJECTION = "sql-injection"
    XSS = "xss"
    FILE_INCLUSION = "file-inclusion"
    CONTROL_SYSTEM_BYPASS = "control-system-bypass"
    THEFT_ACCESS_CREDENTIALS = "theft-access-credentials"
    UNAUTHORIZED_ACCESS_SYSTEM = "unauthorized-access-system"
    UNAUTHORIZED_ACCESS_INFORMATION = "unauthorized-access-information"
    DATA_EXFILTRATION = "data-exfiltration"
    MODIFICATION_INFORMATION = "modification-information"
    DELETION_INFORMATION = "deletion-information"
    ILLEGITIMATE_USE_RESOURCES = "illegitimate-use-resources"
    ILLEGITIMATE_USE_NAME = "illegitimate-use-name"
    EMAIL_FLOODING = "email-flooding"
    SPAM = "spam"
    COPYRIGHTED_CONTENT = "copyrighted-content"
    CONTENT_FORBIDDEN_BY_LAW = "content-forbidden-by-law"
    UNSPECIFIED = "unspecified"
    UNDETERMINED = "undetermined"


class EuropolEventTaxonomy(BaseModel):
    """Model for the Europol type of events taxonomy taxonomy."""

    namespace: str = "europol-event"
    description: str = """This taxonomy was designed to describe the type of events"""
    version: int = 1
    exclusive: bool = False
    predicates: List[EuropolEventTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
