"""Taxonomy model for dni-ism."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DniIsmTaxonomyPredicate(str, Enum):
    CLASSIFICATION_ALL = "classification:all"
    CLASSIFICATION_US = "classification:us"
    SCICONTROLS = "scicontrols"
    COMPLIES_WITH = "complies:with"
    ATOMICENERGYMARKINGS = "atomicenergymarkings"
    NOTICE = "notice"
    NONIC = "nonic"
    NONUSCONTROLS = "nonuscontrols"
    DISSEM = "dissem"


class DniIsmTaxonomyClassificationAllEntry(str, Enum):
    R = "R"
    C = "C"
    S = "S"
    TS = "TS"
    U = "U"


class DniIsmTaxonomyClassificationUsEntry(str, Enum):
    C = "C"
    S = "S"
    TS = "TS"
    U = "U"


class DniIsmTaxonomyScicontrolsEntry(str, Enum):
    EL = "EL"
    EL_EU = "EL-EU"
    EL_NK = "EL-NK"
    HCS = "HCS"
    HCS_O = "HCS-O"
    HCS_P = "HCS-P"
    KDK = "KDK"
    KDK_BLFH = "KDK-BLFH"
    KDK_IDIT = "KDK-IDIT"
    KDK_KAND = "KDK-KAND"
    RSV = "RSV"
    SI = "SI"
    SI_G = "SI-G"
    TK = "TK"


class DniIsmTaxonomyCompliesWithEntry(str, Enum):
    USGOV = "USGov"
    USIC = "USIC"
    USDOD = "USDOD"
    OTHER_AUTHORITY = "OtherAuthority"


class DniIsmTaxonomyAtomicenergymarkingsEntry(str, Enum):
    RD = "RD"
    RD_CNWDI = "RD-CNWDI"
    FRD = "FRD"
    DCNI = "DCNI"
    UCNI = "UCNI"
    TFNI = "TFNI"


class DniIsmTaxonomyNoticeEntry(str, Enum):
    FISA = "FISA"
    IMC = "IMC"
    CNWDI = "CNWDI"
    RD = "RD"
    FRD = "FRD"
    DS = "DS"
    LES = "LES"
    LES_NF = "LES-NF"
    DSEN = "DSEN"
    DO_D_DIST_A = "DoD-Dist-A"
    DO_D_DIST_B = "DoD-Dist-B"
    DO_D_DIST_C = "DoD-Dist-C"
    DO_D_DIST_D = "DoD-Dist-D"
    DO_D_DIST_E = "DoD-Dist-E"
    DO_D_DIST_F = "DoD-Dist-F"
    DO_D_DIST_X = "DoD-Dist-X"
    US_PERSON = "US-Person"
    PRE13526_ORCON = "pre13526ORCON"
    POC = "POC"
    COMSEC = "COMSEC"


class DniIsmTaxonomyNonicEntry(str, Enum):
    NNPI = "NNPI"
    DS = "DS"
    XD = "XD"
    ND = "ND"
    SBU = "SBU"
    SBU_NF = "SBU-NF"
    LES = "LES"
    LES_NF = "LES-NF"
    SSI = "SSI"


class DniIsmTaxonomyNonuscontrolsEntry(str, Enum):
    ATOMAL = "ATOMAL"
    BOHEMIA = "BOHEMIA"
    BALK = "BALK"


class DniIsmTaxonomyDissemEntry(str, Enum):
    RS = "RS"
    FOUO = "FOUO"
    OC = "OC"
    OC_USGOV = "OC-USGOV"
    IMC = "IMC"
    NF = "NF"
    PR = "PR"
    REL = "REL"
    RELIDO = "RELIDO"
    DSEN = "DSEN"
    FISA = "FISA"
    DISPLAYONLY = "DISPLAYONLY"


class DniIsmTaxonomy(BaseModel):
    """Model for the dni-ism taxonomy."""

    namespace: str = "dni-ism"
    description: str = """A subset of Information Security Marking Metadata ISM as required by Executive Order (EO) 13526. As described by DNI.gov as Data Encoding Specifications for Information Security Marking Metadata in Controlled Vocabulary Enumeration Values for ISM"""
    version: int = 3
    exclusive: bool = False
    predicates: List[DniIsmTaxonomyPredicate] = []
    classification_all_entries: List[DniIsmTaxonomyClassificationAllEntry] = []
    classification_us_entries: List[DniIsmTaxonomyClassificationUsEntry] = []
    scicontrols_entries: List[DniIsmTaxonomyScicontrolsEntry] = []
    complies_with_entries: List[DniIsmTaxonomyCompliesWithEntry] = []
    atomicenergymarkings_entries: List[DniIsmTaxonomyAtomicenergymarkingsEntry] = []
    notice_entries: List[DniIsmTaxonomyNoticeEntry] = []
    nonic_entries: List[DniIsmTaxonomyNonicEntry] = []
    nonuscontrols_entries: List[DniIsmTaxonomyNonuscontrolsEntry] = []
    dissem_entries: List[DniIsmTaxonomyDissemEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
