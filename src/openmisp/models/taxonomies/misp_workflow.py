"""Taxonomy model for MISP workflow."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class MispWorkflowTaxonomyPredicate(str, Enum):
    ACTION_TAKEN = "action-taken"
    ANALYSIS = "analysis"
    MUTABILITY = "mutability"
    RUN = "run"


class MispWorkflowTaxonomyActionTakenEntry(str, Enum):
    IDS_FLAG_REMOVED = "ids-flag-removed"
    IDS_FLAG_ADDED = "ids-flag-added"
    PUSHED_TO_ZMQ = "pushed-to-zmq"
    EMAIL_SENT = "email-sent"
    WEBHOOK_TRIGGERED = "webhook-triggered"
    EXECUTION_STOPPED = "execution-stopped"


class MispWorkflowTaxonomyAnalysisEntry(str, Enum):
    FALSE_POSITIVE = "false-positive"
    HIGHLY_LIKELY_POSITIVE = "highly-likely-positive"
    KNOWN_FILE_HASH = "known-file-hash"


class MispWorkflowTaxonomyMutabilityEntry(str, Enum):
    ALLOWED = "allowed"


class MispWorkflowTaxonomyRunEntry(str, Enum):
    ALLOWED = "allowed"


class MispWorkflowTaxonomy(BaseModel):
    """Model for the MISP workflow taxonomy."""

    namespace: str = "misp-workflow"
    description: str = """MISP workflow taxonomy to support result of workflow execution."""
    version: int = 3
    exclusive: bool = False
    predicates: List[MispWorkflowTaxonomyPredicate] = []
    action_taken_entries: List[MispWorkflowTaxonomyActionTakenEntry] = []
    analysis_entries: List[MispWorkflowTaxonomyAnalysisEntry] = []
    mutability_entries: List[MispWorkflowTaxonomyMutabilityEntry] = []
    run_entries: List[MispWorkflowTaxonomyRunEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
