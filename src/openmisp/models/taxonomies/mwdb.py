"""Taxonomy model for mwdb."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class MwdbTaxonomyPredicate(str, Enum):
    LOCATION_TYPE = "location_type"
    FAMILY = "family"


class MwdbTaxonomyLocationTypeEntry(str, Enum):
    CNC = "cnc"
    DOWNLOAD_URL = "download_url"
    PANEL = "panel"
    PEER = "peer"
    OTHER = "other"


class MwdbTaxonomyFamilyEntry(str, Enum):
    AGENTTESLA = "agenttesla"
    ANDROMEDA = "andromeda"
    ANUBIS = "anubis"
    AVEMARIA = "avemaria"
    AZORULT = "azorult"
    BRUSHALOADER = "brushaloader"
    BUBLIK = "bublik"
    BUNITU = "bunitu"
    CERBER = "cerber"
    CHTHONIC = "chthonic"
    CITADEL = "citadel"
    COREBOT = "corebot"
    CRYPTOMIX = "cryptomix"
    CRYPTOSHIELD = "cryptoshield"
    CRYPTOWALL = "cryptowall"
    DANABOT = "danabot"
    DANALOADER = "danaloader"
    DRIDEX = "dridex"
    DRIDEX_WORKER = "dridex-worker"
    DYRE = "dyre"
    EMOTET = "emotet"
    EMOTET5_UPNP = "emotet5_upnp"
    EMOTET_DOC = "emotet_doc"
    EMOTET_SPAM = "emotet_spam"
    EMOTET_UPNP = "emotet_upnp"
    EVIL_PONY = "evil-pony"
    FLOKIBOT = "flokibot"
    FORMBOOK = "formbook"
    GANDCRAB = "gandcrab"
    GET2 = "get2"
    GLOBEIMPOSTER = "globeimposter"
    GLUEDROPPER = "gluedropper"
    GOOTKIT = "gootkit"
    H1N1 = "h1n1"
    HANCITOR = "hancitor"
    HAWKEYE = "hawkeye"
    ICEDID = "icedid"
    ICEID = "iceid"
    ICEIX = "iceix"
    ISFB = "isfb"
    JAFF = "jaff"
    KBOT = "kbot"
    KEGOTIP = "kegotip"
    KINS = "kins"
    KOVTER = "kovter"
    KPOT = "kpot"
    KRONOS = "kronos"
    LOCKY = "locky"
    LOKIBOT = "lokibot"
    MADLOCKER = "madlocker"
    MADNESS_PRO = "madness_pro"
    MAOLOA = "maoloa"
    MIRAI = "mirai"
    MMBB = "mmbb"
    NANOCORE = "nanocore"
    NECURS = "necurs"
    NETWIRE = "netwire"
    NEUTRINO = "neutrino"
    NJRAT = "njrat"
    NYMAIM = "nymaim"
    ODINAFF = "odinaff"
    ONLINER = "onliner"
    OSTAP = "ostap"
    PANDA = "panda"
    PHORPIEX = "phorpiex"
    PONY = "pony"
    PUSHDO = "pushdo"
    QADARS = "qadars"
    QAKBOT = "qakbot"
    QUANTLOADER = "quantloader"
    QUASARRAT = "quasarrat"
    RAMNIT = "ramnit"
    REMCOS = "remcos"
    RETEFE = "retefe"
    RUCKGUV = "ruckguv"
    SAGE = "sage"
    SENDSAFE = "sendsafe"
    SHIFU = "shifu"
    SLAVE = "slave"
    SMOKELOADER = "smokeloader"
    SYSTEMBC = "systembc"
    TESLACRYPT = "teslacrypt"
    TEST = "test"
    TESTMOD = "testmod"
    TINBA = "tinba"
    TINBA_DGA = "tinba_dga"
    TINYNUKE = "tinynuke"
    TOFSEE = "tofsee"
    TORMENT = "torment"
    TORRENTLOCKER = "torrentlocker"
    TRICKBOT = "trickbot"
    TROLDESH = "troldesh"
    UNKNOWN = "unknown"
    VAWTRAK = "vawtrak"
    VJWORM = "vjworm"
    VMZEUS = "vmzeus"
    VMZEUS2 = "vmzeus2"
    WANNACRY = "wannacry"
    XAGENT = "xagent"
    ZEUS = "zeus"
    ZLOADER = "zloader"


class MwdbTaxonomy(BaseModel):
    """Model for the mwdb taxonomy."""

    namespace: str = "mwdb"
    description: str = """Malware Database (mwdb) Taxonomy - Tags used across the platform"""
    version: int = 2
    exclusive: bool = False
    predicates: List[MwdbTaxonomyPredicate] = []
    location_type_entries: List[MwdbTaxonomyLocationTypeEntry] = []
    family_entries: List[MwdbTaxonomyFamilyEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
