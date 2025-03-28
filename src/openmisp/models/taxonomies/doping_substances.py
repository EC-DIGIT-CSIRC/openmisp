"""Taxonomy model for Doping substances."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DopingSubstancesTaxonomyPredicate(str, Enum):
    ANABOLIC_AGENTS = "anabolic agents"
    PEPTIDE_HORMONES__GROWTH_FACTORS__RELATED_SUBSTANCES_AND_MIMETICS = (
        "peptide hormones, growth factors, related substances and mimetics"
    )
    BETA_2_AGONISTS = "beta-2 agonists"
    HORMONE_AND_METABOLIC_MODULATORS = "hormone and metabolic modulators"
    DIURETICS_AND_MASKING_AGENTS = "diuretics and masking agents"
    MANIPULATION_OF_BLOOD_AND_BLOOD_COMPONENTS = "manipulation of blood and blood components"
    CHEMICAL_AND_PHYSICAL_MANIPULATION = "chemical and physical manipulation"
    GENE_AND_CELL_DOPING = "gene and cell doping"
    STIMULANTS = "stimulants"
    NARCOTICS = "narcotics"
    CANNABINOIDS = "cannabinoids"
    GLUCOCORTICOIDS = "glucocorticoids"
    BETA_BLOCKERS = "beta-blockers"


class DopingSubstancesTaxonomyAnabolicAgentsEntry(str, Enum):
    T_1_ANDROSTENEDIOL = "1-androstenediol"
    T_1_ANDROSTENEDIONE = "1-androstenedione"
    T_1_ANDROSTERONE = "1-androsterone"
    T_1_EPIANDROSTERONE = "1-epiandrosterone"
    T_1_TESTOSTERONE = "1-testosterone"
    T_4_ANDROSTENEDIOL = "4-androstenediol"
    T_4_HYDROXYTESTOSTERONE = "4-hydroxytestosterone"
    T_5_ANDROSTENEDIONE = "5-androstenedione"
    T_7__HYDROXY_DHEA = "7α-hydroxy-dhea"
    T_7___HYDROXY_DHEA = "7β-hydroxy-dhea"
    T_7_KETO_DHEA = "7-keto-dhea"
    T_17__METHYLEPITHIOSTANOL = "17α-methylepithiostanol"
    T_19_NORANDROSTENEDIOL = "19-norandrostenediol"
    T_19_NORANDROSTENEDIONE = "19-norandrostenedione"
    ANDROST_4_ENE_3_11_17_TRIONE = "androst-4-ene-3,11,17-trione"
    ANDROSTANOLONE = "androstanolone"
    ANDROSTENEDIOL = "androstenediol"
    ANDROSTENEDIONE = "androstenedione"
    BOLASTERONE = "bolasterone"
    BOLDENONE = "boldenone"
    BOLDIONE = "boldione"
    CALUSTERONE = "calusterone"
    CLOSTEBOL = "clostebol"
    DANAZOL = "danazol"
    DEHYDROCHLORMETHYLTESTOSTERONE = "dehydrochlormethyltestosterone"
    DESOXYMETHYLTESTOSTERONE = "desoxymethyltestosterone"
    DROSTANOLONE = "drostanolone"
    EPIANDROSTERONE = "epiandrosterone"
    EPI_DIHYDROTESTOSTERONE = "epi-dihydrotestosterone"
    EPITESTOSTERONE = "epitestosterone"
    ETHYLESTRENOL = "ethylestrenol"
    FLUOXYMESTERONE = "fluoxymesterone"
    FORMEBOLONE = "formebolone"
    FURAZABOL = "furazabol"
    GESTRINONE = "gestrinone"
    MESTANOLONE = "mestanolone"
    MESTEROLONE = "mesterolone"
    METANDIENONE = "metandienone"
    METENOLONE = "metenolone"
    METHANDRIOL = "methandriol"
    METHASTERONE = "methasterone"
    METHYL_1_TESTOSTERONE = "methyl-1-testosterone"
    METHYLCLOSTEBOL = "methylclostebol"
    METHYLDIENOLONE = "methyldienolone"
    METHYLNORTESTOSTERONE = "methylnortestosterone"
    METHYLTESTOSTERONE = "methyltestosterone"
    METRIBOLONE = "metribolone"
    MIBOLERONE = "mibolerone"
    NANDROLONE = "nandrolone"
    NORBOLETONE = "norboletone"
    NORCLOSTEBOL = "norclostebol"
    NORETHANDROLONE = "norethandrolone"
    OXABOLONE = "oxabolone"
    OXANDROLONE = "oxandrolone"
    OXYMESTERONE = "oxymesterone"
    OXYMETHOLONE = "oxymetholone"
    PRASTERONE = "prasterone"
    PROSTANOZOL = "prostanozol"
    QUINBOLONE = "quinbolone"
    STANOZOLOL = "stanozolol"
    STENBOLONE = "stenbolone"
    TESTOSTERONE = "testosterone"
    TETRAHYDROGESTRINONE = "tetrahydrogestrinone"
    TIBOLONE = "tibolone"
    TRENBOLONE = "trenbolone"
    CLENBUTEROL = "clenbuterol"
    OSILODROSTAT = "osilodrostat"
    RACTOPAMINE = "ractopamine"
    SELECTIVE_ANDROGEN_RECEPTOR_MODULATORS = "selective androgen receptor modulators"
    ZERANOL = "zeranol"
    ZILPATEROL = "zilpaterol"


class DopingSubstancesTaxonomyPeptideHormonesGrowthFactorsRelatedSubstancesAndMimeticsEntry(str, Enum):
    DARBEPOETINS = "darbepoetins"
    ERYTHROPOIETINS = "erythropoietins"
    EPO_BASED_CONSTRUCTS = "epo-based constructs"
    EPO_MIMETIC_AGENTS = "epo-mimetic agents"
    COBALT = "cobalt"
    DAPRODUSTAT = "daprodustat"
    IOX2 = "iox2"
    MOLIDUSTAT = "molidustat"
    ROXADUSTAT = "roxadustat"
    VADADUSTAT = "vadadustat"
    XENON = "xenon"
    K_11706 = "k-11706"
    LUSPATERCEPT = "luspatercept"
    SOTATERCEPT = "sotatercept"
    ASIALO_EPO = "asialo epo"
    CARBAMYLATED_EPO = "carbamylated epo"
    BUSERELIN = "buserelin"
    DESLORELIN = "deslorelin"
    GONADORELIN = "gonadorelin"
    GOSERELIN = "goserelin"
    LEUPRORELIN = "leuprorelin"
    NAFARELIN = "nafarelin"
    TRIPTORELIN = "triptorelin"
    CORTICORELIN = "corticorelin"
    GROWTH_HORMONE_ANALOGUES__E_G__LONAPEGSOMATROPIN__SOMAPACITAN_AND_SOMATROGON = (
        "growth hormone analogues, e.g. lonapegsomatropin, somapacitan and somatrogon"
    )
    GROWTH_HORMONE_FRAGMENTS__E_G__AOD_9604_AND_HGH_176_191 = "growth hormone fragments, e.g. aod-9604 and hgh 176-191"
    GROWTH_HORMONE_RELEASING_HORMONE = "growth hormone-releasing hormone"
    GROWTH_HORMONE_SECRETAGOGUES = "growth hormone secretagogues"
    GH_RELEASING_PEPTIDES = "gh-releasing peptides"
    FIBROBLAST_GROWTH_FACTORS = "fibroblast growth factors"
    HEPATOCYTE_GROWTH_FACTOR = "hepatocyte growth factor"
    INSULIN_LIKE_GROWTH_FACTOR_1 = "insulin-like growth factor 1"
    MECHANO_GROWTH_FACTORS = "mechano growth factors"
    PLATELET_DERIVED_GROWTH_FACTOR = "platelet-derived growth factor"
    THYMOSIN__4_AND_ITS_DERIVATIVES_E_G__TB_500 = "thymosin-β4 and its derivatives e.g. tb-500"
    VASCULAR_ENDOTHELIAL_GROWTH_FACTOR = "vascular endothelial growth factor"


class DopingSubstancesTaxonomyBeta2AgonistsEntry(str, Enum):
    ARFORMOTEROL = "arformoterol"
    FENOTEROL = "fenoterol"
    HIGENAMINE = "higenamine"
    INDACATEROL = "indacaterol"
    LEVOSALBUTAMOL = "levosalbutamol"
    OLODATEROL = "olodaterol"
    PROCATEROL = "procaterol"
    REPROTEROL = "reproterol"
    TERBUTALINE = "terbutaline"
    TRETOQUINOL = "tretoquinol"
    TULOBUTEROL = "tulobuterol"
    SALBUTAMOL = "salbutamol"
    FORMOTEROL = "formoterol"
    SALMETEROL = "salmeterol"
    VILANTEROL = "vilanterol"


class DopingSubstancesTaxonomyHormoneAndMetabolicModulatorsEntry(str, Enum):
    T_2_ANDROSTENOL = "2-androstenol"
    T_2_ANDROSTENONE = "2-androstenone"
    T_3_ANDROSTENOL = "3-androstenol"
    T_3_ANDROSTENONE = "3-androstenone"
    T_4_ANDROSTENE_3_6_17_TRIONE = "4-androstene-3,6,17 trione"
    AMINOGLUTETHIMIDE = "aminoglutethimide"
    ANASTROZOLE = "anastrozole"
    ANDROSTA_1_4_6_TRIENE_3_17_DIONE = "androsta-1,4,6-triene-3,17-dione"
    ANDROSTA_3_5_DIENE_7_17_DIONE = "androsta-3,5-diene-7,17-dione"
    EXEMESTANE = "exemestane"
    FORMESTANE = "formestane"
    LETROZOLE = "letrozole"
    TESTOLACTONE = "testolactone"
    BAZEDOXIFENE = "bazedoxifene"
    CLOMIFENE = "clomifene"
    CYCLOFENIL = "cyclofenil"
    FULVESTRANT = "fulvestrant"
    OSPEMIFENE = "ospemifene"
    RALOXIFENE = "raloxifene"
    TAMOXIFEN = "tamoxifen"
    TOREMIFENE = "toremifene"
    ACTIVIN_A_NEUTRALIZING_ANTIBODIES = "activin a-neutralizing antibodies"
    ACTIVIN_RECEPTOR_IIB_COMPETITORS = "activin receptor iib competitors"
    DECOY_ACTIVIN_RECEPTORS = "decoy activin receptors"
    ANTI_ACTIVIN_RECEPTOR_IIB_ANTIBODIES = "anti-activin receptor iib antibodies"
    MYOSTATIN_INHIBITORS = "myostatin inhibitors"
    AGENTS_REDUCING_OR_ABLATING_MYOSTATIN_EXPRESSION = "agents reducing or ablating myostatin expression"
    MYOSTATIN_BINDING_PROTEINS = "myostatin-binding proteins"
    MYOSTATINI___OR_PRECURSOR___NEUTRALIZING__ANTIBODIES = "myostatini - or precursor - neutralizing  antibodies"


class DopingSubstancesTaxonomyDiureticsAndMaskingAgentsEntry(str, Enum):
    DESMOPRESSIN = "desmopressin"
    PROBENECID = "probenecid"
    PLASMA_EXPANDERS = "plasma expanders"
    ACETAZOLAMIDE = "acetazolamide"
    AMILORIDE = "amiloride"
    BUMETANIDE = "bumetanide"
    CANRENONE = "canrenone"
    CHLORTALIDONE = "chlortalidone"
    ETACRYNIC_ACID = "etacrynic acid"
    FUROSEMIDE = "furosemide"
    INDAPAMIDE = "indapamide"
    METOLAZONE = "metolazone"
    SPIRONOLACTONE = "spironolactone"
    THIAZIDES = "thiazides"
    TORASEMIDE = "torasemide"
    TRIAMTERENE = "triamterene"
    VAPTANS = "vaptans"
    VAPTANS__E_G__TOLVAPTAN_ = "vaptans, e.g. tolvaptan."
    DROSPIRENONE = "drospirenone"
    PAMABROM = "pamabrom"
    CARBONIC_ANHYDRASE_INHIBITORS = "carbonic anhydrase inhibitors"
    FELYPRESSIN = "felypressin"


class DopingSubstancesTaxonomyStimulantsEntry(str, Enum):
    ADRAFINIL = "adrafinil"
    AMFEPRAMONE = "amfepramone"
    AMFETAMINE = "amfetamine"
    AMFETAMINIL = "amfetaminil"
    AMIPHENAZOLE = "amiphenazole"
    BENFLUOREX = "benfluorex"
    BENZYLPIPERAZINE = "benzylpiperazine"
    BROMANTAN = "bromantan"
    CLOBENZOREX = "clobenzorex"
    COCAINE = "cocaine"
    CROPROPAMIDE = "cropropamide"
    CROTETAMIDE = "crotetamide"
    FENCAMINE = "fencamine"
    FENETYLLINE = "fenetylline"
    FENFLURAMINE = "fenfluramine"
    FENPROPOREX = "fenproporex"
    FONTURACETAM = "fonturacetam"
    FURFENOREX = "furfenorex"
    LISDEXAMFETAMINE = "lisdexamfetamine"
    MEFENOREX = "mefenorex"
    MEPHENTERMINE = "mephentermine"
    MESOCARB = "mesocarb"
    METAMFETAMINE = "metamfetamine"
    P_METHYLAMFETAMINE = "p-methylamfetamine"
    MODAFINIL = "modafinil"
    NORFENFLURAMINE = "norfenfluramine"
    PHENDIMETRAZINE = "phendimetrazine"
    PHENTERMINE = "phentermine"
    PRENYLAMINE = "prenylamine"
    PROLINTANE = "prolintane"
    T_3_METHYLHEXAN_2_AMINE = "3-methylhexan-2-amine"
    T_4_FLUOROMETHYLPHENIDATE = "4-fluoromethylphenidate"
    T_4_METHYLHEXAN_2_AMINE = "4-methylhexan-2-amine"
    T_4_METHYLPENTAN_2_AMINE = "4-methylpentan-2-amine"
    T_5_METHYLHEXAN_2_AMINE = "5-methylhexan-2-amine"
    BENZFETAMINE = "benzfetamine"
    CATHINE__ = "cathine**"
    CATHINONE_AND_ITS_ANALOGUES = "cathinone and its analogues"
    DIMETAMFETAMINE = "dimetamfetamine"
    EPHEDRINE___ = "ephedrine***"
    EPINEPHRINE____ = "epinephrine****"
    ETAMIVAN = "etamivan"
    ETHYLPHENIDATE = "ethylphenidate"
    ETILAMFETAMINE = "etilamfetamine"
    ETILEFRINE = "etilefrine"
    FAMPROFAZONE = "famprofazone"
    FENBUTRAZATE = "fenbutrazate"
    FENCAMFAMIN = "fencamfamin"
    HEPTAMINOL = "heptaminol"
    HYDRAFINIL = "hydrafinil"
    HYDROXYAMFETAMINE = "hydroxyamfetamine"
    ISOMETHEPTENE = "isometheptene"
    LEVMETAMFETAMINE = "levmetamfetamine"
    MECLOFENOXATE = "meclofenoxate"
    METHYLENEDIOXYMETHAM__PHETAMINE = "methylenedioxymetham- phetamine"
    METHYLEPHEDRINE___ = "methylephedrine***"
    METHYLNAPHTHIDATE = "methylnaphthidate"
    METHYLPHENIDATE = "methylphenidate"
    NIKETHAMIDE = "nikethamide"
    NORFENEFRINE = "norfenefrine"
    OCTODRINE = "octodrine"
    OCTOPAMINE = "octopamine"
    OXILOFRINE = "oxilofrine"
    PEMOLINE = "pemoline"
    PENTETRAZOL = "pentetrazol"
    PHENETHYLAMINE_AND_ITS_DERIVATIVES = "phenethylamine and its derivatives"
    PHENMETRAZINE = "phenmetrazine"
    PHENPROMETHAMINE = "phenpromethamine"
    PROPYLHEXEDRINE = "propylhexedrine"
    PSEUDOEPHEDRINE_____ = "pseudoephedrine*****"
    SELEGILINE = "selegiline"
    SIBUTRAMINE = "sibutramine"
    SOLRIAMFETOL = "solriamfetol"
    STRYCHNINE = "strychnine"
    TENAMFETAMINE = "tenamfetamine"
    TUAMINOHEPTANE = "tuaminoheptane"
    CLONIDINE = "clonidine"
    IMIDAZOLE_DERIVATIVES = "imidazole derivatives"


class DopingSubstancesTaxonomyNarcoticsEntry(str, Enum):
    BUPRENORPHINE = "buprenorphine"
    DEXTROMORAMIDE = "dextromoramide"
    DIAMORPHINE = "diamorphine"
    FENTANYL = "fentanyl"
    HYDROMORPHONE = "hydromorphone"
    METHADONE = "methadone"
    MORPHINE = "morphine"
    NICOMORPHINE = "nicomorphine"
    OXYCODONE = "oxycodone"
    OXYMORPHONE = "oxymorphone"
    PENTAZOCINE = "pentazocine"
    PETHIDINE = "pethidine"


class DopingSubstancesTaxonomyCannabinoidsEntry(str, Enum):
    IN_CANNABIS = "in cannabis"
    SYNTHETIC_CANNABINOIDS_THAT_MIMIC_THE_EFFECTS_OF_THC = "synthetic cannabinoids that mimic the effects of thc"
    NATURAL_AND_SYNTHETIC_TETRAHYDROCANNABINOLS = "natural and synthetic tetrahydrocannabinols"
    CANNABIDIOL = "cannabidiol"


class DopingSubstancesTaxonomyGlucocorticoidsEntry(str, Enum):
    BECLOMETASONE = "beclometasone"
    BETAMETHASONE = "betamethasone"
    BUDESONIDE = "budesonide"
    CICLESONIDE = "ciclesonide"
    CORTISONE = "cortisone"
    DEFLAZACORT = "deflazacort"
    DEXAMETHASONE = "dexamethasone"
    FLUCORTOLONE = "flucortolone"
    FLUNISOLIDE = "flunisolide"
    FLUTICASONE = "fluticasone"
    HYDROCORTISONE = "hydrocortisone"
    METHYLPREDNISOLONE = "methylprednisolone"
    MOMETASONE = "mometasone"
    PREDNISOLONE = "prednisolone"
    PREDNISONE = "prednisone"
    TRIAMCINOLONE_ACETONIDE = "triamcinolone acetonide"


class DopingSubstancesTaxonomyBetaBlockersEntry(str, Enum):
    ACEBUTOLOL = "acebutolol"
    ALPRENOLOL = "alprenolol"
    ATENOLOL = "atenolol"
    BETAXOLOL = "betaxolol"
    BISOPROLOL = "bisoprolol"
    BUNOLOL = "bunolol"
    CARTEOLOL = "carteolol"
    CARVEDILOL = "carvedilol"
    CELIPROLOL = "celiprolol"
    ESMOLOL = "esmolol"
    LABETALOL = "labetalol"
    METIPRANOLOL = "metipranolol"
    METOPROLOL = "metoprolol"
    NADOLOL = "nadolol"
    NEBIVOLOL = "nebivolol"
    OXPRENOLOL = "oxprenolol"
    PINDOLOL = "pindolol"
    PROPRANOLOL = "propranolol"
    SOTALOL = "sotalol"
    TIMOLOL = "timolol"


class DopingSubstancesTaxonomy(BaseModel):
    """Model for the Doping substances taxonomy."""

    namespace: str = "doping-substances"
    description: str = """This taxonomy aims to list doping substances"""
    version: int = 2
    exclusive: bool = False
    predicates: List[DopingSubstancesTaxonomyPredicate] = []
    anabolic_agents_entries: List[DopingSubstancesTaxonomyAnabolicAgentsEntry] = []
    peptide_hormones__growth_factors__related_substances_and_mimetics_entries: List[
        DopingSubstancesTaxonomyPeptideHormonesGrowthFactorsRelatedSubstancesAndMimeticsEntry
    ] = []
    beta_2_agonists_entries: List[DopingSubstancesTaxonomyBeta2AgonistsEntry] = []
    hormone_and_metabolic_modulators_entries: List[DopingSubstancesTaxonomyHormoneAndMetabolicModulatorsEntry] = []
    diuretics_and_masking_agents_entries: List[DopingSubstancesTaxonomyDiureticsAndMaskingAgentsEntry] = []
    stimulants_entries: List[DopingSubstancesTaxonomyStimulantsEntry] = []
    narcotics_entries: List[DopingSubstancesTaxonomyNarcoticsEntry] = []
    cannabinoids_entries: List[DopingSubstancesTaxonomyCannabinoidsEntry] = []
    glucocorticoids_entries: List[DopingSubstancesTaxonomyGlucocorticoidsEntry] = []
    beta_blockers_entries: List[DopingSubstancesTaxonomyBetaBlockersEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
