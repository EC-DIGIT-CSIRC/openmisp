"""Taxonomy model for Exercise."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ExerciseTaxonomyPredicate(str, Enum):
    CYBER_EUROPE = "cyber-europe"
    CYBER_STORM = "cyber-storm"
    LOCKED_SHIELDS = "locked-shields"
    LUKEX = "lukex"
    CYBER_COALITION = "cyber-coalition"
    PACE = "pace"
    CYBER_SOPEX = "cyber-sopex"
    GENERIC = "generic"


class ExerciseTaxonomyCyberEuropeEntry(str, Enum):
    T_2024 = "2024"
    T_2022 = "2022"
    T_2018 = "2018"
    T_2016 = "2016"


class ExerciseTaxonomyCyberStormEntry(str, Enum):
    SPRING_2018 = "spring-2018"


class ExerciseTaxonomyLockedShieldsEntry(str, Enum):
    T_2017 = "2017"
    T_2018 = "2018"
    T_2019 = "2019"
    T_2020 = "2020"
    T_2021 = "2021"
    T_2022 = "2022"
    T_2023 = "2023"
    T_2024 = "2024"


class ExerciseTaxonomyLukexEntry(str, Enum):
    T_2020 = "2020"


class ExerciseTaxonomyCyberCoalitionEntry(str, Enum):
    T_2017 = "2017"
    T_2018 = "2018"
    T_2019 = "2019"
    T_2020 = "2020"
    T_2021 = "2021"


class ExerciseTaxonomyPaceEntry(str, Enum):
    T_2017 = "2017"
    T_2018 = "2018"


class ExerciseTaxonomyCyberSopexEntry(str, Enum):
    T_2019 = "2019"
    T_2018 = "2018"
    T_2020 = "2020"
    T_2021 = "2021"


class ExerciseTaxonomyGenericEntry(str, Enum):
    COMCHECK = "comcheck"
    RED_TEAMING = "red-teaming"


class ExerciseTaxonomy(BaseModel):
    """Model for the Exercise taxonomy."""

    namespace: str = "exercise"
    description: str = (
        """Exercise is a taxonomy to describe if the information is part of one or more cyber or crisis exercise."""
    )
    version: int = 12
    exclusive: bool = False
    predicates: List[ExerciseTaxonomyPredicate] = []
    cyber_europe_entries: List[ExerciseTaxonomyCyberEuropeEntry] = []
    cyber_storm_entries: List[ExerciseTaxonomyCyberStormEntry] = []
    locked_shields_entries: List[ExerciseTaxonomyLockedShieldsEntry] = []
    lukex_entries: List[ExerciseTaxonomyLukexEntry] = []
    cyber_coalition_entries: List[ExerciseTaxonomyCyberCoalitionEntry] = []
    pace_entries: List[ExerciseTaxonomyPaceEntry] = []
    cyber_sopex_entries: List[ExerciseTaxonomyCyberSopexEntry] = []
    generic_entries: List[ExerciseTaxonomyGenericEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
