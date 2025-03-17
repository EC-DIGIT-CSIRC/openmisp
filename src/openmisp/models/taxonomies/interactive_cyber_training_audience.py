"""Taxonomy model for Interactive Cyber Training - Audience."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InteractiveCyberTrainingAudienceTaxonomyPredicate(str, Enum):
    SECTOR = "sector"
    PURPOSE = "purpose"
    PROFICIENCY_LEVEL = "proficiency-level"
    TARGET_AUDIENCE = "target-audience"


class InteractiveCyberTrainingAudienceTaxonomySectorEntry(str, Enum):
    ACADEMIC_SCHOOL = "academic-school"
    ACADEMIC_UNIVERSITY = "academic-university"
    PUBLIC_GOVERNMENT = "public-government"
    PUBLIC_AUTHORITIES = "public-authorities"
    PUBLIC_NGO = "public-ngo"
    PUBLIC_MILITARY = "public-military"
    PRIVATE = "private"


class InteractiveCyberTrainingAudienceTaxonomyPurposeEntry(str, Enum):
    AWARENESS = "awareness"
    SKILLS = "skills"
    COLLABORATION = "collaboration"
    COMMUNICATION = "communication"
    LEADERSHIP = "leadership"


class InteractiveCyberTrainingAudienceTaxonomyProficiencyLevelEntry(str, Enum):
    BEGINNER = "beginner"
    PROFESSIONAL = "professional"
    EXPERT = "expert"


class InteractiveCyberTrainingAudienceTaxonomyTargetAudienceEntry(str, Enum):
    STUDENT_TRAINEE = "student-trainee"
    IT_USER = "it-user"
    IT_PROFESSIONAL = "it-professional"
    IT_SPECIALIST = "it-specialist"
    MANAGEMENT = "management"


class InteractiveCyberTrainingAudienceTaxonomy(BaseModel):
    """Model for the Interactive Cyber Training - Audience taxonomy."""

    namespace: str = "interactive-cyber-training-audience"
    description: str = """Describes the target of cyber training and education."""
    version: int = 1
    exclusive: bool = False
    predicates: List[InteractiveCyberTrainingAudienceTaxonomyPredicate] = []
    sector_entries: List[InteractiveCyberTrainingAudienceTaxonomySectorEntry] = []
    purpose_entries: List[InteractiveCyberTrainingAudienceTaxonomyPurposeEntry] = []
    proficiency_level_entries: List[InteractiveCyberTrainingAudienceTaxonomyProficiencyLevelEntry] = []
    target_audience_entries: List[InteractiveCyberTrainingAudienceTaxonomyTargetAudienceEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
