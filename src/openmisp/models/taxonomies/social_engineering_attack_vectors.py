"""Taxonomy model for Social Engineering Attack Vectors."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class SocialEngineeringAttackVectorsTaxonomyPredicate(str, Enum):
    TECHNICAL = "technical"
    NON_TECHNICAL = "non-technical"


class SocialEngineeringAttackVectorsTaxonomyTechnicalEntry(str, Enum):
    VISHING = "vishing"
    SPEAR_PHISHING = "spear-phishing"
    INTERESTING_SOFTWARE = "interesting-software"
    BAITING = "baiting"
    WATERHOLING = "waterholing"
    PHISHING_AND_TROJAN_EMAIL = "phishing-and-trojan-email"
    SPAM_EMAIL = "spam-email"
    POPUP_WINDOW = "popup-window"
    TAILGATING = "tailgating"


class SocialEngineeringAttackVectorsTaxonomyNonTechnicalEntry(str, Enum):
    PRETEXTING_IMPERSONATION = "pretexting-impersonation"
    HOAXING = "hoaxing"
    AUTHORITATIVE_VOICE = "authoritative-voice"
    TECHNICAL_EXPERT = "technical-expert"
    SMUDGE_ATTACK = "smudge-attack"
    DUMPSER_DIVING = "dumpser-diving"
    SHOULDER_SURFING = "shoulder-surfing"
    SPYING = "spying"
    SUPPORT_STAFF = "support-staff"


class SocialEngineeringAttackVectorsTaxonomy(BaseModel):
    """Model for the Social Engineering Attack Vectors taxonomy."""

    namespace: str = "social-engineering-attack-vectors"
    description: str = """Attack vectors used in social engineering as described in 'A Taxonomy of Social Engineering Defense Mechanisms' by Dalal Alharthi and others."""
    version: int = 1
    exclusive: bool = False
    predicates: List[SocialEngineeringAttackVectorsTaxonomyPredicate] = []
    technical_entries: List[SocialEngineeringAttackVectorsTaxonomyTechnicalEntry] = []
    non_technical_entries: List[SocialEngineeringAttackVectorsTaxonomyNonTechnicalEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
