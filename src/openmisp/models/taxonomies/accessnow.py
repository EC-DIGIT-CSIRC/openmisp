"""Taxonomy model for accessnow."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class AccessnowTaxonomyPredicate(str, Enum):
    ANTI_CORRUPTION_TRANSPARENCY = "anti-corruption-transparency"
    ANTI_WAR_VIOLENCE = "anti-war-violence"
    CULTURE = "culture"
    ECONOMIC_CHANGE = "economic-change"
    EDUCATION = "education"
    ELECTION_MONITORING = "election-monitoring"
    ENVIRONMENT = "environment"
    FREEDOM_EXPRESSION = "freedom-expression"
    FREEDOM_TOOL_DEVELOPMENT = "freedom-tool-development"
    FUNDING = "funding"
    HEALTH = "health"
    HUMAN_RIGHTS = "human-rights"
    INTERNET_TELECOM = "internet-telecom"
    LGBT_GENDER_SEXUALITY = "lgbt-gender-sexuality"
    POLICY = "policy"
    POLITICS = "politics"
    PRIVACY = "privacy"
    RAPID_RESPONSE = "rapid-response"
    REFUGEES = "refugees"
    SECURITY = "security"
    WOMENS_RIGHT = "womens-right"
    YOUTH_RIGHTS = "youth-rights"


class AccessnowTaxonomy(BaseModel):
    """Model for the accessnow taxonomy."""

    namespace: str = "accessnow"
    description: str = (
        """Access Now classification to classify an issue (such as security, human rights, youth rights)."""
    )
    version: int = 3
    exclusive: bool = False
    predicates: List[AccessnowTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
