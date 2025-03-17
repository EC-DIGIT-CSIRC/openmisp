"""Taxonomy model for drugs."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DrugsTaxonomyPredicate(str, Enum):
    ALKALOIDS_AND_DERIVATIVES = "alkaloids-and-derivatives"
    BENZENOIDS = "benzenoids"
    HOMOGENEOUS_METAL_COMPOUNDS = "homogeneous-metal-compounds"
    HOMOGENEOUS_NON_METAL_COMPOUNDS = "homogeneous-non-metal-compounds"
    HYDROCARBONS = "hydrocarbons"
    HYDROCARBON_DERIVATIVES = "hydrocarbon-derivatives"
    LIGNANS__NEOLIGNANS_AND_RELATED_COMPOUNDS = "lignans,-neolignans-and-related-compounds"
    LIPIDS_AND_LIPID_LIKE_MOLECULES = "lipids-and-lipid-like-molecules"
    MIXED_METAL_NON_METAL_COMPOUNDS = "mixed-metal/non-metal-compounds"
    NUCLEOSIDES__NUCLEOTIDES__AND_ANALOGUES = "nucleosides,-nucleotides,-and-analogues"
    ORGANIC_1_3_DIPOLAR_COMPOUNDS = "organic-1,3-dipolar-compounds"
    ORGANIC_ACIDS_AND_DERIVATIVES = "organic-acids-and-derivatives"
    ORGANIC_ACIDS = "organic-acids"
    ORGANIC_NITROGEN_COMPOUNDS = "organic-nitrogen-compounds"
    ORGANIC_OXYGEN_COMPOUNDS = "organic-oxygen-compounds"
    ORGANIC_POLYMERS = "organic-polymers"
    ORGANIC_SALTS = "organic-salts"
    ORGANOHALOGEN_COMPOUNDS = "organohalogen-compounds"
    ORGANOHETEROCYCLIC_COMPOUNDS = "organoheterocyclic-compounds"
    ORGANOMETALLIC_COMPOUNDS = "organometallic-compounds"
    ORGANOPHOSPHORUS_COMPOUNDS = "organophosphorus-compounds"
    ORGANOSULFUR_COMPOUNDS = "organosulfur-compounds"
    PHENYLPROPANOIDS_AND_POLYKETIDES = "phenylpropanoids-and-polyketides"


class DrugsTaxonomyAlkaloidsAndDerivativesEntry(str, Enum):
    AJMALINE_SARPAGINE_ALKALOIDS = "ajmaline-sarpagine-alkaloids"
    T__ALLOCOLCHICINE_ALKALOIDS = " allocolchicine-alkaloids"
    T__AMARYLLIDACEAE_ALKALOIDS = " Amaryllidaceae alkaloids"
    APORPHINES = "aporphines"
    CAMPTOTHECINS = "camptothecins"
    CEPHALOTAXUS_ALKALOIDS = "cephalotaxus-alkaloids"
    CINCHONA_ALKALOIDS = "cinchona-alkaloids"
    EBURNAN_TYPE_ALKALOIDS = "eburnan-type-alkaloids"
    EPIBATIDINE_ANALOGUES = "epibatidine-analogues"
    ERGOLINE_AND_DERIVATIVES = "ergoline-and-derivatives"
    HARMALA_ALKALOIDS = "harmala-alkaloids"
    IBOGAN_TYPE_ALKALOIDS = "ibogan-type-alkaloids"
    LUPIN_ALKALOIDS = "lupin-alkaloids"
    MORPHINANS = "morphinans"
    PHTHALIDE_ISOQUINOLINES = "phthalide-isoquinolines"
    PROTOBERBERINE_ALKALOIDS_AND_DERIVATIVES = "protoberberine-alkaloids-and-derivatives"
    TROPANE_ALKALOIDS = "tropane-alkaloids"
    VINCA_ALKALOIDS = "vinca-alkaloids"
    YOHIMBINE_ALKALOIDS = "yohimbine-alkaloids"


class DrugsTaxonomyBenzenoidsEntry(str, Enum):
    ANTHRACENES = "anthracenes"
    BENZENE_AND_SUBSTITUTED_DERIVATIVES = "benzene-and-substituted-derivatives"
    DIBENZOCYCLOHEPTENES = "dibenzocycloheptenes"
    FLUORENES = "fluorenes"
    INDANES = "indanes"
    INDENES_AND_ISOINDENES = "indenes-and-isoindenes"
    NAPHTHACENES = "naphthacenes"
    PHENANTHRENES_AND_DERIVATIVES = "phenanthrenes-and-derivatives"
    PHENOL_ESTERS = "phenol-esters"
    PHENOL_ETHERS = "phenol-ethers"
    PHENOLS = "phenols"
    PYRENES = "pyrenes"
    TETRALINS = "tetralins"
    TRIPHENYL_COMPOUNDS = "triphenyl-compounds"


class DrugsTaxonomyHomogeneousMetalCompoundsEntry(str, Enum):
    HOMOGENEOUS_ACTINIDE_COMPOUNDS = "homogeneous-actinide-compounds"
    HOMOGENEOUS_ALKALI_METAL_COMPOUNDS = "homogeneous-alkali-metal-compounds"
    HOMOGENEOUS_ALKALINE_EARTH_METAL_COMPOUNDS = "homogeneous-alkaline-earth-metal-compounds"
    HOMOGENEOUS_LANTHANIDE_COMPOUNDS = "homogeneous-lanthanide-compounds"
    HOMOGENEOUS_METALLOID_COMPOUNDS = "homogeneous-metalloid-compounds"
    HOMOGENEOUS_POST_TRANSITION_METAL_COMPOUNDS = "homogeneous-post-transition-metal-compounds"
    HOMOGENEOUS_TRANSITION_METAL_COMPOUNDS = "homogeneous-transition-metal-compounds"


class DrugsTaxonomyHomogeneousNonMetalCompoundsEntry(str, Enum):
    HALOGEN_ORGANIDES = "halogen-organides"
    HOMOGENEOUS_HALOGENS = "homogeneous-halogens"
    HOMOGENEOUS_NOBLE_GASES = "homogeneous-noble-gases"
    HOMOGENEOUS_OTHER_NON_METAL_COMPOUNDS = "homogeneous-other-non-metal-compounds"
    NON_METAL_OXOANIONIC_COMPOUNDS = "non-metal-oxoanionic-compounds"
    OTHER_NON_METAL_HALIDES = "other-non-metal-halides"
    OTHER_NON_METAL_ORGANIDES = "other-non-metal-organides"


class DrugsTaxonomyHydrocarbonsEntry(str, Enum):
    POLYCYCLIC_HYDROCARBONS = "polycyclic-hydrocarbons"


class DrugsTaxonomyHydrocarbonDerivativesEntry(str, Enum):
    TROPONES = "tropones"


class DrugsTaxonomyLignansNeolignansAndRelatedCompoundsEntry(str, Enum):
    ARYLTETRALIN_LIGNANS = "aryltetralin-lignans"
    DIBENZYLBUTANE_LIGNANS = "dibenzylbutane-lignans"
    FLAVONOLIGNANS = "flavonolignans"
    FURANOID_LIGNANS = "furanoid-lignans"
    LIGNAN_LACTONES = "lignan-lactones"


class DrugsTaxonomyLipidsAndLipidLikeMoleculesEntry(str, Enum):
    FATTY_ACYLS = "fatty-acyls"
    GLYCERO_3_DITHIOPHOSPHOCHOLINES = "glycero-3-dithiophosphocholines"
    GLYCEROLIPIDS = "glycerolipids"
    GLYCEROPHOSPHOLIPIDS = "glycerophospholipids"
    PRENOL_LIPIDS = "prenol-lipids"
    SACCHAROLIPIDS = "saccharolipids"
    S_ALKYL_COAS = "s-alkyl-coas"
    SPHINGOLIPIDS = "sphingolipids"
    STEROIDS_AND_STEROID_DERIVATIVES = "steroids-and-steroid-derivatives"


class DrugsTaxonomyMixedMetalNonMetalCompoundsEntry(str, Enum):
    ALKALI_METAL_ORGANIDES = "alkali-metal-organides"
    ALKALI_METAL_OXOANIONIC_COMPOUNDS = "alkali-metal-oxoanionic-compounds"
    ALKALI_METAL_SALTS = "alkali-metal-salts"
    ALKALINE_EARTH_METAL_ORGANIDES = "alkaline-earth-metal-organides"
    ALKALINE_EARTH_METAL_OXOANIONIC_COMPOUNDS = "alkaline-earth-metal-oxoanionic-compounds"
    ALKALINE_EARTH_METAL_SALTS = "alkaline-earth-metal-salts"
    METALLOID_ORGANIDES = "metalloid-organides"
    METALLOID_OXOANIONIC_COMPOUNDS = "metalloid-oxoanionic-compounds"
    MISCELLANEOUS_MIXED_METAL_NON_METALS = "miscellaneous-mixed-metal/non-metals"
    OTHER_MIXED_METAL_NON_METAL_OXOANIONIC_COMPOUNDS = "other-mixed-metal/non-metal-oxoanionic-compounds"
    POST_TRANSITION_METAL_ORGANIDES = "post-transition-metal-organides"
    POST_TRANSITION_METAL_OXOANIONIC_COMPOUNDS = "post-transition-metal-oxoanionic-compounds"
    POST_TRANSITION_METAL_SALTS = "post-transition-metal-salts"
    TRANSITION_METAL_ORGANIDES = "transition-metal-organides"
    TRANSITION_METAL_OXOANIONIC_COMPOUNDS = "transition-metal-oxoanionic-compounds"
    TRANSITION_METAL_SALTS = "transition-metal-salts"


class DrugsTaxonomyNucleosidesNucleotidesAndAnaloguesEntry(str, Enum):
    T_2__3__DIDEOXY_3__THIONUCLEOSIDE_MONOPHOSPHATES = "2',3'-dideoxy-3'-thionucleoside-monophosphates"
    T_2__5__DIDEOXYRIBONUCLEOSIDES = "2',5'-dideoxyribonucleosides"
    T__3___GT_5___DINUCLEOTIDES_AND_ANALOGUES = "(3'-&gt;5')-dinucleotides-and-analogues"
    T_5__DEOXYRIBONUCLEOSIDES = "5'-deoxyribonucleosides"
    T__5___GT_5___DINUCLEOTIDES = "(5'-&gt;5')-dinucleotides"
    BENZIMIDAZOLE_RIBONUCLEOSIDES_AND_RIBONUCLEOTIDES = "benzimidazole-ribonucleosides-and-ribonucleotides"
    FLAVIN_NUCLEOTIDES = "flavin-nucleotides"
    GLYCINAMIDE_RIBONUCLEOTIDES = "glycinamide-ribonucleotides"
    IMIDAZOLE_4_5_C_PYRIDINE_RIBONUCLEOSIDES_AND_RIBONUCLEOTIDES = (
        "imidazole[4,5-c]pyridine-ribonucleosides-and-ribonucleotides"
    )
    IMIDAZOLE_RIBONUCLEOSIDES_AND_RIBONUCLEOTIDES = "imidazole-ribonucleosides-and-ribonucleotides"
    MOLYBDOPTERIN_DINUCLEOTIDES = "molybdopterin-dinucleotides"
    NUCLEOSIDE_AND_NUCLEOTIDE_ANALOGUES = "nucleoside-and-nucleotide-analogues"
    PURINE_NUCLEOSIDES = "purine-nucleosides"
    PYRAZOLO_3_4_D_PYRIMIDINE_GLYCOSIDES = "pyrazolo[3,4-d]pyrimidine-glycosides"
    PYRIDINE_NUCLEOTIDES = "pyridine-nucleotides"
    PYRIMIDINE_NUCLEOSIDES = "pyrimidine-nucleosides"
    PYRIMIDINE_NUCLEOTIDES = "pyrimidine-nucleotides"
    PYRROLOPYRIMIDINE_NUCLEOSIDES_AND_NUCLEOTIDES = "pyrrolopyrimidine-nucleosides-and-nucleotides"
    RIBONUCLEOSIDE_3__PHOSPHATES = "ribonucleoside-3'-phosphates"
    TRIAZOLE_RIBONUCLEOSIDES_AND_RIBONUCLEOTIDES = "triazole-ribonucleosides-and-ribonucleotides"


class DrugsTaxonomyOrganic13DipolarCompoundsEntry(str, Enum):
    ALLYL_TYPE_1_3_DIPOLAR_ORGANIC_COMPOUNDS = "allyl-type-1,3-dipolar-organic-compounds"


class DrugsTaxonomyOrganicAcidsAndDerivativesEntry(str, Enum):
    BORONIC_ACID_DERIVATIVES = "boronic-acid-derivatives"
    CARBOXIMIDIC_ACIDS_AND_DERIVATIVES = "carboximidic-acids-and-derivatives"
    CARBOXYLIC_ACIDS_AND_DERIVATIVES = "carboxylic-acids-and-derivatives"
    HYDROXY_ACIDS_AND_DERIVATIVES = "hydroxy-acids-and-derivatives"
    KETO_ACIDS_AND_DERIVATIVES = "keto-acids-and-derivatives"
    ORGANIC_CARBONIC_ACIDS_AND_DERIVATIVES = "organic-carbonic-acids-and-derivatives"
    ORGANIC_PHOSPHONIC_ACIDS_AND_DERIVATIVES = "organic-phosphonic-acids-and-derivatives"
    ORGANIC_PHOSPHORIC_ACIDS_AND_DERIVATIVES = "organic-phosphoric-acids-and-derivatives"
    ORGANIC_SULFONIC_ACIDS_AND_DERIVATIVES = "organic-sulfonic-acids-and-derivatives"
    ORGANIC_SULFURIC_ACIDS_AND_DERIVATIVES = "organic-sulfuric-acids-and-derivatives"
    ORGANIC_THIOPHOSPHORIC_ACIDS_AND_DERIVATIVES = "organic-thiophosphoric-acids-and-derivatives"
    ORTHOCARBOXYLIC_ACID_DERIVATIVES = "orthocarboxylic-acid-derivatives"
    PEPTIDOMIMETICS = "peptidomimetics"
    THIOSULFINIC_ACID_ESTERS = "thiosulfinic-acid-esters"


class DrugsTaxonomyOrganicAcidsEntry(str, Enum):
    CARBOXYLIC_ACIDS_AND_DERIVATIVES = "carboxylic-acids-and-derivatives"


class DrugsTaxonomyOrganicNitrogenCompoundsEntry(str, Enum):
    ORGANONITROGEN_COMPOUNDS = "organonitrogen-compounds"


class DrugsTaxonomyOrganicOxygenCompoundsEntry(str, Enum):
    ORGANIC_OXIDES = "organic-oxides"
    ORGANIC_OXOANIONIC_COMPOUNDS = "organic-oxoanionic-compounds"
    ORGANOOXYGEN_COMPOUNDS = "organooxygen-compounds"


class DrugsTaxonomyOrganicPolymersEntry(str, Enum):
    PHOSPHOROTHIOATE_POLYNUCLEOTIDES = "phosphorothioate-polynucleotides"
    POLYPEPTIDES = "polypeptides"
    POLYSACCHARIDES = "polysaccharides"


class DrugsTaxonomyOrganicSaltsEntry(str, Enum):
    ORGANIC_METAL_SALTS = "organic-metal-salts"


class DrugsTaxonomyOrganohalogenCompoundsEntry(str, Enum):
    ACYL_HALIDES = "acyl-halides"
    ALKYL_HALIDES = "alkyl-halides"
    ARYL_HALIDES = "aryl-halides"
    HALOHYDRINS = "halohydrins"
    ORGANOCHLORIDES = "organochlorides"
    ORGANOFLUORIDES = "organofluorides"
    SULFONYL_HALIDES = "sulfonyl-halides"
    VINYL_HALIDES = "vinyl-halides"


class DrugsTaxonomyOrganoheterocyclicCompoundsEntry(str, Enum):
    AZASPIRODECANE_DERIVATIVES = "azaspirodecane-derivatives"
    AZEPANES = "azepanes"
    AZOBENZENES = "azobenzenes"
    AZOLES = "azoles"
    AZOLIDINES = "azolidines"
    AZOLINES = "azolines"
    BENZAZEPINES = "benzazepines"
    BENZIMIDAZOLES = "benzimidazoles"
    BENZISOXAZOLES = "benzisoxazoles"
    BENZOCYCLOHEPTAPYRIDINES = "benzocycloheptapyridines"
    BENZODIAZEPINES = "benzodiazepines"
    BENZODIOXANES = "benzodioxanes"
    BENZODIOXOLES = "benzodioxoles"
    BENZOFURANS = "benzofurans"
    BENZOPYRANS = "benzopyrans"
    BENZOPYRAZOLES = "benzopyrazoles"
    BENZOTHIADIAZOLES = "benzothiadiazoles"
    BENZOTHIAZEPINES = "benzothiazepines"
    BENZOTHIAZINES = "benzothiazines"
    BENZOTHIAZOLES = "benzothiazoles"
    BENZOTHIEPINS = "benzothiepins"
    BENZOTHIOPHENES = "benzothiophenes"
    BENZOTHIOPYRANS = "benzothiopyrans"
    BENZOTRIAZOLES = "benzotriazoles"
    BENZOXADIAZOLES = "benzoxadiazoles"
    BENZOXAZEPINES = "benzoxazepines"
    BENZOXAZINES = "benzoxazines"
    BENZOXAZOLES = "benzoxazoles"
    BENZOXEPINES = "benzoxepines"
    BI__AND_OLIGOTHIOPHENES = "bi--and-oligothiophenes"
    BIOTIN_AND_DERIVATIVES = "biotin-and-derivatives"
    COUMARANS = "coumarans"
    CYCLOHEPTAPYRANS = "cycloheptapyrans"
    CYCLOHEPTATHIOPHENES = "cycloheptathiophenes"
    DIAZANAPHTHALENES = "diazanaphthalenes"
    DIAZEPANES = "diazepanes"
    DIAZINANES = "diazinanes"
    DIAZINES = "diazines"
    DIHYDROFURANS = "dihydrofurans"
    DIHYDROISOQUINOLINES = "dihydroisoquinolines"
    DIHYDROTHIOPHENES = "dihydrothiophenes"
    DIOXABOROLANES = "dioxaborolanes"
    DIOXANES = "dioxanes"
    DIOXOLOPYRANS = "dioxolopyrans"
    DITHIANES = "dithianes"
    DITHIOLANES = "dithiolanes"
    EPOXIDES = "epoxides"
    FURANS = "furans"
    FUROFURANS = "furofurans"
    FUROPYRANS = "furopyrans"
    FUROPYRIDINES = "furopyridines"
    FUROPYRROLES = "furopyrroles"
    HETEROAROMATIC_COMPOUNDS = "heteroaromatic-compounds"
    IMIDAZO_1_5_A_PYRAZINES = "imidazo[1,5-a]pyrazines"
    IMIDAZODIAZEPINES = "imidazodiazepines"
    IMIDAZOPYRAZINES = "imidazopyrazines"
    IMIDAZOPYRIDINES = "imidazopyridines"
    IMIDAZOPYRIMIDINES = "imidazopyrimidines"
    IMIDAZOTETRAZINES = "imidazotetrazines"
    IMIDAZOTHIAZOLES = "imidazothiazoles"
    INDOLES_AND_DERIVATIVES = "indoles-and-derivatives"
    INDOLIZIDINES = "indolizidines"
    ISOCOUMARANS = "isocoumarans"
    ISOINDOLES_AND_DERIVATIVES = "isoindoles-and-derivatives"
    ISOQUINOLINES_AND_DERIVATIVES = "isoquinolines-and-derivatives"
    ISOXAZOLOPYRIDINES = "isoxazolopyridines"
    LACTAMS = "lactams"
    LACTONES = "lactones"
    METALLOHETEROCYCLIC_COMPOUNDS = "metalloheterocyclic-compounds"
    NAPHTHOFURANS = "naphthofurans"
    NAPHTHOPYRANS = "naphthopyrans"
    OXANES = "oxanes"
    OXAZAPHOSPHINANES = "oxazaphosphinanes"
    OXAZINANES = "oxazinanes"
    OXEPANES = "oxepanes"
    PHENANTHROLINES = "phenanthrolines"
    PIPERAZINOAZEPINES = "piperazinoazepines"
    PIPERIDINES = "piperidines"
    PTERIDINES_AND_DERIVATIVES = "pteridines-and-derivatives"
    PYRANODIOXINS = "pyranodioxins"
    PYRANOPYRIDINES = "pyranopyridines"
    PYRANOPYRIMIDINES = "pyranopyrimidines"
    PYRANS = "pyrans"
    PYRAZOLOPYRIDINES = "pyrazolopyridines"
    PYRAZOLOPYRIMIDINES = "pyrazolopyrimidines"
    PYRAZOLOTRIAZINES = "pyrazolotriazines"
    PYRIDINES_AND_DERIVATIVES = "pyridines-and-derivatives"
    PYRIDOPYRIMIDINES = "pyridopyrimidines"
    PYRROLES = "pyrroles"
    PYRROLIDINES = "pyrrolidines"
    PYRROLINES = "pyrrolines"
    PYRROLIZINES = "pyrrolizines"
    PYRROLOAZEPINES = "pyrroloazepines"
    PYRROLOPYRAZINES = "pyrrolopyrazines"
    PYRROLOPYRAZOLES = "pyrrolopyrazoles"
    PYRROLOPYRIDINES = "pyrrolopyridines"
    PYRROLOPYRIMIDINES = "pyrrolopyrimidines"
    PYRROLOTRIAZINES = "pyrrolotriazines"
    QUINOLINES_AND_DERIVATIVES = "quinolines-and-derivatives"
    QUINUCLIDINES = "quinuclidines"
    SELENAZOLES = "selenazoles"
    TETRAHYDROFURANS = "tetrahydrofurans"
    TETRAHYDROISOQUINOLINES = "tetrahydroisoquinolines"
    TETRAPYRROLES_AND_DERIVATIVES = "tetrapyrroles-and-derivatives"
    THIADIAZINANES = "thiadiazinanes"
    THIADIAZINES = "thiadiazines"
    THIANES = "thianes"
    THIAZEPINES = "thiazepines"
    THIAZINANES = "thiazinanes"
    THIAZINES = "thiazines"
    THIENODIAZEPINES = "thienodiazepines"
    THIENOIMIDAZOLIDINES = "thienoimidazolidines"
    THIENOPYRIDINES = "thienopyridines"
    THIENOPYRIMIDINES = "thienopyrimidines"
    THIENOPYRROLES = "thienopyrroles"
    THIENOTHIAZINES = "thienothiazines"
    THIOCHROMANES = "thiochromanes"
    THIOCHROMENES = "thiochromenes"
    THIOLANES = "thiolanes"
    THIOPHENES = "thiophenes"
    TRIAZINANES = "triazinanes"
    TRIAZINES = "triazines"
    TRIAZOLOPYRAZINES = "triazolopyrazines"
    TRIAZOLOPYRIDINES = "triazolopyridines"
    TRIAZOLOPYRIMIDINES = "triazolopyrimidines"
    TRIOXANES = "trioxanes"


class DrugsTaxonomyOrganometallicCompoundsEntry(str, Enum):
    ORGANOMETALLOID_COMPOUNDS = "organometalloid-compounds"
    ORGANO_POST_TRANSITION_METAL_COMPOUNDS = "organo-post-transition-metal-compounds"


class DrugsTaxonomyOrganophosphorusCompoundsEntry(str, Enum):
    ORGANIC_PHOSPHINES_AND_DERIVATIVES = "organic-phosphines-and-derivatives"
    ORGANOPHOSPHINIC_ACIDS_AND_DERIVATIVES = "organophosphinic-acids-and-derivatives"
    ORGANOTHIOPHOSPHORUS_COMPOUNDS = "organothiophosphorus-compounds"


class DrugsTaxonomyOrganosulfurCompoundsEntry(str, Enum):
    ISOTHIOUREAS = "isothioureas"
    ORGANIC_DISULFIDES = "organic-disulfides"
    SULFONYLS = "sulfonyls"
    SULFOXIDES = "sulfoxides"
    THIOCARBONYL_COMPOUNDS = "thiocarbonyl-compounds"
    THIOETHERS = "thioethers"
    THIOLS = "thiols"
    THIOUREAS = "thioureas"


class DrugsTaxonomyPhenylpropanoidsAndPolyketidesEntry(str, Enum):
    T_2_ARYLBENZOFURAN_FLAVONOIDS = "2-arylbenzofuran-flavonoids"
    ANTHRACYCLINES = "anthracyclines"
    AURONE_FLAVONOIDS = "aurone-flavonoids"
    CINNAMIC_ACIDS_AND_DERIVATIVES = "cinnamic-acids-and-derivatives"
    CINNAMYL_ALCOHOLS = "cinnamyl-alcohols"
    COUMARINS_AND_DERIVATIVES = "coumarins-and-derivatives"
    DEPSIDES_AND_DEPSIDONES = "depsides-and-depsidones"
    DIARYLHEPTANOIDS = "diarylheptanoids"
    FLAVONOIDS = "flavonoids"
    ISOCHROMANEQUINONES = "isochromanequinones"
    ISOCOUMARINS_AND_DERIVATIVES = "isocoumarins-and-derivatives"
    ISOFLAVONOIDS = "isoflavonoids"
    LINEAR_1_3_DIARYLPROPANOIDS = "linear-1,3-diarylpropanoids"
    MACROLACTAMS = "macrolactams"
    MACROLIDE_LACTAMS = "macrolide-lactams"
    MACROLIDES_AND_ANALOGUES = "macrolides-and-analogues"
    NEOFLAVONOIDS = "neoflavonoids"
    PHENYLPROPANOIC_ACIDS = "phenylpropanoic-acids"
    SAXITOXINS__GONYAUTOXINS__AND_DERIVATIVES = "saxitoxins,-gonyautoxins,-and-derivatives"
    STILBENES = "stilbenes"
    TANNINS = "tannins"
    TETRACYCLINES = "tetracyclines"


class DrugsTaxonomy(BaseModel):
    """Model for the drugs taxonomy."""

    namespace: str = "drugs"
    description: str = (
        """A taxonomy based on the superclass and class of drugs. Based on https://www.drugbank.ca/releases/latest"""
    )
    version: int = 2
    exclusive: bool = False
    predicates: List[DrugsTaxonomyPredicate] = []
    alkaloids_and_derivatives_entries: List[DrugsTaxonomyAlkaloidsAndDerivativesEntry] = []
    benzenoids_entries: List[DrugsTaxonomyBenzenoidsEntry] = []
    homogeneous_metal_compounds_entries: List[DrugsTaxonomyHomogeneousMetalCompoundsEntry] = []
    homogeneous_non_metal_compounds_entries: List[DrugsTaxonomyHomogeneousNonMetalCompoundsEntry] = []
    hydrocarbons_entries: List[DrugsTaxonomyHydrocarbonsEntry] = []
    hydrocarbon_derivatives_entries: List[DrugsTaxonomyHydrocarbonDerivativesEntry] = []
    lignans__neolignans_and_related_compounds_entries: List[DrugsTaxonomyLignansNeolignansAndRelatedCompoundsEntry] = []
    lipids_and_lipid_like_molecules_entries: List[DrugsTaxonomyLipidsAndLipidLikeMoleculesEntry] = []
    mixed_metal_non_metal_compounds_entries: List[DrugsTaxonomyMixedMetalNonMetalCompoundsEntry] = []
    nucleosides__nucleotides__and_analogues_entries: List[DrugsTaxonomyNucleosidesNucleotidesAndAnaloguesEntry] = []
    organic_1_3_dipolar_compounds_entries: List[DrugsTaxonomyOrganic13DipolarCompoundsEntry] = []
    organic_acids_and_derivatives_entries: List[DrugsTaxonomyOrganicAcidsAndDerivativesEntry] = []
    organic_acids_entries: List[DrugsTaxonomyOrganicAcidsEntry] = []
    organic_nitrogen_compounds_entries: List[DrugsTaxonomyOrganicNitrogenCompoundsEntry] = []
    organic_oxygen_compounds_entries: List[DrugsTaxonomyOrganicOxygenCompoundsEntry] = []
    organic_polymers_entries: List[DrugsTaxonomyOrganicPolymersEntry] = []
    organic_salts_entries: List[DrugsTaxonomyOrganicSaltsEntry] = []
    organohalogen_compounds_entries: List[DrugsTaxonomyOrganohalogenCompoundsEntry] = []
    organoheterocyclic_compounds_entries: List[DrugsTaxonomyOrganoheterocyclicCompoundsEntry] = []
    organometallic_compounds_entries: List[DrugsTaxonomyOrganometallicCompoundsEntry] = []
    organophosphorus_compounds_entries: List[DrugsTaxonomyOrganophosphorusCompoundsEntry] = []
    organosulfur_compounds_entries: List[DrugsTaxonomyOrganosulfurCompoundsEntry] = []
    phenylpropanoids_and_polyketides_entries: List[DrugsTaxonomyPhenylpropanoidsAndPolyketidesEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
