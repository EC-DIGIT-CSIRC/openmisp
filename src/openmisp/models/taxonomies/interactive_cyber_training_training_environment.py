"""Taxonomy model for Interactive Cyber Training - Training Environment."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InteractiveCyberTrainingTrainingEnvironmentTaxonomyPredicate(str, Enum):
    TRAINING_TYPE = "training-type"
    SCENARIO = "scenario"


class InteractiveCyberTrainingTrainingEnvironmentTaxonomyTrainingTypeEntry(str, Enum):
    TABLETOP_GAME_SPEECH = "tabletop-game-speech"
    TABLETOP_GAME_TEXT = "tabletop-game-text"
    TABLETOP_GAME_MULTIMEDIA = "tabletop-game-multimedia"
    CAPTURE_THE_FLAG_QUIZ = "capture-the-flag-quiz"
    CAPTURE_THE_FLAG_JEOPARDY = "capture-the-flag-jeopardy"
    CAPTURE_THE_FLAG_ATTACK = "capture-the-flag-attack"
    CAPTURE_THE_FLAG_DEFENCE = "capture-the-flag-defence"
    CAPTURE_THE_FLAG_ATTACK_DEFENCE = "capture-the-flag-attack-defence"
    CYBER_TRAINING_RANGE_CLASSROOM_PRACTICE = "cyber-training-range-classroom-practice"
    CYBER_TRAINING_RANGE_SINGLE_TEAM_TRAINING = "cyber-training-range-single-team-training"
    CYBER_TRAINING_RANGE_MULTIPLE_TEAM_TRAINING = "cyber-training-range-multiple-team-training"
    PROJECT_APPROACH = "project-approach"


class InteractiveCyberTrainingTrainingEnvironmentTaxonomyScenarioEntry(str, Enum):
    SUPERVISED = "supervised"
    UNSUPERVISED = "unsupervised"
    FREE_MULTIPLE_CHOICE = "free-multiple-choice"
    PROBLEM_DRIVEN = "problem-driven"
    STORYLINE_DRIVEN = "storyline-driven"
    CHALLENGES_TARGET_NETWORK = "challenges-target-network"
    CHALLENGES_TARGET_HOST = "challenges-target-host"
    CHALLENGES_TARGET_APPLICATION = "challenges-target-application"
    CHALLENGES_TARGET_PROTOCOL = "challenges-target-protocol"
    CHALLENGES_TARGET_DATA = "challenges-target-data"
    CHALLENGES_TARGET_PERSON = "challenges-target-person"
    CHALLENGES_TARGET_PHYSICAL = "challenges-target-physical"
    CHALLENGES_TYPE_FOOT_PRINTING = "challenges-type-foot-printing"
    CHALLENGES_TYPE_SCANNING = "challenges-type-scanning"
    CHALLENGES_TYPE_ENUMERATION = "challenges-type-enumeration"
    CHALLENGES_TYPE_PIVOTING = "challenges-type-pivoting"
    CHALLENGES_TYPE_EXPLOITATION = "challenges-type-exploitation"
    CHALLENGES_TYPE_PRIVILEGE_ESCALATION = "challenges-type-privilege-escalation"
    CHALLENGES_TYPE_COVERING_TRACKS = "challenges-type-covering-tracks"
    CHALLENGES_TYPE_MAINTAINING = "challenges-type-maintaining"


class InteractiveCyberTrainingTrainingEnvironmentTaxonomy(BaseModel):
    """Model for the Interactive Cyber Training - Training Environment taxonomy."""

    namespace: str = "interactive-cyber-training-training-environment"
    description: str = """The training environment details the environment around the training, consisting of training type and scenario."""
    version: int = 1
    exclusive: bool = False
    predicates: List[InteractiveCyberTrainingTrainingEnvironmentTaxonomyPredicate] = []
    training_type_entries: List[InteractiveCyberTrainingTrainingEnvironmentTaxonomyTrainingTypeEntry] = []
    scenario_entries: List[InteractiveCyberTrainingTrainingEnvironmentTaxonomyScenarioEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
