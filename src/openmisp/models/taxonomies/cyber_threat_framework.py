"""Taxonomy model for Cyber Threat Framework."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CyberThreatFrameworkTaxonomyPredicate(str, Enum):
    PREPARATION = "Preparation"
    ENGAGEMENT = "Engagement"
    PRESENCE = "Presence"
    EFFECT_CONSEQUENCE = "Effect/Consequence"


class CyberThreatFrameworkTaxonomyPreparationEntry(str, Enum):
    PLAN_ACTIVITY = "plan-activity"
    CONDUCT_RESEARCH_AND_ANALYSIS = "conduct-research-and-analysis"
    DEVELOP_RESOURCE_AND_CAPABILITIES = "develop-resource-and-capabilities"
    ACQUIRE_VICTIM_AND_SPECIFIC_KNOWLEDGE = "acquire-victim-and-specific-knowledge"
    COMPLETE_PREPARATIONS = "complete-preparations"


class CyberThreatFrameworkTaxonomyEngagementEntry(str, Enum):
    DEPLOY_CAPABILITY = "deploy-capability"
    INTERACT_WITH_INTENDED_VICTIM = "interact-with-intended-victim"
    EXPLOIT_VULNERABILITIES = "exploit-vulnerabilities"
    DELIVER_MALICIOUS_CAPABILITIES = "deliver-malicious-capabilities"


class CyberThreatFrameworkTaxonomyPresenceEntry(str, Enum):
    ESTABLISH_CONTROLLED_ACCESS = "establish-controlled-access"
    HIDE = "hide"
    EXPAND_PRESENCE = "expand-presence"
    REFINE_FOCUS_OF_ACTIVITY = "refine-focus-of-activity"
    ESTABLISH_PERSISTENCE = "establish-persistence"


class CyberThreatFrameworkTaxonomyEffectConsequenceEntry(str, Enum):
    ENABLE_OTHER_OPERATIONS = "enable-other-operations"
    DENY_ACCESS = "deny-access"
    EXTRACT_DATA = "extract-data"
    ALTER_DATA_AND_OR_COMPUTER_NETWORK_OR_SYSTEM_BEHAVIOR = "alter-data-and-or-computer-network-or-system-behavior"
    DESTROY_HARDWARE_SOFTWARE_OR_DATA = "destroy-hardware-software-or-data"


class CyberThreatFrameworkTaxonomy(BaseModel):
    """Model for the Cyber Threat Framework taxonomy."""

    namespace: str = "cyber-threat-framework"
    description: str = """Cyber Threat Framework was developed by the US Government to enable consistent characterization and categorization of cyber threat events, and to identify trends or changes in the activities of cyber adversaries. https://www.dni.gov/index.php/cyber-threat-framework"""
    version: int = 2
    exclusive: bool = False
    predicates: List[CyberThreatFrameworkTaxonomyPredicate] = []
    preparation_entries: List[CyberThreatFrameworkTaxonomyPreparationEntry] = []
    engagement_entries: List[CyberThreatFrameworkTaxonomyEngagementEntry] = []
    presence_entries: List[CyberThreatFrameworkTaxonomyPresenceEntry] = []
    effect_consequence_entries: List[CyberThreatFrameworkTaxonomyEffectConsequenceEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
