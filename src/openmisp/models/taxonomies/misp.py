"""Taxonomy model for MISP."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class MispTaxonomyPredicate(str, Enum):
    UI = "ui"
    API = "api"
    EXPANSION = "expansion"
    CONTRIBUTOR = "contributor"
    CONFIDENCE_LEVEL = "confidence-level"
    THREAT_LEVEL = "threat-level"
    AUTOMATION_LEVEL = "automation-level"
    SHOULD_NOT_SYNC = "should-not-sync"
    TOOL = "tool"
    MISP2YARA = "misp2yara"
    EVENT_TYPE = "event-type"
    IDS = "ids"


class MispTaxonomyUiEntry(str, Enum):
    HIDE = "hide"


class MispTaxonomyApiEntry(str, Enum):
    HIDE = "hide"


class MispTaxonomyExpansionEntry(str, Enum):
    BLOCK = "block"


class MispTaxonomyContributorEntry(str, Enum):
    PGPFINGERPRINT = "pgpfingerprint"


class MispTaxonomyConfidenceLevelEntry(str, Enum):
    COMPLETELY_CONFIDENT = "completely-confident"
    USUALLY_CONFIDENT = "usually-confident"
    FAIRLY_CONFIDENT = "fairly-confident"
    RARELY_CONFIDENT = "rarely-confident"
    UNCONFIDENT = "unconfident"
    CONFIDENCE_CANNOT_BE_EVALUATED = "confidence-cannot-be-evaluated"


class MispTaxonomyThreatLevelEntry(str, Enum):
    NO_RISK = "no-risk"
    LOW_RISK = "low-risk"
    MEDIUM_RISK = "medium-risk"
    HIGH_RISK = "high-risk"


class MispTaxonomyAutomationLevelEntry(str, Enum):
    UNSUPERVISED = "unsupervised"
    REVIEWED = "reviewed"
    MANUAL = "manual"


class MispTaxonomyToolEntry(str, Enum):
    MISP2STIX = "misp2stix"
    MISP2YARA = "misp2yara"


class MispTaxonomyMisp2yaraEntry(str, Enum):
    GENERATED = "generated"
    AS_IS = "as-is"
    VALID = "valid"
    INVALID = "invalid"


class MispTaxonomyEventTypeEntry(str, Enum):
    OBSERVATION = "observation"
    INCIDENT = "incident"
    REPORT = "report"
    COLLECTION = "collection"
    ANALYSIS = "analysis"
    AUTOMATIC_ANALYSIS = "automatic-analysis"


class MispTaxonomyIdsEntry(str, Enum):
    FORCE = "force"
    TRUE = "true"
    FALSE = "false"


class MispTaxonomy(BaseModel):
    """Model for the MISP taxonomy."""

    namespace: str = "misp"
    description: str = """MISP taxonomy to infer with MISP behavior or operation."""
    version: int = 14
    exclusive: bool = False
    predicates: List[MispTaxonomyPredicate] = []
    ui_entries: List[MispTaxonomyUiEntry] = []
    api_entries: List[MispTaxonomyApiEntry] = []
    expansion_entries: List[MispTaxonomyExpansionEntry] = []
    contributor_entries: List[MispTaxonomyContributorEntry] = []
    confidence_level_entries: List[MispTaxonomyConfidenceLevelEntry] = []
    threat_level_entries: List[MispTaxonomyThreatLevelEntry] = []
    automation_level_entries: List[MispTaxonomyAutomationLevelEntry] = []
    tool_entries: List[MispTaxonomyToolEntry] = []
    misp2yara_entries: List[MispTaxonomyMisp2yaraEntry] = []
    event_type_entries: List[MispTaxonomyEventTypeEntry] = []
    ids_entries: List[MispTaxonomyIdsEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
