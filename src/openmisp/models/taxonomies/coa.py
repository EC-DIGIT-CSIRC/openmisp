"""Taxonomy model for coa."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CoaTaxonomyPredicate(str, Enum):
    DISCOVER = "discover"
    DETECT = "detect"
    DENY = "deny"
    DISRUPT = "disrupt"
    DEGRADE = "degrade"
    DECEIVE = "deceive"
    DESTROY = "destroy"


class CoaTaxonomyDiscoverEntry(str, Enum):
    PROXY = "proxy"
    IDS = "ids"
    FIREWALL = "firewall"
    PCAP = "pcap"
    REMOTE_ACCESS = "remote-access"
    AUTHENTICATION = "authentication"
    HONEYPOT = "honeypot"
    SYSLOG = "syslog"
    WEB = "web"
    DATABASE = "database"
    MAIL = "mail"
    ANTIVIRUS = "antivirus"
    MALWARE_COLLECTION = "malware-collection"
    OTHER = "other"
    UNSPECIFIED = "unspecified"


class CoaTaxonomyDetectEntry(str, Enum):
    PROXY = "proxy"
    NIDS = "nids"
    HIDS = "hids"
    OTHER = "other"
    SYSLOG = "syslog"
    FIREWALL = "firewall"
    EMAIL = "email"
    WEB = "web"
    DATABASE = "database"
    REMOTE_ACCESS = "remote-access"
    MALWARE_COLLECTION = "malware-collection"
    ANTIVIRUS = "antivirus"
    UNSPECIFIED = "unspecified"


class CoaTaxonomyDenyEntry(str, Enum):
    PROXY = "proxy"
    FIREWALL = "firewall"
    WAF = "waf"
    EMAIL = "email"
    CHROOT = "chroot"
    REMOTE_ACCESS = "remote-access"
    OTHER = "other"
    UNSPECIFIED = "unspecified"


class CoaTaxonomyDisruptEntry(str, Enum):
    NIPS = "nips"
    HIPS = "hips"
    OTHER = "other"
    EMAIL = "email"
    MEMORY_PROTECTION = "memory-protection"
    SANDBOXING = "sandboxing"
    ANTIVIRUS = "antivirus"
    UNSPECIFIED = "unspecified"


class CoaTaxonomyDegradeEntry(str, Enum):
    BANDWIDTH = "bandwidth"
    TARPIT = "tarpit"
    OTHER = "other"
    EMAIL = "email"
    UNSPECIFIED = "unspecified"


class CoaTaxonomyDeceiveEntry(str, Enum):
    HONEYPOT = "honeypot"
    DNS = "DNS"
    OTHER = "other"
    EMAIL = "email"
    UNSPECIFIED = "unspecified"


class CoaTaxonomyDestroyEntry(str, Enum):
    ARREST = "arrest"
    SEIZE = "seize"
    PHYSICAL = "physical"
    DOS = "dos"
    HACK_BACK = "hack-back"
    OTHER = "other"
    UNSPECIFIED = "unspecified"


class CoaTaxonomy(BaseModel):
    """Model for the coa taxonomy."""

    namespace: str = "coa"
    description: str = """Course of action taken within organization to discover, detect, deny, disrupt, degrade, deceive and/or destroy an attack."""
    version: int = 2
    exclusive: bool = False
    predicates: List[CoaTaxonomyPredicate] = []
    discover_entries: List[CoaTaxonomyDiscoverEntry] = []
    detect_entries: List[CoaTaxonomyDetectEntry] = []
    deny_entries: List[CoaTaxonomyDenyEntry] = []
    disrupt_entries: List[CoaTaxonomyDisruptEntry] = []
    degrade_entries: List[CoaTaxonomyDegradeEntry] = []
    deceive_entries: List[CoaTaxonomyDeceiveEntry] = []
    destroy_entries: List[CoaTaxonomyDestroyEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
