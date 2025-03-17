"""Taxonomy model for Continuous Monitoring Resolution Category."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class UseCaseApplicabilityTaxonomyPredicate(str, Enum):
    ANNOUNCED_ADMINISTRATIVE_USER_ACTION = "announced-administrative/user-action"
    UNANNOUNCED_ADMINISTRATIVE_USER_ACTION = "unannounced-administrative/user-action"
    LOG_MANAGEMENT_RULE_CONFIGURATION_ERROR = "log-management-rule-configuration-error"
    DETECTION_DEVICE_RULE_CONFIGURATION_ERROR = "detection-device/rule-configuration-error"
    BAD_IOC_RULE_PATTERN_VALUE = "bad-IOC/rule-pattern-value"
    TEST_ALERT = "test-alert"
    CONFIRMED_ATTACK_WITH_IR_ACTIONS = "confirmed-attack-with-IR-actions"
    CONFIRMED_ATTACK_ATTEMPT_WITHOUT_IR_ACTIONS = "confirmed-attack-attempt-without-IR-actions"


class UseCaseApplicabilityTaxonomy(BaseModel):
    """Model for the Continuous Monitoring Resolution Category taxonomy."""

    namespace: str = "use-case-applicability"
    description: str = """The Use Case Applicability categories reflect standard resolution categories, to clearly display alerting rule configuration problems."""
    version: int = 1
    exclusive: bool = False
    predicates: List[UseCaseApplicabilityTaxonomyPredicate] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
