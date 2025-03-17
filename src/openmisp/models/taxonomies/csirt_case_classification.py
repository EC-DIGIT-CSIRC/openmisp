"""Taxonomy model for csirt_case_classification."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CsirtCaseClassificationTaxonomyPredicate(str, Enum):
    INCIDENT_CATEGORY = "incident-category"
    CRITICALITY_CLASSIFICATION = "criticality-classification"
    SENSITIVITY_CLASSIFICATION = "sensitivity-classification"


class CsirtCaseClassificationTaxonomyIncidentCategoryEntry(str, Enum):
    DOS = "DOS"
    FORENSICS = "forensics"
    COMPROMISED_INFORMATION = "compromised-information"
    COMPROMISED_ASSET = "compromised-asset"
    UNLAWFUL_ACTIVITY = "unlawful-activity"
    INTERNAL_HACKING = "internal-hacking"
    EXTERNAL_HACKING = "external-hacking"
    MALWARE = "malware"
    EMAIL = "email"
    CONSULTING = "consulting"
    POLICY_VIOLATION = "policy-violation"


class CsirtCaseClassificationTaxonomyCriticalityClassificationEntry(str, Enum):
    T_1 = "1"
    T_2 = "2"
    T_3 = "3"


class CsirtCaseClassificationTaxonomySensitivityClassificationEntry(str, Enum):
    T_1 = "1"
    T_2 = "2"
    T_3 = "3"


class CsirtCaseClassificationTaxonomy(BaseModel):
    """Model for the csirt_case_classification taxonomy."""

    namespace: str = "csirt_case_classification"
    description: str = """It is critical that the CSIRT provide consistent and timely response to the customer, and that sensitive information is handled appropriately.  This document provides the guidelines needed for CSIRT Incident Managers (IM) to classify the case category, criticality level, and sensitivity level for each CSIRT case.  This information will be entered into the Incident Tracking System (ITS) when a case is created.  Consistent case classification is required for the CSIRT to provide accurate reporting to management on a regular basis.  In addition, the classifications will provide CSIRT IM’s with proper case handling procedures and will form the basis of SLA’s between the CSIRT and other Company departments."""
    version: int = 1
    exclusive: bool = False
    predicates: List[CsirtCaseClassificationTaxonomyPredicate] = []
    incident_category_entries: List[CsirtCaseClassificationTaxonomyIncidentCategoryEntry] = []
    criticality_classification_entries: List[CsirtCaseClassificationTaxonomyCriticalityClassificationEntry] = []
    sensitivity_classification_entries: List[CsirtCaseClassificationTaxonomySensitivityClassificationEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
