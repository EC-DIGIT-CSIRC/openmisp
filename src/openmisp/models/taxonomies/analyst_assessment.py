"""Taxonomy model for Analyst (Self) Assessment."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class AnalystAssessmentTaxonomyPredicate(str, Enum):
    EXPERIENCE = "experience"
    BINARY_REVERSING_ARCH = "binary-reversing-arch"
    BINARY_REVERSING_EXPERIENCE = "binary-reversing-experience"
    OS = "os"
    WEB = "web"
    WEB_EXPERIENCE = "web-experience"
    CRYPTO_EXPERIENCE = "crypto-experience"


class AnalystAssessmentTaxonomyExperienceEntry(str, Enum):
    LESS_THAN_1_YEAR = "less-than-1-year"
    BETWEEN_1_AND_5_YEARS = "between-1-and-5-years"
    BETWEEN_5_AND_10_YEARS = "between-5-and-10-years"
    BETWEEN_10_AND_20_YEARS = "between-10-and-20-years"
    MORE_THAN_20_YEARS = "more-than-20-years"


class AnalystAssessmentTaxonomyBinaryReversingArchEntry(str, Enum):
    X86 = "x86"
    ARM = "arm"
    MIPS = "mips"
    POWERPC = "powerpc"


class AnalystAssessmentTaxonomyBinaryReversingExperienceEntry(str, Enum):
    LESS_THAN_1_YEAR = "less-than-1-year"
    BETWEEN_1_AND_5_YEARS = "between-1-and-5-years"
    BETWEEN_5_AND_10_YEARS = "between-5-and-10-years"
    BETWEEN_10_AND_20_YEARS = "between-10-and-20-years"
    MORE_THAN_20_YEARS = "more-than-20-years"


class AnalystAssessmentTaxonomyOsEntry(str, Enum):
    WINDOWS = "windows"
    LINUX = "linux"
    IOS = "ios"
    MACOS = "macos"
    ANDROID = "android"
    BSD = "bsd"


class AnalystAssessmentTaxonomyWebEntry(str, Enum):
    IPEX = "ipex"
    COMMON = "common"
    JS_DESOBFUSCATION = "js-desobfuscation"


class AnalystAssessmentTaxonomyWebExperienceEntry(str, Enum):
    LESS_THAN_1_YEAR = "less-than-1-year"
    BETWEEN_1_AND_5_YEARS = "between-1-and-5-years"
    BETWEEN_5_AND_10_YEARS = "between-5-and-10-years"
    BETWEEN_10_AND_20_YEARS = "between-10-and-20-years"
    MORE_THAN_20_YEARS = "more-than-20-years"


class AnalystAssessmentTaxonomyCryptoExperienceEntry(str, Enum):
    LESS_THAN_1_YEAR = "less-than-1-year"
    BETWEEN_1_AND_5_YEARS = "between-1-and-5-years"
    BETWEEN_5_AND_10_YEARS = "between-5-and-10-years"
    BETWEEN_10_AND_20_YEARS = "between-10-and-20-years"
    MORE_THAN_20_YEARS = "more-than-20-years"


class AnalystAssessmentTaxonomy(BaseModel):
    """Model for the Analyst (Self) Assessment taxonomy."""

    namespace: str = "analyst-assessment"
    description: str = """A series of assessment predicates describing the analyst capabilities to perform analysis. These assessment can be assigned by the analyst him/herself or by another party evaluating the analyst."""
    version: int = 4
    exclusive: bool = False
    predicates: List[AnalystAssessmentTaxonomyPredicate] = []
    experience_entries: List[AnalystAssessmentTaxonomyExperienceEntry] = []
    binary_reversing_arch_entries: List[AnalystAssessmentTaxonomyBinaryReversingArchEntry] = []
    binary_reversing_experience_entries: List[AnalystAssessmentTaxonomyBinaryReversingExperienceEntry] = []
    os_entries: List[AnalystAssessmentTaxonomyOsEntry] = []
    web_entries: List[AnalystAssessmentTaxonomyWebEntry] = []
    web_experience_entries: List[AnalystAssessmentTaxonomyWebExperienceEntry] = []
    crypto_experience_entries: List[AnalystAssessmentTaxonomyCryptoExperienceEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
