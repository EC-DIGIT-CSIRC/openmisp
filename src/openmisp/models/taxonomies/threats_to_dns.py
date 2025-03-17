"""Taxonomy model for Threats to DNS."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ThreatsToDnsTaxonomyPredicate(str, Enum):
    DNS_PROTOCOL_ATTACKS = "dns-protocol-attacks"
    DNS_SERVER_ATTACKS = "dns-server-attacks"
    DNS_ABUSE_OR_MISUSE = "dns-abuse-or-misuse"


class ThreatsToDnsTaxonomyDnsProtocolAttacksEntry(str, Enum):
    MAN_IN_THE_MIDDLE_ATTACK = "man-in-the-middle-attack"
    DNS_SPOOFING = "dns-spoofing"
    DNS_REBINDING = "dns-rebinding"


class ThreatsToDnsTaxonomyDnsServerAttacksEntry(str, Enum):
    SERVER_DOS_AND_DDOS = "server-dos-and-ddos"
    SERVER_HIJACKING = "server-hijacking"
    CACHE_POISONING = "cache-poisoning"


class ThreatsToDnsTaxonomyDnsAbuseOrMisuseEntry(str, Enum):
    DOMAIN_NAME_REGISTRATION_ABUSE_CYBERSQUATTING = "domain-name-registration-abuse-cybersquatting"
    DOMAIN_NAME_REGISTRATION_ABUSE_TYPOSQUATTING = "domain-name-registration-abuse-typosquatting"
    DOMAIN_NAME_REGISTRATION_ABUSE_DOMAIN_REPUTATION_AND_RE_REGISTRATION = (
        "domain-name-registration-abuse-domain-reputation-and-re-registration"
    )
    DNS_REFLECTION_DNS_AMPLIFICATION = "dns-reflection-dns-amplification"
    MALICIOUS_OR_COMPROMISED_DOMAINS_IPS_MALICIOUS_BOTNETS_C2 = (
        "malicious-or-compromised-domains-ips-malicious-botnets-c2"
    )
    MALICIOUS_OR_COMPROMISED_DOMAINS_IPS_FAST_FLUX_DOMAINS = "malicious-or-compromised-domains-ips-fast-flux-domains"
    MALICIOUS_OR_COMPROMISED_DOMAINS_IPS_MALICIOUS_DGAS = "malicious-or-compromised-domains-ips-malicious-dgas"
    COVERT_CHANNELS_MALICIOUS_DNS_TUNNELING = "covert-channels-malicious-dns-tunneling"
    COVERT_CHANNELS_MALICIOUS_PAYLOAD_DISTRIBUTION = "covert-channels-malicious-payload-distribution"
    BENIGN_SERVICES_APPLICATIONS_MALICIOUS_DNS_RESOLVERS = "benign-services-applications-malicious-dns-resolvers"
    BENIGN_SERVICES_APPLICATIONS_MALICIOUS_SCANNERS = "benign-services-applications-malicious-scanners"
    BENIGN_SERVICES_APPLICATIONS_URL_SHORTENERS = "benign-services-applications-url-shorteners"


class ThreatsToDnsTaxonomy(BaseModel):
    """Model for the Threats to DNS taxonomy."""

    namespace: str = "threats-to-dns"
    description: str = """An overview of some of the known attacks related to DNS as described by Torabi, S., Boukhtouta, A., Assi, C., & Debbabi, M. (2018) in Detecting Internet Abuse by Analyzing Passive DNS Traffic: A Survey of Implemented Systems. IEEE Communications Surveys & Tutorials, 1–1. doi:10.1109/comst.2018.2849614"""
    version: int = 1
    exclusive: bool = False
    predicates: List[ThreatsToDnsTaxonomyPredicate] = []
    dns_protocol_attacks_entries: List[ThreatsToDnsTaxonomyDnsProtocolAttacksEntry] = []
    dns_server_attacks_entries: List[ThreatsToDnsTaxonomyDnsServerAttacksEntry] = []
    dns_abuse_or_misuse_entries: List[ThreatsToDnsTaxonomyDnsAbuseOrMisuseEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
