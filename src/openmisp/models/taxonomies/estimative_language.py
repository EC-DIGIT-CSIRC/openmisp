"""Taxonomy model for Estimative languages."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class EstimativeLanguageTaxonomyPredicate(str, Enum):
    LIKELIHOOD_PROBABILITY = "likelihood-probability"
    CONFIDENCE_IN_ANALYTIC_JUDGMENT = "confidence-in-analytic-judgment"


class EstimativeLanguageTaxonomyLikelihoodProbabilityEntry(str, Enum):
    ALMOST_NO_CHANCE = "almost-no-chance"
    VERY_UNLIKELY = "very-unlikely"
    UNLIKELY = "unlikely"
    ROUGHLY_EVEN_CHANCE = "roughly-even-chance"
    LIKELY = "likely"
    VERY_LIKELY = "very-likely"
    ALMOST_CERTAIN = "almost-certain"


class EstimativeLanguageTaxonomyConfidenceInAnalyticJudgmentEntry(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"


class EstimativeLanguageTaxonomy(BaseModel):
    """Model for the Estimative languages taxonomy."""

    namespace: str = "estimative-language"
    description: str = """Estimative language to describe quality and credibility of underlying sources, data, and methodologies based Intelligence Community Directive 203 (ICD 203) and JP 2-0, Joint Intelligence"""
    version: int = 5
    exclusive: bool = False
    predicates: List[EstimativeLanguageTaxonomyPredicate] = []
    likelihood_probability_entries: List[EstimativeLanguageTaxonomyLikelihoodProbabilityEntry] = []
    confidence_in_analytic_judgment_entries: List[EstimativeLanguageTaxonomyConfidenceInAnalyticJudgmentEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
