"""Taxonomy model for smart-airports-threats."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class SmartAirportsThreatsTaxonomyPredicate(str, Enum):
    HUMAN_ERRORS = "human-errors"
    SYSTEM_FAILURES = "system-failures"
    NATURAL_AND_SOCIAL_PHENOMENA = "natural-and-social-phenomena"
    THIRD_PARTY_FAILURES = "third-party-failures"
    MALICIOUS_ACTIONS = "malicious-actions"


class SmartAirportsThreatsTaxonomyHumanErrorsEntry(str, Enum):
    CONFIGURATION_ERRORS = "configuration-errors"
    OPERATOR_OR_USER_ERROR = "operator-or-user-error"
    LOSS_OF_HARDWARE = "loss-of-hardware"
    NON_COMPLIANCE_WITH_POLICIES_OR_PROCEDURE = "non-compliance-with-policies-or-procedure"


class SmartAirportsThreatsTaxonomySystemFailuresEntry(str, Enum):
    FAILURES_OF_DEVICES_OR_SYSTEMS = "failures-of-devices-or-systems"
    FAILURES_OR_DISRUPTIONS_OF_COMMUNICATION_LINKS = "failures-or-disruptions-of-communication-links"
    FAILURES_OF_PARTS_OF_DEVICES = "failures-of-parts-of-devices"
    FAILURES_OR_DISRUPTIONS_OF_MAIN_SUPPLY = "failures-or-disruptions-of-main-supply"
    FAILURES_OR_DISRUPTIONS_OF_THE_POWER_SUPPLY = "failures-or-disruptions-of-the-power-supply"
    MALFUNCTIONS_OF_PARTS_OF_DEVICES = "malfunctions-of-parts-of-devices"
    MALFUNCTIONS_OF_DEVICES_OR_SYSTEMS = "malfunctions-of-devices-or-systems"
    FAILURES_OF_HARDWARE = "failures-of-hardware"
    SOFTWARE_BUGS = "software-bugs"


class SmartAirportsThreatsTaxonomyNaturalAndSocialPhenomenaEntry(str, Enum):
    EARTHQUAKES = "earthquakes"
    FIRES = "fires"
    EXTREME_WEATHER = "extreme-weather"
    SOLAR_FLARE = "solar-flare"
    VOLCANO_EXPLOSION = "volcano-explosion"
    NUCLEAR_INCIDENT = "nuclear-incident"
    DANGEROUS_CHEMICAL_INCIDENTS = "dangerous-chemical-incidents"
    PANDEMIC = "pandemic"
    SOCIAL_DISRUPTIONS = "social-disruptions"
    SHORTAGE_OF_FUEL = "shortage-of-fuel"
    SPACE_DEBRIS_AND_METEORITES = "space-debris-and-meteorites"


class SmartAirportsThreatsTaxonomyThirdPartyFailuresEntry(str, Enum):
    INTERNET_SERVICE_PROVIDER = "internet-service-provider"
    CLOUD_SERVICE_PROVIDER = "cloud-service-provider"
    UTILITIES_POWER_OR_GAS_OR_WATER = "utilities-power-or-gas-or-water"
    REMOTE_MAINTENANCE_PROVIDER = "remote-maintenance-provider"
    SECURITY_TESTING_COMPANIES = "security-testing-companies"


class SmartAirportsThreatsTaxonomyMaliciousActionsEntry(str, Enum):
    DENIAL_OF_SERVICE_ATTACKS_VIA_AMPLIFICATION_REFLECTION = "denial-of-service-attacks-via-amplification-reflection"
    DENIAL_OF_SERVICE_ATTACKS_VIA_FLOODING = "denial-of-service-attacks-via-flooding"
    DENIAL_OF_SERVICE_ATTACKS_VIA_JAMMING = "denial-of-service-attacks-via-jamming"
    MALICIOUS_SOFTWARE_ON_IT_ASSETS_MALWARE = "malicious-software-on-it-assets-malware"
    MALICIOUS_SOFTWARE_ON_IT_ASSETS_REMOTE_ARBITRARY_CODE_EXECUTION = (
        "malicious-software-on-it-assets-remote-arbitrary-code-execution"
    )
    EXPLOITATION_OF_SOFTWARE_VULNERABILITIES_IMPLEMENTATION_FLAWS = (
        "exploitation-of-software-vulnerabilities-implementation-flaws"
    )
    EXPLOITATION_OF_SOFTWARE_VULNERABILITIES_DESIGN_FLAWS = "exploitation-of-software-vulnerabilities-design-flaws"
    EXPLOITATION_OF_SOFTWARE_VULNERABILITIES_APT = "exploitation-of-software-vulnerabilities-apt"
    MISUSE_OF_AUTHORITY_OR_AUTHORISATION_UNAUTHORIZED_USE_OF_SOFTWARE = (
        "misuse-of-authority-or-authorisation-unauthorized-use-of-software"
    )
    MISUSE_OF_AUTHORITY_OR_AUTHORISATION_UNAUTHORIZED_INSTALLATION_OF_SOFTWARE = (
        "misuse-of-authority-or-authorisation-unauthorized-installation-of-software"
    )
    MISUSE_OF_AUTHORITY_OR_AUTHORISATION_REPUDIATION_OF_ACTIONS = (
        "misuse-of-authority-or-authorisation-repudiation-of-actions"
    )
    MISUSE_OF_AUTHORITY_OR_AUTHORISATION_ABUSE_OF_PERSONAL_DATA = (
        "misuse-of-authority-or-authorisation-abuse-of-personal-data"
    )
    MISUSE_OF_AUTHORITY_OR_AUTHORISATION_USING_INFORMATION_FROM_AN_UNRELIABLE_SOURCE = (
        "misuse-of-authority-or-authorisation-using-information-from-an-unreliable-source"
    )
    MISUSE_OF_AUTHORITY_OR_AUTHORISATION_UNINTENTIONAL_CHANGE_OF_DATA_IN_AN_INFORMATION_SYSTEM = (
        "misuse-of-authority-or-authorisation-unintentional-change-of-data-in-an-information-system"
    )
    MISUSE_OF_AUTHORITY_OR_AUTHORISATION_INADEQUATE_DESIGN_AND_PLANNING_OR_LACK_OF_ADOPTION = (
        "misuse-of-authority-or-authorisation-inadequate-design-and-planning-or-lack-of-adoption"
    )
    MISUSE_OF_AUTHORITY_OR_AUTHORISATION_DATA_LEAKAGE_OR_SHARING = (
        "misuse-of-authority-or-authorisation-data-leakage-or-sharing"
    )
    NETWORK_OR_INTERCEPTION_ATTACKS_MANIPULATION_OF_ROUTING_INFORMATION = (
        "network-or-interception-attacks-manipulation-of-routing-information"
    )
    NETWORK_OR_INTERCEPTION_ATTACKS_SPOOFING = "network-or-interception-attacks-spoofing"
    NETWORK_OR_INTERCEPTION_ATTACKS_UNAUTHORIZED_ACCESS = "network-or-interception-attacks-unauthorized-access"
    NETWORK_OR_INTERCEPTION_ATTACKS_AUTHENTICATION_ATTACKS = "network-or-interception-attacks-authentication-attacks"
    NETWORK_OR_INTERCEPTION_ATTACKS_REPLAY_ATTACKS = "network-or-interception-attacks-replay-attacks"
    NETWORK_OR_INTERCEPTION_ATTACKS_REPUDIATION_OF_ACTIONS = "network-or-interception-attacks-repudiation-of-actions"
    NETWORK_OR_INTERCEPTION_ATTACKS_WIRETAPS = "network-or-interception-attacks-wiretaps"
    NETWORK_OR_INTERCEPTION_ATTACKS_WIRELESS_COMMS = "network-or-interception-attacks-wireless-comms"
    NETWORK_OR_INTERCEPTION_ATTACKS_NETWORK_RECONNAISSANCE_INFORMATION_GATHERING = (
        "network-or-interception-attacks-network-reconnaissance-information-gathering"
    )
    SOCIAL_ATTACKS_PHISHING_SPEARPHISHING = "social-attacks-phishing-spearphishing"
    SOCIAL_ATTACKS_PRETEXTING = "social-attacks-pretexting"
    SOCIAL_ATTACKS_UNTRUSTED_LINKS = "social-attacks-untrusted-links"
    SOCIAL_ATTACKS_BAITING = "social-attacks-baiting"
    SOCIAL_ATTACKS_REVERSE_SOCIAL_ENGINEERING = "social-attacks-reverse-social-engineering"
    SOCIAL_ATTACKS_IMPERSONATION = "social-attacks-impersonation"
    TAMPERING_WITH_DEVICES_UNAUTHORISED_MODIFICATION_OF_DATA = (
        "tampering-with-devices-unauthorised-modification-of-data"
    )
    TAMPERING_WITH_DEVICES_UNAUTHORISED_MODIFICATION_OF_HARDWARE_OR_SOFTWARE = (
        "tampering-with-devices-unauthorised-modification-of-hardware-or-software"
    )
    BREACH_OF_PHYSICAL_ACCESS_CONTROLS_BYPASS_AUTHENTICATION = (
        "breach-of-physical-access-controls-bypass-authentication"
    )
    BREACH_OF_PHYSICAL_ACCESS_CONTROLS_PRIVILEGE_ESCALATION = "breach-of-physical-access-controls-privilege-escalation"
    PHYSICAL_ATTACKS_ON_AIRPORT_ASSETS_VANDALISM = "physical-attacks-on-airport-assets-vandalism"
    PHYSICAL_ATTACKS_ON_AIRPORT_ASSETS_SABOTAGE = "physical-attacks-on-airport-assets-sabotage"
    PHYSICAL_ATTACKS_ON_AIRPORT_ASSETS_EXPLOSIVE_OR_BOMB_THREATS = (
        "physical-attacks-on-airport-assets-explosive-or-bomb-threats"
    )
    PHYSICAL_ATTACKS_ON_AIRPORT_ASSETS_MALICIOUS_TAMPERING = "physical-attacks-on-airport-assets-malicious-tampering"


class SmartAirportsThreatsTaxonomy(BaseModel):
    """Model for the smart-airports-threats taxonomy."""

    namespace: str = "smart-airports-threats"
    description: str = """Threat taxonomy in the scope of securing smart airports by ENISA. https://www.enisa.europa.eu/publications/securing-smart-airports"""
    version: int = 1
    exclusive: bool = False
    predicates: List[SmartAirportsThreatsTaxonomyPredicate] = []
    human_errors_entries: List[SmartAirportsThreatsTaxonomyHumanErrorsEntry] = []
    system_failures_entries: List[SmartAirportsThreatsTaxonomySystemFailuresEntry] = []
    natural_and_social_phenomena_entries: List[SmartAirportsThreatsTaxonomyNaturalAndSocialPhenomenaEntry] = []
    third_party_failures_entries: List[SmartAirportsThreatsTaxonomyThirdPartyFailuresEntry] = []
    malicious_actions_entries: List[SmartAirportsThreatsTaxonomyMaliciousActionsEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
