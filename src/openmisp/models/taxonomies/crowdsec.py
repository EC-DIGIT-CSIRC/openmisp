"""Taxonomy model for crowdsec."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CrowdsecTaxonomyPredicate(str, Enum):
    BEHAVIOR = "behavior"
    FALSE_POSITIVE = "false-positive"
    CLASSIFICATION = "classification"


class CrowdsecTaxonomyBehaviorEntry(str, Enum):
    DATABASE_BRUTEFORCE = "database-bruteforce"
    FTP_BRUTEFORCE = "ftp-bruteforce"
    GENERIC_EXPLOIT = "generic-exploit"
    HTTP_BRUTEFORCE = "http-bruteforce"
    HTTP_CRAWL = "http-crawl"
    HTTP_EXPLOIT = "http-exploit"
    HTTP_SCAN = "http-scan"
    HTTP_SPAM = "http-spam"
    IOT_BRUTEFORCE = "iot-bruteforce"
    LDAP_BRUTEFORCE = "ldap-bruteforce"
    POP3_IMAP_BRUTEFORCE = "pop3/imap-bruteforce"
    SIP_BRUTEFORCE = "sip-bruteforce"
    SMB_BRUTEFORCE = "smb-bruteforce"
    SMTP_SPAM = "smtp-spam"
    SSH_BRUTEFORCE = "ssh-bruteforce"
    TCP_SCAN = "tcp-scan"
    TELNET_BRUTEFORCE = "telnet-bruteforce"
    VM_MANAGEMENT_BRUTEFORCE = "vm-management-bruteforce"
    WINDOWS_BRUTEFORCE = "windows-bruteforce"


class CrowdsecTaxonomyFalsePositiveEntry(str, Enum):
    CDN_CLOUDFLARE_EXIT_NODE = "cdn-cloudflare_exit_node"
    CDN_EXIT_NODE = "cdn-exit_node"
    IP_PRIVATE_RANGE = "ip-private_range"
    MSP_SCANNER = "msp-scanner"
    SEO_CRAWLER = "seo-crawler"
    SEO_DUCKDUCKBOT = "seo-duckduckbot"
    SEO_PINTEREST = "seo-pinterest"


class CrowdsecTaxonomyClassificationEntry(str, Enum):
    COMMUNITY_BLOCKLIST = "community-blocklist"
    PROFILE_INSECURE_SERVICES = "profile-insecure_services"
    PROFILE_MANY_SERVICES = "profile-many_services"
    PROXY_TOR = "proxy-tor"
    PROXY_VPN = "proxy-vpn"
    RANGE_DATA_CENTER = "range-data_center"
    SCANNER_ALPHASTRIKE = "scanner-alphastrike"
    SCANNER_BINARYEDGE = "scanner-binaryedge"
    SCANNER_CENSYS = "scanner-censys"
    SCANNER_CERT_SSI_GOUV_FR = "scanner-cert.ssi.gouv.fr"
    SCANNER_CISA_DHS_GOV = "scanner-cisa.dhs.gov"
    SCANNER_INTERNET_CENSUS = "scanner-internet-census"
    SCANNER_LEAKIX = "scanner-leakix"
    SCANNER_LEGIT = "scanner-legit"
    SCANNER_SHADOWSERVER_ORG = "scanner-shadowserver.org"
    SCANNER_SHODAN = "scanner-shodan"
    SCANNER_STRETCHOID = "scanner-stretchoid"
    PROFILE_FAKE_RDNS = "profile-fake_rdns"
    PROFILE_NXDOMAIN = "profile-nxdomain"
    PROFILE_ROUTER = "profile-router"
    PROFILE_PROXY = "profile-proxy"
    PROFILE_JUPITER_VPN = "profile-jupiter-vpn"
    DEVICE_CYBEROAM = "device-cyberoam"
    DEVICE_MICROTIK = "device-microtik"
    DEVICE_ASUSWRT = "device-asuswrt"
    DEVICE_HIKVISION = "device-hikvision"
    DEVICE_IPCAM = "device-ipcam"
    PROFILE_LIKELY_BOTNET = "profile-likely_botnet"


class CrowdsecTaxonomy(BaseModel):
    """Model for the crowdsec taxonomy."""

    namespace: str = "crowdsec"
    description: str = """Crowdsec IP address classifications and behaviors taxonomy."""
    version: int = 1
    exclusive: bool = False
    predicates: List[CrowdsecTaxonomyPredicate] = []
    behavior_entries: List[CrowdsecTaxonomyBehaviorEntry] = []
    false_positive_entries: List[CrowdsecTaxonomyFalsePositiveEntry] = []
    classification_entries: List[CrowdsecTaxonomyClassificationEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
