"""Taxonomy model for acs-marking."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class AcsMarkingTaxonomyPredicate(str, Enum):
    PRIVILEGE_ACTION = "privilege_action"
    CLASSIFICATION = "classification"
    FORMAL_DETERMINATION = "formal_determination"
    CAVEAT = "caveat"
    SENSITIVITY = "sensitivity"
    SHAREABILITY = "shareability"
    ENTITY = "entity"


class AcsMarkingTaxonomyPrivilegeActionEntry(str, Enum):
    DSPLY = "DSPLY"
    IDSRC = "IDSRC"
    TENOT = "TENOT"
    NETDEF = "NETDEF"
    LEGAL = "LEGAL"
    INTEL = "INTEL"
    TEARLINE = "TEARLINE"
    OPACTION = "OPACTION"
    REQUEST = "REQUEST"
    ANONYMOUSACCESS = "ANONYMOUSACCESS"
    CISAUSES = "CISAUSES"


class AcsMarkingTaxonomyClassificationEntry(str, Enum):
    U = "U"
    C = "C"
    S = "S"
    TS = "TS"


class AcsMarkingTaxonomyFormalDeterminationEntry(str, Enum):
    AIS = "AIS"
    FOUO = "FOUO"
    NF = "NF"
    PII_NECESSARY_TO_UNDERSTAND_THREAT = "PII-NECESSARY-TO-UNDERSTAND-THREAT"
    NO_PII_PRESENT = "NO-PII-PRESENT"
    PUBREL = "PUBREL"
    INFORMATION_DIRECTLY_RELATED_TO_CYBERSECURITY_THREAT = "INFORMATION-DIRECTLY-RELATED-TO-CYBERSECURITY-THREAT"


class AcsMarkingTaxonomyCaveatEntry(str, Enum):
    FISA = "FISA"
    POSSIBLEPII = "POSSIBLEPII"
    CISAPROPRIETARY = "CISAPROPRIETARY"


class AcsMarkingTaxonomySensitivityEntry(str, Enum):
    NTOC_DHS_ECYBER_SVC_SHARE_NSA_NSA = "NTOC_DHS_ECYBER_SVC_SHARE.NSA.NSA"
    PCII = "PCII"
    LES = "LES"
    INT = "INT"
    PII = "PII"
    PR = "PR"
    TEI = "TEI"


class AcsMarkingTaxonomyShareabilityEntry(str, Enum):
    NCC = "NCC"
    EM = "EM"
    LE = "LE"
    IC = "IC"


class AcsMarkingTaxonomyEntityEntry(str, Enum):
    MIL = "MIL"
    GOV = "GOV"
    CTR = "CTR"
    SVR = "SVR"
    SVC = "SVC"
    DEV = "DEV"
    NET = "NET"


class AcsMarkingTaxonomy(BaseModel):
    """Model for the acs-marking taxonomy."""

    namespace: str = "acs-marking"
    description: str = """The Access Control Specification (ACS) marking type defines the object types required to implement automated access control systems based on the relevant policies governing sharing between participants."""
    version: int = 1
    exclusive: bool = False
    predicates: List[AcsMarkingTaxonomyPredicate] = []
    privilege_action_entries: List[AcsMarkingTaxonomyPrivilegeActionEntry] = []
    classification_entries: List[AcsMarkingTaxonomyClassificationEntry] = []
    formal_determination_entries: List[AcsMarkingTaxonomyFormalDeterminationEntry] = []
    caveat_entries: List[AcsMarkingTaxonomyCaveatEntry] = []
    sensitivity_entries: List[AcsMarkingTaxonomySensitivityEntry] = []
    shareability_entries: List[AcsMarkingTaxonomyShareabilityEntry] = []
    entity_entries: List[AcsMarkingTaxonomyEntityEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
