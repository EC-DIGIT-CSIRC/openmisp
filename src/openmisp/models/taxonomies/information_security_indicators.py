"""Taxonomy model for information-security-indicators."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class InformationSecurityIndicatorsTaxonomyPredicate(str, Enum):
    IEX = "IEX"
    IMF = "IMF"
    IDB = "IDB"
    IWH = "IWH"
    VBH = "VBH"
    VSW = "VSW"
    VCF = "VCF"
    VTC = "VTC"
    VOR = "VOR"
    IMP = "IMP"


class InformationSecurityIndicatorsTaxonomyIexEntry(str, Enum):
    FGY_1 = "FGY.1"
    FGY_2 = "FGY.2"
    SPM_1 = "SPM.1"
    PHI_1 = "PHI.1"
    PHI_2 = "PHI.2"
    INT_1 = "INT.1"
    INT_2 = "INT.2"
    INT_3 = "INT.3"
    DFC_1 = "DFC.1"
    MIS_1 = "MIS.1"
    DOS_1 = "DOS.1"
    MLW_1 = "MLW.1"
    MLW_2 = "MLW.2"
    MLW_3 = "MLW.3"
    MLW_4 = "MLW.4"
    PHY_1 = "PHY.1"


class InformationSecurityIndicatorsTaxonomyImfEntry(str, Enum):
    BRE_1 = "BRE.1"
    BRE_2 = "BRE.2"
    BRE_3 = "BRE.3"
    BRE_4 = "BRE.4"
    MDL_1 = "MDL.1"
    LOM_1 = "LOM.1"
    LOG_1 = "LOG.1"
    LOG_2 = "LOG.2"
    LOG_3 = "LOG.3"


class InformationSecurityIndicatorsTaxonomyIdbEntry(str, Enum):
    UID_1 = "UID.1"
    RGH_1 = "RGH.1"
    RGH_2 = "RGH.2"
    RGH_3 = "RGH.3"
    RGH_4 = "RGH.4"
    RGH_5 = "RGH.5"
    RGH_6 = "RGH.6"
    RGH_7 = "RGH.7"
    MIS_1 = "MIS.1"
    IAC_1 = "IAC.1"
    LOG_1 = "LOG.1"


class InformationSecurityIndicatorsTaxonomyIwhEntry(str, Enum):
    VNP_1 = "VNP.1"
    VNP_2 = "VNP.2"
    VNP_3 = "VNP.3"
    VCN_1 = "VCN.1"
    UKN_1 = "UKN.1"
    UNA_1 = "UNA.1"


class InformationSecurityIndicatorsTaxonomyVbhEntry(str, Enum):
    PRC_1 = "PRC.1"
    PRC_2 = "PRC.2"
    PRC_3 = "PRC.3"
    PRC_4 = "PRC.4"
    PRC_5 = "PRC.5"
    PRC_6 = "PRC.6"
    IAC_1 = "IAC.1"
    IAC_2 = "IAC.2"
    FTR_1 = "FTR.1"
    FTR_2 = "FTR.2"
    FTR_3 = "FTR.3"
    WTI_1 = "WTI.1"
    WTI_2 = "WTI.2"
    WTI_3 = "WTI.3"
    WTI_4 = "WTI.4"
    WTI_5 = "WTI.5"
    WTI_6 = "WTI.6"
    PSW_1 = "PSW.1"
    PSW_2 = "PSW.2"
    PSW_3 = "PSW.3"
    RGH_1 = "RGH.1"
    HUW_1 = "HUW.1"
    HUW_2 = "HUW.2"


class InformationSecurityIndicatorsTaxonomyVswEntry(str, Enum):
    WSR_1 = "WSR.1"
    OSW_1 = "OSW.1"
    WBR_1 = "WBR.1"


class InformationSecurityIndicatorsTaxonomyVcfEntry(str, Enum):
    DIS_1 = "DIS.1"
    LOG_1 = "LOG.1"
    FWR_1 = "FWR.1"
    WTI_1 = "WTI.1"
    WTI_2 = "WTI.2"
    UAC_1 = "UAC.1"
    UAC_2 = "UAC.2"
    UAC_3 = "UAC.3"
    UAC_4 = "UAC.4"
    UAC_5 = "UAC.5"


class InformationSecurityIndicatorsTaxonomyVtcEntry(str, Enum):
    BKP_1 = "BKP.1"
    IDS_1 = "IDS.1"
    WFI_1 = "WFI.1"
    RAP_1 = "RAP.1"
    NRG_1 = "NRG.1"
    PHY_1 = "PHY.1"


class InformationSecurityIndicatorsTaxonomyVorEntry(str, Enum):
    DSC_1 = "DSC.1"
    VNP_1 = "VNP.1"
    VNP_2 = "VNP.2"
    VNR_1 = "VNR.1"
    RCT_1 = "RCT.1"
    RCT_2 = "RCT.2"
    PRT_1 = "PRT.1"
    PRT_2 = "PRT.2"
    PRT_3 = "PRT.3"


class InformationSecurityIndicatorsTaxonomyImpEntry(str, Enum):
    COS_1 = "COS.1"
    TIM_1 = "TIM.1"
    TIM_2 = "TIM.2"
    TIM_3 = "TIM.3"


class InformationSecurityIndicatorsTaxonomy(BaseModel):
    """Model for the information-security-indicators taxonomy."""

    namespace: str = "information-security-indicators"
    description: str = (
        """A full set of operational indicators for organizations to use to benchmark their security posture."""
    )
    version: int = 1
    exclusive: bool = False
    predicates: List[InformationSecurityIndicatorsTaxonomyPredicate] = []
    iex_entries: List[InformationSecurityIndicatorsTaxonomyIexEntry] = []
    imf_entries: List[InformationSecurityIndicatorsTaxonomyImfEntry] = []
    idb_entries: List[InformationSecurityIndicatorsTaxonomyIdbEntry] = []
    iwh_entries: List[InformationSecurityIndicatorsTaxonomyIwhEntry] = []
    vbh_entries: List[InformationSecurityIndicatorsTaxonomyVbhEntry] = []
    vsw_entries: List[InformationSecurityIndicatorsTaxonomyVswEntry] = []
    vcf_entries: List[InformationSecurityIndicatorsTaxonomyVcfEntry] = []
    vtc_entries: List[InformationSecurityIndicatorsTaxonomyVtcEntry] = []
    vor_entries: List[InformationSecurityIndicatorsTaxonomyVorEntry] = []
    imp_entries: List[InformationSecurityIndicatorsTaxonomyImpEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
