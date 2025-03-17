"""Taxonomy model for vmray."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class VmrayTaxonomyPredicate(str, Enum):
    VERDICT = "verdict"
    VTI_ANALYSIS_SCORE = "vti_analysis_score"
    ARTIFACT = "artifact"


class VmrayTaxonomyVerdictEntry(str, Enum):
    MALICIOUS = "malicious"
    SUSPICIOUS = "suspicious"
    CLEAN = "clean"
    N_A = "n/a"


class VmrayTaxonomyVtiAnalysisScoreEntry(str, Enum):
    T__1_5 = "-1/5"
    T_1_5 = "1/5"
    T_2_5 = "2/5"
    T_3_5 = "3/5"
    T_4_5 = "4/5"
    T_5_5 = "5/5"


class VmrayTaxonomyArtifactEntry(str, Enum):
    IOC = "ioc"


class VmrayTaxonomy(BaseModel):
    """Model for the vmray taxonomy."""

    namespace: str = "vmray"
    description: str = """VMRay taxonomies to map VMRay Thread Identifier scores and artifacts."""
    version: int = 1
    exclusive: bool = False
    predicates: List[VmrayTaxonomyPredicate] = []
    verdict_entries: List[VmrayTaxonomyVerdictEntry] = []
    vti_analysis_score_entries: List[VmrayTaxonomyVtiAnalysisScoreEntry] = []
    artifact_entries: List[VmrayTaxonomyArtifactEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
