"""Taxonomy model for CNSD Taxonomia de Incidentes de Seguridad Digital."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class CnsdTaxonomyPredicate(str, Enum):
    CONTENIDO_ABUSIVO = "Contenido abusivo"
    DISPONIBILIDAD = "Disponibilidad"
    FRAUDE = "Fraude"
    FUGA_DE_INFORMACI_N = "Fuga de información"
    INTENTOS_DE_INTRUSI_N = "Intentos de intrusión"
    INTRUSI_N = "Intrusión"
    MALWARE = "Malware"
    RECOPILACI_N_DE_INFORMACI_N = "Recopilación de información"
    OTROS = "Otros"


class CnsdTaxonomyContenidoAbusivoEntry(str, Enum):
    SPAM = "spam"
    COPYRIGHT = "copyright"
    EXPLOTACION_SEXUAL_INFANTIL = "explotacion sexual infantil"


class CnsdTaxonomyDisponibilidadEntry(str, Enum):
    DO_S_DDO_S = "DoS/DDoS"
    SABOTAJE = "sabotaje"


class CnsdTaxonomyFraudeEntry(str, Enum):
    MAL_USO = "mal-uso"
    REPRES_FALSA = "repres-falsa"


class CnsdTaxonomyFugaDeInformaciNEntry(str, Enum):
    ACC_NO_AUTORIZADO = "acc-no-autorizado"
    MODI_ELIM_NO_AUTORIZADA = "modi-elim-no-autorizada"


class CnsdTaxonomyIntentosDeIntrusiNEntry(str, Enum):
    EXPLOT_VULNERAB = "explot-vulnerab"
    INTENTO_INICIO_SESI_N = "intento-inicio-sesión"


class CnsdTaxonomyIntrusiNEntry(str, Enum):
    EXPLOT_EXTRA_VULNERAB = "explot-extra-vulnerab"
    COMPROMETER_CUENTA = "comprometer-cuenta"


class CnsdTaxonomyMalwareEntry(str, Enum):
    INFECCI_N = "infección"
    DISTRIBUCI_N = "distribución"
    C_C = "c&c"
    CONEXI_N_MALICIOSA = "conexión-maliciosa"
    INDETERMINADO = "indeterminado"


class CnsdTaxonomyRecopilaciNDeInformaciNEntry(str, Enum):
    SCANNING = "scanning"
    SNIFFING = "sniffing"
    PHISHING = "phishing"


class CnsdTaxonomyOtrosEntry(str, Enum):
    INC_NO_LISTADO = "inc-no-listado"
    INC_INDETER = "inc-indeter"
    APT = "APT"
    CIBERTERRORISMO = "ciberterrorismo"
    DANOS_EN_ACTIVOS = "danos-en-activos"


class CnsdTaxonomy(BaseModel):
    """Model for the CNSD Taxonomia de Incidentes de Seguridad Digital taxonomy."""

    namespace: str = "cnsd"
    description: str = """La presente taxonomia es la primera versión disponible para el Centro Nacional de Seguridad Digital del Perú."""
    version: int = 20220513
    exclusive: bool = False
    predicates: List[CnsdTaxonomyPredicate] = []
    contenido_abusivo_entries: List[CnsdTaxonomyContenidoAbusivoEntry] = []
    disponibilidad_entries: List[CnsdTaxonomyDisponibilidadEntry] = []
    fraude_entries: List[CnsdTaxonomyFraudeEntry] = []
    fuga_de_informaci_n_entries: List[CnsdTaxonomyFugaDeInformaciNEntry] = []
    intentos_de_intrusi_n_entries: List[CnsdTaxonomyIntentosDeIntrusiNEntry] = []
    intrusi_n_entries: List[CnsdTaxonomyIntrusiNEntry] = []
    malware_entries: List[CnsdTaxonomyMalwareEntry] = []
    recopilaci_n_de_informaci_n_entries: List[CnsdTaxonomyRecopilaciNDeInformaciNEntry] = []
    otros_entries: List[CnsdTaxonomyOtrosEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
