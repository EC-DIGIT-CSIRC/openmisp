"""Taxonomy model for aviation."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class AviationTaxonomyPredicate(str, Enum):
    TARGET = "target"
    TARGET_SYSTEMS = "target-systems"
    TARGET_SUB_SYSTEMS = "target-sub-systems"
    IMPACT = "impact"
    LIKELIHOOD = "likelihood"
    CRITICALITY = "criticality"
    CERTAINTY = "certainty"


class AviationTaxonomyTargetEntry(str, Enum):
    AIRLINE = "airline"
    AIRSPACE_USERS = "airspace users"
    AIRPORT = "airport"
    ANSP = "ansp"
    INTERNATIONAL_ASSOCIATION = "international-association"
    CAA = "caa"
    MANUFACTURER = "manufacturer"
    SERVICE_PROVIDER = "service-provider"
    NETWORK_MANAGER = "network-manager"
    MILITARY = "military"


class AviationTaxonomyTargetSystemsEntry(str, Enum):
    ATM = "ATM"
    AIS = "AIS"
    MET = "MET"
    SAR = "SAR"
    CNS = "CNS"
    AIRPORT_MANAGEMENT_SYSTEMS = "airport-management-systems"
    AIRPORT_ONLINE_SERVICES = "airport-online-services"
    AIRPORT_FIDS_SYSTEMS = "airport-fids-systems"
    AIRLINE_MANAGEMENT_SYSTEMS = "airline-management-systems"
    AIRLINE_ONLINE_SERVICES = "airline-online-services"


class AviationTaxonomyTargetSubSystemsEntry(str, Enum):
    ATM_NEW_PENS = "ATM:NewPENS"
    ATM_SWIM = "ATM:SWIM"
    ATM_ATS_ATC = "ATM:ATS:ATC"
    ATM_ATS_FIS = "ATM:ATS:FIS"
    ATM_ATS_ALRS = "ATM:ATS:ALRS"
    ATM_ATS_ATFM = "ATM:ATS:ATFM"
    ATM_ATS_ASM = "ATM:ATS:ASM"
    CNS_COM_GROUND_GROUND = "CNS:COM:Ground-Ground"
    CNS_COM_GROUND_AIR = "CNS:COM:Ground-Air"
    CNS_COM_AIR_AIR = "CNS:COM:Air-Air"
    CNS_COM_ASTERIX = "CNS:COM:Asterix"
    CNS_COM_VDL = "CNS:COM:VDL"
    CNS_SUR_ADS_B = "CNS:SUR:ADS-B"
    CNS_SUR_ADS_C = "CNS:SUR:ADS-C"
    CNS_SUR_RADAR = "CNS:SUR:Radar"
    CNS_SUR_PR = "CNS:SUR:PR"
    CNS_SUR_SSR = "CNS:SUR:SSR"
    CNS_NAV_GNSS = "CNS:Nav:GNSS"
    CNS_NAV_GPS = "CNS:Nav:GPS"
    CNS_NAV_GLONASS = "CNS:Nav:GLONASS"
    CNS_NAV_ILS = "CNS:Nav:ILS"
    CNS_NAV_GLS = "CNS:Nav:GLS"


class AviationTaxonomyImpactEntry(str, Enum):
    TRIVIAL = "trivial"
    MINOR = "minor"
    MODERATE = "moderate"
    MAJOR = "major"
    EXTREME = "extreme"


class AviationTaxonomyLikelihoodEntry(str, Enum):
    ALMOST_NO_CHANCE = "almost-no-chance"
    VERY_UNLIKELY = "very-unlikely"
    UNLIKELY = "unlikely"
    ROUGHLY_EVEN_CHANCE = "roughly-even-chance"
    LIKELY = "likely"
    VERY_LIKELY = "very-likely"
    ALMOST_CERTAIN = "almost-certain"


class AviationTaxonomyCriticalityEntry(str, Enum):
    SAFETY_CRITICAL = "safety-critical"
    MISSION_CRITICAL = "mission-critical"
    BUSINESS_CRITICAL = "business-critical"


class AviationTaxonomyCertaintyEntry(str, Enum):
    T_100 = "100"
    T_93 = "93"
    T_75 = "75"
    T_50 = "50"
    T_30 = "30"
    T_7 = "7"
    T_0 = "0"


class AviationTaxonomy(BaseModel):
    """Model for the aviation taxonomy."""

    namespace: str = "aviation"
    description: str = """A taxonomy describing security threats or incidents against the aviation sector."""
    version: int = 1
    exclusive: bool = False
    predicates: List[AviationTaxonomyPredicate] = []
    target_entries: List[AviationTaxonomyTargetEntry] = []
    target_systems_entries: List[AviationTaxonomyTargetSystemsEntry] = []
    target_sub_systems_entries: List[AviationTaxonomyTargetSubSystemsEntry] = []
    impact_entries: List[AviationTaxonomyImpactEntry] = []
    likelihood_entries: List[AviationTaxonomyLikelihoodEntry] = []
    criticality_entries: List[AviationTaxonomyCriticalityEntry] = []
    certainty_entries: List[AviationTaxonomyCertaintyEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
