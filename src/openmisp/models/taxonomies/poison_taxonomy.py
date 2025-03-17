"""Taxonomy model for poison-taxonomy."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class PoisonTaxonomyTaxonomyPredicate(str, Enum):
    POISONOUS_PLANT = "Poisonous plant"
    POISONOUS_FUNGUS = "Poisonous fungus"


class PoisonTaxonomyTaxonomyPoisonousFungusEntry(str, Enum):
    AGARICUS_CALIFORNICUS_CALIFORNIA_ = "Agaricus californicus/California "
    AGARICUS_HONDENSIS_FELT_RINGED_ = "Agaricus hondensis/Felt-ringed "
    AGARICUS_MENIERI = "Agaricus menieri"
    AGARICUS_MOELLERI = "Agaricus moelleri"
    AGARICUS_PHAEOLEPIDOTUS = "Agaricus phaeolepidotus"
    AGARICUS_PLACOMYCES = "Agaricus placomyces"
    AGARICUS_XANTHODERMUS_YELLOW_STAINING_MUSHROOM = "Agaricus xanthodermus/Yellow-staining mushroom"
    AMANITA_ABRUPTA_AMERICAN_ABRUPT_BULBED_LEPIDELLA = "Amanita abrupta/American abrupt-bulbed Lepidella"
    AMANITA_APRICA_SUNSHINE_AMANITA = "Amanita aprica/Sunshine amanita"
    AMANITA_BOUDIERI_BOUDIER_S_LEPIDELLA = "Amanita boudieri/Boudier's lepidella"
    AMANITA_CITRINA = "Amanita citrina"
    AMANITA_COKERI_COKER_S_AMANITA = "Amanita cokeri/Coker's amanita"
    AMANITA_COTHURNATA_BOOTED_AMANITA = "Amanita cothurnata/Booted amanita"
    AMANITA_ECHINOCEPHALA_EUROPEAN_SOLITARY_AMANITA = "Amanita echinocephala/European solitary amanita"
    AMANITA_FARINOSA_POWDERY_AMANITA = "Amanita farinosa/Powdery Amanita"
    AMANITA_FLAVORUBESCENS = "Amanita flavorubescens"
    AMANITA_GEMMATA_GEMMED_AMANITA = "Amanita gemmata/Gemmed Amanita"
    AMANITA_GIOIOSA = "Amanita gioiosa"
    AMANITA_GRACILIOR = "Amanita gracilior"
    AMANITA_HETEROCHROMA_EUCALYPTUS_FLY_AGARIC = "Amanita heterochroma/Eucalyptus fly agaric"
    AMANITA_HONGOI_HONGO_S_AMANITA = "Amanita hongoi/Hongo's Amanita"
    AMANITA_IBOTENGUTAKE_JAPANESE_RINGED_BULBED_AMANITA = "Amanita ibotengutake/Japanese ringed-bulbed Amanita"
    AMANITA_MUSCARIA_FLY_AGARIC = "Amanita muscaria/Fly agaric"
    AMANITA_NEOOVOIDEA_EAST_ASIAN_EGG_AMIDELLA = "Amanita neoovoidea/East Asian egg amidella"
    AMANITA_PANTHERINA_PANTHER_CAP = "Amanita pantherina/Panther cap"
    AMANITA_PORPHYRIA_GREY_VEILED_AMANITA = "Amanita porphyria/Grey veiled Amanita"
    AMANITA_PSEUDOPORPHYRIA_HONGO_S_FALSE_DEATH_CAP = "Amanita pseudoporphyria/Hongo's false death cap"
    AMANITA_PSEUDOREGALIS_FALSE_ROYAL_FLY_AGARIC = "Amanita pseudoregalis/False royal fly agaric"
    AMANITA_PSEUDORUBESCENS_FALSE_BLUSHER = "Amanita pseudorubescens/False blusher"
    AMANITA_REGALIS_ROYAL_FLY_AGARIC = "Amanita regalis/Royal fly agaric"
    AMANITA_SMITHIANA_SMITH_S_AMANITA = "Amanita smithiana/Smith's Amanita"
    AMPULLOCLITOCYBE_CLAVIPES_CLUB_FOOTED_CLITOCYBE = "Ampulloclitocybe clavipes/Club-footed clitocybe"
    CHLOROPHYLLUM_MOLYBDITES_GREEN_SPORED_PARASOL = "Chlorophyllum molybdites/Green-spored parasol"
    CLITOCYBE_CERUSSATA = "Clitocybe cerussata"
    CLITOCYBE_DEALBATA = "Clitocybe dealbata"
    COPRINOPSIS_ALOPECIA = "Coprinopsis alopecia"
    COPRINOPSIS_ATRAMENTARIA_COMMON_INK_CAP = "Coprinopsis atramentaria/Common ink cap"
    COPRINOPSIS_ROMAGNESIANA_SCALY_INK_CAP = "Coprinopsis romagnesiana/Scaly ink cap"
    CORTINARIUS_BOLARIS = "Cortinarius bolaris"
    CORTINARIUS_CALLISTEUS = "Cortinarius callisteus"
    CORTINARIUS_CINNABARINUS = "Cortinarius cinnabarinus"
    CORTINARIUS_CINNAMOMEOFULVUS = "Cortinarius cinnamomeofulvus"
    CORTINARIUS_CINNAMOMEOLUTEUS = "Cortinarius cinnamomeoluteus"
    CORTINARIUS_CINNAMOMEUS = "Cortinarius cinnamomeus"
    CORTINARIUS_CRUENTUS = "Cortinarius cruentus"
    CORTINARIUS_GENTILIS = "Cortinarius gentilis"
    CORTINARIUS_LIMONIUS = "Cortinarius limonius"
    CORTINARIUS_MALICORIUS = "Cortinarius malicorius"
    CORTINARIUS_MIRANDUS = "Cortinarius mirandus"
    CORTINARIUS_PALUSTRIS = "Cortinarius palustris"
    CORTINARIUS_PHOENICEUS = "Cortinarius phoeniceus"
    CORTINARIUS_RUBICUNDULUS = "Cortinarius rubicundulus"
    CORTINARIUS_SMITHII_SMITH_S_CORTINARIUS = "Cortinarius smithii/Smith's Cortinarius"
    CUDONIA_CIRCINANS = "Cudonia circinans"
    GYROMITRA_PERLATA_PIG_S_EARS = "Gyromitra perlata/Pig's ears"
    ECHINODERMA_ASPERUM_FRECKLED_DAPPERLING = "Echinoderma asperum/Freckled dapperling"
    ECHINODERMA_CALCICOLA = "Echinoderma calcicola"
    ENTOLOMA_ALBIDUM = "Entoloma albidum"
    ENTOLOMA_RHODOPOLIUM_WOOD_PINKGILL = "Entoloma rhodopolium/Wood pinkgill"
    ENTOLOMA_SINUATUM_LIVID_ENTOLOMA = "Entoloma sinuatum/Livid Entoloma"
    HEBELOMA_CRUSTULINIFORME_POISON_PIE = "Hebeloma crustuliniforme/Poison pie"
    HEBELOMA_SINAPIZANS_ROUGH_STALKED_HEBELOMA = "Hebeloma sinapizans/Rough-stalked hebeloma"
    HELVELLA_CRISPA_ELFIN_SADDLE = "Helvella crispa/Elfin saddle"
    HELVELLA_DRYOPHILA_OAK_LOVING_ELFIN_SADDLE = "Helvella dryophila/Oak-loving elfin saddle"
    HELVELLA_LACTEA = "Helvella lactea"
    HELVELLA_LACUNOSA_SLATE_GREY_SADDLE = "Helvella lacunosa/Slate grey saddle"
    HELVELLA_VESPERTINA_WESTERN_BLACK_ELFIN_SADDLE = "Helvella vespertina/Western black elfin saddle"
    HAPALOPILUS_NIDULANS_TENDER_NESTING_POLYPORE = "Hapalopilus nidulans/Tender nesting polypore"
    HYPHOLOMA_FASCICULARE_SULPHUR_TUFT = "Hypholoma fasciculare/Sulphur tuft"
    HYPHOLOMA_LATERITIUM_BRICK_CAP = "Hypholoma lateritium/Brick cap"
    HYPHOLOMA_MARGINATUM = "Hypholoma marginatum"
    HYPHOLOMA_RADICOSUM = "Hypholoma radicosum"
    IMPERATOR_RHODOPURPUREUS = "Imperator rhodopurpureus"
    IMPERATOR_TOROSUS = "Imperator torosus"
    INOCYBE_FIBROSA = "Inocybe fibrosa"
    INOCYBE_GEOPHYLLA_EARTHY_INOCYBE = "Inocybe geophylla/Earthy inocybe"
    INOCYBE_HYSTRIX = "Inocybe hystrix"
    INOCYBE_LACERA_TORN_FIBERCAP = "Inocybe lacera/Torn fibercap"
    INOCYBE_LILACINA = "Inocybe lilacina"
    INOCYBE_SUBLILACINA = "Inocybe sublilacina"
    INOCYBE_RIMOSA = "Inocybe rimosa"
    INOCYBE_SAMBUCINA = "Inocybe sambucina"
    LACTARIUS_TORMINOSUS_WOOLLY_MILKCAP = "Lactarius torminosus/Woolly milkcap"
    MYCENA_DIOSMA = "Mycena diosma"
    MYCENA_PURA_LILAC_BONNET = "Mycena pura/Lilac bonnet"
    MYCENA_ROSEA_ROSY_BONNET = "Mycena rosea/Rosy bonnet"
    NEONOTHOPANUS_NAMBI = "Neonothopanus nambi"
    PANAEOLUS_CINCTULUS_BANDED_MOTTLEGILL = "Panaeolus cinctulus/banded mottlegill"
    PSILOCYBE_SEMILANCEATA_LIBERTY_CAP = "Psilocybe semilanceata/Liberty cap"
    OMPHALOTUS_ILLUDENS_JACK_O_LANTERN_MUSHROOM = "Omphalotus illudens/Jack-O'lantern mushroom"
    OMPHALOTUS_JAPONICUS_TSUKIYOTAKE = "Omphalotus japonicus/Tsukiyotake"
    OMPHALOTUS_NIDIFORMIS_GHOST_FUNGUS = "Omphalotus nidiformis/Ghost fungus"
    OMPHALOTUS_OLEARIUS_JACK_O_LANTERN_MUSHROOM = "Omphalotus olearius/Jack-O'lantern mushroom"
    OMPHALOTUS_OLIVASCENS_WESTERN_JACK_O__LANTERN_MUSHROOM = "Omphalotus olivascens/Western jack-o'-lantern mushroom"
    PARALEPISTOPSIS_ACROMELALGA = "Paralepistopsis acromelalga"
    PARALEPISTOPSIS_AMOENOLENS_PARALYSIS_FUNNEL = "Paralepistopsis amoenolens/Paralysis funnel"
    PHOLIOTINA_RUGOSA = "Pholiotina rugosa"
    RAMARIA_FORMOSA_BEAUTIFUL_CLAVARIA = "Ramaria formosa/Beautiful clavaria"
    RAMARIA_NEOFORMOSA = "Ramaria neoformosa"
    RAMARIA_PALLIDA = "Ramaria pallida"
    RUBROBOLETUS_LEGALIAE_LE_GAL_S_BOLETE = "Rubroboletus legaliae/Le Gal's bolete"
    RUBROBOLETUS_LUPINUS_WOLVES_BOLETE = "Rubroboletus lupinus/Wolves bolete"
    RUBROBOLETUS_PULCHERRIMUS = "Rubroboletus pulcherrimus"
    RUBROBOLETUS_SATANAS_SATAN_S_BOLETE = "Rubroboletus satanas/Satan's bolete"
    RUSSULA_EMETICA_THE_SICKENER = "Russula emetica/The sickener"
    RUSSULA_SUBNIGRICANS = "Russula subnigricans"
    SARCOSPHAERA_CORONARIA_PINK_CROWN = "Sarcosphaera coronaria/Pink crown"
    TRICHOLOMA_EQUESTRE_YELLOW_KNIGHT = "Tricholoma equestre/Yellow knight"
    TRICHOLOMA_FILAMENTOSUM = "Tricholoma filamentosum"
    TRICHOLOMA_PARDINUM_TIGER_TRICHOLOMA = "Tricholoma pardinum/Tiger tricholoma"
    TRICHOLOMA_MUSCARIUM = "Tricholoma muscarium"
    TROGIA_VENENATA_LITTLE_WHITE_MUSHROOM = "Trogia venenata/Little white mushroom"
    TURBINELLUS_FLOCCOSUS_WOOLLY_FALSE_CHANTERELLE = "Turbinellus floccosus/Woolly false chanterelle"
    TURBINELLUS_KAUFFMANII = "Turbinellus kauffmanii"
    AGROCYBE_ARENICOLA = "Agrocybe arenicola"
    AMANITA_ALBOCREATA_RINGLESS_PANTHER = "Amanita albocreata/Ringless panther"
    AMANITA_ALTIPES_YELLOW_LONG_STEM_AMANITA = "Amanita altipes/Yellow long-stem Amanita"
    AMANITA_BRECKONII = "Amanita breckonii"
    AMANITA_CECILIAE_SNAKESKIN_GRISETTE = "Amanita ceciliae/Snakeskin grisette"
    AMANITA_ELIAE_FRIES_S_AMANITA = "Amanita eliae/Fries's Amanita"
    AMANITA_FLAVOCONIA_YELLOW_DUST_AMANITA = "Amanita flavoconia/Yellow-dust Amanita"
    AMANITA_FROSTIANA_FROST_S_AMANITA = "Amanita frostiana/Frost's Amanita"
    AMANITA_NEHUTA_MAHORI_DUST_AMANITA = "Amanita nehuta/Mahori dust Amanita"
    AMANITA_PARCIVOLVATA = "Amanita parcivolvata"
    AMANITA_PARVIPANTHERINA = "Amanita parvipantherina"
    AMANITA_PETALINIVOLVA = "Amanita petalinivolva"
    AMANITA_ROSEOTINCTA = "Amanita roseotincta"
    AMANITA_RUBROVOLVATA_RED_VOLVA_AMANITA = "Amanita rubrovolvata/Red volva Amanita"
    AMANITA_SUBFROSTIANA_FALSE_FROST_S_AMANITA = "Amanita subfrostiana/False Frost's Amanita"
    AMANITA_VELATIPES = "Amanita velatipes"
    AMANITA_VISCIDOLUTEA = "Amanita viscidolutea"
    AMANITA_WELLSII_WELLS_S_AMANITA = "Amanita wellsii/Wells's Amanita"
    AMANITA_XANTHOCEPHALA_VERMILION_GRISETTE = "Amanita xanthocephala/Vermilion grisette"
    ARMILLARIA_MELLEA_HONEY_FUNGUS = "Armillaria mellea/Honey fungus"
    CALOCERA_VISCOSA_YELLOW_STAGSHORN = "Calocera viscosa/Yellow stagshorn"
    CHLOROPHYLLUM_BRUNNEUM_SHAGGY_PARASOL = "Chlorophyllum brunneum/Shaggy parasol"
    CHOIROMYCES_VENOSUS = "Choiromyces venosus"
    CLITOCYBE_FRAGRANS = "Clitocybe fragrans"
    CLITOCYBE_NEBULARIS_CLOUDED_AGARIC = "Clitocybe nebularis/Clouded agaric"
    CONOCYBE_SUBOVALIS = "Conocybe subovalis"
    COPRINELLUS_MICACEUS_MICA_CAP = "Coprinellus micaceus/Mica cap"
    LACTARIUS_CHRYSORRHEUS_YELLOWDROP_MILKCAP = "Lactarius chrysorrheus/Yellowdrop milkcap"
    LACTARIUS_HELVUS_FENUGREEK_MILKCAP = "Lactarius helvus/Fenugreek milkcap"
    LEPIOTA_CRISTATA_STINKING_DAPPERLING = "Lepiota cristata/Stinking dapperling"
    MARASMIUS_COLLINUS = "Marasmius collinus"
    RUSSULA_OLIVACEA = "Russula olivacea"
    RUSSULA_VISCIDA = "Russula viscida"
    SCHIZOPHYLLUM_COMMUNE = "Schizophyllum commune"
    SCLERODERMA_CITRINUM_COMMON_EARTHBALL = "Scleroderma citrinum/common earthball"
    STROPHARIA_AERUGINOSA_VERDIGRIS_AGARIC = "Stropharia aeruginosa/Verdigris agaric"
    SUILLUS_GRANULATUS_WEEPING_BOLETE = "Suillus granulatus/Weeping bolete"
    TRICHOLOMA_SULPHUREUM_GAS_AGARIC = "Tricholoma sulphureum/Gas agaric"


class PoisonTaxonomyTaxonomy(BaseModel):
    """Model for the poison-taxonomy taxonomy."""

    namespace: str = "poison-taxonomy"
    description: str = """Non-exhaustive taxonomy of natural poison"""
    version: int = 1
    exclusive: bool = False
    predicates: List[PoisonTaxonomyTaxonomyPredicate] = []
    poisonous_fungus_entries: List[PoisonTaxonomyTaxonomyPoisonousFungusEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
