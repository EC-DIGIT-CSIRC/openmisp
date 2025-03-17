"""Taxonomy model for open_threat."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class OpenThreatTaxonomyPredicate(str, Enum):
    THREAT_CATEGORY = "threat-category"
    THREAT_NAME = "threat-name"


class OpenThreatTaxonomyThreatCategoryEntry(str, Enum):
    PHYSICAL = "Physical"
    RESOURCE = "Resource"
    PERSONAL = "Personal"
    TECHNICAL = "Technical"


class OpenThreatTaxonomyThreatNameEntry(str, Enum):
    PHY_001 = "PHY-001"
    PHY_002 = "PHY-002"
    PHY_003 = "PHY-003"
    PHY_004 = "PHY-004"
    PHY_005 = "PHY-005"
    PHY_006 = "PHY-006"
    PHY_007 = "PHY-007"
    PHY_008 = "PHY-008"
    PHY_009 = "PHY-009"
    PHY_010 = "PHY-010"
    PHY_011 = "PHY-011"
    PHY_012 = "PHY-012"
    PHY_013 = "PHY-013"
    PHY_014 = "PHY-014"
    RES_001 = "RES-001"
    RES_002 = "RES-002"
    RES_003 = "RES-003"
    RES_004 = "RES-004"
    RES_005 = "RES-005"
    RES_006 = "RES-006"
    RES_007 = "RES-007"
    RES_008 = "RES-008"
    RES_009 = "RES-009"
    RES_010 = "RES-010"
    RES_011 = "RES-011"
    RES_012 = "RES-012"
    RES_013 = "RES-013"
    PER_001 = "PER-001"
    PER_002 = "PER-002"
    PER_003 = "PER-003"
    PER_004 = "PER-004"
    PER_005 = "PER-005"
    PER_006 = "PER-006"
    PER_007 = "PER-007"
    TEC_001 = "TEC-001"
    TEC_002 = "TEC-002"
    TEC_003 = "TEC-003"
    TEC_004 = "TEC-004"
    TEC_005 = "TEC-005"
    TEC_006 = "TEC-006"
    TEC_007 = "TEC-007"
    TEC_008 = "TEC-008"
    TEC_009 = "TEC-009"
    TEC_010 = "TEC-010"
    TEC_011 = "TEC-011"
    TEC_012 = "TEC-012"
    TEC_013 = "TEC-013"
    TEC_014 = "TEC-014"
    TEC_015 = "TEC-015"
    TEC_016 = "TEC-016"
    TEC_017 = "TEC-017"
    TEC_018 = "TEC-018"
    TEC_019 = "TEC-019"
    TEC_020 = "TEC-020"
    TEC_021 = "TEC-021"
    TEC_022 = "TEC-022"
    TEC_023 = "TEC-023"
    TEC_024 = "TEC-024"
    TEC_025 = "TEC-025"
    TEC_026 = "TEC-026"
    TEC_027 = "TEC-027"
    TEC_028 = "TEC-028"
    TEC_029 = "TEC-029"
    TEC_030 = "TEC-030"
    TEC_031 = "TEC-031"
    TEC_032 = "TEC-032"
    TEC_033 = "TEC-033"
    TEC_034 = "TEC-034"
    TEC_035 = "TEC-035"
    TEC_036 = "TEC-036"
    TEC_037 = "TEC-037"
    TEC_038 = "TEC-038"
    TEC_039 = "TEC-039"
    TEC_040 = "TEC-040"
    TEC_041 = "TEC-041"


class OpenThreatTaxonomy(BaseModel):
    """Model for the open_threat taxonomy."""

    namespace: str = "open_threat"
    description: str = """Open Threat Taxonomy v1.1 base on James Tarala of SANS http://www.auditscripts.com/resources/open_threat_taxonomy_v1.1a.pdf, https://files.sans.org/summit/Threat_Hunting_Incident_Response_Summit_2016/PDFs/Using-Open-Tools-to-Convert-Threat-Intelligence-into-Practical-Defenses-James-Tarala-SANS-Institute.pdf, https://www.youtube.com/watch?v=5rdGOOFC_yE, and https://www.rsaconference.com/writable/presentations/file_upload/str-r04_using-an-open-source-threat-model-for-prioritized-defense-final.pdf"""
    version: int = 1
    exclusive: bool = False
    predicates: List[OpenThreatTaxonomyPredicate] = []
    threat_category_entries: List[OpenThreatTaxonomyThreatCategoryEntry] = []
    threat_name_entries: List[OpenThreatTaxonomyThreatNameEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
