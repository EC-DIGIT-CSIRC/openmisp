"""Taxonomy model for workflow to support analysis."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class WorkflowTaxonomyPredicate(str, Enum):
    TODO = "todo"
    STATE = "state"


class WorkflowTaxonomyTodoEntry(str, Enum):
    EXPANSION = "expansion"
    REVIEW = "review"
    REVIEW_FOR_PRIVACY = "review-for-privacy"
    REVIEW_BEFORE_PUBLICATION = "review-before-publication"
    RELEASE_REQUESTED = "release-requested"
    REVIEW_FOR_FALSE_POSITIVE = "review-for-false-positive"
    REVIEW_THE_SOURCE_CREDIBILITY = "review-the-source-credibility"
    ADD_MISSING_MISP_GALAXY_CLUSTER_VALUES = "add-missing-misp-galaxy-cluster-values"
    CREATE_MISSING_MISP_GALAXY_CLUSTER = "create-missing-misp-galaxy-cluster"
    CREATE_MISSING_MISP_GALAXY_CLUSTER_RELATIONSHIP = "create-missing-misp-galaxy-cluster-relationship"
    CREATE_MISSING_MISP_GALAXY = "create-missing-misp-galaxy"
    CREATE_MISSING_RELATIONSHIP = "create-missing-relationship"
    ADD_CONTEXT = "add-context"
    ADD_TAGGING = "add-tagging"
    CHECK_PASSIVE_DNS_FOR_SHARED_HOSTING = "check-passive-dns-for-shared-hosting"
    REVIEW_CLASSIFICATION = "review-classification"
    REVIEW_THE_GRAMMAR = "review-the-grammar"
    DO_NOT_DELETE = "do-not-delete"
    ADD_MITRE_ATTACK_CLUSTER = "add-mitre-attack-cluster"
    ADDITIONAL_TASK = "additional-task"
    CREATE_EVENT = "create-event"
    PRESERVE_EVIDENCE = "preserve-evidence"
    REVIEW_RELEVANCE = "review-relevance"
    REVIEW_COMPLETENESS = "review-completeness"
    REVIEW_ACCURACY = "review-accuracy"
    REVIEW_QUALITY = "review-quality"


class WorkflowTaxonomyStateEntry(str, Enum):
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"
    DRAFT = "draft"
    ONGOING = "ongoing"
    REJECTED = "rejected"
    RELEASE = "release"


class WorkflowTaxonomy(BaseModel):
    """Model for the workflow to support analysis taxonomy."""

    namespace: str = "workflow"
    description: str = """Workflow support language is a common language to support intelligence analysts to perform their analysis on data and information."""
    version: int = 14
    exclusive: bool = False
    predicates: List[WorkflowTaxonomyPredicate] = []
    todo_entries: List[WorkflowTaxonomyTodoEntry] = []
    state_entries: List[WorkflowTaxonomyStateEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
