"""Taxonomy model for Interactive Cyber Training - Technical Setup."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InteractiveCyberTrainingTechnicalSetupTaxonomyPredicate(str, Enum):
    ENVIRONMENT_STRUCTURE = "environment-structure"
    DEPLOYMENT = "deployment"
    ORCHESTRATION = "orchestration"


class InteractiveCyberTrainingTechnicalSetupTaxonomyEnvironmentStructureEntry(str, Enum):
    TABLETOP_STYLE = "tabletop-style"
    ONLINE_COLLABORATION_PLATFORM = "online-collaboration-platform"
    ONLINE_E_LEARNING_PLATFORM = "online-e-learning-platform"
    HOSTING = "hosting"
    SIMULATED_NETWORK_INFRASTRUCTURE = "simulated-network-infrastructure"
    EMULATED_NETWORK_INFRASTRUCTURE = "emulated-network-infrastructure"
    REAL_NETWORK_INFRASTRUCTURE = "real-network-infrastructure"


class InteractiveCyberTrainingTechnicalSetupTaxonomyDeploymentEntry(str, Enum):
    PHYSICAL_ON_PREMISE = "physical-on-premise"
    VIRTUAL_ON_PREMISE = "virtual-on-premise"
    CLOUD = "cloud"


class InteractiveCyberTrainingTechnicalSetupTaxonomyOrchestrationEntry(str, Enum):
    NONE_AUTOMATION = "none-automation"
    PARTIALLY_AUTOMATION = "partially-automation"
    COMPLETE_AUTOMATION = "complete-automation"
    PORTABILITY_MISCELLANEOUS = "portability-miscellaneous"
    PORTABILITY_EXCHANGENABLE_FORMAT = "portability-exchangenable-format"
    MAINTAINABILITY_MODIFIABILITY = "maintainability-modifiability"
    MAINTAINABILITY_MODULARITY = "maintainability-modularity"
    COMPATIBILITY = "compatibility"


class InteractiveCyberTrainingTechnicalSetupTaxonomy(BaseModel):
    """Model for the Interactive Cyber Training - Technical Setup taxonomy."""

    namespace: str = "interactive-cyber-training-technical-setup"
    description: str = """The technical setup consists of environment structure, deployment, and orchestration."""
    version: int = 1
    exclusive: bool = False
    predicates: List[InteractiveCyberTrainingTechnicalSetupTaxonomyPredicate] = []
    environment_structure_entries: List[InteractiveCyberTrainingTechnicalSetupTaxonomyEnvironmentStructureEntry] = []
    deployment_entries: List[InteractiveCyberTrainingTechnicalSetupTaxonomyDeploymentEntry] = []
    orchestration_entries: List[InteractiveCyberTrainingTechnicalSetupTaxonomyOrchestrationEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
