"""Taxonomy model for collaborative intelligence support language."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CollaborativeIntelligenceTaxonomyPredicate(str, Enum):
    REQUEST = "request"


class CollaborativeIntelligenceTaxonomyRequestEntry(str, Enum):
    SAMPLE = "sample"
    EXTRACTED_MALWARE_CONFIG = "extracted-malware-config"
    DEOBFUSCATED_SAMPLE = "deobfuscated-sample"
    MORE_SAMPLES = "more-samples"
    RELATED_SAMPLES = "related-samples"
    STATIC_ANALYSIS = "static-analysis"
    DETECTION_SIGNATURE = "detection-signature"
    CONTEXT = "context"
    ABUSE_CONTACT = "abuse-contact"
    HISTORICAL_INFORMATION = "historical-information"
    COMPLEMENTARY_VALIDATION = "complementary-validation"
    TARGET_INFORMATION = "target-information"
    REQUEST_ANALYSIS = "request-analysis"
    MORE_INFORMATION = "more-information"


class CollaborativeIntelligenceTaxonomy(BaseModel):
    """Model for the collaborative intelligence support language taxonomy."""

    namespace: str = "collaborative-intelligence"
    description: str = """Collaborative intelligence support language is a common language to support analysts to perform their analysis to get crowdsourced support when using threat intelligence sharing platform like MISP. The objective of this language is to advance collaborative analysis and to share earlier than later."""
    version: int = 3
    exclusive: bool = False
    predicates: List[CollaborativeIntelligenceTaxonomyPredicate] = []
    request_entries: List[CollaborativeIntelligenceTaxonomyRequestEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
