"""Taxonomy model for Failure mode in machine learning.."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class FailureModeInMachineLearningTaxonomyPredicate(str, Enum):
    INTENTIONALLY_MOTIVATED_FAILURES_SUMMARY = "intentionally-motivated-failures-summary"
    UNINTENDED_FAILURES_SUMMARY = "unintended-failures-summary"


class FailureModeInMachineLearningTaxonomyIntentionallyMotivatedFailuresSummaryEntry(str, Enum):
    T_1_PERTURBATION_ATTACK = "1-perturbation-attack"
    T_2_POISONING_ATTACK = "2-poisoning-attack"
    T_3_MODEL_INVERSION = "3-model-inversion"
    T_4_MEMBERSHIP_INFERENCE = "4-membership-inference"
    T_5_MODEL_STEALING = "5-model-stealing"
    T_6_REPROGRAMMING_ML_SYSTEM = "6-reprogramming-ML-system"
    T_7_ADVERSARIAL_EXAMPLE_IN_PHYSICAL_DOMAIN = "7-adversarial-example-in-physical-domain"
    T_8_MALICIOUS_ML_PROVIDER_RECOVERING_TRAINING_DATA = "8-malicious-ML-provider-recovering-training-data"
    T_9_ATTACKING_THE_ML_SUPPLY_CHAIN = "9-attacking-the-ML-supply-chain"
    T_10_BACKDOOR_ML = "10-backdoor-ML"
    T_10_EXPLOIT_SOFTWARE_DEPENDENCIES = "10-exploit-software-dependencies"


class FailureModeInMachineLearningTaxonomyUnintendedFailuresSummaryEntry(str, Enum):
    T_12_REWARD_HACKING = "12-reward-hacking"
    T_13_SIDE_EFFECTS = "13-side-effects"
    T_14_DISTRIBUTIONAL_SHIFTS = "14-distributional-shifts"
    T_15_NATURAL_ADVERSARIAL_EXAMPLES = "15-natural-adversarial-examples"
    T_16_COMMON_CORRUPTION = "16-common-corruption"
    T_17_INCOMPLETE_TESTING = "17-incomplete-testing"


class FailureModeInMachineLearningTaxonomy(BaseModel):
    """Model for the Failure mode in machine learning. taxonomy."""

    namespace: str = "failure-mode-in-machine-learning"
    description: str = """The purpose of this taxonomy is to jointly tabulate both the of these failure modes in a single place. Intentional failures wherein the failure is caused by an active adversary attempting to subvert the system to attain her goals – either to misclassify the result, infer private training data, or to steal the underlying algorithm. Unintentional failures wherein the failure is because an ML system produces a formally correct but completely unsafe outcome."""
    version: int = 1
    exclusive: bool = False
    predicates: List[FailureModeInMachineLearningTaxonomyPredicate] = []
    intentionally_motivated_failures_summary_entries: List[
        FailureModeInMachineLearningTaxonomyIntentionallyMotivatedFailuresSummaryEntry
    ] = []
    unintended_failures_summary_entries: List[FailureModeInMachineLearningTaxonomyUnintendedFailuresSummaryEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
