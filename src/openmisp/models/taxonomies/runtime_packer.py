"""Taxonomy model for runtime-packer."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class RuntimePackerTaxonomyPredicate(str, Enum):
    DEX = "dex"
    ELF = "elf"
    MACHO = "macho"
    PE = "pe"
    CLI_ASSEMBLY = "cli-assembly"


class RuntimePackerTaxonomyDexEntry(str, Enum):
    APK_PROTECT = "apk-protect"
    APPCODE_PACKER = "appcode-packer"
    APPSEALING = "appsealing"
    ARXAN = "arxan"
    BANGCLE = "bangcle"
    DEXGUARD = "dexguard"
    DEXPROTECTOR = "dexprotector"
    JIAGU = "jiagu"
    LEGU = "legu"
    PROGUARD = "proguard"


class RuntimePackerTaxonomyElfEntry(str, Enum):
    BURNEYE = "burneye"
    BZEXE = "bzexe"
    ELFUCK = "elfuck"
    EZURI = "ezuri"
    GZEXE = "gzexe"
    M0DERN_P4CKER = "m0dern_p4cker"
    MIDGETPACK = "midgetpack"
    PAKKERO = "pakkero"
    PAPAW = "papaw"
    SHIVA = "shiva"
    SILENT_PACKER = "silent_packer"
    UPX = "upx"
    WARD = "ward"


class RuntimePackerTaxonomyMachoEntry(str, Enum):
    ELECKEY = "eleckey"
    LATURI = "laturi"
    MPRESS = "mpress"
    MUNCHO = "muncho"
    PAKR = "pakr"
    UPX = "upx"


class RuntimePackerTaxonomyPeEntry(str, Enum):
    T__NETSHRINK = ".netshrink"
    ACPROTECT = "acprotect"
    AEGIS = "aegis"
    AINEXE = "ainexe"
    ALIENYZE = "alienyze"
    AMBER = "amber"
    ANDROMEDA = "andromeda"
    APACK = "apack"
    ARMADILLO = "armadillo"
    ASPACK = "aspack"
    ASPROTECT = "asprotect"
    ATOMPEPACKER = "atompepacker"
    AUTOIT = "autoit"
    AXPROTECTOR = "axprotector"
    BERO = "bero"
    BOXEDAPP_PACKER = "boxedapp-packer"
    CEXE = "cexe"
    CODE_VIRTUALIZER = "code-virtualizer"
    CONFUSEREX = "confuserex"
    CRINKLER = "crinkler"
    CRUNCH = "crunch"
    DOTBUNDLE = "dotbundle"
    DRAGON_ARMOR = "dragon-armor"
    ELECKEY = "eleckey"
    ENIGMA_PROTECTOR = "enigma-protector"
    ENIGMA_VIRTUAL_BOX = "enigma-virtual-box"
    ERONANA_PACKER = "eronana-packer"
    EXE_BUNDLE = "exe-bundle"
    EXE_STEALTH = "exe-stealth"
    EXE32PACK = "exe32pack"
    EXPRESSOR = "expressor"
    FSG = "fsg"
    GOPACKER = "gopacker"
    HUAN = "huan"
    HXOR_PACKER = "hxor-packer"
    JDPACK = "jdpack"
    KKRUNCHY = "kkrunchy"
    LIAPP = "liapp"
    MASKPE = "maskpe"
    MEW = "mew"
    MOLEBOX = "molebox"
    MORPHINE = "morphine"
    MPRESS = "mpress"
    NEOLITE = "neolite"
    NETCRYPT = "netcrypt"
    NSPACK = "nspack"
    OBSIDIUM = "obsidium"
    ORIGAMI = "origami"
    PACKMAN = "packman"
    PECOMPACT = "pecompact"
    PELOCK = "pelock"
    PEPACKER = "pepacker"
    PERPLEX = "perplex"
    PESHIELD = "peshield"
    PESPIN = "pespin"
    PETITE = "petite"
    PETOY = "petoy"
    PEZOR = "pezor"
    PROCRYPT = "procrypt"
    RLPACK_BASIC = "rlpack-basic"
    RPCRYPT = "rpcrypt"
    SEPACKER = "sepacker"
    SIMPLEDPACK = "simpledpack"
    SMART_PACKER_PRO = "smart-packer-pro"
    SQUISHY = "squishy"
    TELOCK = "telock"
    THEARK = "theark"
    THEMIDA = "themida"
    THINSTALL = "thinstall"
    UPACK = "upack"
    UPX = "upx"
    VMPROTECT = "vmprotect"
    VPROTECT = "vprotect"
    WINUPACK = "winupack"
    WWPACK = "wwpack"
    XCOMP_XPACK = "xcomp-xpack"
    YODA_CRYPTER = "yoda-crypter"
    YODA_PROTECTOR = "yoda-protector"
    ZPROTECT = "zprotect"


class RuntimePackerTaxonomy(BaseModel):
    """Model for the runtime-packer taxonomy."""

    namespace: str = "runtime-packer"
    description: str = """Runtime or software packer used to combine compressed or encrypted data with the decompression or decryption code. This code can add additional obfuscations mechanisms including polymorphic-packer, virtualization or other obfuscation techniques. This taxonomy lists all the known or official packer used for legitimate use or for packing malicious binaries."""
    version: int = 3
    exclusive: bool = False
    predicates: List[RuntimePackerTaxonomyPredicate] = []
    dex_entries: List[RuntimePackerTaxonomyDexEntry] = []
    elf_entries: List[RuntimePackerTaxonomyElfEntry] = []
    macho_entries: List[RuntimePackerTaxonomyMachoEntry] = []
    pe_entries: List[RuntimePackerTaxonomyPeEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
