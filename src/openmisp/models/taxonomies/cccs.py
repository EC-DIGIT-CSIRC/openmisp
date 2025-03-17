"""Taxonomy model for CCCS."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CccsTaxonomyPredicate(str, Enum):
    EVENT = "event"
    DISCLOSURE_TYPE = "disclosure-type"
    DOMAIN_CATEGORY = "domain-category"
    EMAIL_TYPE = "email-type"
    EXPLOITATION_TECHNIQUE = "exploitation-technique"
    IP_CATEGORY = "ip-category"
    MALICIOUSNESS = "maliciousness"
    MALWARE_CATEGORY = "malware-category"
    MISUSAGE_TYPE = "misusage-type"
    MITIGATION_TYPE = "mitigation-type"
    ORIGIN = "origin"
    ORIGINATING_ORGANIZATION = "originating-organization"
    SCAN_TYPE = "scan-type"
    SEVERITY = "severity"
    THREAT_VECTOR = "threat-vector"


class CccsTaxonomyEventEntry(str, Enum):
    BEACON = "beacon"
    BROWSER_BASED_EXPLOITATION = "browser-based-exploitation"
    DOS = "dos"
    EMAIL = "email"
    EXFILTRATION = "exfiltration"
    GENERIC_EVENT = "generic-event"
    IMPROPER_USAGE = "improper-usage"
    MALWARE_ARTIFACTS = "malware-artifacts"
    MALWARE_DOWNLOAD = "malware-download"
    PHISHING = "phishing"
    REMOTE_ACCESS = "remote-access"
    REMOTE_EXPLOITATION = "remote-exploitation"
    SCAN = "scan"
    SCRAPING = "scraping"
    TRAFFIC_INTERCEPTION = "traffic-interception"


class CccsTaxonomyDisclosureTypeEntry(str, Enum):
    GOC_CREDENTIAL_DISCLOSURE = "goc-credential-disclosure"
    PERSONAL_CREDENTIAL_DISCLOSURE = "personal-credential-disclosure"
    PERSONAL_INFORMATION_DISCLOSURE = "personal-information-disclosure"
    NONE = "none"
    OTHER = "other"


class CccsTaxonomyDomainCategoryEntry(str, Enum):
    C2 = "c2"
    PROXY = "proxy"
    SEEDED = "seeded"
    WATERINGHOLE = "wateringhole"
    CLOUD_INFRASTRUCTURE = "cloud-infrastructure"
    NAME_SERVER = "name-server"
    SINKHOLED = "sinkholed"


class CccsTaxonomyEmailTypeEntry(str, Enum):
    SPAM = "spam"
    CONTENT__DELIVERY__ATTACK = r"content\-delivery\-attack"
    PHISHING = "phishing"
    BAITING = "baiting"
    UNKNOWN = "unknown"


class CccsTaxonomyExploitationTechniqueEntry(str, Enum):
    SQL_INJECTION = "sql-injection"
    DIRECTORY_TRAVERSAL = "directory-traversal"
    REMOTE_FILE_INCLUSION = "remote-file-inclusion"
    CODE_INJECTION = "code-injection"
    OTHER = "other"


class CccsTaxonomyIpCategoryEntry(str, Enum):
    C2 = "c2"
    PROXY = "proxy"
    SEEDED = "seeded"
    WATERINGHOLE = "wateringhole"
    CLOUD_INFRASTRUCTURE = "cloud-infrastructure"
    NETWORK_GATEWAY = "network-gateway"
    SERVER = "server"
    DNS_SERVER = "dns-server"
    SMTP_SERVER = "smtp-server"
    WEB_SERVER = "web-server"
    FILE_SERVER = "file-server"
    DATABASE_SERVER = "database-server"
    SECURITY_APPLIANCE = "security-appliance"
    TOR_NODE = "tor-node"
    SINKHOLE = "sinkhole"
    ROUTER = "router"


class CccsTaxonomyMaliciousnessEntry(str, Enum):
    NON_MALICIOUS = "non-malicious"
    SUSPICIOUS = "suspicious"
    MALICIOUS = "malicious"


class CccsTaxonomyMalwareCategoryEntry(str, Enum):
    EXPLOIT_KIT = "exploit-kit"
    FIRST_STAGE = "first-stage"
    SECOND_STAGE = "second-stage"
    SCANNER = "scanner"
    DOWNLOADER = "downloader"
    PROXY = "proxy"
    REVERSE_PROXY = "reverse-proxy"
    WEBSHELL = "webshell"
    RANSOMWARE = "ransomware"
    ADWARE = "adware"
    SPYWARE = "spyware"
    VIRUS = "virus"
    WORM = "worm"
    TROJAN = "trojan"
    ROOTKIT = "rootkit"
    KEYLOGGER = "keylogger"
    BROWSER_HIJACKER = "browser-hijacker"


class CccsTaxonomyMisusageTypeEntry(str, Enum):
    UNAUTHORIZED_USAGE = "unauthorized-usage"
    MISCONFIGURATION = "misconfiguration"
    LACK_OF_ENCRYPTION = "lack-of-encryption"
    VULNERABLE_SOFTWARE = "vulnerable-software"
    PRIVILEGE_ESCALATION = "privilege-escalation"
    OTHER = "other"


class CccsTaxonomyMitigationTypeEntry(str, Enum):
    ANTI_VIRUS = "anti-virus"
    CONTENT_FILTERING_SYSTEM = "content-filtering-system"
    DYNAMIC_DEFENSE = "dynamic-defense"
    INSUFFICIENT_PRIVILEGES = "insufficient-privileges"
    IDS = "ids"
    SINK_HOLE___TAKE_DOWN_BY_THIRD_PARTY = "sink-hole-/-take-down-by-third-party"
    ISP = "isp"
    INVALID_CREDENTIALS = "invalid-credentials"
    NOT_VULNERABLE = "not-vulnerable"
    OTHER = "other"
    UNKNOWN = "unknown"
    USER = "user"


class CccsTaxonomyOriginEntry(str, Enum):
    SUBSCRIBER = "subscriber"
    INTERNET = "internet"


class CccsTaxonomyOriginatingOrganizationEntry(str, Enum):
    CSE = "cse"
    NSA = "nsa"
    GCHQ = "gchq"
    ASD = "asd"
    GCSB = "gcsb"
    OPEN_SOURCE = "open-source"
    T_3RD_PARTY = "3rd-party"
    OTHER = "other"


class CccsTaxonomyScanTypeEntry(str, Enum):
    OPEN_PORT = "open-port"
    ICMP = "icmp"
    OS_FINGERPRINTING = "os-fingerprinting"
    WEB = "web"
    OTHER = "other"


class CccsTaxonomySeverityEntry(str, Enum):
    RECONNAISSANCE = "reconnaissance"
    ATTEMPTED_COMPROMISE = "attempted-compromise"
    EXPLOITED = "exploited"


class CccsTaxonomyThreatVectorEntry(str, Enum):
    APPLICATION_CMS = "application:cms"
    APPLICATION_BASH = "application:bash"
    APPLICATION_ACROBAT_READER = "application:acrobat-reader"
    APPLICATION_MS_EXCEL = "application:ms-excel"
    APPLICATION_OTHER = "application:other"
    LANGUAGE_SQL = "language:sql"
    LANGUAGE_PHP = "language:php"
    LANGUAGE_JAVASCRIPT = "language:javascript"
    LANGUAGE_OTHER = "language:other"
    PROTOCOL_DNS = "protocol:dns"
    PROTOCOL_FTP = "protocol:ftp"
    PROTOCOL_HTTP = "protocol:http"
    PROTOCOL_ICMP = "protocol:icmp"
    PROTOCOL_NTP = "protocol:ntp"
    PROTOCOL_RDP = "protocol:rdp"
    PROTOCOL_SMB = "protocol:smb"
    PROTOCOL_SNMP = "protocol:snmp"
    PROTOCOL_SSL = "protocol:ssl"
    PROTOCOL_TELNET = "protocol:telnet"
    PROTOCOL_SIP = "protocol:sip"


class CccsTaxonomy(BaseModel):
    """Model for the CCCS taxonomy."""

    namespace: str = "cccs"
    description: str = """Internal taxonomy for CCCS."""
    version: int = 2
    exclusive: bool = False
    predicates: List[CccsTaxonomyPredicate] = []
    event_entries: List[CccsTaxonomyEventEntry] = []
    disclosure_type_entries: List[CccsTaxonomyDisclosureTypeEntry] = []
    domain_category_entries: List[CccsTaxonomyDomainCategoryEntry] = []
    email_type_entries: List[CccsTaxonomyEmailTypeEntry] = []
    exploitation_technique_entries: List[CccsTaxonomyExploitationTechniqueEntry] = []
    ip_category_entries: List[CccsTaxonomyIpCategoryEntry] = []
    maliciousness_entries: List[CccsTaxonomyMaliciousnessEntry] = []
    malware_category_entries: List[CccsTaxonomyMalwareCategoryEntry] = []
    misusage_type_entries: List[CccsTaxonomyMisusageTypeEntry] = []
    mitigation_type_entries: List[CccsTaxonomyMitigationTypeEntry] = []
    origin_entries: List[CccsTaxonomyOriginEntry] = []
    originating_organization_entries: List[CccsTaxonomyOriginatingOrganizationEntry] = []
    scan_type_entries: List[CccsTaxonomyScanTypeEntry] = []
    severity_entries: List[CccsTaxonomySeverityEntry] = []
    threat_vector_entries: List[CccsTaxonomyThreatVectorEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
