"""Taxonomy model for ENISA Threat Taxonomy."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EnisaTaxonomyPredicate(str, Enum):
    PHYSICAL_ATTACK = "physical-attack"
    UNINTENTIONAL_DAMAGE = "unintentional-damage"
    DISASTER = "disaster"
    FAILURES_MALFUNCTION = "failures-malfunction"
    OUTAGES = "outages"
    EAVESDROPPING_INTERCEPTION_HIJACKING = "eavesdropping-interception-hijacking"
    LEGAL = "legal"
    NEFARIOUS_ACTIVITY_ABUSE = "nefarious-activity-abuse"


class EnisaTaxonomyPhysicalAttackEntry(str, Enum):
    FRAUD = "fraud"
    FRAUD_BY_EMPLOYEES = "fraud-by-employees"
    SABOTAGE = "sabotage"
    VANDALISM = "vandalism"
    THEFT = "theft"
    THEFT_OF_MOBILE_DEVICES = "theft-of-mobile-devices"
    THEFT_OF_FIXED_HARDWARE = "theft-of-fixed-hardware"
    THEFT_OF_DOCUMENTS = "theft-of-documents"
    THEFT_OF_BACKUPS = "theft-of-backups"
    INFORMATION_LEAK_OR_UNAUTHORISED_SHARING = "information-leak-or-unauthorised-sharing"
    UNAUTHORISED_PHYSICAL_ACCESS_OR_UNAUTHORISED_ENTRY_TO_PREMISES = (
        "unauthorised-physical-access-or-unauthorised-entry-to-premises"
    )
    COERCION_OR_EXTORTION_OR_CORRUPTION = "coercion-or-extortion-or-corruption"
    DAMAGE_FROM_THE_WAFARE = "damage-from-the-wafare"
    TERRORIST_ATTACK = "terrorist-attack"


class EnisaTaxonomyUnintentionalDamageEntry(str, Enum):
    INFORMATION_LEAK_OR_SHARING_DUE_TO_HUMAN_ERROR = "information-leak-or-sharing-due-to-human-error"
    ACCIDENTAL_LEAKS_OR_SHARING_OF_DATA_BY_EMPLOYEES = "accidental-leaks-or-sharing-of-data-by-employees"
    LEAKS_OF_DATA_VIA_MOBILE_APPLICATIONS = "leaks-of-data-via-mobile-applications"
    LEAKS_OF_DATA_VIA_WEB_APPLICATIONS = "leaks-of-data-via-web-applications"
    LEAKS_OF_INFORMATION_TRANSFERRED_BY_NETWORK = "leaks-of-information-transferred-by-network"
    ERRONEOUS_USE_OR_ADMINISTRATION_OF_DEVICES_AND_SYSTEMS = "erroneous-use-or-administration-of-devices-and-systems"
    LOSS_OF_INFORMATION_DUE_TO_MAINTENANCE_ERRORS_OR_OPERATORS_ERRORS = (
        "loss-of-information-due-to-maintenance-errors-or-operators-errors"
    )
    LOSS_OF_INFORMATION_DUE_TO_CONFIGURATION_OR_INSTALLATION_ERROR = (
        "loss-of-information-due-to-configuration-or-installation error"
    )
    INCREASING_RECOVERY_TIME = "increasing-recovery-time"
    LOST_OF_INFORMATION_DUE_TO_USER_ERRORS = "lost-of-information-due-to-user-errors"
    USING_INFORMATION_FROM_AN_UNRELIABLE_SOURCE = "using-information-from-an-unreliable-source"
    UNINTENTIONAL_CHANGE_OF_DATA_IN_AN_INFORMATION_SYSTEM = "unintentional-change-of-data-in-an-information-system"
    INADEQUATE_DESIGN_AND_PLANNING_OR_IMPROPER_ADAPTATION = "inadequate-design-and-planning-or-improper-adaptation"
    DAMAGE_CAUSED_BY_A_THIRD_PARTY = "damage-caused-by-a-third-party"
    SECURITY_FAILURE_CAUSED_BY_THIRD_PARTY = "security-failure-caused-by-third-party"
    DAMAGES_RESULTING_FROM_PENETRATION_TESTING = "damages-resulting-from-penetration-testing"
    LOSS_OF_INFORMATION_IN_THE_CLOUD = "loss-of-information-in-the-cloud"
    LOSS_OF__INTEGRITY_OF__SENSITIVE_INFORMATION = "loss-of-(integrity-of)-sensitive-information"
    LOSS_OF_INTEGRITY_OF_CERTIFICATES = "loss-of-integrity-of-certificates"
    LOSS_OF_DEVICES_AND_STORAGE_MEDIA_AND_DOCUMENTS = "loss-of-devices-and-storage-media-and-documents"
    LOSS_OF_DEVICES_OR_MOBILE_DEVICES = "loss-of-devices-or-mobile-devices"
    LOSS_OF_STORAGE_MEDIA = "loss-of-storage-media"
    LOSS_OF_DOCUMENTATION_OF_IT_INFRASTRUCTURE = "loss-of-documentation-of-IT-Infrastructure"
    DESTRUCTION_OF_RECORDS = "destruction-of-records"
    INFECTION_OF_REMOVABLE_MEDIA = "infection-of-removable-media"
    ABUSE_OF_STORAGE = "abuse-of-storage"


class EnisaTaxonomyDisasterEntry(str, Enum):
    DISASTER = "disaster"
    FIRE = "fire"
    POLLUTION_DUST_CORROSION = "pollution-dust-corrosion"
    THUNDERSTRIKE = "thunderstrike"
    WATER = "water"
    EXPLOSION = "explosion"
    DANGEROUS_RADIATION_LEAK = "dangerous-radiation-leak"
    UNFAVOURABLE_CLIMATIC_CONDITIONS = "unfavourable-climatic-conditions"
    LOSS_OF_DATA_OR_ACCESSIBILITY_OF_IT_INFRASTRUCTURE_AS_A_RESULT_OF_HEIGHTENED_HUMIDITY = (
        "loss-of-data-or-accessibility-of-IT-infrastructure-as-a-result-of-heightened-humidity"
    )
    LOST_OF_DATA_OR_ACCESSIBILITY_OF_IT_INFRASTRUCTURE_AS_A_RESULT_OF_VERY_HIGH_TEMPERATURE = (
        "lost-of-data-or-accessibility-of-IT-infrastructure-as-a-result-of-very-high-temperature"
    )
    THREATS_FROM_SPACE_OR_ELECTROMAGNETIC_STORM = "threats-from-space-or-electromagnetic-storm"
    WILDLIFE = "wildlife"


class EnisaTaxonomyFailuresMalfunctionEntry(str, Enum):
    FAILURE_OF_DEVICES_OR_SYSTEMS = "failure-of-devices-or-systems"
    FAILURE_OF_DATA_MEDIA = "failure-of-data-media"
    HARDWARE_FAILURE = "hardware-failure"
    FAILURE_OF_APPLICATIONS_AND_SERVICES = "failure-of-applications-and-services"
    FAILURE_OF_PARTS_OF_DEVICES_CONNECTORS_PLUG_INS = "failure-of-parts-of-devices-connectors-plug-ins"
    FAILURE_OR_DISRUPTION_OF_COMMUNICATION_LINKS_COMMUNICATION_NETWORKS = (
        "failure-or-disruption-of-communication-links-communication networks"
    )
    FAILURE_OF_CABLE_NETWORKS = "failure-of-cable-networks"
    FAILURE_OF_WIRELESS_NETWORKS = "failure-of-wireless-networks"
    FAILURE_OF_MOBILE_NETWORKS = "failure-of-mobile-networks"
    FAILURE_OR_DISRUPTION_OF_MAIN_SUPPLY = "failure-or-disruption-of-main-supply"
    FAILURE_OR_DISRUPTION_OF_POWER_SUPPLY = "failure-or-disruption-of-power-supply"
    FAILURE_OF_COOLING_INFRASTRUCTURE = "failure-of-cooling-infrastructure"
    FAILURE_OR_DISRUPTION_OF_SERVICE_PROVIDERS_SUPPLY_CHAIN = "failure-or-disruption-of-service-providers-supply-chain"
    MALFUNCTION_OF_EQUIPMENT_DEVICES_OR_SYSTEMS = "malfunction-of-equipment-devices-or-systems"


class EnisaTaxonomyOutagesEntry(str, Enum):
    ABSENCE_OF_PERSONNEL = "absence-of-personnel"
    STRIKE = "strike"
    LOSS_OF_SUPPORT_SERVICES = "loss-of-support-services"
    INTERNET_OUTAGE = "internet-outage"
    NETWORK_OUTAGE = "network-outage"
    OUTAGE_OF_CABLE_NETWORKS = "outage-of-cable-networks"
    OUTAGE_OF_SHORT_RANGE_WIRELESS_NETWORKS = "Outage-of-short-range-wireless-networks"
    OUTAGES_OF_LONG_RANGE_WIRELESS_NETWORKS = "outages-of-long-range-wireless-networks"


class EnisaTaxonomyEavesdroppingInterceptionHijackingEntry(str, Enum):
    WAR_DRIVING = "war-driving"
    INTERCEPTING_COMPROMISING_EMISSIONS = "intercepting-compromising-emissions"
    INTERCEPTION_OF_INFORMATION = "interception-of-information"
    CORPORATE_ESPIONAGE = "corporate-espionage"
    NATION_STATE_ESPIONAGE = "nation-state-espionage"
    INFORMATION_LEAKAGE_DUE_TO_UNSECURED_WI_FI_LIKE_ROGUE_ACCESS_POINTS = (
        "information-leakage-due-to-unsecured-wi-fi-like-rogue-access-points"
    )
    INTERFERING_RADIATION = "interfering-radiation"
    REPLAY_OF_MESSAGES = "replay-of-messages"
    NETWORK_RECONNAISSANCE_NETWORK_TRAFFIC_MANIPULATION_AND_INFORMATION_GATHERING = (
        "network-reconnaissance-network-traffic-manipulation-and-information-gathering"
    )
    MAN_IN_THE_MIDDLE_SESSION_HIJACKING = "man-in-the-middle-session-hijacking"


class EnisaTaxonomyLegalEntry(str, Enum):
    VIOLATION_OF_RULES_AND_REGULATIONS_BREACH_OF_LEGISLATION = (
        "violation-of-rules-and-regulations-breach-of-legislation"
    )
    FAILURE_TO_MEET_CONTRACTUAL_REQUIREMENTS = "failure-to-meet-contractual-requirements"
    FAILURE_TO_MEET_CONTRACTUAL_REQUIREMENTS_BY_THIRD_PARTY = "failure-to-meet-contractual-requirements-by-third-party"
    UNAUTHORIZED_USE_OF_IPR_PROTECTED_RESOURCES = "unauthorized-use-of-IPR-protected-resources"
    ILLEGAL_USAGE_OF_FILE_SHARING_SERVICES = "illegal-usage-of-file-sharing-services"
    ABUSE_OF_PERSONAL_DATA = "abuse-of-personal-data"
    JUDICIARY_DECISIONS_OR_COURT_ORDER = "judiciary-decisions-or-court-order"


class EnisaTaxonomyNefariousActivityAbuseEntry(str, Enum):
    IDENTITY_THEFT_IDENTITY_FRAUD_ACCOUNT_ = "identity-theft-identity-fraud-account)"
    CREDENTIALS_STEALING_TROJANS = "credentials-stealing-trojans"
    RECEIVING_UNSOLICITED_E_MAIL = "receiving-unsolicited-e-mail"
    SPAM = "spam"
    UNSOLICITED_INFECTED_E_MAILS = "unsolicited-infected-e-mails"
    DENIAL_OF_SERVICE = "denial-of-service"
    DISTRIBUTED_DENIAL_OF_NETWORK_SERVICE_NETWORK_LAYER_ATTACK = (
        "distributed-denial-of-network-service-network-layer-attack"
    )
    DISTRIBUTED_DENIAL_OF_NETWORK_SERVICE_APPLICATION_LAYER_ATTACK = (
        "distributed-denial-of-network-service-application-layer-attack"
    )
    DISTRIBUTED_DENIAL_OF_NETWORK_SERVICE_AMPLIFICATION_REFLECTION_ATTACK = (
        "distributed-denial-of-network-service-amplification-reflection-attack"
    )
    MALICIOUS_CODE_SOFTWARE_ACTIVITY = "malicious-code-software-activity"
    SEARCH_ENGINE_POISONING = "search-engine-poisoning"
    EXPLOITATION_OF_FAKE_TRUST_OF_SOCIAL_MEDIA = "exploitation-of-fake-trust-of-social-media"
    WORMS_TROJANS = "worms-trojans"
    ROOTKITS = "rootkits"
    MOBILE_MALWARE = "mobile-malware"
    INFECTED_TRUSTED_MOBILE_APPS = "infected-trusted-mobile-apps"
    ELEVATION_OF_PRIVILEGES = "elevation-of-privileges"
    WEB_APPLICATION_ATTACKS_INJECTION_ATTACKS_CODE_INJECTION_SQL_XSS = (
        "web-application-attacks-injection-attacks-code-injection-SQL-XSS"
    )
    SPYWARE_OR_DECEPTIVE_ADWARE = "spyware-or-deceptive-adware"
    VIRUSES = "viruses"
    ROGUE_SECURITY_SOFTWARE_ROGUEWARE_SCAREWARE = "rogue-security-software-rogueware-scareware"
    RANSOMWARE = "ransomware"
    EXPLOITS_EXPLOIT_KITS = "exploits-exploit-kits"
    SOCIAL_ENGINEERING = "social-engineering"
    PHISHING_ATTACKS = "phishing-attacks"
    SPEAR_PHISHING_ATTACKS = "spear-phishing-attacks"
    ABUSE_OF_INFORMATION_LEAKAGE = "abuse-of-information-leakage"
    LEAKAGE_AFFECTING_MOBILE_PRIVACY_AND_MOBILE_APPLICATIONS = (
        "leakage-affecting-mobile-privacy-and-mobile-applications"
    )
    LEAKAGE_AFFECTING_WEB_PRIVACY_AND_WEB_APPLICATIONS = "leakage-affecting-web-privacy-and-web-applications"
    LEAKAGE_AFFECTING_NETWORK_TRAFFIC = "leakage-affecting-network-traffic"
    LEAKAGE_AFFECTING_CLOUD_COMPUTING = "leakage-affecting-cloud-computing"
    GENERATION_AND_USE_OF_ROGUE_CERTIFICATES = "generation-and-use-of-rogue-certificates"
    LOSS_OF_INTEGRITY_OF_SENSITIVE_INFORMATION = "loss-of-integrity-of-sensitive-information"
    MAN_IN_THE_MIDDLE_SESSION_HIJACKING = "man-in-the-middle-session-hijacking"
    SOCIAL_ENGINEERING_VIA_SIGNED_MALWARE = "social-engineering-via-signed-malware"
    FAKE_SSL_CERTIFICATES = "fake-SSL-certificates"
    MANIPULATION_OF_HARDWARE_AND_SOFTWARE = "manipulation-of-hardware-and-software"
    ANONYMOUS_PROXIES = "anonymous-proxies"
    ABUSE_OF_COMPUTING_POWER_OF_CLOUD_TO_LAUNCH_ATTACKS_CYBERCRIME_AS_A_SERVICE_ = (
        "abuse-of-computing-power-of-cloud-to-launch-attacks-cybercrime-as-a-service)"
    )
    ABUSE_OF_VULNERABILITIES_0_DAY_VULNERABILITIES = "abuse-of-vulnerabilities-0-day-vulnerabilities"
    ACCESS_OF_WEB_SITES_THROUGH_CHAINS_OF_HTTP_PROXIES_OBFUSCATION = (
        "access-of-web-sites-through-chains-of-HTTP-Proxies-Obfuscation"
    )
    ACCESS_TO_DEVICE_SOFTWARE = "access-to-device-software"
    ALTERNATION_OF_SOFTWARE = "alternation-of-software"
    ROGUE_HARDWARE = "rogue-hardware"
    MANIPULATION_OF_INFORMATION = "manipulation-of-information"
    REPUDIATION_OF_ACTIONS = "repudiation-of-actions"
    ADDRESS_SPACE_HIJACKING_IP_PREFIXES = "address-space-hijacking-IP-prefixes"
    ROUTING_TABLE_MANIPULATION = "routing-table-manipulation"
    DNS_POISONING_OR_DNS_SPOOFING_OR_DNS_MANIPULATIONS = "DNS-poisoning-or-DNS-spoofing-or-DNS-Manipulations"
    FALSIFICATION_OF_RECORD = "falsification-of-record"
    AUTONOMOUS_SYSTEM_HIJACKING = "autonomous-system-hijacking"
    AUTONOMOUS_SYSTEM_MANIPULATION = "autonomous-system-manipulation"
    FALSIFICATION_OF_CONFIGURATIONS = "falsification-of-configurations"
    MISUSE_OF_AUDIT_TOOLS = "misuse-of-audit-tools"
    MISUSE_OF_INFORMATION_OR_INFORMATION_SYSTEMS_INCLUDING_MOBILE_APPS = (
        "misuse-of-information-or-information systems-including-mobile-apps"
    )
    UNAUTHORIZED_ACTIVITIES = "unauthorized-activities"
    UNAUTHORISED_USE_OR_ADMINISTRATION_OF_DEVICES_AND_SYSTEMS = (
        "Unauthorised-use-or-administration-of-devices-and-systems"
    )
    UNAUTHORISED_USE_OF_SOFTWARE = "unauthorised-use-of-software"
    UNAUTHORIZED_ACCESS_TO_THE_INFORMATION_SYSTEMS_OR_NETWORKS_LIKE_IMPI_PROTOCOL_DNS_REGISTRAR_HIJACKING_ = (
        "unauthorized-access-to-the-information-systems-or-networks-like-IMPI-Protocol-DNS-Registrar-Hijacking)"
    )
    NETWORK_INTRUSION = "network-intrusion"
    UNAUTHORIZED_CHANGES_OF_RECORDS = "unauthorized-changes-of-records"
    UNAUTHORIZED_INSTALLATION_OF_SOFTWARE = "unauthorized-installation-of-software"
    WEB_BASED_ATTACKS_DRIVE_BY_DOWNLOAD_OR_MALICIOUS_URLS_OR_BROWSER_BASED_ATTACKS = (
        "Web-based-attacks-drive-by-download-or-malicious-URLs-or-browser-based-attacks"
    )
    COMPROMISING_CONFIDENTIAL_INFORMATION_LIKE_DATA_BREACHES = (
        "compromising-confidential-information-like-data-breaches"
    )
    HOAX = "hoax"
    FALSE_RUMOUR_AND_OR_FAKE_WARNING = "false-rumour-and-or-fake-warning"
    REMOTE_ACTIVITY_EXECUTION = "remote-activity-execution"
    REMOTE_COMMAND_EXECUTION = "remote-command-execution"
    REMOTE_ACCESS_TOOL = "remote-access-tool"
    BOTNETS_REMOTE_ACTIVITY = "botnets-remote-activity"
    TARGETED_ATTACKS = "targeted-attacks"
    MOBILE_MALWARE_EXFILTRATION = "mobile-malware-exfiltration"
    SPEAR_PHISHING_ATTACKS_TARGETED = "spear-phishing-attacks-targeted"
    INSTALLATION_OF_SOPHISTICATED_AND_TARGETED_MALWARE = "installation-of-sophisticated-and-targeted-malware"
    WATERING_HOLE_ATTACKS = "watering-hole-attacks"
    FAILED_BUSINESS_PROCESS = "failed-business-process"
    BRUTE_FORCE = "brute-force"
    ABUSE_OF_AUTHORIZATIONS = "abuse-of-authorizations"


class EnisaTaxonomy(BaseModel):
    """Model for the ENISA Threat Taxonomy taxonomy."""

    namespace: str = "enisa"
    description: str = """The present threat taxonomy is an initial version that has been developed on the basis of available ENISA material. This material has been used as an ENISA-internal structuring aid for information collection and threat consolidation purposes. It emerged in the time period 2012-2015."""
    version: int = 20170725
    exclusive: bool = False
    predicates: List[EnisaTaxonomyPredicate] = []
    physical_attack_entries: List[EnisaTaxonomyPhysicalAttackEntry] = []
    unintentional_damage_entries: List[EnisaTaxonomyUnintentionalDamageEntry] = []
    disaster_entries: List[EnisaTaxonomyDisasterEntry] = []
    failures_malfunction_entries: List[EnisaTaxonomyFailuresMalfunctionEntry] = []
    outages_entries: List[EnisaTaxonomyOutagesEntry] = []
    eavesdropping_interception_hijacking_entries: List[EnisaTaxonomyEavesdroppingInterceptionHijackingEntry] = []
    legal_entries: List[EnisaTaxonomyLegalEntry] = []
    nefarious_activity_abuse_entries: List[EnisaTaxonomyNefariousActivityAbuseEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
