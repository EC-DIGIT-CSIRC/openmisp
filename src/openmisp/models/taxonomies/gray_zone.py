"""Taxonomy model for GrayZone."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GrayZoneTaxonomyPredicate(str, Enum):
    ADVERSARY_EMULATION = "Adversary Emulation"
    BEACONS = "Beacons"
    DETERRENCE = "Deterrence"
    DECEPTION = "Deception"
    TARPITS__SANDBOXES_AND_HONEYPOTS = "Tarpits, Sandboxes and Honeypots"
    INTELLIGENCE_AND_COUNTERINTELLIGENCE = "Intelligence and Counterintelligence"
    ADVERSARY_TAKEDOWNS = "Adversary Takedowns"
    RANSOMWARE = "Ransomware"
    RESCUE_MISSIONS = "Rescue Missions"
    SANCTIONS__INDICTMENTS___TRADE_REMEDIES = "Sanctions, Indictments & Trade Remedies"


class GrayZoneTaxonomyAdversaryEmulationEntry(str, Enum):
    THREAT_MODELING = "Threat Modeling"
    PURPLE_TEAMING = "Purple Teaming"
    BLUE_TEAM = "Blue Team"
    RED_TEAM = "Red Team"


class GrayZoneTaxonomyBeaconsEntry(str, Enum):
    INFORM = "Inform"
    NOTIFY = "Notify"


class GrayZoneTaxonomyDeterrenceEntry(str, Enum):
    BY_RETALIATION = "by Retaliation"
    BY_DENIAL = "by Denial"
    BY_ENTANGLEMENT = "by Entanglement"


class GrayZoneTaxonomyDeceptionEntry(str, Enum):
    DECEPTION = "Deception"
    DENIAL = "Denial"
    COUNTER_DECEPTION = "CounterDeception"


class GrayZoneTaxonomyTarpitsSandboxesAndHoneypotsEntry(str, Enum):
    HONEYPOTS = "Honeypots"
    SANDBOXES = "Sandboxes"
    TARPITS = "Tarpits"


class GrayZoneTaxonomyIntelligenceAndCounterintelligenceEntry(str, Enum):
    INTEL_PASSIVE = "Intel Passive"
    INTEL_ACTIVE = "Intel Active"
    COUNTERINTEL_DEFENSIVE = "Counterintel Defensive"
    COUNTERINTEL_DEFENSIVE___DETERRENCE = "Counterintel Defensive - Deterrence"
    COUNTERINTEL_DEFENSIVE___DETECTION = "Counterintel Defensive - Detection"
    COUNTERINTEL_OFFENSIVE = "Counterintel Offensive"
    COUNTERINTEL_OFFENSIVE___DETECTION = "Counterintel Offensive - Detection"
    COUNTERINTEL_OFFENSIVE___DECEPTION = "Counterintel Offensive - Deception"
    COUNTERINTEL_OFFENSIVE___NEUTRALIZATION = "Counterintel Offensive - Neutralization"


class GrayZoneTaxonomyAdversaryTakedownsEntry(str, Enum):
    BOTNET_TAKEDOWNS = "Botnet Takedowns"
    DOMAIN_TAKEDOWNS = "Domain Takedowns"
    INFRASTRUCTURE_TAKEDOWNS = "Infrastructure Takedowns"


class GrayZoneTaxonomyRansomwareEntry(str, Enum):
    RANSOMWARE = "Ransomware"


class GrayZoneTaxonomyRescueMissionsEntry(str, Enum):
    RESCUE_MISSIONS = "Rescue Missions"


class GrayZoneTaxonomySanctionsIndictmentsTradeRemediesEntry(str, Enum):
    SANCTIONS__INDICTMENTS___TRADE_REMEDIES = "Sanctions, Indictments & Trade Remedies"


class GrayZoneTaxonomy(BaseModel):
    """Model for the GrayZone taxonomy."""

    namespace: str = "GrayZone"
    description: str = """Gray Zone of Active defense includes all elements which lay between reactive defense elements and offensive operations. It does fill the gray spot between them. Taxo may be used for active defense planning or modeling."""
    version: int = 3
    exclusive: bool = False
    predicates: List[GrayZoneTaxonomyPredicate] = []
    adversary_emulation_entries: List[GrayZoneTaxonomyAdversaryEmulationEntry] = []
    beacons_entries: List[GrayZoneTaxonomyBeaconsEntry] = []
    deterrence_entries: List[GrayZoneTaxonomyDeterrenceEntry] = []
    deception_entries: List[GrayZoneTaxonomyDeceptionEntry] = []
    tarpits__sandboxes_and_honeypots_entries: List[GrayZoneTaxonomyTarpitsSandboxesAndHoneypotsEntry] = []
    intelligence_and_counterintelligence_entries: List[GrayZoneTaxonomyIntelligenceAndCounterintelligenceEntry] = []
    adversary_takedowns_entries: List[GrayZoneTaxonomyAdversaryTakedownsEntry] = []
    ransomware_entries: List[GrayZoneTaxonomyRansomwareEntry] = []
    rescue_missions_entries: List[GrayZoneTaxonomyRescueMissionsEntry] = []
    sanctions__indictments___trade_remedies_entries: List[GrayZoneTaxonomySanctionsIndictmentsTradeRemediesEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
