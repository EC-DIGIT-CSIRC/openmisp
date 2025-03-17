"""Taxonomy model for targeted-threat-index."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class TargetedThreatIndexTaxonomyPredicate(str, Enum):
    TARGETING_SOPHISTICATION_BASE_VALUE = "targeting-sophistication-base-value"
    TECHNICAL_SOPHISTICATION_MULTIPLIER = "technical-sophistication-multiplier"


class TargetedThreatIndexTaxonomyTargetingSophisticationBaseValueEntry(str, Enum):
    NOT_TARGETED = "not-targeted"
    TARGETED_BUT_NOT_CUSTOMIZED = "targeted-but-not-customized"
    TARGETED_AND_POORLY_CUSTOMIZED = "targeted-and-poorly-customized"
    TARGETED_AND_CUSTOMIZED = "targeted-and-customized"
    TARGETED_AND_WELL_CUSTOMIZED = "targeted-and-well-customized"
    TARGETED_AND_HIGHLY_CUSTOMIZED_USING_SENSITIVE_DATA = "targeted-and-highly-customized-using-sensitive-data"


class TargetedThreatIndexTaxonomyTechnicalSophisticationMultiplierEntry(str, Enum):
    THE_SAMPLE_CONTAINS_NO_CODE_PROTECTION = "the-sample-contains-no code-protection"
    THE_SAMPLE_CONTAINS_A_SIMPLE_METHOD_OF_PROTECTION = "the-sample-contains-a-simple-method-of-protection"
    THE_SAMPLE_CONTAINS_MULTIPLE_MINOR_CODE_PROTECTION_TECHNIQUES = (
        "the-sample-contains-multiple-minor-code-protection-techniques"
    )
    THE_SAMPLE_CONTAINS_MINOR_CODE_PROTECTION_TECHNIQUES_PLUS_ONE_ADVANCED = (
        "the-sample-contains-minor-code-protection-techniques-plus-one-advanced"
    )
    THE_SAMPLE_CONTAINS_MULTIPLE_ADVANCED_PROTECTION_TECHNIQUES = (
        "the-sample-contains-multiple-advanced-protection-techniques"
    )


class TargetedThreatIndexTaxonomy(BaseModel):
    """Model for the targeted-threat-index taxonomy."""

    namespace: str = "targeted-threat-index"
    description: str = """The Targeted Threat Index is a metric for assigning an overall threat ranking score to email messages that deliver malware to a victim’s computer. The TTI metric was first introduced at SecTor 2013 by Seth Hardy as part of the talk “RATastrophe: Monitoring a Malware Menagerie” along with Katie Kleemola and Greg Wiseman."""
    version: int = 3
    exclusive: bool = False
    predicates: List[TargetedThreatIndexTaxonomyPredicate] = []
    targeting_sophistication_base_value_entries: List[
        TargetedThreatIndexTaxonomyTargetingSophisticationBaseValueEntry
    ] = []
    technical_sophistication_multiplier_entries: List[
        TargetedThreatIndexTaxonomyTechnicalSophisticationMultiplierEntry
    ] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
