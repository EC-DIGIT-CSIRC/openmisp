"""Taxonomy model for Interactive Cyber Training - Training Setup."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InteractiveCyberTrainingTrainingSetupTaxonomyPredicate(str, Enum):
    SCORING = "scoring"
    ROLES = "roles"
    TRAINING_MODE = "training-mode"
    CUSTOMIZATION_LEVEL = "customization-level"


class InteractiveCyberTrainingTrainingSetupTaxonomyScoringEntry(str, Enum):
    NO_SCORING = "no-scoring"
    ASSESSMENT_STATIC = "assessment-static"
    ASSESSMENT_DYNAMIC = "assessment-dynamic"
    AWARDING_MANUAL = "awarding-manual"
    AWARDING_AUTOMATIC = "awarding-automatic"
    AWARDING_MIXED = "awarding-mixed"


class InteractiveCyberTrainingTrainingSetupTaxonomyRolesEntry(str, Enum):
    NO_SPECIFIC_ROLE = "no-specific-role"
    TRANSPARENT_TEAM_OBSERVER_WATCHER = "transparent-team-observer-watcher"
    WHITE_TEAM_TRAINER_INSTRUCTOR = "white-team-trainer-instructor"
    GREEN_TEAM_ORGANIZER_ADMIN = "green-team-organizer-admin"
    RED_TEAM_ATTACKER = "red-team-attacker"
    BLUE_TEAM_DEFENDER = "blue-team-defender"
    GRAY_TEAM_BYSTANDER = "gray-team-bystander"
    YELLOW_TEAM_INSIDER = "yellow-team-insider"
    PURPLE_TEAM_BRIDGE = "purple-team-bridge"


class InteractiveCyberTrainingTrainingSetupTaxonomyTrainingModeEntry(str, Enum):
    SINGLE = "single"
    TEAM = "team"
    CROSS_GROUP = "cross-group"


class InteractiveCyberTrainingTrainingSetupTaxonomyCustomizationLevelEntry(str, Enum):
    GENERAL = "general"
    SPECIFIC = "specific"
    INDIVIDUAL = "individual"


class InteractiveCyberTrainingTrainingSetupTaxonomy(BaseModel):
    """Model for the Interactive Cyber Training - Training Setup taxonomy."""

    namespace: str = "interactive-cyber-training-training-setup"
    description: str = """The training setup further describes the training itself with the scoring, roles, the training mode as well as the customization level."""
    version: int = 1
    exclusive: bool = False
    predicates: List[InteractiveCyberTrainingTrainingSetupTaxonomyPredicate] = []
    scoring_entries: List[InteractiveCyberTrainingTrainingSetupTaxonomyScoringEntry] = []
    roles_entries: List[InteractiveCyberTrainingTrainingSetupTaxonomyRolesEntry] = []
    training_mode_entries: List[InteractiveCyberTrainingTrainingSetupTaxonomyTrainingModeEntry] = []
    customization_level_entries: List[InteractiveCyberTrainingTrainingSetupTaxonomyCustomizationLevelEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
