"""Taxonomy model for death-possibilities."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DeathPossibilitiesTaxonomyPredicate(str, Enum):
    T__001_009__INTESTINAL_INFECTIOUS_DISEASES = "(001-009) Intestinal infectious diseases"
    T__010_018__TUBERCULOSIS = "(010-018) Tuberculosis"
    T__020_027__ZOONOTIC_BACTERIAL_DISEASES = "(020-027) Zoonotic bacterial diseases"
    T__030_041__OTHER_BACTERIAL_DISEASES = "(030-041) Other bacterial diseases"
    T__042_042__HUMAN_IMMUNODEFICIENCY_VIRUS__HIV__INFECTION = "(042-042) Human immunodeficiency virus [HIV] infection"
    T__045_049__POLIOMYELITIS_AND_OTHER_NON_ARTHROPOD_BORNE_VIRAL_DISEASES_OF_CENTRAL_NERVOUS_SYSTEM = (
        "(045-049) Poliomyelitis and other non-arthropod-borne viral diseases of central nervous system"
    )
    T__050_057__VIRAL_DISEASES_ACCOMPANIED_BY_EXANTHEM = "(050-057) Viral diseases accompanied by exanthem"
    T__060_066__ARTHROPOD_BORNE_VIRAL_DISEASES = "(060-066) Arthropod-borne viral diseases"
    T__070_079__OTHER_DISEASES_DUE_TO_VIRUSES_AND_CHLAMYDIAE = "(070-079) Other diseases due to viruses and Chlamydiae"
    T__080_088__RICKETTSIOSES_AND_OTHER_ARTHROPOD_BORNE_DISEASES = (
        "(080-088) Rickettsioses and other arthropod-borne diseases"
    )
    T__090_099__SYPHILIS_AND_OTHER_VENEREAL_DISEASES = "(090-099) Syphilis and other venereal diseases"
    T__100_104__OTHER_SPIROCHAETAL_DISEASES = "(100-104) Other spirochaetal diseases"
    T__110_118__MYCOSES = "(110-118) Mycoses"
    T__120_129__HELMINTHIASES = "(120-129) Helminthiases"
    T__130_136__OTHER_INFECTIOUS_AND_PARASITIC_DISEASES = "(130-136) Other infectious and parasitic diseases"
    T__137_139__LATE_EFFECTS_OF_INFECTIOUS_AND_PARASITIC_DISEASES = (
        "(137-139) Late effects of infectious and parasitic diseases"
    )
    T__140_149__MALIGNANT_NEOPLASM_OF_LIP__ORAL_CAVITY_AND_PHARYNX = (
        "(140-149) Malignant neoplasm of lip, oral cavity and pharynx"
    )
    T__150_159__MALIGNANT_NEOPLASM_OF_DIGESTIVE_ORGANS_AND_PERITONEUM = (
        "(150-159) Malignant neoplasm of digestive organs and peritoneum"
    )
    T__160_165__MALIGNANT_NEOPLASM_OF_RESPIRATORY_AND_INTRATHORACIC_ORGANS = (
        "(160-165) Malignant neoplasm of respiratory and intrathoracic organs"
    )
    T__170_176__MALIGNANT_NEOPLASM_OF_BONE__CONNECTIVE_TISSUE__SKIN_AND_BREAST = (
        "(170-176) Malignant neoplasm of bone, connective tissue, skin and breast"
    )
    T__179_189__MALIGNANT_NEOPLASM_OF_GENITO_URINARY_ORGANS = "(179-189) Malignant neoplasm of genito-urinary organs"
    T__190_199__MALIGNANT_NEOPLASM_OF_OTHER_AND_UNSPECIFIED_SITES = (
        "(190-199) Malignant neoplasm of other and unspecified sites"
    )
    T__200_208__MALIGNANT_NEOPLASM_OF_LYMPHATIC_AND_HAEMATOPOIETIC_TISSUE = (
        "(200-208) Malignant neoplasm of lymphatic and haematopoietic tissue"
    )
    T__210_229__BENIGN_NEOPLASMS = "(210-229) Benign neoplasms"
    T__230_234__CARCINOMA_IN_SITU = "(230-234) Carcinoma in situ"
    T__235_238__NEOPLASMS_OF_UNCERTAIN_BEHAVIOUR = "(235-238) Neoplasms of uncertain behaviour"
    T__239_239__NEOPLASMS_OF_UNSPECIFIED_NATURE = "(239-239) Neoplasms of unspecified nature"
    T__240_246__DISORDERS_OF_THYROID_GLAND = "(240-246) Disorders of thyroid gland"
    T__250_259__DISEASES_OF_OTHER_ENDOCRINE_GLANDS = "(250-259) Diseases of other endocrine glands"
    T__260_269__NUTRITIONAL_DEFICIENCIES = "(260-269) Nutritional deficiencies"
    T__270_279__OTHER_METABOLIC_DISORDERS_AND_IMMUNITY_DISORDERS = (
        "(270-279) Other metabolic disorders and immunity disorders"
    )
    T__280_289__DISEASES_OF_BLOOD_AND_BLOOD_FORMING_ORGANS = "(280-289) Diseases of blood and blood-forming organs"
    T__290_294__ORGANIC_PSYCHOTIC_CONDITIONS = "(290-294) Organic psychotic conditions"
    T__295_299__OTHER_PSYCHOSES = "(295-299) Other psychoses"
    T__300_316__NEUROTIC_DISORDERS__PERSONALITY_DISORDERS_AND_OTHER_NONPSYCHOTIC_MENTAL_DISORDERS = (
        "(300-316) Neurotic disorders, personality disorders and other nonpsychotic mental disorders"
    )
    T__317_319__MENTAL_RETARDATION = "(317-319) Mental retardation"
    T__320_326__INFLAMMATORY_DISEASES_OF_THE_CENTRAL_NERVOUS_SYSTEM = (
        "(320-326) Inflammatory diseases of the central nervous system"
    )
    T__330_337__HEREDITARY_AND_DEGENERATIVE_DISEASES_OF_THE_CENTRAL_NERVOUS_SYSTEM = (
        "(330-337) Hereditary and degenerative diseases of the central nervous system"
    )
    T__340_349__OTHER_DISORDERS_OF_THE_CENTRAL_NERVOUS_SYSTEM = (
        "(340-349) Other disorders of the central nervous system"
    )
    T__350_359__DISORDERS_OF_THE_PERIPHERAL_NERVOUS_SYSTEM = "(350-359) Disorders of the peripheral nervous system"
    T__360_379__DISORDERS_OF_THE_EYE_AND_ADNEXA = "(360-379) Disorders of the eye and adnexa"
    T__380_389__DISEASES_OF_THE_EAR_AND_MASTOID_PROCESS = "(380-389) Diseases of the ear and mastoid process"
    T__390_392__ACUTE_RHEUMATIC_FEVER = "(390-392) Acute rheumatic fever"
    T__393_398__CHRONIC_RHEUMATIC_HEART_DISEASE = "(393-398) Chronic rheumatic heart disease"
    T__401_405__HYPERTENSIVE_DISEASE = "(401-405) Hypertensive disease"
    T__410_414__ISCHAEMIC_HEART_DISEASE = "(410-414) Ischaemic heart disease"
    T__415_417__DISEASES_OF_PULMONARY_CIRCULATION = "(415-417) Diseases of pulmonary circulation"
    T__420_429__OTHER_FORMS_OF_HEART_DISEASE = "(420-429) Other forms of heart disease"
    T__430_438__CEREBROVASCULAR_DISEASE = "(430-438) Cerebrovascular disease"
    T__440_448__DISEASES_OF_ARTERIES__ARTERIOLES_AND_CAPILLARIES = (
        "(440-448) Diseases of arteries, arterioles and capillaries"
    )
    T__451_459__DISEASES_OF_VEINS_AND_LYMPHATICS__AND_OTHER_DISEASES_OF_CIRCULATORY_SYSTEM = (
        "(451-459) Diseases of veins and lymphatics, and other diseases of circulatory system"
    )
    T__460_466__ACUTE_RESPIRATORY_INFECTIONS = "(460-466) Acute respiratory infections"
    T__470_478__OTHER_DISEASES_OF_UPPER_RESPIRATORY_TRACT = "(470-478) Other diseases of upper respiratory tract"
    T__480_487__PNEUMONIA_AND_INFLUENZA = "(480-487) Pneumonia and influenza"
    T__490_496__CHRONIC_OBSTRUCTIVE_PULMONARY_DISEASE_AND_ALLIED_CONDITIONS = (
        "(490-496) Chronic obstructive pulmonary disease and allied conditions"
    )
    T__500_508__PNEUMOCONIOSES_AND_OTHER_LUNG_DISEASES_DUE_TO_EXTERNAL_AGENTS = (
        "(500-508) Pneumoconioses and other lung diseases due to external agents"
    )
    T__510_519__OTHER_DISEASES_OF_RESPIRATORY_SYSTEM = "(510-519) Other diseases of respiratory system"
    T__520_529__DISEASES_OF_ORAL_CAVITY__SALIVARY_GLANDS_AND_JAWS = (
        "(520-529) Diseases of oral cavity, salivary glands and jaws"
    )
    T__530_537__DISEASES_OF_OESOPHAGUS__STOMACH_AND_DUODENUM = "(530-537) Diseases of oesophagus, stomach and duodenum"
    T__540_543__APPENDICITIS = "(540-543) Appendicitis"
    T__550_553__HERNIA_OF_ABDOMINAL_CAVITY = "(550-553) Hernia of abdominal cavity"
    T__555_558__NON_INFECTIVE_ENTERITIS_AND_COLITIS = "(555-558) Non-infective enteritis and colitis"
    T__560_569__OTHER_DISEASES_OF_INTESTINES_AND_PERITONEUM = "(560-569) Other diseases of intestines and peritoneum"
    T__570_579__OTHER_DISEASES_OF_DIGESTIVE_SYSTEM = "(570-579) Other diseases of digestive system"
    T__580_589__NEPHRITIS__NEPHROTIC_SYNDROME_AND_NEPHROSIS = "(580-589) Nephritis, nephrotic syndrome and nephrosis"
    T__590_599__OTHER_DISEASES_OF_URINARY_SYSTEM = "(590-599) Other diseases of urinary system"
    T__600_608__DISEASES_OF_MALE_GENITAL_ORGANS = "(600-608) Diseases of male genital organs"
    T__610_611__DISORDERS_OF_BREAST = "(610-611) Disorders of breast"
    T__614_616__INFLAMMATORY_DISEASE_OF_FEMALE_PELVIC_ORGANS = "(614-616) Inflammatory disease of female pelvic organs"
    T__617_629__OTHER_DISORDERS_OF_FEMALE_GENITAL_TRACT = "(617-629) Other disorders of female genital tract"
    T__630_633__ECTOPIC_AND_MOLAR_PREGNANCY = "(630-633) Ectopic and molar pregnancy"
    T__634_639__OTHER_PREGNANCY_WITH_ABORTIVE_OUTCOME = "(634-639) Other pregnancy with abortive outcome"
    T__640_648__COMPLICATIONS_MAINLY_RELATED_TO_PREGNANCY = "(640-648) Complications mainly related to pregnancy"
    T__650_659__NORMAL_DELIVERY_AND_OTHER_INDICATIONS_FOR_CARE_IN_PREGNANCY__LABOUR_AND_DELIVERY = (
        "(650-659) Normal delivery and other indications for care in pregnancy, labour and delivery"
    )
    T__660_669__COMPLICATIONS_OCCURRING_MAINLY_IN_THE_COURSE_OF_LABOUR_AND_DELIVERY = (
        "(660-669) Complications occurring mainly in the course of labour and delivery"
    )
    T__670_677__COMPLICATIONS_OF_THE_PUERPERIUM = "(670-677) Complications of the puerperium"
    T__680_686__INFECTIONS_OF_SKIN_AND_SUBCUTANEOUS_TISSUE = "(680-686) Infections of skin and subcutaneous tissue"
    T__690_698__OTHER_INFLAMMATORY_CONDITIONS_OF_SKIN_AND_SUBCUTANEOUS_TISSUE = (
        "(690-698) Other inflammatory conditions of skin and subcutaneous tissue"
    )
    T__700_709__OTHER_DISEASES_OF_SKIN_AND_SUBCUTANEOUS_TISSUE = (
        "(700-709) Other diseases of skin and subcutaneous tissue"
    )
    T__710_719__ARTHROPATHIES_AND_RELATED_DISORDERS = "(710-719) Arthropathies and related disorders"
    T__720_724__DORSOPATHIES = "(720-724) Dorsopathies"
    T__725_729__RHEUMATISM__EXCLUDING_THE_BACK = "(725-729) Rheumatism, excluding the back"
    T__730_739__OSTEOPATHIES__CHONDROPATHIES_AND_ACQUIRED_MUSCULOSKELETAL_DEFORMITIES = (
        "(730-739) Osteopathies, chondropathies and acquired musculoskeletal deformities"
    )
    T__740_759__CONGENITAL_ANOMALIES = "(740-759) Congenital anomalies"
    T__760_763__MATERNAL_CAUSES_OF_PERINATAL_MORBIDITY_AND_MORTALITY = (
        "(760-763) Maternal causes of perinatal morbidity and mortality"
    )
    T__764_779__OTHER_CONDITIONS_ORIGINATING_IN_THE_PERINATAL_PERIOD = (
        "(764-779) Other conditions originating in the perinatal period"
    )
    T__780_789__SYMPTOMS = "(780-789) Symptoms"
    T__790_796__NONSPECIFIC_ABNORMAL_FINDINGS = "(790-796) Nonspecific abnormal findings"
    T__797_799__ILL_DEFINED_AND_UNKNOWN_CAUSES_OF_MORBIDITY_AND_MORTALITY = (
        "(797-799) Ill-defined and unknown causes of morbidity and mortality"
    )
    T__800_804__FRACTURE_OF_SKULL = "(800-804) Fracture of skull"
    T__805_809__FRACTURE_OF_NECK_AND_TRUNK = "(805-809) Fracture of neck and trunk"
    T__810_819__FRACTURE_OF_UPPER_LIMB = "(810-819) Fracture of upper limb"
    T__820_829__FRACTURE_OF_LOWER_LIMB = "(820-829) Fracture of lower limb"
    T__830_839__DISLOCATION = "(830-839) Dislocation"
    T__840_848__SPRAINS_AND_STRAINS_OF_JOINTS_AND_ADJACENT_MUSCLES = (
        "(840-848) Sprains and strains of joints and adjacent muscles"
    )
    T__850_854__INTRACRANIAL_INJURY__EXCLUDING_THOSE_WITH_SKULL_FRACTURE = (
        "(850-854) Intracranial injury, excluding those with skull fracture"
    )
    T__860_869__INTERNAL_INJURY_OF_CHEST__ABDOMEN_AND_PELVIS = "(860-869) Internal injury of chest, abdomen and pelvis"
    T__870_879__OPEN_WOUND_OF_HEAD__NECK_AND_TRUNK = "(870-879) Open wound of head, neck and trunk"
    T__880_887__OPEN_WOUND_OF_UPPER_LIMB = "(880-887) Open wound of upper limb"
    T__890_897__OPEN_WOUND_OF_LOWER_LIMB = "(890-897) Open wound of lower limb"
    T__900_904__INJURY_TO_BLOOD_VESSELS = "(900-904) Injury to blood vessels"
    T__905_909__LATE_EFFECTS_OF_INJURIES__POISONINGS__TOXIC_EFFECTS_AND_OTHER_EXTERNAL_CAUSES = (
        "(905-909) Late effects of injuries, poisonings, toxic effects and other external causes"
    )
    T__910_919__SUPERFICIAL_INJURY = "(910-919) Superficial injury"
    T__920_924__CONTUSION_WITH_INTACT_SKIN_SURFACE = "(920-924) Contusion with intact skin surface"
    T__925_929__CRUSHING_INJURY = "(925-929) Crushing injury"
    T__930_939__EFFECTS_OF_FOREIGN_BODY_ENTERING_THROUGH_ORIFICE = (
        "(930-939) Effects of foreign body entering through orifice"
    )
    T__940_949__BURNS = "(940-949) Burns"
    T__950_957__INJURY_TO_NERVES_AND_SPINAL_CORD = "(950-957) Injury to nerves and spinal cord"
    T__958_959__CERTAIN_TRAUMATIC_COMPLICATIONS_AND_UNSPECIFIED_INJURIES = (
        "(958-959) Certain traumatic complications and unspecified injuries"
    )
    T__960_979__POISONING_BY_DRUGS__MEDICAMENTS_AND_BIOLOGICAL_SUBSTANCES = (
        "(960-979) Poisoning by drugs, medicaments and biological substances"
    )
    T__980_989__TOXIC_EFFECTS_OF_SUBSTANCES_CHIEFLY_NONMEDICINAL_AS_TO_SOURCE = (
        "(980-989) Toxic effects of substances chiefly nonmedicinal as to source"
    )
    T__990_995__OTHER_AND_UNSPECIFIED_EFFECTS_OF_EXTERNAL_CAUSES = (
        "(990-995) Other and unspecified effects of external causes"
    )
    T__996_999__COMPLICATIONS_OF_SURGICAL_AND_MEDICAL_CARE__NOT_ELSEWHERE_CLASSIFIED = (
        "(996-999) Complications of surgical and medical care, not elsewhere classified"
    )
    T__E800_E807__RAILWAY_ACCIDENTS = "(E800-E807) Railway accidents"
    T__E810_E819__MOTOR_VEHICLE_TRAFFIC_ACCIDENTS = "(E810-E819) Motor vehicle traffic accidents"
    T__E820_E825__MOTOR_VEHICLE_NONTRAFFIC_ACCIDENTS = "(E820-E825) Motor vehicle nontraffic accidents"
    T__E826_E829__OTHER_ROAD_VEHICLE_ACCIDENTS = "(E826-E829) Other road vehicle accidents"
    T__E830_E838__WATER_TRANSPORT_ACCIDENTS = "(E830-E838) Water transport accidents"
    T__E840_E845__AIR_AND_SPACE_TRANSPORT_ACCIDENTS = "(E840-E845) Air and space transport accidents"
    T__E846_E848__VEHICLE_ACCIDENTS_NOT_ELSEWHERE_CLASSIFIABLE = (
        "(E846-E848) Vehicle accidents not elsewhere classifiable"
    )
    T__E849_E858__ACCIDENTAL_POISONING_BY_DRUGS__MEDICAMENTS_AND_BIOLOGICALS = (
        "(E849-E858) Accidental poisoning by drugs, medicaments and biologicals"
    )
    T__E860_E869__ACCIDENTAL_POISONING_BY_OTHER_SOLID_AND_LIQUID_SUBSTANCES__GASES_AND_VAPOURS = (
        "(E860-E869) Accidental poisoning by other solid and liquid substances, gases and vapours"
    )
    T__E870_E876__MISADVENTURES_TO_PATIENTS_DURING_SURGICAL_AND_MEDICAL_CARE = (
        "(E870-E876) Misadventures to patients during surgical and medical care"
    )
    T__E878_E879__SURGICAL_AND_MEDICAL_PROCEDURES_AS_THE_CAUSE_OF_ABNORMAL_REACTION_OF_PATIENT_OR_LATER_COMPLICATION__WITHOUT_MENTION_OF_MISADVENTURE_AT_THE_TIME_OF_PROCEDURE = "(E878-E879) Surgical and medical procedures as the cause of abnormal reaction of patient or later complication, without mention of misadventure at the time of procedure"
    T__E880_E888__ACCIDENTAL_FALLS = "(E880-E888) Accidental falls"
    T__E890_E899__ACCIDENTS_CAUSED_BY_FIRE_AND_FLAMES = "(E890-E899) Accidents caused by fire and flames"
    T__E900_E909__ACCIDENTS_DUE_TO_NATURAL_AND_ENVIRONMENTAL_FACTORS = (
        "(E900-E909) Accidents due to natural and environmental factors"
    )
    T__E910_E915__ACCIDENTS_CAUSED_BY_SUBMERSION__SUFFOCATION_AND_FOREIGN_BODIES = (
        "(E910-E915) Accidents caused by submersion, suffocation and foreign bodies"
    )
    T__E916_E928__OTHER_ACCIDENTS = "(E916-E928) Other accidents"
    T__E929_E929__LATE_EFFECTS_OF_ACCIDENTAL_INJURY = "(E929-E929) Late effects of accidental injury"
    T__E930_E949__DRUGS__MEDICAMENTS_AND_BIOLOGICAL_SUBSTANCES_CAUSING_ADVERSE_EFFECTS_IN_THERAPEUTIC_USE = (
        "(E930-E949) Drugs, medicaments and biological substances causing adverse effects in therapeutic use"
    )
    T__E950_E959__SUICIDE_AND_SELF_INFLICTED_INJURY = "(E950-E959) Suicide and self-inflicted injury"
    T__E960_E969__HOMICIDE_AND_INJURY_PURPOSELY_INFLICTED_BY_OTHER_PERSONS = (
        "(E960-E969) Homicide and injury purposely inflicted by other persons"
    )


class DeathPossibilitiesTaxonomyT001009IntestinalInfectiousDiseasesEntry(str, Enum):
    T_001_CHOLERA = "001 Cholera"
    T_002_TYPHOID_AND_PARATYPHOID_FEVERS = "002 Typhoid and paratyphoid fevers"
    T_003_OTHER_SALMONELLA_INFECTIONS = "003 Other Salmonella infections"
    T_004_SHIGELLOSIS = "004 Shigellosis"
    T_005_OTHER_FOOD_POISONING__BACTERIAL_ = "005 Other food poisoning (bacterial)"
    T_006_AMOEBIASIS = "006 Amoebiasis"
    T_007_OTHER_PROTOZOAL_INTESTINAL_DISEASES = "007 Other protozoal intestinal diseases"
    T_008_INTESTINAL_INFECTIONS_DUE_TO_OTHER_ORGANISMS = "008 Intestinal infections due to other organisms"
    T_009_ILL_DEFINED_INTESTINAL_INFECTIONS = "009 Ill-defined intestinal infections"


class DeathPossibilitiesTaxonomyT010018TuberculosisEntry(str, Enum):
    T_010_PRIMARY_TUBERCULOUS_INFECTION = "010 Primary tuberculous infection"
    T_011_PULMONARY_TUBERCULOSIS = "011 Pulmonary tuberculosis"
    T_012_OTHER_RESPIRATORY_TUBERCULOSIS = "012 Other respiratory tuberculosis"
    T_013_TUBERCULOSIS_OF_MENINGES_AND_CENTRAL_NERVOUS_SYSTEM = (
        "013 Tuberculosis of meninges and central nervous system"
    )
    T_014_TUBERCULOSIS_OF_INTESTINES__PERITONEUM_AND_MESENTERIC_GLANDS = (
        "014 Tuberculosis of intestines, peritoneum and mesenteric glands"
    )
    T_015_TUBERCULOSIS_OF_BONES_AND_JOINTS = "015 Tuberculosis of bones and joints"
    T_016_TUBERCULOSIS_OF_GENITO_URINARY_SYSTEM = "016 Tuberculosis of genito-urinary system"
    T_017_TUBERCULOSIS_OF_OTHER_ORGANS = "017 Tuberculosis of other organs"
    T_018_MILIARY_TUBERCULOSIS = "018 Miliary tuberculosis"


class DeathPossibilitiesTaxonomyT020027ZoonoticBacterialDiseasesEntry(str, Enum):
    T_020_PLAGUE = "020 Plague"
    T_021_TULARAEMIA = "021 Tularaemia"
    T_022_ANTHRAX = "022 Anthrax"
    T_023_BRUCELLOSIS = "023 Brucellosis"
    T_024_GLANDERS = "024 Glanders"
    T_025_MELIOIDOSIS = "025 Melioidosis"
    T_026_RAT_BITE_FEVER = "026 Rat-bite fever"
    T_027_OTHER_ZOONOTIC_BACTERIAL_DISEASES = "027 Other zoonotic bacterial diseases"


class DeathPossibilitiesTaxonomyT030041OtherBacterialDiseasesEntry(str, Enum):
    T_030_LEPROSY = "030 Leprosy"
    T_031_DISEASES_DUE_TO_OTHER_MYCOBACTERIA = "031 Diseases due to other mycobacteria"
    T_032_DIPHTHERIA = "032 Diphtheria"
    T_033_WHOOPING_COUGH = "033 Whooping cough"
    T_034_STREPTOCOCCAL_SORE_THROAT_AND_SCARLATINA = "034 Streptococcal sore throat and scarlatina"
    T_035_ERYSIPELAS = "035 Erysipelas"
    T_036_MENINGOCOCCAL_INFECTION = "036 Meningococcal infection"
    T_037_TETANUS = "037 Tetanus"
    T_038_SEPTICAEMIA = "038 Septicaemia"
    T_039_ACTINOMYCOTIC_INFECTIONS = "039 Actinomycotic infections"
    T_040_OTHER_BACTERIAL_DISEASES = "040 Other bacterial diseases"
    T_041_BACTERIAL_INFECTION_IN_CONDITIONS_CLASSIFIED_ELSEWHERE_AND_OF_UNSPECIFIED_SITE = (
        "041 Bacterial infection in conditions classified elsewhere and of unspecified site"
    )


class DeathPossibilitiesTaxonomyT042042HumanImmunodeficiencyVirusHivInfectionEntry(str, Enum):
    T_042_HUMAN_IMMUNODEFICIENCY_VIRUS__HIV__DISEASE = "042 Human immunodeficiency virus [HIV] disease"


class DeathPossibilitiesTaxonomyT045049PoliomyelitisAndOtherNonArthropodBorneViralDiseasesOfCentralNervousSystemEntry(
    str, Enum
):
    T_045_ACUTE_POLIOMYELITIS = "045 Acute poliomyelitis"
    T_046_SLOW_VIRUS_INFECTION_OF_CENTRAL_NERVOUS_SYSTEM = "046 Slow virus infection of central nervous system"
    T_047_MENINGITIS_DUE_TO_ENTEROVIRUS = "047 Meningitis due to enterovirus"
    T_048_OTHER_ENTEROVIRUS_DISEASES_OF_CENTRAL_NERVOUS_SYSTEM = (
        "048 Other enterovirus diseases of central nervous system"
    )
    T_049_OTHER_NON_ARTHROPOD_BORNE_VIRAL_DISEASES_OF_CENTRAL_NERVOUS_SYSTEM = (
        "049 Other non-arthropod-borne viral diseases of central nervous system"
    )


class DeathPossibilitiesTaxonomyT050057ViralDiseasesAccompaniedByExanthemEntry(str, Enum):
    T_050_SMALLPOX = "050 Smallpox"
    T_051_COWPOX_AND_PARAVACCINIA = "051 Cowpox and paravaccinia"
    T_052_CHICKENPOX = "052 Chickenpox"
    T_053_HERPES_ZOSTER = "053 Herpes zoster"
    T_054_HERPES_SIMPLEX = "054 Herpes simplex"
    T_055_MEASLES = "055 Measles"
    T_056_RUBELLA = "056 Rubella"
    T_057_OTHER_VIRAL_EXANTHEMATA = "057 Other viral exanthemata"


class DeathPossibilitiesTaxonomyT060066ArthropodBorneViralDiseasesEntry(str, Enum):
    T_060_YELLOW_FEVER = "060 Yellow fever"
    T_061_DENGUE = "061 Dengue"
    T_062_MOSQUITO_BORNE_VIRAL_ENCEPHALITIS = "062 Mosquito-borne viral encephalitis"
    T_063_TICK_BORNE_VIRAL_ENCEPHALITIS = "063 Tick-borne viral encephalitis"
    T_064_VIRAL_ENCEPHALITIS_TRANSMITTED_BY_OTHER_AND_UNSPECIFIED_ARTHROPODS = (
        "064 Viral encephalitis transmitted by other and unspecified arthropods"
    )
    T_065_ARTHROPOD_BORNE_HAEMORRHAGIC_FEVER = "065 Arthropod-borne haemorrhagic fever"
    T_066_OTHER_ARTHROPOD_BORNE_VIRAL_DISEASES = "066 Other arthropod-borne viral diseases"


class DeathPossibilitiesTaxonomyT070079OtherDiseasesDueToVirusesAndChlamydiaeEntry(str, Enum):
    T_070_VIRAL_HEPATITIS = "070 Viral hepatitis"
    T_071_RABIES = "071 Rabies"
    T_072_MUMPS = "072 Mumps"
    T_073_ORNITHOSIS = "073 Ornithosis"
    T_074_SPECIFIC_DISEASES_DUE_TO_COXSACKIE_VIRUS = "074 Specific diseases due to Coxsackie virus"
    T_075_INFECTIOUS_MONONUCLEOSIS = "075 Infectious mononucleosis"
    T_076_TRACHOMA = "076 Trachoma"
    T_077_OTHER_DISEASES_OF_CONJUNCTIVA_DUE_TO_VIRUSES_AND_CHLAMYDIAE = (
        "077 Other diseases of conjunctiva due to viruses and Chlamydiae"
    )
    T_078_OTHER_DISEASES_DUE_TO_VIRUSES_AND_CHLAMYDIAE = "078 Other diseases due to viruses and Chlamydiae"
    T_079_VIRAL_AND_CHLAMYDIAL_INFECTION_IN_CONDITIONS_CLASSIFIED_ELSEWHERE_AND_OF_UNSPECIFIED_SITE = (
        "079 Viral and chlamydial infection in conditions classified elsewhere and of unspecified site"
    )


class DeathPossibilitiesTaxonomyT080088RickettsiosesAndOtherArthropodBorneDiseasesEntry(str, Enum):
    T_080_LOUSE_BORNE__EPIDEMIC__TYPHUS = "080 Louse-borne [epidemic] typhus"
    T_081_OTHER_TYPHUS = "081 Other typhus"
    T_082_TICK_BORNE_RICKETTSIOSES = "082 Tick-borne rickettsioses"
    T_083_OTHER_RICKETTSIOSES = "083 Other rickettsioses"
    T_084_MALARIA = "084 Malaria"
    T_085_LEISHMANIASIS = "085 Leishmaniasis"
    T_086_TRYPANOSOMIASIS = "086 Trypanosomiasis"
    T_087_RELAPSING_FEVER = "087 Relapsing fever"
    T_088_OTHER_ARTHROPOD_BORNE_DISEASES = "088 Other arthropod-borne diseases"


class DeathPossibilitiesTaxonomyT090099SyphilisAndOtherVenerealDiseasesEntry(str, Enum):
    T_090_CONGENITAL_SYPHILIS = "090 Congenital syphilis"
    T_091_EARLY_SYPHILIS__SYMPTOMATIC = "091 Early syphilis, symptomatic"
    T_092_EARLY_SYPHILIS__LATENT = "092 Early syphilis, latent"
    T_093_CARDIOVASCULAR_SYPHILIS = "093 Cardiovascular syphilis"
    T_094_NEUROSYPHILIS = "094 Neurosyphilis"
    T_095_OTHER_FORMS_OF_LATE_SYPHILIS__WITH_SYMPTOMS = "095 Other forms of late syphilis, with symptoms"
    T_096_LATE_SYPHILIS__LATENT = "096 Late syphilis, latent"
    T_097_OTHER_AND_UNSPECIFIED_SYPHILIS = "097 Other and unspecified syphilis"
    T_098_GONOCOCCAL_INFECTIONS = "098 Gonococcal infections"
    T_099_OTHER_VENEREAL_DISEASES = "099 Other venereal diseases"


class DeathPossibilitiesTaxonomyT100104OtherSpirochaetalDiseasesEntry(str, Enum):
    T_100_LEPTOSPIROSIS = "100 Leptospirosis"
    T_101_VINCENT_S_ANGINA = "101 Vincent's angina"
    T_102_YAWS = "102 Yaws"
    T_103_PINTA = "103 Pinta"
    T_104_OTHER_SPIROCHAETAL_INFECTION = "104 Other spirochaetal infection"


class DeathPossibilitiesTaxonomyT110118MycosesEntry(str, Enum):
    T_110_DERMATOPHYTOSIS = "110 Dermatophytosis"
    T_111_DERMATOMYCOSIS__OTHER_AND_UNSPECIFIED = "111 Dermatomycosis, other and unspecified"
    T_112_CANDIDIASIS = "112 Candidiasis"
    T_113_ACTINOMYCOSIS = "113 Actinomycosis"
    T_114_COCCIDIOIDOMYCOSIS = "114 Coccidioidomycosis"
    T_115_HISTOPLASMOSIS = "115 Histoplasmosis"
    T_116_BLASTOMYCOTIC_INFECTION = "116 Blastomycotic infection"
    T_117_OTHER_MYCOSES = "117 Other mycoses"
    T_118_OPPORTUNISTIC_MYCOSES = "118 Opportunistic mycoses"


class DeathPossibilitiesTaxonomyT120129HelminthiasesEntry(str, Enum):
    T_120_SCHISTOSOMIASIS__BILHARZIASIS_ = "120 Schistosomiasis [bilharziasis]"
    T_121_OTHER_TREMATODE_INFECTIONS = "121 Other trematode infections"
    T_122_ECHINOCOCCOSIS = "122 Echinococcosis"
    T_123_OTHER_CESTODE_INFECTION = "123 Other cestode infection"
    T_124_TRICHINOSIS = "124 Trichinosis"
    T_125_FILARIAL_INFECTION_AND_DRACONTIASIS = "125 Filarial infection and dracontiasis"
    T_126_ANKYLOSTOMIASIS_AND_NECATORIASIS = "126 Ankylostomiasis and necatoriasis"
    T_127_OTHER_INTESTINAL_HELMINTHIASES = "127 Other intestinal helminthiases"
    T_128_OTHER_AND_UNSPECIFIED_HELMINTHIASES = "128 Other and unspecified helminthiases"
    T_129_INTESTINAL_PARASITISM__UNSPECIFIED = "129 Intestinal parasitism, unspecified"


class DeathPossibilitiesTaxonomyT130136OtherInfectiousAndParasiticDiseasesEntry(str, Enum):
    T_130_TOXOPLASMOSIS = "130 Toxoplasmosis"
    T_131_TRICHOMONIASIS = "131 Trichomoniasis"
    T_132_PEDICULOSIS_AND_PHTHIRUS_INFESTATION = "132 Pediculosis and phthirus infestation"
    T_133_ACARIASIS = "133 Acariasis"
    T_134_OTHER_INFESTATION = "134 Other infestation"
    T_135_SARCOIDOSIS = "135 Sarcoidosis"
    T_136_OTHER_AND_UNSPECIFIED_INFECTIOUS_AND_PARASITIC_DISEASES = (
        "136 Other and unspecified infectious and parasitic diseases"
    )


class DeathPossibilitiesTaxonomyT137139LateEffectsOfInfectiousAndParasiticDiseasesEntry(str, Enum):
    T_137_LATE_EFFECTS_OF_TUBERCULOSIS = "137 Late effects of tuberculosis"
    T_138_LATE_EFFECTS_OF_ACUTE_POLIOMYELITIS = "138 Late effects of acute poliomyelitis"
    T_139_LATE_EFFECTS_OF_OTHER_INFECTIOUS_AND_PARASITIC_DISEASES = (
        "139 Late effects of other infectious and parasitic diseases"
    )


class DeathPossibilitiesTaxonomyT140149MalignantNeoplasmOfLipOralCavityAndPharynxEntry(str, Enum):
    T_140_MALIGNANT_NEOPLASM_OF_LIP = "140 Malignant neoplasm of lip"
    T_141_MALIGNANT_NEOPLASM_OF_TONGUE = "141 Malignant neoplasm of tongue"
    T_142_MALIGNANT_NEOPLASM_OF_MAJOR_SALIVARY_GLANDS = "142 Malignant neoplasm of major salivary glands"
    T_143_MALIGNANT_NEOPLASM_OF_GUM = "143 Malignant neoplasm of gum"
    T_144_MALIGNANT_NEOPLASM_OF_FLOOR_OF_MOUTH = "144 Malignant neoplasm of floor of mouth"
    T_145_MALIGNANT_NEOPLASM_OF_OTHER_AND_UNSPECIFIED_PARTS_OF_MOUTH = (
        "145 Malignant neoplasm of other and unspecified parts of mouth"
    )
    T_146_MALIGNANT_NEOPLASM_OF_OROPHARYNX = "146 Malignant neoplasm of oropharynx"
    T_147_MALIGNANT_NEOPLASM_OF_NASOPHARYNX = "147 Malignant neoplasm of nasopharynx"
    T_148_MALIGNANT_NEOPLASM_OF_HYPOPHARYNX = "148 Malignant neoplasm of hypopharynx"
    T_149_MALIGNANT_NEOPLASM_OF_OTHER_AND_ILL_DEFINED_SITES_WITHIN_THE_LIP__ORAL_CAVITY_AND_PHARYNX = (
        "149 Malignant neoplasm of other and ill-defined sites within the lip, oral cavity and pharynx"
    )


class DeathPossibilitiesTaxonomyT150159MalignantNeoplasmOfDigestiveOrgansAndPeritoneumEntry(str, Enum):
    T_150_MALIGNANT_NEOPLASM_OF_OESOPHAGUS = "150 Malignant neoplasm of oesophagus"
    T_151_MALIGNANT_NEOPLASM_OF_STOMACH = "151 Malignant neoplasm of stomach"
    T_152_MALIGNANT_NEOPLASM_OF_SMALL_INTESTINE__INCLUDING_DUODENUM = (
        "152 Malignant neoplasm of small intestine, including duodenum"
    )
    T_153_MALIGNANT_NEOPLASM_OF_COLON = "153 Malignant neoplasm of colon"
    T_154_MALIGNANT_NEOPLASM_OF_RECTUM__RECTOSIGMOID_JUNCTION_AND_ANUS = (
        "154 Malignant neoplasm of rectum, rectosigmoid junction and anus"
    )
    T_155_MALIGNANT_NEOPLASM_OF_LIVER_AND_INTRAHEPATIC_BILE_DUCTS = (
        "155 Malignant neoplasm of liver and intrahepatic bile ducts"
    )
    T_156_MALIGNANT_NEOPLASM_OF_GALLBLADDER_AND_EXTRAHEPATIC_BILE_DUCTS = (
        "156 Malignant neoplasm of gallbladder and extrahepatic bile ducts"
    )
    T_157_MALIGNANT_NEOPLASM_OF_PANCREAS = "157 Malignant neoplasm of pancreas"
    T_158_MALIGNANT_NEOPLASM_OF_RETROPERITONEUM_AND_PERITONEUM = (
        "158 Malignant neoplasm of retroperitoneum and peritoneum"
    )
    T_159_MALIGNANT_NEOPLASM_OF_OTHER_AND_ILL_DEFINED_SITES_WITHIN_THE_DIGESTIVE_ORGANS_AND_PERITONEUM = (
        "159 Malignant neoplasm of other and ill-defined sites within the digestive organs and peritoneum"
    )


class DeathPossibilitiesTaxonomyT160165MalignantNeoplasmOfRespiratoryAndIntrathoracicOrgansEntry(str, Enum):
    T_160_MALIGNANT_NEOPLASM_OF_NASAL_CAVITIES__MIDDLE_EAR_AND_ACCESSORY_SINUSES = (
        "160 Malignant neoplasm of nasal cavities, middle ear and accessory sinuses"
    )
    T_161_MALIGNANT_NEOPLASM_OF_LARYNX = "161 Malignant neoplasm of larynx"
    T_162_MALIGNANT_NEOPLASM_OF_TRACHEA__BRONCHUS_AND_LUNG = "162 Malignant neoplasm of trachea, bronchus and lung"
    T_163_MALIGNANT_NEOPLASM_OF_PLEURA = "163 Malignant neoplasm of pleura"
    T_164_MALIGNANT_NEOPLASM_OF_THYMUS__HEART_AND_MEDIASTINUM = (
        "164 Malignant neoplasm of thymus, heart and mediastinum"
    )
    T_165_MALIGNANT_NEOPLASM_OF_OTHER_AND_ILL_DEFINED_SITES_WITHIN_THE_RESPIRATORY_SYSTEM_AND_INTRATHORACIC_ORGANS = (
        "165 Malignant neoplasm of other and ill-defined sites within the respiratory system and intrathoracic organs"
    )


class DeathPossibilitiesTaxonomyT170176MalignantNeoplasmOfBoneConnectiveTissueSkinAndBreastEntry(str, Enum):
    T_170_MALIGNANT_NEOPLASM_OF_BONE_AND_ARTICULAR_CARTILAGE = "170 Malignant neoplasm of bone and articular cartilage"
    T_171_MALIGNANT_NEOPLASM_OF_CONNECTIVE_AND_OTHER_SOFT_TISSUE = (
        "171 Malignant neoplasm of connective and other soft tissue"
    )
    T_172_MALIGNANT_MELANOMA_OF_SKIN = "172 Malignant melanoma of skin"
    T_173_OTHER_MALIGNANT_NEOPLASM_OF_SKIN = "173 Other malignant neoplasm of skin"
    T_174_MALIGNANT_NEOPLASM_OF_FEMALE_BREAST = "174 Malignant neoplasm of female breast"
    T_175_MALIGNANT_NEOPLASM_OF_MALE_BREAST = "175 Malignant neoplasm of male breast"
    T_176_KAPOSI_S_SARCOMA = "176 Kaposi's sarcoma"


class DeathPossibilitiesTaxonomyT179189MalignantNeoplasmOfGenitoUrinaryOrgansEntry(str, Enum):
    T_179_MALIGNANT_NEOPLASM_OF_UTERUS__PART_UNSPECIFIED = "179 Malignant neoplasm of uterus, part unspecified"
    T_180_MALIGNANT_NEOPLASM_OF_CERVIX_UTERI = "180 Malignant neoplasm of cervix uteri"
    T_181_MALIGNANT_NEOPLASM_OF_PLACENTA = "181 Malignant neoplasm of placenta"
    T_182_MALIGNANT_NEOPLASM_OF_BODY_OF_UTERUS = "182 Malignant neoplasm of body of uterus"
    T_183_MALIGNANT_NEOPLASM_OF_OVARY_AND_OTHER_UTERINE_ADNEXA = (
        "183 Malignant neoplasm of ovary and other uterine adnexa"
    )
    T_184_MALIGNANT_NEOPLASM_OF_OTHER_AND_UNSPECIFIED_FEMALE_GENITAL_ORGANS = (
        "184 Malignant neoplasm of other and unspecified female genital organs"
    )
    T_185_MALIGNANT_NEOPLASM_OF_PROSTATE = "185 Malignant neoplasm of prostate"
    T_186_MALIGNANT_NEOPLASM_OF_TESTIS = "186 Malignant neoplasm of testis"
    T_187_MALIGNANT_NEOPLASM_OF_PENIS_AND_OTHER_MALE_GENITAL_ORGANS = (
        "187 Malignant neoplasm of penis and other male genital organs"
    )
    T_188_MALIGNANT_NEOPLASM_OF_BLADDER = "188 Malignant neoplasm of bladder"
    T_189_MALIGNANT_NEOPLASM_OF_KIDNEY_AND_OTHER_AND_UNSPECIFIED_URINARY_ORGANS = (
        "189 Malignant neoplasm of kidney and other and unspecified urinary organs"
    )


class DeathPossibilitiesTaxonomyT190199MalignantNeoplasmOfOtherAndUnspecifiedSitesEntry(str, Enum):
    T_190_MALIGNANT_NEOPLASM_OF_EYE = "190 Malignant neoplasm of eye"
    T_191_MALIGNANT_NEOPLASM_OF_BRAIN = "191 Malignant neoplasm of brain"
    T_192_MALIGNANT_NEOPLASM_OF_OTHER_AND_UNSPECIFIED_PARTS_OF_NERVOUS_SYSTEM = (
        "192 Malignant neoplasm of other and unspecified parts of nervous system"
    )
    T_193_MALIGNANT_NEOPLASM_OF_THYROID_GLAND = "193 Malignant neoplasm of thyroid gland"
    T_194_MALIGNANT_NEOPLASM_OF_OTHER_ENDOCRINE_GLANDS_AND_RELATED_STRUCTURES = (
        "194 Malignant neoplasm of other endocrine glands and related structures"
    )
    T_195_MALIGNANT_NEOPLASM_OF_OTHER_AND_ILL_DEFINED_SITES = "195 Malignant neoplasm of other and ill-defined sites"
    T_196_SECONDARY_AND_UNSPECIFIED_MALIGNANT_NEOPLASM_OF_LYMPH_NODES = (
        "196 Secondary and unspecified malignant neoplasm of lymph nodes"
    )
    T_197_SECONDARY_MALIGNANT_NEOPLASM_OF_RESPIRATORY_AND_DIGESTIVE_SYSTEMS = (
        "197 Secondary malignant neoplasm of respiratory and digestive systems"
    )
    T_198_SECONDARY_MALIGNANT_NEOPLASM_OF_OTHER_SPECIFIED_SITES = (
        "198 Secondary malignant neoplasm of other specified sites"
    )
    T_199_MALIGNANT_NEOPLASM_WITHOUT_SPECIFICATION_OF_SITE = "199 Malignant neoplasm without specification of site"


class DeathPossibilitiesTaxonomyT200208MalignantNeoplasmOfLymphaticAndHaematopoieticTissueEntry(str, Enum):
    T_200_LYMPHOSARCOMA_AND_RETICULOSARCOMA = "200 Lymphosarcoma and reticulosarcoma"
    T_201_HODGKIN_S_DISEASE = "201 Hodgkin's disease"
    T_202_OTHER_MALIGNANT_NEOPLASM_OF_LYMPHOID_AND_HISTIOCYTIC_TISSUE = (
        "202 Other malignant neoplasm of lymphoid and histiocytic tissue"
    )
    T_203_MULTIPLE_MYELOMA_AND_IMMUNOPROLIFERATIVE_NEOPLASMS = "203 Multiple myeloma and immunoproliferative neoplasms"
    T_204_LYMPHOID_LEUKAEMIA = "204 Lymphoid leukaemia"
    T_205_MYELOID_LEUKAEMIA = "205 Myeloid leukaemia"
    T_206_MONOCYTIC_LEUKAEMIA = "206 Monocytic leukaemia"
    T_207_OTHER_SPECIFIED_LEUKAEMIA = "207 Other specified leukaemia"
    T_208_LEUKAEMIA_OF_UNSPECIFIED_CELL_TYPE = "208 Leukaemia of unspecified cell type"


class DeathPossibilitiesTaxonomyT210229BenignNeoplasmsEntry(str, Enum):
    T_210_BENIGN_NEOPLASM_OF_LIP__ORAL_CAVITY_AND_PHARYNX = "210 Benign neoplasm of lip, oral cavity and pharynx"
    T_211_BENIGN_NEOPLASM_OF_OTHER_PARTS_OF_DIGESTIVE_SYSTEM = "211 Benign neoplasm of other parts of digestive system"
    T_212_BENIGN_NEOPLASM_OF_RESPIRATORY_AND_INTRATHORACIC_ORGANS = (
        "212 Benign neoplasm of respiratory and intrathoracic organs"
    )
    T_213_BENIGN_NEOPLASM_OF_BONE_AND_ARTICULAR_CARTILAGE = "213 Benign neoplasm of bone and articular cartilage"
    T_214_LIPOMA = "214 Lipoma"
    T_215_OTHER_BENIGN_NEOPLASM_OF_CONNECTIVE_AND_OTHER_SOFT_TISSUE = (
        "215 Other benign neoplasm of connective and other soft tissue"
    )
    T_216_BENIGN_NEOPLASM_OF_SKIN = "216 Benign neoplasm of skin"
    T_217_BENIGN_NEOPLASM_OF_BREAST = "217 Benign neoplasm of breast"
    T_218_UTERINE_LEIOMYOMA = "218 Uterine leiomyoma"
    T_219_OTHER_BENIGN_NEOPLASM_OF_UTERUS = "219 Other benign neoplasm of uterus"
    T_220_BENIGN_NEOPLASM_OF_OVARY = "220 Benign neoplasm of ovary"
    T_221_BENIGN_NEOPLASM_OF_OTHER_FEMALE_GENITAL_ORGANS = "221 Benign neoplasm of other female genital organs"
    T_222_BENIGN_NEOPLASM_OF_MALE_GENITAL_ORGANS = "222 Benign neoplasm of male genital organs"
    T_223_BENIGN_NEOPLASM_OF_KIDNEY_AND_OTHER_URINARY_ORGANS = "223 Benign neoplasm of kidney and other urinary organs"
    T_224_BENIGN_NEOPLASM_OF_EYE = "224 Benign neoplasm of eye"
    T_225_BENIGN_NEOPLASM_OF_BRAIN_AND_OTHER_PARTS_OF_NERVOUS_SYSTEM = (
        "225 Benign neoplasm of brain and other parts of nervous system"
    )
    T_226_BENIGN_NEOPLASM_OF_THYROID_GLAND = "226 Benign neoplasm of thyroid gland"
    T_227_BENIGN_NEOPLASM_OF_OTHER_ENDOCRINE_GLANDS_AND_RELATED_STRUCTURES = (
        "227 Benign neoplasm of other endocrine glands and related structures"
    )
    T_228_HAEMANGIOMA_AND_LYMPHANGIOMA__ANY_SITE = "228 Haemangioma and lymphangioma, any site"
    T_229_BENIGN_NEOPLASM_OF_OTHER_AND_UNSPECIFIED_SITES = "229 Benign neoplasm of other and unspecified sites"


class DeathPossibilitiesTaxonomyT230234CarcinomaInSituEntry(str, Enum):
    T_230_CARCINOMA_IN_SITU_OF_DIGESTIVE_ORGANS = "230 Carcinoma in situ of digestive organs"
    T_231_CARCINOMA_IN_SITU_OF_RESPIRATORY_SYSTEM = "231 Carcinoma in situ of respiratory system"
    T_232_CARCINOMA_IN_SITU_OF_SKIN = "232 Carcinoma in situ of skin"
    T_233_CARCINOMA_IN_SITU_OF_BREAST_AND_GENITO_URINARY_SYSTEM = (
        "233 Carcinoma in situ of breast and genito-urinary system"
    )
    T_234_CARCINOMA_IN_SITU_OF_OTHER_AND_UNSPECIFIED_SITES = "234 Carcinoma in situ of other and unspecified sites"


class DeathPossibilitiesTaxonomyT235238NeoplasmsOfUncertainBehaviourEntry(str, Enum):
    T_235_NEOPLASM_OF_UNCERTAIN_BEHAVIOUR_OF_DIGESTIVE_AND_RESPIRATORY_SYSTEMS = (
        "235 Neoplasm of uncertain behaviour of digestive and respiratory systems"
    )
    T_236_NEOPLASM_OF_UNCERTAIN_BEHAVIOUR_OF_GENITO_URINARY_ORGANS = (
        "236 Neoplasm of uncertain behaviour of genito-urinary organs"
    )
    T_237_NEOPLASM_OF_UNCERTAIN_BEHAVIOUR_OF_ENDOCRINE_GLANDS_AND_NERVOUS_SYSTEM = (
        "237 Neoplasm of uncertain behaviour of endocrine glands and nervous system"
    )
    T_238_NEOPLASM_OF_UNCERTAIN_BEHAVIOUR_OF_OTHER_AND_UNSPECIFIED_SITES_AND_TISSUES = (
        "238 Neoplasm of uncertain behaviour of other and unspecified sites and tissues"
    )


class DeathPossibilitiesTaxonomyT239239NeoplasmsOfUnspecifiedNatureEntry(str, Enum):
    T_239_NEOPLASM_OF_UNSPECIFIED_NATURE = "239 Neoplasm of unspecified nature"


class DeathPossibilitiesTaxonomyT240246DisordersOfThyroidGlandEntry(str, Enum):
    T_240_SIMPLE_AND_UNSPECIFIED_GOITRE = "240 Simple and unspecified goitre"
    T_241_NON_TOXIC_NODULAR_GOITRE = "241 Non-toxic nodular goitre"
    T_242_THYROTOXICOSIS_WITH_OR_WITHOUT_GOITRE = "242 Thyrotoxicosis with or without goitre"
    T_243_CONGENITAL_HYPOTHYROIDISM = "243 Congenital hypothyroidism"
    T_244_ACQUIRED_HYPOTHYROIDISM = "244 Acquired hypothyroidism"
    T_245_THYROIDITIS = "245 Thyroiditis"
    T_246_OTHER_DISORDERS_OF_THYROID = "246 Other disorders of thyroid"


class DeathPossibilitiesTaxonomyT250259DiseasesOfOtherEndocrineGlandsEntry(str, Enum):
    T_250_DIABETES_MELLITUS = "250 Diabetes mellitus"
    T_251_OTHER_DISORDERS_OF_PANCREATIC_INTERNAL_SECRETION = "251 Other disorders of pancreatic internal secretion"
    T_252_DISORDERS_OF_PARATHYROID_GLAND = "252 Disorders of parathyroid gland"
    T_253_DISORDERS_OF_THE_PITUITARY_GLAND_AND_ITS_HYPOTHALAMIC_CONTROL = (
        "253 Disorders of the pituitary gland and its hypothalamic control"
    )
    T_254_DISEASES_OF_THYMUS_GLAND = "254 Diseases of thymus gland"
    T_255_DISORDERS_OF_ADRENAL_GLANDS = "255 Disorders of adrenal glands"
    T_256_OVARIAN_DYSFUNCTION = "256 Ovarian dysfunction"
    T_257_TESTICULAR_DYSFUNCTION = "257 Testicular dysfunction"
    T_258_POLYGLANDULAR_DYSFUNCTION_AND_RELATED_DISORDERS = "258 Polyglandular dysfunction and related disorders"
    T_259_OTHER_ENDOCRINE_DISORDERS = "259 Other endocrine disorders"


class DeathPossibilitiesTaxonomyT260269NutritionalDeficienciesEntry(str, Enum):
    T_260_KWASHIORKOR = "260 Kwashiorkor"
    T_261_NUTRITIONAL_MARASMUS = "261 Nutritional marasmus"
    T_262_OTHER_SEVERE_PROTEIN_CALORIE_MALNUTRITION = "262 Other severe protein-calorie malnutrition"
    T_263_OTHER_AND_UNSPECIFIED_PROTEIN_CALORIE_MALNUTRITION = "263 Other and unspecified protein-calorie malnutrition"
    T_264_VITAMIN_A_DEFICIENCY = "264 Vitamin A deficiency"
    T_265_THIAMINE_AND_NIACIN_DEFICIENCY_STATES = "265 Thiamine and niacin deficiency states"
    T_266_DEFICIENCY_OF_B_COMPLEX_COMPONENTS = "266 Deficiency of B-complex components"
    T_267_ASCORBIC_ACID_DEFICIENCY = "267 Ascorbic acid deficiency"
    T_268_VITAMIN_D_DEFICIENCY = "268 Vitamin D deficiency"
    T_269_OTHER_NUTRITIONAL_DEFICIENCIES = "269 Other nutritional deficiencies"


class DeathPossibilitiesTaxonomyT270279OtherMetabolicDisordersAndImmunityDisordersEntry(str, Enum):
    T_270_DISORDERS_OF_AMINO_ACID_TRANSPORT_AND_METABOLISM = "270 Disorders of amino-acid transport and metabolism"
    T_271_DISORDERS_OF_CARBOHYDRATE_TRANSPORT_AND_METABOLISM = "271 Disorders of carbohydrate transport and metabolism"
    T_272_DISORDERS_OF_LIPOID_METABOLISM = "272 Disorders of lipoid metabolism"
    T_273_DISORDERS_OF_PLASMA_PROTEIN_METABOLISM = "273 Disorders of plasma protein metabolism"
    T_274_GOUT = "274 Gout"
    T_275_DISORDERS_OF_MINERAL_METABOLISM = "275 Disorders of mineral metabolism"
    T_276_DISORDERS_OF_FLUID__ELECTROLYTE_AND_ACID_BASE_BALANCE = (
        "276 Disorders of fluid, electrolyte and acid-base balance"
    )
    T_277_OTHER_AND_UNSPECIFIED_DISORDERS_OF_METABOLISM = "277 Other and unspecified disorders of metabolism"
    T_278_OBESITY_AND_OTHER_HYPERALIMENTATION = "278 Obesity and other hyperalimentation"
    T_279_DISORDERS_INVOLVING_THE_IMMUNE_MECHANISM = "279 Disorders involving the immune mechanism"


class DeathPossibilitiesTaxonomyT280289DiseasesOfBloodAndBloodFormingOrgansEntry(str, Enum):
    T_280_IRON_DEFICIENCY_ANAEMIAS = "280 Iron deficiency anaemias"
    T_281_OTHER_DEFICIENCY_ANAEMIAS = "281 Other deficiency anaemias"
    T_282_HEREDITARY_HAEMOLYTIC_ANAEMIAS = "282 Hereditary haemolytic anaemias"
    T_283_ACQUIRED_HAEMOLYTIC_ANAEMIAS = "283 Acquired haemolytic anaemias"
    T_284_APLASTIC_ANAEMIA = "284 Aplastic anaemia"
    T_285_OTHER_AND_UNSPECIFIED_ANAEMIAS = "285 Other and unspecified anaemias"
    T_286_COAGULATION_DEFECTS = "286 Coagulation defects"
    T_287_PURPURA_AND_OTHER_HAEMORRHAGIC_CONDITIONS = "287 Purpura and other haemorrhagic conditions"
    T_288_DISEASES_OF_WHITE_BLOOD_CELLS = "288 Diseases of white blood cells"
    T_289_OTHER_DISEASES_OF_BLOOD_AND_BLOOD_FORMING_ORGANS = "289 Other diseases of blood and blood-forming organs"


class DeathPossibilitiesTaxonomyT290294OrganicPsychoticConditionsEntry(str, Enum):
    T_290_SENILE_AND_PRESENILE_ORGANIC_PSYCHOTIC_CONDITIONS = "290 Senile and presenile organic psychotic conditions"
    T_291_ALCOHOLIC_PSYCHOSES = "291 Alcoholic psychoses"
    T_292_DRUG_PSYCHOSES = "292 Drug psychoses"
    T_293_TRANSIENT_ORGANIC_PSYCHOTIC_CONDITIONS = "293 Transient organic psychotic conditions"
    T_294_OTHER_ORGANIC_PSYCHOTIC_CONDITIONS__CHRONIC_ = "294 Other organic psychotic conditions (chronic)"


class DeathPossibilitiesTaxonomyT295299OtherPsychosesEntry(str, Enum):
    T_295_SCHIZOPHRENIC_PSYCHOSES = "295 Schizophrenic psychoses"
    T_296_AFFECTIVE_PSYCHOSES = "296 Affective psychoses"
    T_297_PARANOID_STATES = "297 Paranoid states"
    T_298_OTHER_NONORGANIC_PSYCHOSES = "298 Other nonorganic psychoses"
    T_299_PSYCHOSES_WITH_ORIGIN_SPECIFIC_TO_CHILDHOOD = "299 Psychoses with origin specific to childhood"


class DeathPossibilitiesTaxonomyT300316NeuroticDisordersPersonalityDisordersAndOtherNonpsychoticMentalDisordersEntry(
    str, Enum
):
    T_300_NEUROTIC_DISORDERS = "300 Neurotic disorders"
    T_301_PERSONALITY_DISORDERS = "301 Personality disorders"
    T_302_SEXUAL_DEVIATIONS_AND_DISORDERS = "302 Sexual deviations and disorders"
    T_303_ALCOHOL_DEPENDENCE_SYNDROME = "303 Alcohol dependence syndrome"
    T_304_DRUG_DEPENDENCE = "304 Drug dependence"
    T_305_NONDEPENDENT_ABUSE_OF_DRUGS = "305 Nondependent abuse of drugs"
    T_306_PHYSIOLOGICAL_MALFUNCTION_ARISING_FROM_MENTAL_FACTORS = (
        "306 Physiological malfunction arising from mental factors"
    )
    T_307_SPECIAL_SYMPTOMS_OR_SYNDROMES_NOT_ELSEWHERE_CLASSIFIED = (
        "307 Special symptoms or syndromes not elsewhere classified"
    )
    T_308_ACUTE_REACTION_TO_STRESS = "308 Acute reaction to stress"
    T_309_ADJUSTMENT_REACTION = "309 Adjustment reaction"
    T_310_SPECIFIC_NONPSYCHOTIC_MENTAL_DISORDERS_FOLLOWING_ORGANIC_BRAIN_DAMAGE = (
        "310 Specific nonpsychotic mental disorders following organic brain damage"
    )
    T_311_DEPRESSIVE_DISORDER__NOT_ELSEWHERE_CLASSIFIED = "311 Depressive disorder, not elsewhere classified"
    T_312_DISTURBANCE_OF_CONDUCT_NOT_ELSEWHERE_CLASSIFIED = "312 Disturbance of conduct not elsewhere classified"
    T_313_DISTURBANCE_OF_EMOTIONS_SPECIFIC_TO_CHILDHOOD_AND_ADOLESCENCE = (
        "313 Disturbance of emotions specific to childhood and adolescence"
    )
    T_314_HYPERKINETIC_SYNDROME_OF_CHILDHOOD = "314 Hyperkinetic syndrome of childhood"
    T_315_SPECIFIC_DELAYS_IN_DEVELOPMENT = "315 Specific delays in development"
    T_316_PSYCHIC_FACTORS_ASSOCIATED_WITH_DISEASES_CLASSIFIED_ELSEWHERE = (
        "316 Psychic factors associated with diseases classified elsewhere"
    )


class DeathPossibilitiesTaxonomyT317319MentalRetardationEntry(str, Enum):
    T_317_MILD_MENTAL_RETARDATION = "317 Mild mental retardation"
    T_318_OTHER_SPECIFIED_MENTAL_RETARDATION = "318 Other specified mental retardation"
    T_319_UNSPECIFIED_MENTAL_RETARDATION = "319 Unspecified mental retardation"


class DeathPossibilitiesTaxonomyT320326InflammatoryDiseasesOfTheCentralNervousSystemEntry(str, Enum):
    T_320_BACTERIAL_MENINGITIS = "320 Bacterial meningitis"
    T_321_MENINGITIS_DUE_TO_OTHER_ORGANISMS = "321 Meningitis due to other organisms"
    T_322_MENINGITIS_OF_UNSPECIFIED_CAUSE = "322 Meningitis of unspecified cause"
    T_323_ENCEPHALITIS__MYELITIS_AND_ENCEPHALOMYELITIS = "323 Encephalitis, myelitis and encephalomyelitis"
    T_324_INTRACRANIAL_AND_INTRASPINAL_ABSCESS = "324 Intracranial and intraspinal abscess"
    T_325_PHLEBITIS_AND_THROMBOPHLEBITIS_OF_INTRACRANIAL_VENOUS_SINUSES = (
        "325 Phlebitis and thrombophlebitis of intracranial venous sinuses"
    )
    T_326_LATE_EFFECTS_OF_INTRACRANIAL_ABSCESS_OR_PYOGENIC_INFECTION = (
        "326 Late effects of intracranial abscess or pyogenic infection"
    )


class DeathPossibilitiesTaxonomyT330337HereditaryAndDegenerativeDiseasesOfTheCentralNervousSystemEntry(str, Enum):
    T_330_CEREBRAL_DEGENERATIONS_USUALLY_MANIFEST_IN_CHILDHOOD = (
        "330 Cerebral degenerations usually manifest in childhood"
    )
    T_331_OTHER_CEREBRAL_DEGENERATIONS = "331 Other cerebral degenerations"
    T_332_PARKINSON_S_DISEASE = "332 Parkinson's disease"
    T_333_OTHER_EXTRAPYRAMIDAL_DISEASE_AND_ABNORMAL_MOVEMENT_DISORDERS = (
        "333 Other extrapyramidal disease and abnormal movement disorders"
    )
    T_334_SPINOCEREBELLAR_DISEASE = "334 Spinocerebellar disease"
    T_335_ANTERIOR_HORN_CELL_DISEASE = "335 Anterior horn cell disease"
    T_336_OTHER_DISEASES_OF_SPINAL_CORD = "336 Other diseases of spinal cord"
    T_337_DISORDERS_OF_THE_AUTONOMIC_NERVOUS_SYSTEM = "337 Disorders of the autonomic nervous system"


class DeathPossibilitiesTaxonomyT340349OtherDisordersOfTheCentralNervousSystemEntry(str, Enum):
    T_340_MULTIPLE_SCLEROSIS = "340 Multiple sclerosis"
    T_341_OTHER_DEMYELINATING_DISEASES_OF_CENTRAL_NERVOUS_SYSTEM = (
        "341 Other demyelinating diseases of central nervous system"
    )
    T_342_HEMIPLEGIA = "342 Hemiplegia"
    T_343_INFANTILE_CEREBRAL_PALSY = "343 Infantile cerebral palsy"
    T_344_OTHER_PARALYTIC_SYNDROMES = "344 Other paralytic syndromes"
    T_345_EPILEPSY = "345 Epilepsy"
    T_346_MIGRAINE = "346 Migraine"
    T_347_CATAPLEXY_AND_NARCOLEPSY = "347 Cataplexy and narcolepsy"
    T_348_OTHER_CONDITIONS_OF_BRAIN = "348 Other conditions of brain"
    T_349_OTHER_AND_UNSPECIFIED_DISORDERS_OF_THE_NERVOUS_SYSTEM = (
        "349 Other and unspecified disorders of the nervous system"
    )


class DeathPossibilitiesTaxonomyT350359DisordersOfThePeripheralNervousSystemEntry(str, Enum):
    T_350_TRIGEMINAL_NERVE_DISORDERS = "350 Trigeminal nerve disorders"
    T_351_FACIAL_NERVE_DISORDERS = "351 Facial nerve disorders"
    T_352_DISORDERS_OF_OTHER_CRANIAL_NERVES = "352 Disorders of other cranial nerves"
    T_353_NERVE_ROOT_AND_PLEXUS_DISORDERS = "353 Nerve root and plexus disorders"
    T_354_MONONEURITIS_OF_UPPER_LIMB_AND_MONONEURITIS_MULTIPLEX = (
        "354 Mononeuritis of upper limb and mononeuritis multiplex"
    )
    T_355_MONONEURITIS_OF_LOWER_LIMB = "355 Mononeuritis of lower limb"
    T_356_HEREDITARY_AND_IDIOPATHIC_PERIPHERAL_NEUROPATHY = "356 Hereditary and idiopathic peripheral neuropathy"
    T_357_INFLAMMATORY_AND_TOXIC_NEUROPATHY = "357 Inflammatory and toxic neuropathy"
    T_358_MYONEURAL_DISORDERS = "358 Myoneural disorders"
    T_359_MUSCULAR_DYSTROPHIES_AND_OTHER_MYOPATHIES = "359 Muscular dystrophies and other myopathies"


class DeathPossibilitiesTaxonomyT360379DisordersOfTheEyeAndAdnexaEntry(str, Enum):
    T_360_DISORDERS_OF_THE_GLOBE = "360 Disorders of the globe"
    T_361_RETINAL_DETACHMENTS_AND_DEFECTS = "361 Retinal detachments and defects"
    T_362_OTHER_RETINAL_DISORDERS = "362 Other retinal disorders"
    T_363_CHORIORETINAL_INFLAMMATIONS_AND_SCARS_AND_OTHER_DISORDERS_OF_CHOROID = (
        "363 Chorioretinal inflammations and scars and other disorders of choroid"
    )
    T_364_DISORDERS_OF_IRIS_AND_CILIARY_BODY = "364 Disorders of iris and ciliary body"
    T_365_GLAUCOMA = "365 Glaucoma"
    T_366_CATARACT = "366 Cataract"
    T_367_DISORDERS_OF_REFRACTION_AND_ACCOMMODATION = "367 Disorders of refraction and accommodation"
    T_368_VISUAL_DISTURBANCES = "368 Visual disturbances"
    T_369_BLINDNESS_AND_LOW_VISION = "369 Blindness and low vision"
    T_370_KERATITIS = "370 Keratitis"
    T_371_CORNEAL_OPACITY_AND_OTHER_DISORDERS_OF_CORNEA = "371 Corneal opacity and other disorders of cornea"
    T_372_DISORDERS_OF_CONJUNCTIVA = "372 Disorders of conjunctiva"
    T_373_INFLAMMATION_OF_EYELIDS = "373 Inflammation of eyelids"
    T_374_OTHER_DISORDERS_OF_EYELIDS = "374 Other disorders of eyelids"
    T_375_DISORDERS_OF_LACHRYMAL_SYSTEM = "375 Disorders of lachrymal system"
    T_376_DISORDERS_OF_THE_ORBIT = "376 Disorders of the orbit"
    T_377_DISORDERS_OF_OPTIC_NERVE_AND_VISUAL_PATHWAYS = "377 Disorders of optic nerve and visual pathways"
    T_378_STRABISMUS_AND_OTHER_DISORDERS_OF_BINOCULAR_EYE_MOVEMENTS = (
        "378 Strabismus and other disorders of binocular eye movements"
    )
    T_379_OTHER_DISORDERS_OF_EYE = "379 Other disorders of eye"


class DeathPossibilitiesTaxonomyT380389DiseasesOfTheEarAndMastoidProcessEntry(str, Enum):
    T_380_DISORDERS_OF_EXTERNAL_EAR = "380 Disorders of external ear"
    T_381_NONSUPPURATIVE_OTITIS_MEDIA_AND_EUSTACHIAN_TUBE_DISORDERS = (
        "381 Nonsuppurative otitis media and Eustachian tube disorders"
    )
    T_382_SUPPURATIVE_AND_UNSPECIFIED_OTITIS_MEDIA = "382 Suppurative and unspecified otitis media"
    T_383_MASTOIDITIS_AND_RELATED_CONDITIONS = "383 Mastoiditis and related conditions"
    T_384_OTHER_DISORDERS_OF_TYMPANIC_MEMBRANE = "384 Other disorders of tympanic membrane"
    T_385_OTHER_DISORDERS_OF_MIDDLE_EAR_AND_MASTOID = "385 Other disorders of middle ear and mastoid"
    T_386_VERTIGINOUS_SYNDROMES_AND_OTHER_DISORDERS_OF_VESTIBULAR_SYSTEM = (
        "386 Vertiginous syndromes and other disorders of vestibular system"
    )
    T_387_OTOSCLEROSIS = "387 Otosclerosis"
    T_388_OTHER_DISORDERS_OF_EAR = "388 Other disorders of ear"
    T_389_DEAFNESS = "389 Deafness"


class DeathPossibilitiesTaxonomyT390392AcuteRheumaticFeverEntry(str, Enum):
    T_390_RHEUMATIC_FEVER_WITHOUT_MENTION_OF_HEART_INVOLVEMENT = (
        "390 Rheumatic fever without mention of heart involvement"
    )
    T_391_RHEUMATIC_FEVER_WITH_HEART_INVOLVEMENT = "391 Rheumatic fever with heart involvement"
    T_392_RHEUMATIC_CHOREA = "392 Rheumatic chorea"


class DeathPossibilitiesTaxonomyT393398ChronicRheumaticHeartDiseaseEntry(str, Enum):
    T_393_CHRONIC_RHEUMATIC_PERICARDITIS = "393 Chronic rheumatic pericarditis"
    T_394_DISEASES_OF_MITRAL_VALVE = "394 Diseases of mitral valve"
    T_395_DISEASES_OF_AORTIC_VALVE = "395 Diseases of aortic valve"
    T_396_DISEASES_OF_MITRAL_AND_AORTIC_VALVES = "396 Diseases of mitral and aortic valves"
    T_397_DISEASES_OF_OTHER_ENDOCARDIAL_STRUCTURES = "397 Diseases of other endocardial structures"
    T_398_OTHER_RHEUMATIC_HEART_DISEASE = "398 Other rheumatic heart disease"


class DeathPossibilitiesTaxonomyT401405HypertensiveDiseaseEntry(str, Enum):
    T_401_ESSENTIAL_HYPERTENSION = "401 Essential hypertension"
    T_402_HYPERTENSIVE_HEART_DISEASE = "402 Hypertensive heart disease"
    T_403_HYPERTENSIVE_RENAL_DISEASE = "403 Hypertensive renal disease"
    T_404_HYPERTENSIVE_HEART_AND_RENAL_DISEASE = "404 Hypertensive heart and renal disease"
    T_405_SECONDARY_HYPERTENSION = "405 Secondary hypertension"


class DeathPossibilitiesTaxonomyT410414IschaemicHeartDiseaseEntry(str, Enum):
    T_410_ACUTE_MYOCARDIAL_INFARCTION = "410 Acute myocardial infarction"
    T_411_OTHER_ACUTE_AND_SUBACUTE_FORMS_OF_ISCHAEMIC_HEART_DISEASE = (
        "411 Other acute and subacute forms of ischaemic heart disease"
    )
    T_412_OLD_MYOCARDIAL_INFARCTION = "412 Old myocardial infarction"
    T_413_ANGINA_PECTORIS = "413 Angina pectoris"
    T_414_OTHER_FORMS_OF_CHRONIC_ISCHAEMIC_HEART_DISEASE = "414 Other forms of chronic ischaemic heart disease"


class DeathPossibilitiesTaxonomyT415417DiseasesOfPulmonaryCirculationEntry(str, Enum):
    T_415_ACUTE_PULMONARY_HEART_DISEASE = "415 Acute pulmonary heart disease"
    T_416_CHRONIC_PULMONARY_HEART_DISEASE = "416 Chronic pulmonary heart disease"
    T_417_OTHER_DISEASES_OF_PULMONARY_CIRCULATION = "417 Other diseases of pulmonary circulation"


class DeathPossibilitiesTaxonomyT420429OtherFormsOfHeartDiseaseEntry(str, Enum):
    T_420_ACUTE_PERICARDITIS = "420 Acute pericarditis"
    T_421_ACUTE_AND_SUBACUTE_ENDOCARDITIS = "421 Acute and subacute endocarditis"
    T_422_ACUTE_MYOCARDITIS = "422 Acute myocarditis"
    T_423_OTHER_DISEASES_OF_PERICARDIUM = "423 Other diseases of pericardium"
    T_424_OTHER_DISEASES_OF_ENDOCARDIUM = "424 Other diseases of endocardium"
    T_425_CARDIOMYOPATHY = "425 Cardiomyopathy"
    T_426_CONDUCTION_DISORDERS = "426 Conduction disorders"
    T_427_CARDIAC_DYSRHYTHMIAS = "427 Cardiac dysrhythmias"
    T_428_HEART_FAILURE = "428 Heart failure"
    T_429_ILL_DEFINED_DESCRIPTIONS_AND_COMPLICATIONS_OF_HEART_DISEASE = (
        "429 Ill-defined descriptions and complications of heart disease"
    )


class DeathPossibilitiesTaxonomyT430438CerebrovascularDiseaseEntry(str, Enum):
    T_430_SUBARACHNOID_HAEMORRHAGE = "430 Subarachnoid haemorrhage"
    T_431_INTRACEREBRAL_HAEMORRHAGE = "431 Intracerebral haemorrhage"
    T_432_OTHER_AND_UNSPECIFIED_INTRACRANIAL_HAEMORRHAGE = "432 Other and unspecified intracranial haemorrhage"
    T_433_OCCLUSION_AND_STENOSIS_OF_PRECEREBRAL_ARTERIES = "433 Occlusion and stenosis of precerebral arteries"
    T_434_OCCLUSION_OF_CEREBRAL_ARTERIES = "434 Occlusion of cerebral arteries"
    T_435_TRANSIENT_CEREBRAL_ISCHAEMIA = "435 Transient cerebral ischaemia"
    T_436_ACUTE_BUT_ILL_DEFINED_CEREBROVASCULAR_DISEASE = "436 Acute but ill-defined cerebrovascular disease"
    T_437_OTHER_AND_ILL_DEFINED_CEREBROVASCULAR_DISEASE = "437 Other and ill-defined cerebrovascular disease"
    T_438_LATE_EFFECTS_OF_CEREBROVASCULAR_DISEASE = "438 Late effects of cerebrovascular disease"


class DeathPossibilitiesTaxonomyT440448DiseasesOfArteriesArteriolesAndCapillariesEntry(str, Enum):
    T_440_ATHEROSCLEROSIS = "440 Atherosclerosis"
    T_441_AORTIC_ANEURYSM = "441 Aortic aneurysm"
    T_442_OTHER_ANEURYSM = "442 Other aneurysm"
    T_443_OTHER_PERIPHERAL_VASCULAR_DISEASE = "443 Other peripheral vascular disease"
    T_444_ARTERIAL_EMBOLISM_AND_THROMBOSIS = "444 Arterial embolism and thrombosis"
    T_446_POLYARTERITIS_NODOSA_AND_ALLIED_CONDITIONS = "446 Polyarteritis nodosa and allied conditions"
    T_447_OTHER_DISORDERS_OF_ARTERIES_AND_ARTERIOLES = "447 Other disorders of arteries and arterioles"
    T_448_DISEASES_OF_CAPILLARIES = "448 Diseases of capillaries"


class DeathPossibilitiesTaxonomyT451459DiseasesOfVeinsAndLymphaticsAndOtherDiseasesOfCirculatorySystemEntry(str, Enum):
    T_451_PHLEBITIS_AND_THROMBOPHLEBITIS = "451 Phlebitis and thrombophlebitis"
    T_452_PORTAL_VEIN_THROMBOSIS = "452 Portal vein thrombosis"
    T_453_OTHER_VENOUS_EMBOLISM_AND_THROMBOSIS = "453 Other venous embolism and thrombosis"
    T_454_VARICOSE_VEINS_OF_LOWER_EXTREMITIES = "454 Varicose veins of lower extremities"
    T_455_HAEMORRHOIDS = "455 Haemorrhoids"
    T_456_VARICOSE_VEINS_OF_OTHER_SITES = "456 Varicose veins of other sites"
    T_457_NON_INFECTIVE_DISORDERS_OF_LYMPHATIC_CHANNELS = "457 Non-infective disorders of lymphatic channels"
    T_458_HYPOTENSION = "458 Hypotension"
    T_459_OTHER_DISORDERS_OF_CIRCULATORY_SYSTEM = "459 Other disorders of circulatory system"


class DeathPossibilitiesTaxonomyT460466AcuteRespiratoryInfectionsEntry(str, Enum):
    T_460_ACUTE_NASOPHARYNGITIS__COMMON_COLD_ = "460 Acute nasopharyngitis [common cold]"
    T_461_ACUTE_SINUSITIS = "461 Acute sinusitis"
    T_462_ACUTE_PHARYNGITIS = "462 Acute pharyngitis"
    T_463_ACUTE_TONSILLITIS = "463 Acute tonsillitis"
    T_464_ACUTE_LARYNGITIS_AND_TRACHEITIS = "464 Acute laryngitis and tracheitis"
    T_465_ACUTE_UPPER_RESPIRATORY_INFECTIONS_OF_MULTIPLE_OR_UNSPECIFIED_SITES = (
        "465 Acute upper respiratory infections of multiple or unspecified sites"
    )
    T_466_ACUTE_BRONCHITIS_AND_BRONCHIOLITIS = "466 Acute bronchitis and bronchiolitis"


class DeathPossibilitiesTaxonomyT470478OtherDiseasesOfUpperRespiratoryTractEntry(str, Enum):
    T_470_DEFLECTED_NASAL_SEPTUM = "470 Deflected nasal septum"
    T_471_NASAL_POLYPS = "471 Nasal polyps"
    T_472_CHRONIC_PHARYNGITIS_AND_NASOPHARYNGITIS = "472 Chronic pharyngitis and nasopharyngitis"
    T_473_CHRONIC_SINUSITIS = "473 Chronic sinusitis"
    T_474_CHRONIC_DISEASE_OF_TONSILS_AND_ADENOIDS = "474 Chronic disease of tonsils and adenoids"
    T_475_PERITONSILLAR_ABSCESS = "475 Peritonsillar abscess"
    T_476_CHRONIC_LARYNGITIS_AND_LARYNGOTRACHEITIS = "476 Chronic laryngitis and laryngotracheitis"
    T_477_ALLERGIC_RHINITIS = "477 Allergic rhinitis"
    T_478_OTHER_DISEASES_OF_UPPER_RESPIRATORY_TRACT = "478 Other diseases of upper respiratory tract"


class DeathPossibilitiesTaxonomyT480487PneumoniaAndInfluenzaEntry(str, Enum):
    T_480_VIRAL_PNEUMONIA = "480 Viral pneumonia"
    T_481_PNEUMOCOCCAL_PNEUMONIA = "481 Pneumococcal pneumonia"
    T_482_OTHER_BACTERIAL_PNEUMONIA = "482 Other bacterial pneumonia"
    T_483_PNEUMONIA_DUE_TO_OTHER_SPECIFIED_ORGANISM = "483 Pneumonia due to other specified organism"
    T_484_PNEUMONIA_IN_INFECTIOUS_DISEASES_CLASSIFIED_ELSEWHERE = (
        "484 Pneumonia in infectious diseases classified elsewhere"
    )
    T_485_BRONCHOPNEUMONIA__ORGANISM_UNSPECIFIED = "485 Bronchopneumonia, organism unspecified"
    T_486_PNEUMONIA__ORGANISM_UNSPECIFIED = "486 Pneumonia, organism unspecified"
    T_487_INFLUENZA = "487 Influenza"


class DeathPossibilitiesTaxonomyT490496ChronicObstructivePulmonaryDiseaseAndAlliedConditionsEntry(str, Enum):
    T_490_BRONCHITIS__NOT_SPECIFIED_AS_ACUTE_OR_CHRONIC = "490 Bronchitis, not specified as acute or chronic"
    T_491_CHRONIC_BRONCHITIS = "491 Chronic bronchitis"
    T_492_EMPHYSEMA = "492 Emphysema"
    T_493_ASTHMA = "493 Asthma"
    T_494_BRONCHIECTASIS = "494 Bronchiectasis"
    T_495_EXTRINSIC_ALLERGIC_ALVEOLITIS = "495 Extrinsic allergic alveolitis"
    T_496_CHRONIC_AIRWAYS_OBSTRUCTION__NOT_ELSEWHERE_CLASSIFIED = (
        "496 Chronic airways obstruction, not elsewhere classified"
    )


class DeathPossibilitiesTaxonomyT500508PneumoconiosesAndOtherLungDiseasesDueToExternalAgentsEntry(str, Enum):
    T_500_COALWORKERS__PNEUMOCONIOSIS = "500 Coalworkers' pneumoconiosis"
    T_501_ASBESTOSIS = "501 Asbestosis"
    T_502_PNEUMOCONIOSIS_DUE_TO_OTHER_SILICA_OR_SILICATES = "502 Pneumoconiosis due to other silica or silicates"
    T_503_PNEUMOCONIOSIS_DUE_TO_OTHER_INORGANIC_DUST = "503 Pneumoconiosis due to other inorganic dust"
    T_504_PNEUMOPATHY_DUE_TO_INHALATION_OF_OTHER_DUST = "504 Pneumopathy due to inhalation of other dust"
    T_505_PNEUMOCONIOSIS__UNSPECIFIED = "505 Pneumoconiosis, unspecified"
    T_506_RESPIRATORY_CONDITIONS_DUE_TO_CHEMICAL_FUMES_AND_VAPOURS = (
        "506 Respiratory conditions due to chemical fumes and vapours"
    )
    T_507_PNEUMONITIS_DUE_TO_SOLIDS_AND_LIQUIDS = "507 Pneumonitis due to solids and liquids"
    T_508_RESPIRATORY_CONDITIONS_DUE_TO_OTHER_AND_UNSPECIFIED_EXTERNAL_AGENTS = (
        "508 Respiratory conditions due to other and unspecified external agents"
    )


class DeathPossibilitiesTaxonomyT510519OtherDiseasesOfRespiratorySystemEntry(str, Enum):
    T_510_EMPYEMA = "510 Empyema"
    T_511_PLEURISY = "511 Pleurisy"
    T_512_PNEUMOTHORAX = "512 Pneumothorax"
    T_513_ABSCESS_OF_LUNG_AND_MEDIASTINUM = "513 Abscess of lung and mediastinum"
    T_514_PULMONARY_CONGESTION_AND_HYPOSTASIS = "514 Pulmonary congestion and hypostasis"
    T_515_POSTINFLAMMATORY_PULMONARY_FIBROSIS = "515 Postinflammatory pulmonary fibrosis"
    T_516_OTHER_ALVEOLAR_AND_PARIETOALVEOLAR_PNEUMOPATHY = "516 Other alveolar and parietoalveolar pneumopathy"
    T_517_LUNG_INVOLVEMENT_IN_CONDITIONS_CLASSIFIED_ELSEWHERE = (
        "517 Lung involvement in conditions classified elsewhere"
    )
    T_518_OTHER_DISEASES_OF_LUNG = "518 Other diseases of lung"
    T_519_OTHER_DISEASES_OF_RESPIRATORY_SYSTEM = "519 Other diseases of respiratory system"


class DeathPossibilitiesTaxonomyT520529DiseasesOfOralCavitySalivaryGlandsAndJawsEntry(str, Enum):
    T_520_DISORDERS_OF_TOOTH_DEVELOPMENT_AND_ERUPTION = "520 Disorders of tooth development and eruption"
    T_521_DISEASES_OF_HARD_TISSUES_OF_TEETH = "521 Diseases of hard tissues of teeth"
    T_522_DISEASES_OF_PULP_AND_PERIAPICAL_TISSUES = "522 Diseases of pulp and periapical tissues"
    T_523_GINGIVAL_AND_PERIODONTAL_DISEASES = "523 Gingival and periodontal diseases"
    T_524_DENTOFACIAL_ANOMALIES__INCLUDING_MALOCCLUSION = "524 Dentofacial anomalies, including malocclusion"
    T_525_OTHER_DISEASES_AND_CONDITIONS_OF_THE_TEETH_AND_SUPPORTING_STRUCTURES = (
        "525 Other diseases and conditions of the teeth and supporting structures"
    )
    T_526_DISEASES_OF_THE_JAWS = "526 Diseases of the jaws"
    T_527_DISEASES_OF_THE_SALIVARY_GLANDS = "527 Diseases of the salivary glands"
    T_528_DISEASES_OF_THE_ORAL_SOFT_TISSUES__EXCLUDING_LESIONS_SPECIFIC_FOR_GINGIVA_AND_TONGUE = (
        "528 Diseases of the oral soft tissues, excluding lesions specific for gingiva and tongue"
    )
    T_529_DISEASES_AND_OTHER_CONDITIONS_OF_THE_TONGUE = "529 Diseases and other conditions of the tongue"


class DeathPossibilitiesTaxonomyT530537DiseasesOfOesophagusStomachAndDuodenumEntry(str, Enum):
    T_530_DISEASES_OF_OESOPHAGUS = "530 Diseases of oesophagus"
    T_531_GASTRIC_ULCER = "531 Gastric ulcer"
    T_532_DUODENAL_ULCER = "532 Duodenal ulcer"
    T_533_PEPTIC_ULCER__SITE_UNSPECIFIED = "533 Peptic ulcer, site unspecified"
    T_534_GASTROJEJUNAL_ULCER = "534 Gastrojejunal ulcer"
    T_535_GASTRITIS_AND_DUODENITIS = "535 Gastritis and duodenitis"
    T_536_DISORDERS_OF_FUNCTION_OF_STOMACH = "536 Disorders of function of stomach"
    T_537_OTHER_DISORDERS_OF_STOMACH_AND_DUODENUM = "537 Other disorders of stomach and duodenum"


class DeathPossibilitiesTaxonomyT540543AppendicitisEntry(str, Enum):
    T_540_ACUTE_APPENDICITIS = "540 Acute appendicitis"
    T_541_APPENDICITIS__UNQUALIFIED = "541 Appendicitis, unqualified"
    T_542_OTHER_APPENDICITIS = "542 Other appendicitis"
    T_543_OTHER_DISEASES_OF_APPENDIX = "543 Other diseases of appendix"


class DeathPossibilitiesTaxonomyT550553HerniaOfAbdominalCavityEntry(str, Enum):
    T_550_INGUINAL_HERNIA = "550 Inguinal hernia"
    T_551_OTHER_HERNIA_OF_ABDOMINAL_CAVITY__WITH_GANGRENE = "551 Other hernia of abdominal cavity, with gangrene"
    T_552_OTHER_HERNIA_OF_ABDOMINAL_CAVITY_WITH_OBSTRUCTION__WITHOUT_MENTION_OF_GANGRENE = (
        "552 Other hernia of abdominal cavity with obstruction, without mention of gangrene"
    )
    T_553_OTHER_HERNIA_OF_ABDOMINAL_CAVITY_WITHOUT_MENTION_OF_OBSTRUCTION_OR_GANGRENE = (
        "553 Other hernia of abdominal cavity without mention of obstruction or gangrene"
    )


class DeathPossibilitiesTaxonomyT555558NonInfectiveEnteritisAndColitisEntry(str, Enum):
    T_555_REGIONAL_ENTERITIS = "555 Regional enteritis"
    T_556_IDIOPATHIC_PROCTOCOLITIS = "556 Idiopathic proctocolitis"
    T_557_VASCULAR_INSUFFICIENCY_OF_INTESTINE = "557 Vascular insufficiency of intestine"
    T_558_OTHER_NON_INFECTIVE_GASTRO_ENTERITIS_AND_COLITIS = "558 Other non-infective gastro-enteritis and colitis"


class DeathPossibilitiesTaxonomyT560569OtherDiseasesOfIntestinesAndPeritoneumEntry(str, Enum):
    T_560_INTESTINAL_OBSTRUCTION_WITHOUT_MENTION_OF_HERNIA = "560 Intestinal obstruction without mention of hernia"
    T_562_DIVERTICULA_OF_INTESTINE = "562 Diverticula of intestine"
    T_564_FUNCTIONAL_DIGESTIVE_DISORDERS__NOT_ELSEWHERE_CLASSIFIED = (
        "564 Functional digestive disorders, not elsewhere classified"
    )
    T_565_ANAL_FISSURE_AND_FISTULA = "565 Anal fissure and fistula"
    T_566_ABSCESS_OF_ANAL_AND_RECTAL_REGIONS = "566 Abscess of anal and rectal regions"
    T_567_PERITONITIS = "567 Peritonitis"
    T_568_OTHER_DISORDERS_OF_PERITONEUM = "568 Other disorders of peritoneum"
    T_569_OTHER_DISORDERS_OF_INTESTINE = "569 Other disorders of intestine"


class DeathPossibilitiesTaxonomyT570579OtherDiseasesOfDigestiveSystemEntry(str, Enum):
    T_570_ACUTE_AND_SUBACUTE_NECROSIS_OF_LIVER = "570 Acute and subacute necrosis of liver"
    T_571_CHRONIC_LIVER_DISEASE_AND_CIRRHOSIS = "571 Chronic liver disease and cirrhosis"
    T_572_LIVER_ABSCESS_AND_SEQUELAE_OF_CHRONIC_LIVER_DISEASE = (
        "572 Liver abscess and sequelae of chronic liver disease"
    )
    T_573_OTHER_DISORDERS_OF_LIVER = "573 Other disorders of liver"
    T_574_CHOLELITHIASIS = "574 Cholelithiasis"
    T_575_OTHER_DISORDERS_OF_GALLBLADDER = "575 Other disorders of gallbladder"
    T_576_OTHER_DISORDERS_OF_BILIARY_TRACT = "576 Other disorders of biliary tract"
    T_577_DISEASES_OF_PANCREAS = "577 Diseases of pancreas"
    T_578_GASTRO_INTESTINAL_HAEMORRHAGE = "578 Gastro-intestinal haemorrhage"
    T_579_INTESTINAL_MALABSORPTION = "579 Intestinal malabsorption"


class DeathPossibilitiesTaxonomyT580589NephritisNephroticSyndromeAndNephrosisEntry(str, Enum):
    T_580_ACUTE_GLOMERULONEPHRITIS = "580 Acute glomerulonephritis"
    T_581_NEPHROTIC_SYNDROME = "581 Nephrotic syndrome"
    T_582_CHRONIC_GLOMERULONEPHRITIS = "582 Chronic glomerulonephritis"
    T_583_NEPHRITIS_AND_NEPHROPATHY__NOT_SPECIFIED_AS_ACUTE_OR_CHRONIC = (
        "583 Nephritis and nephropathy, not specified as acute or chronic"
    )
    T_584_ACUTE_RENAL_FAILURE = "584 Acute renal failure"
    T_585_CHRONIC_RENAL_FAILURE = "585 Chronic renal failure"
    T_586_RENAL_FAILURE__UNSPECIFIED = "586 Renal failure, unspecified"
    T_587_RENAL_SCLEROSIS__UNSPECIFIED = "587 Renal sclerosis, unspecified"
    T_588_DISORDERS_RESULTING_FROM_IMPAIRED_RENAL_FUNCTION = "588 Disorders resulting from impaired renal function"
    T_589_SMALL_KIDNEY_OF_UNKNOWN_CAUSE = "589 Small kidney of unknown cause"


class DeathPossibilitiesTaxonomyT590599OtherDiseasesOfUrinarySystemEntry(str, Enum):
    T_590_INFECTIONS_OF_KIDNEY = "590 Infections of kidney"
    T_591_HYDRONEPHROSIS = "591 Hydronephrosis"
    T_592_CALCULUS_OF_KIDNEY_AND_URETER = "592 Calculus of kidney and ureter"
    T_593_OTHER_DISORDERS_OF_KIDNEY_AND_URETER = "593 Other disorders of kidney and ureter"
    T_594_CALCULUS_OF_LOWER_URINARY_TRACT = "594 Calculus of lower urinary tract"
    T_595_CYSTITIS = "595 Cystitis"
    T_596_OTHER_DISORDERS_OF_BLADDER = "596 Other disorders of bladder"
    T_597_URETHRITIS__NOT_SEXUALLY_TRANSMITTED__AND_URETHRAL_SYNDROME = (
        "597 Urethritis, not sexually transmitted, and urethral syndrome"
    )
    T_598_URETHRAL_STRICTURE = "598 Urethral stricture"
    T_599_OTHER_DISORDERS_OF_URETHRA_AND_URINARY_TRACT = "599 Other disorders of urethra and urinary tract"


class DeathPossibilitiesTaxonomyT600608DiseasesOfMaleGenitalOrgansEntry(str, Enum):
    T_600_HYPERPLASIA_OF_PROSTATE = "600 Hyperplasia of prostate"
    T_601_INFLAMMATORY_DISEASES_OF_PROSTATE = "601 Inflammatory diseases of prostate"
    T_602_OTHER_DISORDERS_OF_PROSTATE = "602 Other disorders of prostate"
    T_603_HYDROCELE = "603 Hydrocele"
    T_604_ORCHITIS_AND_EPIDIDYMITIS = "604 Orchitis and epididymitis"
    T_605_REDUNDANT_PREPUCE_AND_PHIMOSIS = "605 Redundant prepuce and phimosis"
    T_606_INFERTILITY__MALE = "606 Infertility, male"
    T_607_DISORDERS_OF_PENIS = "607 Disorders of penis"
    T_608_OTHER_DISORDERS_OF_MALE_GENITAL_ORGANS = "608 Other disorders of male genital organs"


class DeathPossibilitiesTaxonomyT610611DisordersOfBreastEntry(str, Enum):
    T_610_BENIGN_MAMMARY_DYSPLASIAS = "610 Benign mammary dysplasias"
    T_611_OTHER_DISORDERS_OF_BREAST = "611 Other disorders of breast"


class DeathPossibilitiesTaxonomyT614616InflammatoryDiseaseOfFemalePelvicOrgansEntry(str, Enum):
    T_614_INFLAMMATORY_DISEASE_OF_OVARY__FALLOPIAN_TUBE__PELVIC_CELLULAR_TISSUE_AND_PERITONEUM = (
        "614 Inflammatory disease of ovary, Fallopian tube, pelvic cellular tissue and peritoneum"
    )
    T_615_INFLAMMATORY_DISEASES_OF_UTERUS__EXCEPT_CERVIX = "615 Inflammatory diseases of uterus, except cervix"
    T_616_INFLAMMATORY_DISEASE_OF_CERVIX__VAGINA_AND_VULVA = "616 Inflammatory disease of cervix, vagina and vulva"


class DeathPossibilitiesTaxonomyT617629OtherDisordersOfFemaleGenitalTractEntry(str, Enum):
    T_617_ENDOMETRIOSIS = "617 Endometriosis"
    T_618_GENITAL_PROLAPSE = "618 Genital prolapse"
    T_619_FISTULAE_INVOLVING_FEMALE_GENITAL_TRACT = "619 Fistulae involving female genital tract"
    T_620_NONINFLAMMATORY_DISORDERS_OF_OVARY__FALLOPIAN_TUBE_AND_BROAD_LIGAMENT = (
        "620 Noninflammatory disorders of ovary, Fallopian tube and broad ligament"
    )
    T_621_DISORDERS_OF_UTERUS__NOT_ELSEWHERE_CLASSIFIED = "621 Disorders of uterus, not elsewhere classified"
    T_622_NONINFLAMMATORY_DISORDERS_OF_CERVIX = "622 Noninflammatory disorders of cervix"
    T_623_NONINFLAMMATORY_DISORDERS_OF_VAGINA = "623 Noninflammatory disorders of vagina"
    T_624_NONINFLAMMATORY_DISORDERS_OF_VULVA_AND_PERINEUM = "624 Noninflammatory disorders of vulva and perineum"
    T_625_PAIN_AND_OTHER_SYMPTOMS_ASSOCIATED_WITH_FEMALE_GENITAL_ORGANS = (
        "625 Pain and other symptoms associated with female genital organs"
    )
    T_626_DISORDERS_OF_MENSTRUATION_AND_OTHER_ABNORMAL_BLEEDING_FROM_FEMALE_GENITAL_TRACT = (
        "626 Disorders of menstruation and other abnormal bleeding from female genital tract"
    )
    T_627_MENOPAUSAL_AND_POSTMENOPAUSAL_DISORDERS = "627 Menopausal and postmenopausal disorders"
    T_628_INFERTILITY__FEMALE = "628 Infertility, female"
    T_629_OTHER_DISORDERS_OF_FEMALE_GENITAL_ORGANS = "629 Other disorders of female genital organs"


class DeathPossibilitiesTaxonomyT630633EctopicAndMolarPregnancyEntry(str, Enum):
    T_630_HYDATIDIFORM_MOLE = "630 Hydatidiform mole"
    T_631_OTHER_ABNORMAL_PRODUCT_OF_CONCEPTION = "631 Other abnormal product of conception"
    T_632_MISSED_ABORTION = "632 Missed abortion"
    T_633_ECTOPIC_PREGNANCY = "633 Ectopic pregnancy"


class DeathPossibilitiesTaxonomyT634639OtherPregnancyWithAbortiveOutcomeEntry(str, Enum):
    T_634_SPONTANEOUS_ABORTION = "634 Spontaneous abortion"
    T_635_LEGALLY_INDUCED_ABORTION = "635 Legally induced abortion"
    T_636_ILLEGALLY_INDUCED_ABORTION = "636 Illegally induced abortion"
    T_637_UNSPECIFIED_ABORTION = "637 Unspecified abortion"
    T_638_FAILED_ATTEMPTED_ABORTION = "638 Failed attempted abortion"
    T_639_COMPLICATIONS_FOLLOWING_ABORTION_AND_ECTOPIC_AND_MOLAR_PREGNANCIES = (
        "639 Complications following abortion and ectopic and molar pregnancies"
    )


class DeathPossibilitiesTaxonomyT640648ComplicationsMainlyRelatedToPregnancyEntry(str, Enum):
    T_640_HAEMORRHAGE_IN_EARLY_PREGNANCY = "640 Haemorrhage in early pregnancy"
    T_641_ANTEPARTUM_HAEMORRHAGE__ABRUPTIO_PLACENTAE_AND_PLACENTA_PRAEVIA = (
        "641 Antepartum haemorrhage, abruptio placentae and placenta praevia"
    )
    T_642_HYPERTENSION_COMPLICATING_PREGNANCY__CHILDBIRTH_AND_THE_PUERPERIUM = (
        "642 Hypertension complicating pregnancy, childbirth and the puerperium"
    )
    T_643_EXCESSIVE_VOMITING_IN_PREGNANCY = "643 Excessive vomiting in pregnancy"
    T_644_EARLY_OR_THREATENED_LABOUR = "644 Early or threatened labour"
    T_645_PROLONGED_PREGNANCY = "645 Prolonged pregnancy"
    T_646_OTHER_COMPLICATIONS_OF_PREGNANCY__NOT_ELSEWHERE_CLASSIFIED = (
        "646 Other complications of pregnancy, not elsewhere classified"
    )
    T_647_INFECTIVE_AND_PARASITIC_CONDITIONS_IN_THE_MOTHER_CLASSIFIABLE_ELSEWHERE_BUT_COMPLICATING_PREGNANCY__CHILDBIRTH_AND_THE_PUERPERIUM = "647 Infective and parasitic conditions in the mother classifiable elsewhere but complicating pregnancy, childbirth and the puerperium"
    T_648_OTHER_CURRENT_CONDITIONS_IN_THE_MOTHER_CLASSIFIABLE_ELSEWHERE_BUT_COMPLICATING_PREGNANCY__CHILDBIRTH_AND_THE_PUERPERIUM = "648 Other current conditions in the mother classifiable elsewhere but complicating pregnancy, childbirth and the puerperium"


class DeathPossibilitiesTaxonomyT650659NormalDeliveryAndOtherIndicationsForCareInPregnancyLabourAndDeliveryEntry(
    str, Enum
):
    T_650_DELIVERY_IN_A_COMPLETELY_NORMAL_CASE = "650 Delivery in a completely normal case"
    T_651_MULTIPLE_GESTATION = "651 Multiple gestation"
    T_652_MALPOSITION_AND_MALPRESENTATION_OF_FOETUS = "652 Malposition and malpresentation of foetus"
    T_653_DISPROPORTION = "653 Disproportion"
    T_654_ABNORMALITY_OF_ORGANS_AND_SOFT_TISSUES_OF_PELVIS = "654 Abnormality of organs and soft tissues of pelvis"
    T_655_KNOWN_OR_SUSPECTED_FOETAL_ABNORMALITY_AFFECTING_MANAGEMENT_OF_MOTHER = (
        "655 Known or suspected foetal abnormality affecting management of mother"
    )
    T_656_OTHER_FOETAL_AND_PLACENTAL_PROBLEMS_AFFECTING_MANAGEMENT_OF_MOTHER = (
        "656 Other foetal and placental problems affecting management of mother"
    )
    T_657_POLYHYDRAMNIOS = "657 Polyhydramnios"
    T_658_OTHER_PROBLEMS_ASSOCIATED_WITH_AMNIOTIC_CAVITY_AND_MEMBRANES = (
        "658 Other problems associated with amniotic cavity and membranes"
    )
    T_659_OTHER_INDICATIONS_FOR_CARE_OR_INTERVENTION_RELATED_TO_LABOUR_AND_DELIVERY_AND_NOT_ELSEWHERE_CLASSIFIED = (
        "659 Other indications for care or intervention related to labour and delivery and not elsewhere classified"
    )


class DeathPossibilitiesTaxonomyT660669ComplicationsOccurringMainlyInTheCourseOfLabourAndDeliveryEntry(str, Enum):
    T_660_OBSTRUCTED_LABOUR = "660 Obstructed labour"
    T_661_ABNORMALITY_OF_FORCES_OF_LABOUR = "661 Abnormality of forces of labour"
    T_662_LONG_LABOUR = "662 Long labour"
    T_663_UMBILICAL_CORD_COMPLICATIONS = "663 Umbilical cord complications"
    T_664_TRAUMA_TO_PERINEUM_AND_VULVA_DURING_DELIVERY = "664 Trauma to perineum and vulva during delivery"
    T_665_OTHER_OBSTETRICAL_TRAUMA = "665 Other obstetrical trauma"
    T_666_POSTPARTUM_HAEMORRHAGE = "666 Postpartum haemorrhage"
    T_667_RETAINED_PLACENTA_OR_MEMBRANES__WITHOUT_HAEMORRHAGE = (
        "667 Retained placenta or membranes, without haemorrhage"
    )
    T_668_COMPLICATIONS_OF_THE_ADMINISTRATION_OF_ANAESTHETIC_OR_OTHER_SEDATION_IN_LABOUR_AND_DELIVERY = (
        "668 Complications of the administration of anaesthetic or other sedation in labour and delivery"
    )
    T_669_OTHER_COMPLICATIONS_OF_LABOUR_AND_DELIVERY__NOT_ELSEWHERE_CLASSIFIED = (
        "669 Other complications of labour and delivery, not elsewhere classified"
    )


class DeathPossibilitiesTaxonomyT670677ComplicationsOfThePuerperiumEntry(str, Enum):
    T_670_MAJOR_PUERPERAL_INFECTION = "670 Major puerperal infection"
    T_671_VENOUS_COMPLICATIONS_IN_PREGNANCY_AND_THE_PUERPERIUM = (
        "671 Venous complications in pregnancy and the puerperium"
    )
    T_672_PYREXIA_OF_UNKNOWN_ORIGIN_DURING_THE_PUERPERIUM = "672 Pyrexia of unknown origin during the puerperium"
    T_673_OBSTETRICAL_PULMONARY_EMBOLISM = "673 Obstetrical pulmonary embolism"
    T_674_OTHER_AND_UNSPECIFIED_COMPLICATIONS_OF_THE_PUERPERIUM__NOT_ELSEWHERE_CLASSIFIED = (
        "674 Other and unspecified complications of the puerperium, not elsewhere classified"
    )
    T_675_INFECTIONS_OF_THE_BREAST_AND_NIPPLE_ASSOCIATED_WITH_CHILDBIRTH = (
        "675 Infections of the breast and nipple associated with childbirth"
    )
    T_676_OTHER_DISORDERS_OF_THE_BREAST_ASSOCIATED_WITH_CHILDBIRTH__AND_DISORDERS_OF_LACTATION = (
        "676 Other disorders of the breast associated with childbirth, and disorders of lactation"
    )
    T_677_LATE_EFFECT_OF_COMPLICATION_OF_PREGNANCY__CHILDBIRTH_AND_THE_PUERPERIUM = (
        "677 Late effect of complication of pregnancy, childbirth and the puerperium"
    )


class DeathPossibilitiesTaxonomyT680686InfectionsOfSkinAndSubcutaneousTissueEntry(str, Enum):
    T_680_CARBUNCLE_AND_FURUNCLE = "680 Carbuncle and furuncle"
    T_681_CELLULITIS_AND_ABSCESS_OF_FINGER_AND_TOE = "681 Cellulitis and abscess of finger and toe"
    T_682_OTHER_CELLULITIS_AND_ABSCESS = "682 Other cellulitis and abscess"
    T_683_ACUTE_LYMPHADENITIS = "683 Acute lymphadenitis"
    T_684_IMPETIGO = "684 Impetigo"
    T_685_PILONIDAL_CYST = "685 Pilonidal cyst"
    T_686_OTHER_LOCAL_INFECTIONS_OF_SKIN_AND_SUBCUTANEOUS_TISSUE = (
        "686 Other local infections of skin and subcutaneous tissue"
    )


class DeathPossibilitiesTaxonomyT690698OtherInflammatoryConditionsOfSkinAndSubcutaneousTissueEntry(str, Enum):
    T_690_ERYTHEMATOSQUAMOUS_DERMATOSIS = "690 Erythematosquamous dermatosis"
    T_691_ATOPIC_DERMATITIS_AND_RELATED_CONDITIONS = "691 Atopic dermatitis and related conditions"
    T_692_CONTACT_DERMATITIS_AND_OTHER_ECZEMA = "692 Contact dermatitis and other eczema"
    T_693_DERMATITIS_DUE_TO_SUBSTANCES_TAKEN_INTERNALLY = "693 Dermatitis due to substances taken internally"
    T_694_BULLOUS_DERMATOSES = "694 Bullous dermatoses"
    T_695_ERYTHEMATOUS_CONDITIONS = "695 Erythematous conditions"
    T_696_PSORIASIS_AND_SIMILAR_DISORDERS = "696 Psoriasis and similar disorders"
    T_697_LICHEN = "697 Lichen"
    T_698_PRURITUS_AND_RELATED_CONDITIONS = "698 Pruritus and related conditions"


class DeathPossibilitiesTaxonomyT700709OtherDiseasesOfSkinAndSubcutaneousTissueEntry(str, Enum):
    T_700_CORNS_AND_CALLOSITIES = "700 Corns and callosities"
    T_701_OTHER_HYPERTROPHIC_AND_ATROPHIC_CONDITIONS_OF_SKIN = "701 Other hypertrophic and atrophic conditions of skin"
    T_702_OTHER_DERMATOSES = "702 Other dermatoses"
    T_703_DISEASES_OF_NAIL = "703 Diseases of nail"
    T_704_DISEASES_OF_HAIR_AND_HAIR_FOLLICLES = "704 Diseases of hair and hair follicles"
    T_705_DISORDERS_OF_SWEAT_GLANDS = "705 Disorders of sweat glands"
    T_706_DISEASES_OF_SEBACEOUS_GLANDS = "706 Diseases of sebaceous glands"
    T_707_CHRONIC_ULCER_OF_SKIN = "707 Chronic ulcer of skin"
    T_708_URTICARIA = "708 Urticaria"
    T_709_OTHER_DISORDERS_OF_SKIN_AND_SUBCUTANEOUS_TISSUE = "709 Other disorders of skin and subcutaneous tissue"


class DeathPossibilitiesTaxonomyT710719ArthropathiesAndRelatedDisordersEntry(str, Enum):
    T_710_DIFFUSE_DISEASES_OF_CONNECTIVE_TISSUE = "710 Diffuse diseases of connective tissue"
    T_711_ARTHROPATHY_ASSOCIATED_WITH_INFECTIONS = "711 Arthropathy associated with infections"
    T_712_CRYSTAL_ARTHROPATHIES = "712 Crystal arthropathies"
    T_713_ARTHROPATHY_ASSOCIATED_WITH_OTHER_DISORDERS_CLASSIFIED_ELSEWHERE = (
        "713 Arthropathy associated with other disorders classified elsewhere"
    )
    T_714_RHEUMATOID_ARTHRITIS_AND_OTHER_INFLAMMATORY_POLYARTHROPATHIES = (
        "714 Rheumatoid arthritis and other inflammatory polyarthropathies"
    )
    T_715_OSTEO_ARTHROSIS_AND_ALLIED_DISORDERS = "715 Osteo-arthrosis and allied disorders"
    T_716_OTHER_AND_UNSPECIFIED_ARTHROPATHIES = "716 Other and unspecified arthropathies"
    T_717_INTERNAL_DERANGEMENT_OF_KNEE = "717 Internal derangement of knee"
    T_718_OTHER_DERANGEMENT_OF_JOINT = "718 Other derangement of joint"
    T_719_OTHER_AND_UNSPECIFIED_DISORDER_OF_JOINT = "719 Other and unspecified disorder of joint"


class DeathPossibilitiesTaxonomyT720724DorsopathiesEntry(str, Enum):
    T_720_ANKYLOSING_SPONDYLITIS_AND_OTHER_INFLAMMATORY_SPONDYLOPATHIES = (
        "720 Ankylosing spondylitis and other inflammatory spondylopathies"
    )
    T_721_SPONDYLOSIS_AND_ALLIED_DISORDERS = "721 Spondylosis and allied disorders"
    T_722_INTERVERTEBRAL_DISK_DISORDERS = "722 Intervertebral disk disorders"
    T_723_OTHER_DISORDERS_OF_CERVICAL_REGION = "723 Other disorders of cervical region"
    T_724_OTHER_AND_UNSPECIFIED_DISORDERS_OF_BACK = "724 Other and unspecified disorders of back"


class DeathPossibilitiesTaxonomyT725729RheumatismExcludingTheBackEntry(str, Enum):
    T_725_POLYMYALGIA_RHEUMATICA = "725 Polymyalgia rheumatica"
    T_726_PERIPHERAL_ENTHESOPATHIES_AND_ALLIED_SYNDROMES = "726 Peripheral enthesopathies and allied syndromes"
    T_727_OTHER_DISORDERS_OF_SYNOVIUM__TENDON_AND_BURSA = "727 Other disorders of synovium, tendon and bursa"
    T_728_DISORDERS_OF_MUSCLE__LIGAMENT_AND_FASCIA = "728 Disorders of muscle, ligament and fascia"
    T_729_OTHER_DISORDERS_OF_SOFT_TISSUES = "729 Other disorders of soft tissues"


class DeathPossibilitiesTaxonomyT730739OsteopathiesChondropathiesAndAcquiredMusculoskeletalDeformitiesEntry(str, Enum):
    T_730_OSTEOMYELITIS__PERIOSTITIS_AND_OTHER_INFECTIONS_INVOLVING_BONE = (
        "730 Osteomyelitis, periostitis and other infections involving bone"
    )
    T_731_OSTEITIS_DEFORMANS_AND_OSTEOPATHIES_ASSOCIATED_WITH_OTHER_DISORDERS_CLASSIFIED_ELSEWHERE = (
        "731 Osteitis deformans and osteopathies associated with other disorders classified elsewhere"
    )
    T_732_OSTEOCHONDROPATHIES = "732 Osteochondropathies"
    T_733_OTHER_DISORDERS_OF_BONE_AND_CARTILAGE = "733 Other disorders of bone and cartilage"
    T_734_FLAT_FOOT = "734 Flat foot"
    T_735_ACQUIRED_DEFORMITIES_OF_TOE = "735 Acquired deformities of toe"
    T_736_OTHER_ACQUIRED_DEFORMITIES_OF_LIMBS = "736 Other acquired deformities of limbs"
    T_737_CURVATURE_OF_SPINE = "737 Curvature of spine"
    T_738_OTHER_ACQUIRED_DEFORMITY = "738 Other acquired deformity"
    T_739_NONALLOPATHIC_LESIONS__NOT_ELSEWHERE_CLASSIFIED = "739 Nonallopathic lesions, not elsewhere classified"


class DeathPossibilitiesTaxonomyT740759CongenitalAnomaliesEntry(str, Enum):
    T_740_ANENCEPHALUS_AND_SIMILAR_ANOMALIES = "740 Anencephalus and similar anomalies"
    T_741_SPINA_BIFIDA = "741 Spina bifida"
    T_742_OTHER_CONGENITAL_ANOMALIES_OF_NERVOUS_SYSTEM = "742 Other congenital anomalies of nervous system"
    T_743_CONGENITAL_ANOMALIES_OF_EYE = "743 Congenital anomalies of eye"
    T_744_CONGENITAL_ANOMALIES_OF_EAR__FACE_AND_NECK = "744 Congenital anomalies of ear, face and neck"
    T_745_BULBUS_CORDIS_ANOMALIES_AND_ANOMALIES_OF_CARDIAC_SEPTAL_CLOSURE = (
        "745 Bulbus cordis anomalies and anomalies of cardiac septal closure"
    )
    T_746_OTHER_CONGENITAL_ANOMALIES_OF_HEART = "746 Other congenital anomalies of heart"
    T_747_OTHER_CONGENITAL_ANOMALIES_OF_CIRCULATORY_SYSTEM = "747 Other congenital anomalies of circulatory system"
    T_748_CONGENITAL_ANOMALIES_OF_RESPIRATORY_SYSTEM = "748 Congenital anomalies of respiratory system"
    T_749_CLEFT_PALATE_AND_CLEFT_LIP = "749 Cleft palate and cleft lip"
    T_750_OTHER_CONGENITAL_ANOMALIES_OF_UPPER_ALIMENTARY_TRACT = (
        "750 Other congenital anomalies of upper alimentary tract"
    )
    T_751_OTHER_CONGENITAL_ANOMALIES_OF_DIGESTIVE_SYSTEM = "751 Other congenital anomalies of digestive system"
    T_752_CONGENITAL_ANOMALIES_OF_GENITAL_ORGANS = "752 Congenital anomalies of genital organs"
    T_753_CONGENITAL_ANOMALIES_OF_URINARY_SYSTEM = "753 Congenital anomalies of urinary system"
    T_754_CERTAIN_CONGENITAL_MUSCULOSKELETAL_DEFORMITIES = "754 Certain congenital musculoskeletal deformities"
    T_755_OTHER_CONGENITAL_ANOMALIES_OF_LIMBS = "755 Other congenital anomalies of limbs"
    T_756_OTHER_CONGENITAL_MUSCULOSKELETAL_ANOMALIES = "756 Other congenital musculoskeletal anomalies"
    T_757_CONGENITAL_ANOMALIES_OF_THE_INTEGUMENT = "757 Congenital anomalies of the integument"
    T_758_CHROMOSOMAL_ANOMALIES = "758 Chromosomal anomalies"
    T_759_OTHER_AND_UNSPECIFIED_CONGENITAL_ANOMALIES = "759 Other and unspecified congenital anomalies"


class DeathPossibilitiesTaxonomyT760763MaternalCausesOfPerinatalMorbidityAndMortalityEntry(str, Enum):
    T_760_FOETUS_OR_NEWBORN_AFFECTED_BY_MATERNAL_CONDITIONS_WHICH_MAY_BE_UNRELATED_TO_PRESENT_PREGNANCY = (
        "760 Foetus or newborn affected by maternal conditions which may be unrelated to present pregnancy"
    )
    T_761_FOETUS_OR_NEWBORN_AFFECTED_BY_MATERNAL_COMPLICATIONS_OF_PREGNANCY = (
        "761 Foetus or newborn affected by maternal complications of pregnancy"
    )
    T_762_FOETUS_OR_NEWBORN_AFFECTED_BY_COMPLICATIONS_OF_PLACENTA__CORD_AND_MEMBRANES = (
        "762 Foetus or newborn affected by complications of placenta, cord and membranes"
    )
    T_763_FOETUS_OR_NEWBORN_AFFECTED_BY_OTHER_COMPLICATIONS_OF_LABOUR_AND_DELIVERY = (
        "763 Foetus or newborn affected by other complications of labour and delivery"
    )


class DeathPossibilitiesTaxonomyT764779OtherConditionsOriginatingInThePerinatalPeriodEntry(str, Enum):
    T_764_SLOW_FOETAL_GROWTH_AND_FOETAL_MALNUTRITION = "764 Slow foetal growth and foetal malnutrition"
    T_765_DISORDERS_RELATING_TO_SHORT_GESTATION_AND_UNSPECIFIED_LOW_BIRTHWEIGHT = (
        "765 Disorders relating to short gestation and unspecified low birthweight"
    )
    T_766_DISORDERS_RELATING_TO_LONG_GESTATION_AND_HIGH_BIRTHWEIGHT = (
        "766 Disorders relating to long gestation and high birthweight"
    )
    T_767_BIRTH_TRAUMA = "767 Birth trauma"
    T_768_INTRA_UTERINE_HYPOXIA_AND_BIRTH_ASPHYXIA = "768 Intra-uterine hypoxia and birth asphyxia"
    T_769_RESPIRATORY_DISTRESS_SYNDROME = "769 Respiratory distress syndrome"
    T_770_OTHER_RESPIRATORY_CONDITIONS_OF_FOETUS_AND_NEWBORN = "770 Other respiratory conditions of foetus and newborn"
    T_771_INFECTIONS_SPECIFIC_TO_THE_PERINATAL_PERIOD = "771 Infections specific to the perinatal period"
    T_772_FOETAL_AND_NEONATAL_HAEMORRHAGE = "772 Foetal and neonatal haemorrhage"
    T_773_HAEMOLYTIC_DISEASE_OF_FOETUS_OR_NEWBORN__DUE_TO_ISOIMMUNISATION = (
        "773 Haemolytic disease of foetus or newborn, due to isoimmunisation"
    )
    T_774_OTHER_PERINATAL_JAUNDICE = "774 Other perinatal jaundice"
    T_775_ENDOCRINE_AND_METABOLIC_DISTURBANCES_SPECIFIC_TO_THE_FOETUS_AND_NEWBORN = (
        "775 Endocrine and metabolic disturbances specific to the foetus and newborn"
    )
    T_776_HAEMATOLOGICAL_DISORDERS_OF_FOETUS_AND_NEWBORN = "776 Haematological disorders of foetus and newborn"
    T_777_PERINATAL_DISORDERS_OF_DIGESTIVE_SYSTEM = "777 Perinatal disorders of digestive system"
    T_778_CONDITIONS_INVOLVING_THE_INTEGUMENT_AND_TEMPERATURE_REGULATION_OF_FOETUS_AND_NEWBORN = (
        "778 Conditions involving the integument and temperature regulation of foetus and newborn"
    )
    T_779_OTHER_AND_ILL_DEFINED_CONDITIONS_ORIGINATING_IN_THE_PERINATAL_PERIOD = (
        "779 Other and ill-defined conditions originating in the perinatal period"
    )


class DeathPossibilitiesTaxonomyT780789SymptomsEntry(str, Enum):
    T_780_GENERAL_SYMPTOMS = "780 General symptoms"
    T_781_SYMPTOMS_INVOLVING_NERVOUS_AND_MUSCULOSKELETAL_SYSTEMS = (
        "781 Symptoms involving nervous and musculoskeletal systems"
    )
    T_782_SYMPTOMS_INVOLVING_SKIN_AND_OTHER_INTEGUMENTARY_TISSUE = (
        "782 Symptoms involving skin and other integumentary tissue"
    )
    T_783_SYMPTOMS_CONCERNING_NUTRITION__METABOLISM_AND_DEVELOPMENT = (
        "783 Symptoms concerning nutrition, metabolism and development"
    )
    T_784_SYMPTOMS_INVOLVING_HEAD_AND_NECK = "784 Symptoms involving head and neck"
    T_785_SYMPTOMS_INVOLVING_CARDIOVASCULAR_SYSTEM = "785 Symptoms involving cardiovascular system"
    T_786_SYMPTOMS_INVOLVING_RESPIRATORY_SYSTEM_AND_OTHER_CHEST_SYMPTOMS = (
        "786 Symptoms involving respiratory system and other chest symptoms"
    )
    T_787_SYMPTOMS_INVOLVING_DIGESTIVE_SYSTEM = "787 Symptoms involving digestive system"
    T_788_SYMPTOMS_INVOLVING_URINARY_SYSTEM = "788 Symptoms involving urinary system"
    T_789_OTHER_SYMPTOMS_INVOLVING_ABDOMEN_AND_PELVIS = "789 Other symptoms involving abdomen and pelvis"


class DeathPossibilitiesTaxonomyT790796NonspecificAbnormalFindingsEntry(str, Enum):
    T_790_NONSPECIFIC_FINDINGS_ON_EXAMINATION_OF_BLOOD = "790 Nonspecific findings on examination of blood"
    T_791_NONSPECIFIC_FINDINGS_ON_EXAMINATION_OF_URINE = "791 Nonspecific findings on examination of urine"
    T_792_NONSPECIFIC_ABNORMAL_FINDINGS_IN_OTHER_BODY_SUBSTANCES = (
        "792 Nonspecific abnormal findings in other body substances"
    )
    T_793_NONSPECIFIC_ABNORMAL_FINDINGS_ON_RADIOLOGICAL_AND_OTHER_EXAMINATION_OF_BODY_STRUCTURE = (
        "793 Nonspecific abnormal findings on radiological and other examination of body structure"
    )
    T_794_NONSPECIFIC_ABNORMAL_RESULTS_OF_FUNCTION_STUDIES = "794 Nonspecific abnormal results of function studies"
    T_795_NONSPECIFIC_ABNORMAL_HISTOLOGICAL_AND_IMMUNOLOGICAL_FINDINGS = (
        "795 Nonspecific abnormal histological and immunological findings"
    )
    T_796_OTHER_NONSPECIFIC_ABNORMAL_FINDINGS = "796 Other nonspecific abnormal findings"


class DeathPossibilitiesTaxonomyT797799IllDefinedAndUnknownCausesOfMorbidityAndMortalityEntry(str, Enum):
    T_797_SENILITY_WITHOUT_MENTION_OF_PSYCHOSIS = "797 Senility without mention of psychosis"
    T_798_SUDDEN_DEATH__CAUSE_UNKNOWN = "798 Sudden death, cause unknown"
    T_799_OTHER_ILL_DEFINED_AND_UNKNOWN_CAUSES_OF_MORBIDITY_AND_MORTALITY = (
        "799 Other ill-defined and unknown causes of morbidity and mortality"
    )


class DeathPossibilitiesTaxonomyT800804FractureOfSkullEntry(str, Enum):
    T_800_FRACTURE_OF_VAULT_OF_SKULL = "800 Fracture of vault of skull"
    T_801_FRACTURE_OF_BASE_OF_SKULL = "801 Fracture of base of skull"
    T_802_FRACTURE_OF_FACE_BONES = "802 Fracture of face bones"
    T_803_OTHER_AND_UNQUALIFIED_SKULL_FRACTURES = "803 Other and unqualified skull fractures"
    T_804_MULTIPLE_FRACTURES_INVOLVING_SKULL_OR_FACE_WITH_OTHER_BONES = (
        "804 Multiple fractures involving skull or face with other bones"
    )


class DeathPossibilitiesTaxonomyT805809FractureOfNeckAndTrunkEntry(str, Enum):
    T_805_FRACTURE_OF_VERTEBRAL_COLUMN_WITHOUT_MENTION_OF_SPINAL_CORD_LESION = (
        "805 Fracture of vertebral column without mention of spinal cord lesion"
    )
    T_806_FRACTURE_OF_VERTEBRAL_COLUMN_WITH_SPINAL_CORD_LESION = (
        "806 Fracture of vertebral column with spinal cord lesion"
    )
    T_807_FRACTURE_OF_RIB_S___STERNUM__LARYNX_AND_TRACHEA = "807 Fracture of rib(s), sternum, larynx and trachea"
    T_808_FRACTURE_OF_PELVIS = "808 Fracture of pelvis"
    T_809_ILL_DEFINED_FRACTURES_OF_TRUNK = "809 Ill-defined fractures of trunk"


class DeathPossibilitiesTaxonomyT810819FractureOfUpperLimbEntry(str, Enum):
    T_810_FRACTURE_OF_CLAVICLE = "810 Fracture of clavicle"
    T_811_FRACTURE_OF_SCAPULA = "811 Fracture of scapula"
    T_812_FRACTURE_OF_HUMERUS = "812 Fracture of humerus"
    T_813_FRACTURE_OF_RADIUS_AND_ULNA = "813 Fracture of radius and ulna"
    T_814_FRACTURE_OF_CARPAL_BONE_S_ = "814 Fracture of carpal bone(s)"
    T_815_FRACTURE_OF_METACARPAL_BONE_S_ = "815 Fracture of metacarpal bone(s)"
    T_816_FRACTURE_OF_ONE_OR_MORE_PHALANGES_OF_HAND = "816 Fracture of one or more phalanges of hand"
    T_817_MULTIPLE_FRACTURES_OF_HAND_BONES = "817 Multiple fractures of hand bones"
    T_818_ILL_DEFINED_FRACTURES_OF_UPPER_LIMB = "818 Ill-defined fractures of upper limb"
    T_819_MULTIPLE_FRACTURES_INVOLVING_BOTH_UPPER_LIMBS_AND_UPPER_LIMB_WITH_RIB_S__AND_STERNUM = (
        "819 Multiple fractures involving both upper limbs and upper limb with rib(s) and sternum"
    )


class DeathPossibilitiesTaxonomyT820829FractureOfLowerLimbEntry(str, Enum):
    T_820_FRACTURE_OF_NECK_OF_FEMUR = "820 Fracture of neck of femur"
    T_821_FRACTURE_OF_OTHER_AND_UNSPECIFIED_PARTS_OF_FEMUR = "821 Fracture of other and unspecified parts of femur"
    T_822_FRACTURE_OF_PATELLA = "822 Fracture of patella"
    T_823_FRACTURE_OF_TIBIA_AND_FIBULA = "823 Fracture of tibia and fibula"
    T_824_FRACTURE_OF_ANKLE = "824 Fracture of ankle"
    T_825_FRACTURE_OF_ONE_OR_MORE_TARSAL_AND_METATARSAL_BONES = (
        "825 Fracture of one or more tarsal and metatarsal bones"
    )
    T_826_FRACTURE_OF_ONE_OR_MORE_PHALANGES_OF_FOOT = "826 Fracture of one or more phalanges of foot"
    T_827_OTHER__MULTIPLE_AND_ILL_DEFINED_FRACTURES_OF_LOWER_LIMB = (
        "827 Other, multiple and ill-defined fractures of lower limb"
    )
    T_828_MULTIPLE_FRACTURES_INVOLVING_BOTH_LOWER_LIMBS__LOWER_WITH_UPPER_LIMB_AND_LOWER_LIMB_S__WITH_RIB_S__AND_STERNUM = "828 Multiple fractures involving both lower limbs, lower with upper limb and lower limb(s) with rib(s) and sternum"
    T_829_FRACTURE_OF_UNSPECIFIED_BONES = "829 Fracture of unspecified bones"


class DeathPossibilitiesTaxonomyT830839DislocationEntry(str, Enum):
    T_830_DISLOCATION_OF_JAW = "830 Dislocation of jaw"
    T_831_DISLOCATION_OF_SHOULDER = "831 Dislocation of shoulder"
    T_832_DISLOCATION_OF_ELBOW = "832 Dislocation of elbow"
    T_833_DISLOCATION_OF_WRIST = "833 Dislocation of wrist"
    T_834_DISLOCATION_OF_FINGER = "834 Dislocation of finger"
    T_835_DISLOCATION_OF_HIP = "835 Dislocation of hip"
    T_836_DISLOCATION_OF_KNEE = "836 Dislocation of knee"
    T_837_DISLOCATION_OF_ANKLE = "837 Dislocation of ankle"
    T_838_DISLOCATION_OF_FOOT = "838 Dislocation of foot"
    T_839_OTHER__MULTIPLE_AND_ILL_DEFINED_DISLOCATIONS = "839 Other, multiple and ill-defined dislocations"


class DeathPossibilitiesTaxonomyT840848SprainsAndStrainsOfJointsAndAdjacentMusclesEntry(str, Enum):
    T_840_SPRAINS_AND_STRAINS_OF_SHOULDER_AND_UPPER_ARM = "840 Sprains and strains of shoulder and upper arm"
    T_841_SPRAINS_AND_STRAINS_OF_ELBOW_AND_FOREARM = "841 Sprains and strains of elbow and forearm"
    T_842_SPRAINS_AND_STRAINS_OF_WRIST_AND_HAND = "842 Sprains and strains of wrist and hand"
    T_843_SPRAINS_AND_STRAINS_OF_HIP_AND_THIGH = "843 Sprains and strains of hip and thigh"
    T_844_SPRAINS_AND_STRAINS_OF_KNEE_AND_LEG = "844 Sprains and strains of knee and leg"
    T_845_SPRAINS_AND_STRAINS_OF_ANKLE_AND_FOOT = "845 Sprains and strains of ankle and foot"
    T_846_SPRAINS_AND_STRAINS_OF_SACRO_ILIAC_REGION = "846 Sprains and strains of sacro-iliac region"
    T_847_SPRAINS_AND_STRAINS_OF_OTHER_AND_UNSPECIFIED_PARTS_OF_BACK = (
        "847 Sprains and strains of other and unspecified parts of back"
    )
    T_848_OTHER_AND_ILL_DEFINED_SPRAINS_AND_STRAINS = "848 Other and ill-defined sprains and strains"


class DeathPossibilitiesTaxonomyT850854IntracranialInjuryExcludingThoseWithSkullFractureEntry(str, Enum):
    T_850_CONCUSSION = "850 Concussion"
    T_851_CEREBRAL_LACERATION_AND_CONTUSION = "851 Cerebral laceration and contusion"
    T_852_SUBARACHNOID__SUBDURAL_AND_EXTRADURAL_HAEMORRHAGE__FOLLOWING_INJURY = (
        "852 Subarachnoid, subdural and extradural haemorrhage, following injury"
    )
    T_853_OTHER_AND_UNSPECIFIED_INTRACRANIAL_HAEMORRHAGE_FOLLOWING_INJURY = (
        "853 Other and unspecified intracranial haemorrhage following injury"
    )
    T_854_INTRACRANIAL_INJURY_OF_OTHER_AND_UNSPECIFIED_NATURE = (
        "854 Intracranial injury of other and unspecified nature"
    )


class DeathPossibilitiesTaxonomyT860869InternalInjuryOfChestAbdomenAndPelvisEntry(str, Enum):
    T_860_TRAUMATIC_PNEUMOTHORAX_AND_HAEMOTHORAX = "860 Traumatic pneumothorax and haemothorax"
    T_861_INJURY_TO_HEART_AND_LUNG = "861 Injury to heart and lung"
    T_862_INJURY_TO_OTHER_AND_UNSPECIFIED_INTRATHORACIC_ORGANS = (
        "862 Injury to other and unspecified intrathoracic organs"
    )
    T_863_INJURY_TO_GASTRO_INTESTINAL_TRACT = "863 Injury to gastro-intestinal tract"
    T_864_INJURY_TO_LIVER = "864 Injury to liver"
    T_865_INJURY_TO_SPLEEN = "865 Injury to spleen"
    T_866_INJURY_TO_KIDNEY = "866 Injury to kidney"
    T_867_INJURY_TO_PELVIC_ORGANS = "867 Injury to pelvic organs"
    T_868_INJURY_TO_OTHER_INTRA_ABDOMINAL_ORGANS = "868 Injury to other intra-abdominal organs"
    T_869_INTERNAL_INJURY_TO_UNSPECIFIED_OR_ILL_DEFINED_ORGANS = (
        "869 Internal injury to unspecified or ill-defined organs"
    )


class DeathPossibilitiesTaxonomyT870879OpenWoundOfHeadNeckAndTrunkEntry(str, Enum):
    T_870_OPEN_WOUND_OF_OCULAR_ADNEXA = "870 Open wound of ocular adnexa"
    T_871_OPEN_WOUND_OF_EYEBALL = "871 Open wound of eyeball"
    T_872_OPEN_WOUND_OF_EAR = "872 Open wound of ear"
    T_873_OTHER_OPEN_WOUND_OF_HEAD = "873 Other open wound of head"
    T_874_OPEN_WOUND_OF_NECK = "874 Open wound of neck"
    T_875_OPEN_WOUND_OF_CHEST__WALL_ = "875 Open wound of chest (wall)"
    T_876_OPEN_WOUND_OF_BACK = "876 Open wound of back"
    T_877_OPEN_WOUND_OF_BUTTOCK = "877 Open wound of buttock"
    T_878_OPEN_WOUND_OF_GENITAL_ORGANS__EXTERNAL___INCLUDING_TRAUMATIC_AMPUTATION = (
        "878 Open wound of genital organs (external), including traumatic amputation"
    )
    T_879_OPEN_WOUND_OF_OTHER_AND_UNSPECIFIED_SITES__EXCEPT_LIMBS = (
        "879 Open wound of other and unspecified sites, except limbs"
    )


class DeathPossibilitiesTaxonomyT880887OpenWoundOfUpperLimbEntry(str, Enum):
    T_880_OPEN_WOUND_OF_SHOULDER_AND_UPPER_ARM = "880 Open wound of shoulder and upper arm"
    T_881_OPEN_WOUND_OF_ELBOW__FOREARM_AND_WRIST = "881 Open wound of elbow, forearm and wrist"
    T_882_OPEN_WOUND_OF_HAND_EXCEPT_FINGER_S__ALONE = "882 Open wound of hand except finger(s) alone"
    T_883_OPEN_WOUND_OF_FINGER_S_ = "883 Open wound of finger(s)"
    T_884_MULTIPLE_AND_UNSPECIFIED_OPEN_WOUND_OF_UPPER_LIMB = "884 Multiple and unspecified open wound of upper limb"
    T_885_TRAUMATIC_AMPUTATION_OF_THUMB__COMPLETE___PARTIAL_ = "885 Traumatic amputation of thumb (complete) (partial)"
    T_886_TRAUMATIC_AMPUTATION_OF_OTHER_FINGER_S___COMPLETE___PARTIAL_ = (
        "886 Traumatic amputation of other finger(s) (complete) (partial)"
    )
    T_887_TRAUMATIC_AMPUTATION_OF_ARM_AND_HAND__COMPLETE___PARTIAL_ = (
        "887 Traumatic amputation of arm and hand (complete) (partial)"
    )


class DeathPossibilitiesTaxonomyT890897OpenWoundOfLowerLimbEntry(str, Enum):
    T_890_OPEN_WOUND_OF_HIP_AND_THIGH = "890 Open wound of hip and thigh"
    T_891_OPEN_WOUND_OF_KNEE__LEG__EXCEPT_THIGH__AND_ANKLE = "891 Open wound of knee, leg [except thigh] and ankle"
    T_892_OPEN_WOUND_OF_FOOT_EXCEPT_TOE_S__ALONE = "892 Open wound of foot except toe(s) alone"
    T_893_OPEN_WOUND_OF_TOE_S_ = "893 Open wound of toe(s)"
    T_894_MULTIPLE_AND_UNSPECIFIED_OPEN_WOUND_OF_LOWER_LIMB = "894 Multiple and unspecified open wound of lower limb"
    T_895_TRAUMATIC_AMPUTATION_OF_TOE_S___COMPLETE___PARTIAL_ = (
        "895 Traumatic amputation of toe(s) (complete) (partial)"
    )
    T_896_TRAUMATIC_AMPUTATION_OF_FOOT__COMPLETE___PARTIAL_ = "896 Traumatic amputation of foot (complete) (partial)"
    T_897_TRAUMATIC_AMPUTATION_OF_LEG_S___COMPLETE___PARTIAL_ = (
        "897 Traumatic amputation of leg(s) (complete) (partial)"
    )


class DeathPossibilitiesTaxonomyT900904InjuryToBloodVesselsEntry(str, Enum):
    T_900_INJURY_TO_BLOOD_VESSELS_OF_HEAD_AND_NECK = "900 Injury to blood vessels of head and neck"
    T_901_INJURY_TO_BLOOD_VESSELS_OF_THORAX = "901 Injury to blood vessels of thorax"
    T_902_INJURY_TO_BLOOD_VESSELS_OF_ABDOMEN_AND_PELVIS = "902 Injury to blood vessels of abdomen and pelvis"
    T_903_INJURY_TO_BLOOD_VESSELS_OF_UPPER_EXTREMITY = "903 Injury to blood vessels of upper extremity"
    T_904_INJURY_TO_BLOOD_VESSELS_OF_LOWER_EXTREMITY_AND_UNSPECIFIED_SITES = (
        "904 Injury to blood vessels of lower extremity and unspecified sites"
    )


class DeathPossibilitiesTaxonomyT905909LateEffectsOfInjuriesPoisoningsToxicEffectsAndOtherExternalCausesEntry(
    str, Enum
):
    T_905_LATE_EFFECTS_OF_MUSCULOSKELETAL_AND_CONNECTIVE_TISSUE_INJURIES = (
        "905 Late effects of musculoskeletal and connective tissue injuries"
    )
    T_906_LATE_EFFECTS_OF_INJURIES_TO_SKIN_AND_SUBCUTANEOUS_TISSUES = (
        "906 Late effects of injuries to skin and subcutaneous tissues"
    )
    T_907_LATE_EFFECTS_OF_INJURIES_TO_THE_NERVOUS_SYSTEM = "907 Late effects of injuries to the nervous system"
    T_908_LATE_EFFECTS_OF_OTHER_AND_UNSPECIFIED_INJURIES = "908 Late effects of other and unspecified injuries"
    T_909_LATE_EFFECTS_OF_OTHER_AND_UNSPECIFIED_EXTERNAL_CAUSES = (
        "909 Late effects of other and unspecified external causes"
    )


class DeathPossibilitiesTaxonomyT910919SuperficialInjuryEntry(str, Enum):
    T_910_SUPERFICIAL_INJURY_OF_FACE__NECK_AND_SCALP_EXCEPT_EYE = (
        "910 Superficial injury of face, neck and scalp except eye"
    )
    T_911_SUPERFICIAL_INJURY_OF_TRUNK = "911 Superficial injury of trunk"
    T_912_SUPERFICIAL_INJURY_OF_SHOULDER_AND_UPPER_ARM = "912 Superficial injury of shoulder and upper arm"
    T_913_SUPERFICIAL_INJURY_OF_ELBOW__FOREARM_AND_WRIST = "913 Superficial injury of elbow, forearm and wrist"
    T_914_SUPERFICIAL_INJURY_OF_HAND_S__EXCEPT_FINGER_S__ALONE = (
        "914 Superficial injury of hand(s) except finger(s) alone"
    )
    T_915_SUPERFICIAL_INJURY_OF_FINGER_S_ = "915 Superficial injury of finger(s)"
    T_916_SUPERFICIAL_INJURY_OF_HIP__THIGH__LEG_AND_ANKLE = "916 Superficial injury of hip, thigh, leg and ankle"
    T_917_SUPERFICIAL_INJURY_OF_FOOT_AND_TOE_S_ = "917 Superficial injury of foot and toe(s)"
    T_918_SUPERFICIAL_INJURY_OF_EYE_AND_ADNEXA = "918 Superficial injury of eye and adnexa"
    T_919_SUPERFICIAL_INJURY_OF_OTHER__MULTIPLE_AND_UNSPECIFIED_SITES = (
        "919 Superficial injury of other, multiple and unspecified sites"
    )


class DeathPossibilitiesTaxonomyT920924ContusionWithIntactSkinSurfaceEntry(str, Enum):
    T_920_CONTUSION_OF_FACE__SCALP_AND_NECK_EXCEPT_EYE_S_ = "920 Contusion of face, scalp and neck except eye(s)"
    T_921_CONTUSION_OF_EYE_AND_ADNEXA = "921 Contusion of eye and adnexa"
    T_922_CONTUSION_OF_TRUNK = "922 Contusion of trunk"
    T_923_CONTUSION_OF_UPPER_LIMB = "923 Contusion of upper limb"
    T_924_CONTUSION_OF_LOWER_LIMB_AND_OF_OTHER_AND_UNSPECIFIED_SITES = (
        "924 Contusion of lower limb and of other and unspecified sites"
    )


class DeathPossibilitiesTaxonomyT925929CrushingInjuryEntry(str, Enum):
    T_925_CRUSHING_INJURY_OF_FACE__SCALP_AND_NECK = "925 Crushing injury of face, scalp and neck"
    T_926_CRUSHING_INJURY_OF_TRUNK = "926 Crushing injury of trunk"
    T_927_CRUSHING_INJURY_OF_UPPER_LIMB = "927 Crushing injury of upper limb"
    T_928_CRUSHING_INJURY_OF_LOWER_LIMB = "928 Crushing injury of lower limb"
    T_929_CRUSHING_INJURY_OF_MULTIPLE_AND_UNSPECIFIED_SITES = "929 Crushing injury of multiple and unspecified sites"


class DeathPossibilitiesTaxonomyT930939EffectsOfForeignBodyEnteringThroughOrificeEntry(str, Enum):
    T_930_FOREIGN_BODY_ON_EXTERNAL_EYE = "930 Foreign body on external eye"
    T_931_FOREIGN_BODY_IN_EAR = "931 Foreign body in ear"
    T_932_FOREIGN_BODY_IN_NOSE = "932 Foreign body in nose"
    T_933_FOREIGN_BODY_IN_PHARYNX_AND_LARYNX = "933 Foreign body in pharynx and larynx"
    T_934_FOREIGN_BODY_IN_TRACHEA__BRONCHUS_AND_LUNG = "934 Foreign body in trachea, bronchus and lung"
    T_935_FOREIGN_BODY_IN_MOUTH__OESOPHAGUS_AND_STOMACH = "935 Foreign body in mouth, oesophagus and stomach"
    T_936_FOREIGN_BODY_IN_INTESTINE_AND_COLON = "936 Foreign body in intestine and colon"
    T_937_FOREIGN_BODY_IN_ANUS_AND_RECTUM = "937 Foreign body in anus and rectum"
    T_938_FOREIGN_BODY_IN_DIGESTIVE_SYSTEM__UNSPECIFIED = "938 Foreign body in digestive system, unspecified"
    T_939_FOREIGN_BODY_IN_GENITO_URINARY_TRACT = "939 Foreign body in genito-urinary tract"


class DeathPossibilitiesTaxonomyT940949BurnsEntry(str, Enum):
    T_940_BURN_CONFINED_TO_EYE_AND_ADNEXA = "940 Burn confined to eye and adnexa"
    T_941_BURN_OF_FACE__HEAD_AND_NECK = "941 Burn of face, head and neck"
    T_942_BURN_OF_TRUNK = "942 Burn of trunk"
    T_943_BURN_OF_UPPER_LIMB__EXCEPT_WRIST_AND_HAND = "943 Burn of upper limb, except wrist and hand"
    T_944_BURN_OF_WRIST_S__AND_HAND_S_ = "944 Burn of wrist(s) and hand(s)"
    T_945_BURN_OF_LOWER_LIMB_S_ = "945 Burn of lower limb(s)"
    T_946_BURNS_OF_MULTIPLE_SPECIFIED_SITES = "946 Burns of multiple specified sites"
    T_947_BURN_OF_INTERNAL_ORGANS = "947 Burn of internal organs"
    T_948_BURNS_CLASSIFIED_ACCORDING_TO_EXTENT_OF_BODY_SURFACE_INVOLVED = (
        "948 Burns classified according to extent of body surface involved"
    )
    T_949_BURN__UNSPECIFIED = "949 Burn, unspecified"


class DeathPossibilitiesTaxonomyT950957InjuryToNervesAndSpinalCordEntry(str, Enum):
    T_950_INJURY_TO_OPTIC_NERVE_AND_PATHWAYS = "950 Injury to optic nerve and pathways"
    T_951_INJURY_TO_OTHER_CRANIAL_NERVE_S_ = "951 Injury to other cranial nerve(s)"
    T_952_SPINAL_CORD_LESION_WITHOUT_EVIDENCE_OF_SPINAL_BONE_INJURY = (
        "952 Spinal cord lesion without evidence of spinal bone injury"
    )
    T_953_INJURY_TO_NERVE_ROOTS_AND_SPINAL_PLEXUS = "953 Injury to nerve roots and spinal plexus"
    T_954_INJURY_TO_OTHER_NERVE_S__OF_TRUNK_EXCLUDING_SHOULDER_AND_PELVIC_GIRDLES = (
        "954 Injury to other nerve(s) of trunk excluding shoulder and pelvic girdles"
    )
    T_955_INJURY_TO_PERIPHERAL_NERVE_S__OF_SHOULDER_GIRDLE_AND_UPPER_LIMB = (
        "955 Injury to peripheral nerve(s) of shoulder girdle and upper limb"
    )
    T_956_INJURY_TO_PERIPHERAL_NERVE_S__OF_PELVIC_GIRDLE_AND_LOWER_LIMB = (
        "956 Injury to peripheral nerve(s) of pelvic girdle and lower limb"
    )
    T_957_INJURY_TO_OTHER_AND_UNSPECIFIED_NERVES = "957 Injury to other and unspecified nerves"


class DeathPossibilitiesTaxonomyT958959CertainTraumaticComplicationsAndUnspecifiedInjuriesEntry(str, Enum):
    T_958_CERTAIN_EARLY_COMPLICATIONS_OF_TRAUMA = "958 Certain early complications of trauma"
    T_959_INJURY__OTHER_AND_UNSPECIFIED = "959 Injury, other and unspecified"


class DeathPossibilitiesTaxonomyT960979PoisoningByDrugsMedicamentsAndBiologicalSubstancesEntry(str, Enum):
    T_960_POISONING_BY_ANTIBIOTICS = "960 Poisoning by antibiotics"
    T_961_POISONING_BY_OTHER_ANTI_INFECTIVES = "961 Poisoning by other anti-infectives"
    T_962_POISONING_BY_HORMONES_AND_SYNTHETIC_SUBSTITUTES = "962 Poisoning by hormones and synthetic substitutes"
    T_963_POISONING_BY_PRIMARILY_SYSTEMIC_AGENTS = "963 Poisoning by primarily systemic agents"
    T_964_POISONING_BY_AGENTS_PRIMARILY_AFFECTING_BLOOD_CONSTITUENTS = (
        "964 Poisoning by agents primarily affecting blood constituents"
    )
    T_965_POISONING_BY_ANALGESICS__ANTIPYRETICS_AND_ANTIRHEUMATICS = (
        "965 Poisoning by analgesics, antipyretics and antirheumatics"
    )
    T_966_POISONING_BY_ANTICONVULSANTS_AND_ANTI_PARKINSONISM_DRUGS = (
        "966 Poisoning by anticonvulsants and anti-Parkinsonism drugs"
    )
    T_967_POISONING_BY_SEDATIVES_AND_HYPNOTICS = "967 Poisoning by sedatives and hypnotics"
    T_968_POISONING_BY_OTHER_CENTRAL_NERVOUS_SYSTEM_DEPRESSANTS_AND_ANAESTHETICS = (
        "968 Poisoning by other central nervous system depressants and anaesthetics"
    )
    T_969_POISONING_BY_PSYCHOTROPIC_AGENTS = "969 Poisoning by psychotropic agents"
    T_970_POISONING_BY_CENTRAL_NERVOUS_SYSTEM_STIMULANTS = "970 Poisoning by central nervous system stimulants"
    T_971_POISONING_BY_DRUGS_PRIMARILY_AFFECTING_THE_AUTONOMIC_NERVOUS_SYSTEM = (
        "971 Poisoning by drugs primarily affecting the autonomic nervous system"
    )
    T_972_POISONING_BY_AGENTS_PRIMARILY_AFFECTING_THE_CARDIOVASCULAR_SYSTEM = (
        "972 Poisoning by agents primarily affecting the cardiovascular system"
    )
    T_973_POISONING_BY_AGENTS_PRIMARILY_AFFECTING_THE_GASTRO_INTESTINAL_SYSTEM = (
        "973 Poisoning by agents primarily affecting the gastro-intestinal system"
    )
    T_974_POISONING_BY_WATER__MINERAL_AND_URIC_ACID_METABOLISM_DRUGS = (
        "974 Poisoning by water, mineral and uric acid metabolism drugs"
    )
    T_975_POISONING_BY_AGENTS_PRIMARILY_ACTING_ON_THE_SMOOTH_AND_SKELETAL_MUSCLES_AND_RESPIRATORY_SYSTEM = (
        "975 Poisoning by agents primarily acting on the smooth and skeletal muscles and respiratory system"
    )
    T_976_POISONING_BY_AGENTS_PRIMARILY_AFFECTING_SKIN_AND_MUCOUS_MEMBRANE__OPHTHALMOLOGICAL__OTORHINOLARYNGOLOGICAL_AND_DENTAL_DRUGS = "976 Poisoning by agents primarily affecting skin and mucous membrane, ophthalmological, otorhinolaryngological and dental drugs"
    T_977_POISONING_BY_OTHER_AND_UNSPECIFIED_DRUGS_AND_MEDICAMENTS = (
        "977 Poisoning by other and unspecified drugs and medicaments"
    )
    T_978_POISONING_BY_BACTERIAL_VACCINES = "978 Poisoning by bacterial vaccines"
    T_979_POISONING_BY_OTHER_VACCINES_AND_BIOLOGICAL_SUBSTANCES = (
        "979 Poisoning by other vaccines and biological substances"
    )


class DeathPossibilitiesTaxonomyT980989ToxicEffectsOfSubstancesChieflyNonmedicinalAsToSourceEntry(str, Enum):
    T_980_TOXIC_EFFECT_OF_ALCOHOL = "980 Toxic effect of alcohol"
    T_981_TOXIC_EFFECT_OF_PETROLEUM_PRODUCTS = "981 Toxic effect of petroleum products"
    T_982_TOXIC_EFFECT_OF_SOLVENTS_OTHER_THAN_PETROLEUM_BASED = (
        "982 Toxic effect of solvents other than petroleum-based"
    )
    T_983_TOXIC_EFFECT_OF_CORROSIVE_AROMATICS__ACIDS_AND_CAUSTIC_ALKALIS = (
        "983 Toxic effect of corrosive aromatics, acids and caustic alkalis"
    )
    T_984_TOXIC_EFFECT_OF_LEAD_AND_ITS_COMPOUNDS__INCLUDING_FUMES_ = (
        "984 Toxic effect of lead and its compounds (including fumes)"
    )
    T_985_TOXIC_EFFECT_OF_OTHER_METALS = "985 Toxic effect of other metals"
    T_986_TOXIC_EFFECT_OF_CARBON_MONOXIDE = "986 Toxic effect of carbon monoxide"
    T_987_TOXIC_EFFECT_OF_OTHER_GASES__FUMES_OR_VAPOURS = "987 Toxic effect of other gases, fumes or vapours"
    T_988_TOXIC_EFFECT_OF_NOXIOUS_SUBSTANCES_EATEN_AS_FOOD = "988 Toxic effect of noxious substances eaten as food"
    T_989_TOXIC_EFFECT_OF_OTHER_SUBSTANCES__CHIEFLY_NONMEDICINAL_AS_TO_SOURCE = (
        "989 Toxic effect of other substances, chiefly nonmedicinal as to source"
    )


class DeathPossibilitiesTaxonomyT990995OtherAndUnspecifiedEffectsOfExternalCausesEntry(str, Enum):
    T_990_EFFECTS_OF_RADIATION__UNSPECIFIED = "990 Effects of radiation, unspecified"
    T_991_EFFECTS_OF_REDUCED_TEMPERATURE = "991 Effects of reduced temperature"
    T_992_EFFECTS_OF_HEAT_AND_LIGHT = "992 Effects of heat and light"
    T_993_EFFECTS_OF_AIR_PRESSURE = "993 Effects of air pressure"
    T_994_EFFECTS_OF_OTHER_EXTERNAL_CAUSES = "994 Effects of other external causes"
    T_995_CERTAIN_ADVERSE_EFFECTS_NOT_ELSEWHERE_CLASSIFIED = "995 Certain adverse effects not elsewhere classified"


class DeathPossibilitiesTaxonomyT996999ComplicationsOfSurgicalAndMedicalCareNotElsewhereClassifiedEntry(str, Enum):
    T_996_COMPLICATIONS_PECULIAR_TO_CERTAIN_SPECIFIED_PROCEDURES = (
        "996 Complications peculiar to certain specified procedures"
    )
    T_997_COMPLICATIONS_AFFECTING_SPECIFIED_BODY_SYSTEMS__NOT_ELSEWHERE_CLASSIFIED = (
        "997 Complications affecting specified body systems, not elsewhere classified"
    )
    T_998_OTHER_COMPLICATIONS_OF_PROCEDURES__NOT_ELSEWHERE_CLASSIFIED = (
        "998 Other complications of procedures, not elsewhere classified"
    )
    T_999_COMPLICATIONS_OF_MEDICAL_CARE__NOT_ELSEWHERE_CLASSIFIED = (
        "999 Complications of medical care, not elsewhere classified"
    )


class DeathPossibilitiesTaxonomyTE800E807RailwayAccidentsEntry(str, Enum):
    E800_RAILWAY_ACCIDENT_INVOLVING_COLLISION_WITH_ROLLING_STOCK = (
        "E800 Railway accident involving collision with rolling stock"
    )
    E801_RAILWAY_ACCIDENT_INVOLVING_COLLISION_WITH_OTHER_OBJECT = (
        "E801 Railway accident involving collision with other object"
    )
    E802_RAILWAY_ACCIDENT_INVOLVING_DERAILMENT_WITHOUT_ANTECEDENT_COLLISION = (
        "E802 Railway accident involving derailment without antecedent collision"
    )
    E803_RAILWAY_ACCIDENT_INVOLVING_EXPLOSION__FIRE_OR_BURNING = (
        "E803 Railway accident involving explosion, fire or burning"
    )
    E804_FALL_IN__ON_OR_FROM_RAILWAY_TRAIN = "E804 Fall in, on or from railway train"
    E805_HIT_BY_ROLLING_STOCK = "E805 Hit by rolling stock"
    E806_OTHER_SPECIFIED_RAILWAY_ACCIDENT = "E806 Other specified railway accident"
    E807_RAILWAY_ACCIDENT_OF_UNSPECIFIED_NATURE = "E807 Railway accident of unspecified nature"


class DeathPossibilitiesTaxonomyTE810E819MotorVehicleTrafficAccidentsEntry(str, Enum):
    E810_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_INVOLVING_COLLISION_WITH_TRAIN = (
        "E810 Motor vehicle traffic accident involving collision with train"
    )
    E811_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_INVOLVING_RE_ENTRANT_COLLISION_WITH_ANOTHER_MOTOR_VEHICLE = (
        "E811 Motor vehicle traffic accident involving re-entrant collision with another motor vehicle"
    )
    E812_OTHER_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_INVOLVING_COLLISION_WITH_ANOTHER_MOTOR_VEHICLE = (
        "E812 Other motor vehicle traffic accident involving collision with another motor vehicle"
    )
    E813_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_INVOLVING_COLLISION_WITH_OTHER_VEHICLE = (
        "E813 Motor vehicle traffic accident involving collision with other vehicle"
    )
    E814_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_INVOLVING_COLLISION_WITH_PEDESTRIAN = (
        "E814 Motor vehicle traffic accident involving collision with pedestrian"
    )
    E815_OTHER_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_INVOLVING_COLLISION_ON_THE_HIGHWAY = (
        "E815 Other motor vehicle traffic accident involving collision on the highway"
    )
    E816_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_DUE_TO_LOSS_OF_CONTROL__WITHOUT_COLLISION_ON_THE_HIGHWAY = (
        "E816 Motor vehicle traffic accident due to loss of control, without collision on the highway"
    )
    E817_NONCOLLISION_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_WHILE_BOARDING_OR_ALIGHTING = (
        "E817 Noncollision motor vehicle traffic accident while boarding or alighting"
    )
    E818_OTHER_NONCOLLISION_MOTOR_VEHICLE_TRAFFIC_ACCIDENT = "E818 Other noncollision motor vehicle traffic accident"
    E819_MOTOR_VEHICLE_TRAFFIC_ACCIDENT_OF_UNSPECIFIED_NATURE = (
        "E819 Motor vehicle traffic accident of unspecified nature"
    )


class DeathPossibilitiesTaxonomyTE820E825MotorVehicleNontrafficAccidentsEntry(str, Enum):
    E820_NONTRAFFIC_ACCIDENT_INVOLVING_MOTOR_DRIVEN_SNOW_VEHICLE = (
        "E820 Nontraffic accident involving motor-driven snow vehicle"
    )
    E821_NONTRAFFIC_ACCIDENT_INVOLVING_OTHER_OFF_ROAD_MOTOR_VEHICLE = (
        "E821 Nontraffic accident involving other off-road motor vehicle"
    )
    E822_OTHER_MOTOR_VEHICLE_NONTRAFFIC_ACCIDENT_INVOLVING_COLLISION_WITH_MOVING_OBJECT = (
        "E822 Other motor vehicle nontraffic accident involving collision with moving object"
    )
    E823_OTHER_MOTOR_VEHICLE_NONTRAFFIC_ACCIDENT_INVOLVING_COLLISION_WITH_STATIONARY_OBJECT = (
        "E823 Other motor vehicle nontraffic accident involving collision with stationary object"
    )
    E824_OTHER_MOTOR_VEHICLE_NONTRAFFIC_ACCIDENT_WHILE_BOARDING_AND_ALIGHTING = (
        "E824 Other motor vehicle nontraffic accident while boarding and alighting"
    )
    E825_OTHER_MOTOR_VEHICLE_NONTRAFFIC_ACCIDENT_OF_OTHER_AND_UNSPECIFIED_NATURE = (
        "E825 Other motor vehicle nontraffic accident of other and unspecified nature"
    )


class DeathPossibilitiesTaxonomyTE826E829OtherRoadVehicleAccidentsEntry(str, Enum):
    E826_PEDAL_CYCLE_ACCIDENT = "E826 Pedal cycle accident"
    E827_ANIMAL_DRAWN_VEHICLE_ACCIDENT = "E827 Animal-drawn vehicle accident"
    E828_ACCIDENT_INVOLVING_ANIMAL_BEING_RIDDEN = "E828 Accident involving animal being ridden"
    E829_OTHER_ROAD_VEHICLE_ACCIDENTS = "E829 Other road vehicle accidents"


class DeathPossibilitiesTaxonomyTE830E838WaterTransportAccidentsEntry(str, Enum):
    E830_ACCIDENT_TO_WATERCRAFT_CAUSING_SUBMERSION = "E830 Accident to watercraft causing submersion"
    E831_ACCIDENT_TO_WATERCRAFT_CAUSING_OTHER_INJURY = "E831 Accident to watercraft causing other injury"
    E832_OTHER_ACCIDENTAL_SUBMERSION_OR_DROWNING_IN_WATER_TRANSPORT_ACCIDENT = (
        "E832 Other accidental submersion or drowning in water transport accident"
    )
    E833_FALL_ON_STAIRS_OR_LADDERS_IN_WATER_TRANSPORT = "E833 Fall on stairs or ladders in water transport"
    E834_OTHER_FALL_FROM_ONE_LEVEL_TO_ANOTHER_IN_WATER_TRANSPORT = (
        "E834 Other fall from one level to another in water transport"
    )
    E835_OTHER_AND_UNSPECIFIED_FALL_IN_WATER_TRANSPORT = "E835 Other and unspecified fall in water transport"
    E836_MACHINERY_ACCIDENT_IN_WATER_TRANSPORT = "E836 Machinery accident in water transport"
    E837_EXPLOSION__FIRE_OR_BURNING_IN_WATERCRAFT = "E837 Explosion, fire or burning in watercraft"
    E838_OTHER_AND_UNSPECIFIED_WATER_TRANSPORT_ACCIDENT = "E838 Other and unspecified water transport accident"


class DeathPossibilitiesTaxonomyTE840E845AirAndSpaceTransportAccidentsEntry(str, Enum):
    E840_ACCIDENT_TO_POWERED_AIRCRAFT_AT_TAKEOFF_OR_LANDING = "E840 Accident to powered aircraft at takeoff or landing"
    E841_ACCIDENT_TO_POWERED_AIRCRAFT__OTHER_AND_UNSPECIFIED = (
        "E841 Accident to powered aircraft, other and unspecified"
    )
    E842_ACCIDENT_TO_UNPOWERED_AIRCRAFT = "E842 Accident to unpowered aircraft"
    E843_FALL_IN__ON_OR_FROM_AIRCRAFT = "E843 Fall in, on or from aircraft"
    E844_OTHER_SPECIFIED_AIR_TRANSPORT_ACCIDENTS = "E844 Other specified air transport accidents"
    E845_ACCIDENT_INVOLVING_SPACECRAFT = "E845 Accident involving spacecraft"


class DeathPossibilitiesTaxonomyTE846E848VehicleAccidentsNotElsewhereClassifiableEntry(str, Enum):
    E846_ACCIDENTS_INVOLVING_POWERED_VEHICLES_USED_SOLELY_WITHIN_THE_BUILDINGS_AND_PREMISES_OF_AN_INDUSTRIAL_OR_COMMERCIAL_ESTABLISHMENT = "E846 Accidents involving powered vehicles used solely within the buildings and premises of an industrial or commercial establishment"
    E847_ACCIDENTS_INVOLVING_CABLE_CARS_NOT_RUNNING_ON_RAILS = (
        "E847 Accidents involving cable cars not running on rails"
    )
    E848_ACCIDENTS_INVOLVING_OTHER_VEHICLES_NOT_ELSEWHERE_CLASSIFIABLE = (
        "E848 Accidents involving other vehicles not elsewhere classifiable"
    )


class DeathPossibilitiesTaxonomyTE849E858AccidentalPoisoningByDrugsMedicamentsAndBiologicalsEntry(str, Enum):
    E849_PLACE_OF_OCCURRENCE = "E849 Place of occurrence"
    E850_ACCIDENTAL_POISONING_BY_ANALGESICS__ANTIPYRETICS__ANTIRHEUMATICS = (
        "E850 Accidental poisoning by analgesics, antipyretics, antirheumatics"
    )
    E851_ACCIDENTAL_POISONING_BY_BARBITURATES = "E851 Accidental poisoning by barbiturates"
    E852_ACCIDENTAL_POISONING_BY_OTHER_SEDATIVES_AND_HYPNOTICS = (
        "E852 Accidental poisoning by other sedatives and hypnotics"
    )
    E853_ACCIDENTAL_POISONING_BY_TRANQUILLISERS = "E853 Accidental poisoning by tranquillisers"
    E854_ACCIDENTAL_POISONING_BY_OTHER_PSYCHOTROPIC_AGENTS = "E854 Accidental poisoning by other psychotropic agents"
    E855_ACCIDENTAL_POISONING_BY_OTHER_DRUGS_ACTING_ON_CENTRAL_AND_AUTONOMIC_NERVOUS_SYSTEMS = (
        "E855 Accidental poisoning by other drugs acting on central and autonomic nervous systems"
    )
    E856_ACCIDENTAL_POISONING_BY_ANTIBIOTICS = "E856 Accidental poisoning by antibiotics"
    E857_ACCIDENTAL_POISONING_BY_ANTI_INFECTIVES = "E857 Accidental poisoning by anti-infectives"
    E858_ACCIDENTAL_POISONING_BY_OTHER_DRUGS = "E858 Accidental poisoning by other drugs"


class DeathPossibilitiesTaxonomyTE860E869AccidentalPoisoningByOtherSolidAndLiquidSubstancesGasesAndVapoursEntry(
    str, Enum
):
    E860_ACCIDENTAL_POISONING_BY_ALCOHOL__NOT_ELSEWHERE_CLASSIFIED = (
        "E860 Accidental poisoning by alcohol, not elsewhere classified"
    )
    E861_ACCIDENTAL_POISONING_BY_CLEANSING_AND_POLISHING_AGENTS__DISINFECTANTS__PAINTS_AND_VARNISHES = (
        "E861 Accidental poisoning by cleansing and polishing agents, disinfectants, paints and varnishes"
    )
    E862_ACCIDENTAL_POISONING_BY_PETROLEUM_PRODUCTS__OTHER_SOLVENTS_AND_THEIR_VAPOURS__NOT_ELSEWHERE_CLASSIFIED = (
        "E862 Accidental poisoning by petroleum products, other solvents and their vapours, not elsewhere classified"
    )
    E863_ACCIDENTAL_POISONING_BY_AGRICULTURAL_AND_HORTICULTURAL_CHEMICAL_AND_PHARMACEUTICAL_PREPARATIONS_OTHER_THAN_PLANT_FOODS_AND_FERTILISERS = "E863 Accidental poisoning by agricultural and horticultural chemical and pharmaceutical preparations other than plant foods and fertilisers"
    E864_ACCIDENTAL_POISONING_BY_CORROSIVES_AND_CAUSTICS__NOT_ELSEWHERE_CLASSIFIED = (
        "E864 Accidental poisoning by corrosives and caustics, not elsewhere classified"
    )
    E865_ACCIDENTAL_POISONING_FROM_FOODSTUFFS_AND_POISONOUS_PLANTS = (
        "E865 Accidental poisoning from foodstuffs and poisonous plants"
    )
    E866_ACCIDENTAL_POISONING_BY_OTHER_AND_UNSPECIFIED_SOLID_AND_LIQUID_SUBSTANCES = (
        "E866 Accidental poisoning by other and unspecified solid and liquid substances"
    )
    E867_ACCIDENTAL_POISONING_BY_GAS_DISTRIBUTED_BY_PIPELINE = (
        "E867 Accidental poisoning by gas distributed by pipeline"
    )
    E868_ACCIDENTAL_POISONING_BY_OTHER_UTILITY_GAS_AND_OTHER_CARBON_MONOXIDE = (
        "E868 Accidental poisoning by other utility gas and other carbon monoxide"
    )
    E869_ACCIDENTAL_POISONING_BY_OTHER_GASES_AND_VAPOURS = "E869 Accidental poisoning by other gases and vapours"


class DeathPossibilitiesTaxonomyTE870E876MisadventuresToPatientsDuringSurgicalAndMedicalCareEntry(str, Enum):
    E870_ACCIDENTAL_CUT__PUNCTURE__PERFORATION_OR_HAEMORRHAGE_DURING_MEDICAL_CARE = (
        "E870 Accidental cut, puncture, perforation or haemorrhage during medical care"
    )
    E871_FOREIGN_OBJECT_LEFT_IN_BODY_DURING_PROCEDURE = "E871 Foreign object left in body during procedure"
    E872_FAILURE_OF_STERILE_PRECAUTIONS_DURING_PROCEDURE = "E872 Failure of sterile precautions during procedure"
    E873_FAILURE_IN_DOSAGE = "E873 Failure in dosage"
    E874_MECHANICAL_FAILURE_OF_INSTRUMENT_OR_APPARATUS_DURING_PROCEDURE = (
        "E874 Mechanical failure of instrument or apparatus during procedure"
    )
    E875_CONTAMINATED_OR_INFECTED_BLOOD__OTHER_FLUID__DRUG_OR_BIOLOGICAL_SUBSTANCE = (
        "E875 Contaminated or infected blood, other fluid, drug or biological substance"
    )
    E876_OTHER_AND_UNSPECIFIED_MISADVENTURES_DURING_MEDICAL_CARE = (
        "E876 Other and unspecified misadventures during medical care"
    )


class DeathPossibilitiesTaxonomyTE878E879SurgicalAndMedicalProceduresAsTheCauseOfAbnormalReactionOfPatientOrLaterComplicationWithoutMentionOfMisadventureAtTheTimeOfProcedureEntry(
    str, Enum
):
    E878_SURGICAL_OPERATION_AND_OTHER_SURGICAL_PROCEDURES_AS_THE_CAUSE_OF_ABNORMAL_REACTION_OF_PATIENT__OR_OF_LATER_COMPLICATION__WITHOUT_MENTION_OF_MISADVENTURE_AT_THE_TIME_OF_OPERATION = "E878 Surgical operation and other surgical procedures as the cause of abnormal reaction of patient, or of later complication, without mention of misadventure at the time of operation"
    E879_OTHER_PROCEDURES__WITHOUT_MENTION_OF_MISADVENTURE_AT_THE_TIME_OF_PROCEDURE__AS_THE_CAUSE_OF_ABNORMAL_REACTION_OF_PATIENT__OR_OF_LATER_COMPLICATION = "E879 Other procedures, without mention of misadventure at the time of procedure, as the cause of abnormal reaction of patient, or of later complication"


class DeathPossibilitiesTaxonomyTE880E888AccidentalFallsEntry(str, Enum):
    E880_FALL_ON_OR_FROM_STAIRS_OR_STEPS = "E880 Fall on or from stairs or steps"
    E881_FALL_ON_OR_FROM_LADDERS_OR_SCAFFOLDING = "E881 Fall on or from ladders or scaffolding"
    E882_FALL_FROM_OR_OUT_OF_BUILDING_OR_OTHER_STRUCTURE = "E882 Fall from or out of building or other structure"
    E883_FALL_INTO_HOLE_OR_OTHER_OPENING_IN_SURFACE = "E883 Fall into hole or other opening in surface"
    E884_OTHER_FALL_FROM_ONE_LEVEL_TO_ANOTHER = "E884 Other fall from one level to another"
    E885_FALL_ON_SAME_LEVEL_FROM_SLIPPING__TRIPPING_OR_STUMBLING = (
        "E885 Fall on same level from slipping, tripping or stumbling"
    )
    E886_FALL_ON_SAME_LEVEL_FROM_COLLISION__PUSHING_OR_SHOVING__BY_OR_WITH_OTHER_PERSON = (
        "E886 Fall on same level from collision, pushing or shoving, by or with other person"
    )
    E887_FRACTURE__CAUSE_UNSPECIFIED = "E887 Fracture, cause unspecified"
    E888_OTHER_AND_UNSPECIFIED_FALL = "E888 Other and unspecified fall"


class DeathPossibilitiesTaxonomyTE890E899AccidentsCausedByFireAndFlamesEntry(str, Enum):
    E890_CONFLAGRATION_IN_PRIVATE_DWELLING = "E890 Conflagration in private dwelling"
    E891_CONFLAGRATION_IN_OTHER_AND_UNSPECIFIED_BUILDING_OR_STRUCTURE = (
        "E891 Conflagration in other and unspecified building or structure"
    )
    E892_CONFLAGRATION_NOT_IN_BUILDING_OR_STRUCTURE = "E892 Conflagration not in building or structure"
    E893_ACCIDENT_CAUSED_BY_IGNITION_OF_CLOTHING = "E893 Accident caused by ignition of clothing"
    E894_IGNITION_OF_HIGHLY_INFLAMMABLE_MATERIAL = "E894 Ignition of highly inflammable material"
    E895_ACCIDENT_CAUSED_BY_CONTROLLED_FIRE_IN_PRIVATE_DWELLING = (
        "E895 Accident caused by controlled fire in private dwelling"
    )
    E896_ACCIDENT_CAUSED_BY_CONTROLLED_FIRE_IN_OTHER_AND_UNSPECIFIED_BUILDING_OR_STRUCTURE = (
        "E896 Accident caused by controlled fire in other and unspecified building or structure"
    )
    E897_ACCIDENT_CAUSED_BY_CONTROLLED_FIRE_NOT_IN_BUILDING_OR_STRUCTURE = (
        "E897 Accident caused by controlled fire not in building or structure"
    )
    E898_ACCIDENT_CAUSED_BY_OTHER_SPECIFIED_FIRE_AND_FLAMES = "E898 Accident caused by other specified fire and flames"
    E899_ACCIDENT_CAUSED_BY_UNSPECIFIED_FIRE = "E899 Accident caused by unspecified fire"


class DeathPossibilitiesTaxonomyTE900E909AccidentsDueToNaturalAndEnvironmentalFactorsEntry(str, Enum):
    E900_EXCESSIVE_HEAT = "E900 Excessive heat"
    E901_EXCESSIVE_COLD = "E901 Excessive cold"
    E902_HIGH_AND_LOW_AIR_PRESSURE_AND_CHANGES_IN_AIR_PRESSURE = (
        "E902 High and low air pressure and changes in air pressure"
    )
    E903_TRAVEL_AND_MOTION = "E903 Travel and motion"
    E904_HUNGER__THIRST__EXPOSURE__NEGLECT = "E904 Hunger, thirst, exposure, neglect"
    E905_VENOMOUS_ANIMALS_AND_PLANTS_AS_THE_CAUSE_OF_POISONING_AND_TOXIC_REACTIONS = (
        "E905 Venomous animals and plants as the cause of poisoning and toxic reactions"
    )
    E906_OTHER_INJURY_CAUSED_BY_ANIMALS = "E906 Other injury caused by animals"
    E907_LIGHTNING = "E907 Lightning"
    E908_CATACLYSMIC_STORMS_AND_FLOODS_RESULTING_FROM_STORMS = (
        "E908 Cataclysmic storms and floods resulting from storms"
    )
    E909_CATACLYSMIC_EARTH_SURFACE_MOVEMENTS_AND_ERUPTIONS = "E909 Cataclysmic earth surface movements and eruptions"


class DeathPossibilitiesTaxonomyTE910E915AccidentsCausedBySubmersionSuffocationAndForeignBodiesEntry(str, Enum):
    E910_ACCIDENTAL_DROWNING_AND_SUBMERSION = "E910 Accidental drowning and submersion"
    E911_INHALATION_AND_INGESTION_OF_FOOD_CAUSING_OBSTRUCTION_OF_RESPIRATORY_TRACT_OR_SUFFOCATION = (
        "E911 Inhalation and ingestion of food causing obstruction of respiratory tract or suffocation"
    )
    E912_INHALATION_AND_INGESTION_OF_OTHER_OBJECT_CAUSING_OBSTRUCTION_OF_RESPIRATORY_TRACT_OR_SUFFOCATION = (
        "E912 Inhalation and ingestion of other object causing obstruction of respiratory tract or suffocation"
    )
    E913_ACCIDENTAL_MECHANICAL_SUFFOCATION = "E913 Accidental mechanical suffocation"
    E914_FOREIGN_BODY_ACCIDENTALLY_ENTERING_EYE_AND_ADNEXA = "E914 Foreign body accidentally entering eye and adnexa"
    E915_FOREIGN_BODY_ACCIDENTALLY_ENTERING_OTHER_ORIFICE = "E915 Foreign body accidentally entering other orifice"


class DeathPossibilitiesTaxonomyTE916E928OtherAccidentsEntry(str, Enum):
    E916_STRUCK_ACCIDENTALLY_BY_FALLING_OBJECT = "E916 Struck accidentally by falling object"
    E917_STRIKING_AGAINST_OR_STRUCK_ACCIDENTALLY_BY_OBJECTS_OR_PERSONS = (
        "E917 Striking against or struck accidentally by objects or persons"
    )
    E918_CAUGHT_ACCIDENTALLY_IN_OR_BETWEEN_OBJECTS = "E918 Caught accidentally in or between objects"
    E919_ACCIDENTS_CAUSED_BY_MACHINERY = "E919 Accidents caused by machinery"
    E920_ACCIDENTS_CAUSED_BY_CUTTING_AND_PIERCING_INSTRUMENTS_OR_OBJECTS = (
        "E920 Accidents caused by cutting and piercing instruments or objects"
    )
    E921_ACCIDENT_CAUSED_BY_EXPLOSION_OF_PRESSURE_VESSEL = "E921 Accident caused by explosion of pressure vessel"
    E922_ACCIDENT_CAUSED_BY_FIREARM_MISSILE = "E922 Accident caused by firearm missile"
    E923_ACCIDENT_CAUSED_BY_EXPLOSIVE_MATERIAL = "E923 Accident caused by explosive material"
    E924_ACCIDENT_CAUSED_BY_HOT_SUBSTANCE_OR_OBJECT__CAUSTIC_OR_CORROSIVE_MATERIAL_AND_STEAM = (
        "E924 Accident caused by hot substance or object, caustic or corrosive material and steam"
    )
    E925_ACCIDENT_CAUSED_BY_ELECTRIC_CURRENT = "E925 Accident caused by electric current"
    E926_EXPOSURE_TO_RADIATION = "E926 Exposure to radiation"
    E927_OVEREXERTION_AND_STRENUOUS_MOVEMENTS = "E927 Overexertion and strenuous movements"
    E928_OTHER_AND_UNSPECIFIED_ENVIRONMENTAL_AND_ACCIDENTAL_CAUSES = (
        "E928 Other and unspecified environmental and accidental causes"
    )


class DeathPossibilitiesTaxonomyTE929E929LateEffectsOfAccidentalInjuryEntry(str, Enum):
    E929_LATE_EFFECTS_OF_ACCIDENTAL_INJURY = "E929 Late effects of accidental injury"


class DeathPossibilitiesTaxonomyTE930E949DrugsMedicamentsAndBiologicalSubstancesCausingAdverseEffectsInTherapeuticUseEntry(
    str, Enum
):
    E930_ANTIBIOTICS = "E930 Antibiotics"
    E931_OTHER_ANTI_INFECTIVES = "E931 Other anti-infectives"
    E932_HORMONES_AND_SYNTHETIC_SUBSTITUTES = "E932 Hormones and synthetic substitutes"
    E933_PRIMARILY_SYSTEMIC_AGENTS = "E933 Primarily systemic agents"
    E934_AGENTS_PRIMARILY_AFFECTING_BLOOD_CONSTITUENTS = "E934 Agents primarily affecting blood constituents"
    E935_ANALGESICS__ANTIPYRETICS_AND_ANTIRHEUMATICS = "E935 Analgesics, antipyretics and antirheumatics"
    E936_ANTICONVULSANTS_AND_ANTI_PARKINSONISM_DRUGS = "E936 Anticonvulsants and anti-Parkinsonism drugs"
    E937_SEDATIVES_AND_HYPNOTICS = "E937 Sedatives and hypnotics"
    E938_OTHER_CENTRAL_NERVOUS_SYSTEM_DEPRESSANTS_AND_ANAESTHETICS = (
        "E938 Other central nervous system depressants and anaesthetics"
    )
    E939_PSYCHOTROPIC_AGENTS = "E939 Psychotropic agents"
    E940_CENTRAL_NERVOUS_SYSTEM_STIMULANTS = "E940 Central nervous system stimulants"
    E941_DRUGS_PRIMARILY_AFFECTING_THE_AUTONOMIC_NERVOUS_SYSTEM = (
        "E941 Drugs primarily affecting the autonomic nervous system"
    )
    E942_AGENTS_PRIMARILY_AFFECTING_THE_CARDIOVASCULAR_SYSTEM = (
        "E942 Agents primarily affecting the cardiovascular system"
    )
    E943_AGENTS_PRIMARILY_AFFECTING_GASTRO_INTESTINAL_SYSTEM = (
        "E943 Agents primarily affecting gastro-intestinal system"
    )
    E944_WATER__MINERAL_AND_URIC_ACID_METABOLISM_DRUGS = "E944 Water, mineral and uric acid metabolism drugs"
    E945_AGENTS_PRIMARILY_ACTING_ON_THE_SMOOTH_AND_SKELETAL_MUSCLES_AND_RESPIRATORY_SYSTEM = (
        "E945 Agents primarily acting on the smooth and skeletal muscles and respiratory system"
    )
    E946_AGENTS_PRIMARILY_AFFECTING_SKIN_AND_MUCOUS_MEMBRANE__OPHTHALMOLOGICAL__OTORHINOLARYNGOLOGICAL_AND_DENTAL_DRUGS = "E946 Agents primarily affecting skin and mucous membrane, ophthalmological, otorhinolaryngological and dental drugs"
    E947_OTHER_AND_UNSPECIFIED_DRUGS_AND_MEDICAMENTS = "E947 Other and unspecified drugs and medicaments"
    E948_BACTERIAL_VACCINES = "E948 Bacterial vaccines"
    E949_OTHER_VACCINES_AND_BIOLOGICAL_SUBSTANCES = "E949 Other vaccines and biological substances"


class DeathPossibilitiesTaxonomyTE950E959SuicideAndSelfInflictedInjuryEntry(str, Enum):
    E950_SUICIDE_AND_SELF_INFLICTED_POISONING_BY_SOLID_OR_LIQUID_SUBSTANCES = (
        "E950 Suicide and self-inflicted poisoning by solid or liquid substances"
    )
    E951_SUICIDE_AND_SELF_INFLICTED_POISONING_BY_GASES_IN_DOMESTIC_USE = (
        "E951 Suicide and self-inflicted poisoning by gases in domestic use"
    )
    E952_SUICIDE_AND_SELF_INFLICTED_POISONING_BY_OTHER_GASES_AND_VAPOURS = (
        "E952 Suicide and self-inflicted poisoning by other gases and vapours"
    )
    E953_SUICIDE_AND_SELF_INFLICTED_INJURY_BY_HANGING__STRANGULATION_AND_SUFFOCATION = (
        "E953 Suicide and self-inflicted injury by hanging, strangulation and suffocation"
    )
    E954_SUICIDE_AND_SELF_INFLICTED_INJURY_BY_SUBMERSION__DROWNING_ = (
        "E954 Suicide and self-inflicted injury by submersion [drowning]"
    )
    E955_SUICIDE_AND_SELF_INFLICTED_INJURY_BY_FIREARMS_AND_EXPLOSIVES = (
        "E955 Suicide and self-inflicted injury by firearms and explosives"
    )
    E956_SUICIDE_AND_SELF_INFLICTED_INJURY_BY_CUTTING_AND_PIERCING_INSTRUMENTS = (
        "E956 Suicide and self-inflicted injury by cutting and piercing instruments"
    )
    E957_SUICIDE_AND_SELF_INFLICTED_INJURIES_BY_JUMPING_FROM_HIGH_PLACE = (
        "E957 Suicide and self-inflicted injuries by jumping from high place"
    )
    E958_SUICIDE_AND_SELF_INFLICTED_INJURY_BY_OTHER_AND_UNSPECIFIED_MEANS = (
        "E958 Suicide and self-inflicted injury by other and unspecified means"
    )
    E959_LATE_EFFECTS_OF_SELF_INFLICTED_INJURY = "E959 Late effects of self-inflicted injury"


class DeathPossibilitiesTaxonomyTE960E969HomicideAndInjuryPurposelyInflictedByOtherPersonsEntry(str, Enum):
    E960_FIGHT__BRAWL__RAPE = "E960 Fight, brawl, rape"
    E961_ASSAULT_BY_CORROSIVE_OR_CAUSTIC_SUBSTANCE__EXCEPT_POISONING = (
        "E961 Assault by corrosive or caustic substance, except poisoning"
    )
    E962_ASSAULT_BY_POISONING = "E962 Assault by poisoning"
    E963_ASSAULT_BY_HANGING_AND_STRANGULATION = "E963 Assault by hanging and strangulation"
    E964_ASSAULT_BY_SUBMERSION__DROWNING_ = "E964 Assault by submersion [drowning]"
    E965_ASSAULT_BY_FIREARMS_AND_EXPLOSIVES = "E965 Assault by firearms and explosives"
    E966_ASSAULT_BY_CUTTING_AND_PIERCING_INSTRUMENT = "E966 Assault by cutting and piercing instrument"
    E967_CHILD_BATTERING_AND_OTHER_MALTREATMENT = "E967 Child battering and other maltreatment"
    E968_ASSAULT_BY_OTHER_AND_UNSPECIFIED_MEANS = "E968 Assault by other and unspecified means"
    E969_LATE_EFFECTS_OF_INJURY_PURPOSELY_INFLICTED_BY_OTHER_PERSON = (
        "E969 Late effects of injury purposely inflicted by other person"
    )


class DeathPossibilitiesTaxonomy(BaseModel):
    """Model for the death-possibilities taxonomy."""

    namespace: str = "death-possibilities"
    description: str = """Taxonomy of Death Possibilities"""
    version: int = 1
    exclusive: bool = False
    predicates: List[DeathPossibilitiesTaxonomyPredicate] = []
    t__001_009__intestinal_infectious_diseases_entries: List[
        DeathPossibilitiesTaxonomyT001009IntestinalInfectiousDiseasesEntry
    ] = []
    t__010_018__tuberculosis_entries: List[DeathPossibilitiesTaxonomyT010018TuberculosisEntry] = []
    t__020_027__zoonotic_bacterial_diseases_entries: List[
        DeathPossibilitiesTaxonomyT020027ZoonoticBacterialDiseasesEntry
    ] = []
    t__030_041__other_bacterial_diseases_entries: List[
        DeathPossibilitiesTaxonomyT030041OtherBacterialDiseasesEntry
    ] = []
    t__042_042__human_immunodeficiency_virus__hiv__infection_entries: List[
        DeathPossibilitiesTaxonomyT042042HumanImmunodeficiencyVirusHivInfectionEntry
    ] = []
    t__045_049__poliomyelitis_and_other_non_arthropod_borne_viral_diseases_of_central_nervous_system_entries: List[
        DeathPossibilitiesTaxonomyT045049PoliomyelitisAndOtherNonArthropodBorneViralDiseasesOfCentralNervousSystemEntry
    ] = []
    t__050_057__viral_diseases_accompanied_by_exanthem_entries: List[
        DeathPossibilitiesTaxonomyT050057ViralDiseasesAccompaniedByExanthemEntry
    ] = []
    t__060_066__arthropod_borne_viral_diseases_entries: List[
        DeathPossibilitiesTaxonomyT060066ArthropodBorneViralDiseasesEntry
    ] = []
    t__070_079__other_diseases_due_to_viruses_and_chlamydiae_entries: List[
        DeathPossibilitiesTaxonomyT070079OtherDiseasesDueToVirusesAndChlamydiaeEntry
    ] = []
    t__080_088__rickettsioses_and_other_arthropod_borne_diseases_entries: List[
        DeathPossibilitiesTaxonomyT080088RickettsiosesAndOtherArthropodBorneDiseasesEntry
    ] = []
    t__090_099__syphilis_and_other_venereal_diseases_entries: List[
        DeathPossibilitiesTaxonomyT090099SyphilisAndOtherVenerealDiseasesEntry
    ] = []
    t__100_104__other_spirochaetal_diseases_entries: List[
        DeathPossibilitiesTaxonomyT100104OtherSpirochaetalDiseasesEntry
    ] = []
    t__110_118__mycoses_entries: List[DeathPossibilitiesTaxonomyT110118MycosesEntry] = []
    t__120_129__helminthiases_entries: List[DeathPossibilitiesTaxonomyT120129HelminthiasesEntry] = []
    t__130_136__other_infectious_and_parasitic_diseases_entries: List[
        DeathPossibilitiesTaxonomyT130136OtherInfectiousAndParasiticDiseasesEntry
    ] = []
    t__137_139__late_effects_of_infectious_and_parasitic_diseases_entries: List[
        DeathPossibilitiesTaxonomyT137139LateEffectsOfInfectiousAndParasiticDiseasesEntry
    ] = []
    t__140_149__malignant_neoplasm_of_lip__oral_cavity_and_pharynx_entries: List[
        DeathPossibilitiesTaxonomyT140149MalignantNeoplasmOfLipOralCavityAndPharynxEntry
    ] = []
    t__150_159__malignant_neoplasm_of_digestive_organs_and_peritoneum_entries: List[
        DeathPossibilitiesTaxonomyT150159MalignantNeoplasmOfDigestiveOrgansAndPeritoneumEntry
    ] = []
    t__160_165__malignant_neoplasm_of_respiratory_and_intrathoracic_organs_entries: List[
        DeathPossibilitiesTaxonomyT160165MalignantNeoplasmOfRespiratoryAndIntrathoracicOrgansEntry
    ] = []
    t__170_176__malignant_neoplasm_of_bone__connective_tissue__skin_and_breast_entries: List[
        DeathPossibilitiesTaxonomyT170176MalignantNeoplasmOfBoneConnectiveTissueSkinAndBreastEntry
    ] = []
    t__179_189__malignant_neoplasm_of_genito_urinary_organs_entries: List[
        DeathPossibilitiesTaxonomyT179189MalignantNeoplasmOfGenitoUrinaryOrgansEntry
    ] = []
    t__190_199__malignant_neoplasm_of_other_and_unspecified_sites_entries: List[
        DeathPossibilitiesTaxonomyT190199MalignantNeoplasmOfOtherAndUnspecifiedSitesEntry
    ] = []
    t__200_208__malignant_neoplasm_of_lymphatic_and_haematopoietic_tissue_entries: List[
        DeathPossibilitiesTaxonomyT200208MalignantNeoplasmOfLymphaticAndHaematopoieticTissueEntry
    ] = []
    t__210_229__benign_neoplasms_entries: List[DeathPossibilitiesTaxonomyT210229BenignNeoplasmsEntry] = []
    t__230_234__carcinoma_in_situ_entries: List[DeathPossibilitiesTaxonomyT230234CarcinomaInSituEntry] = []
    t__235_238__neoplasms_of_uncertain_behaviour_entries: List[
        DeathPossibilitiesTaxonomyT235238NeoplasmsOfUncertainBehaviourEntry
    ] = []
    t__239_239__neoplasms_of_unspecified_nature_entries: List[
        DeathPossibilitiesTaxonomyT239239NeoplasmsOfUnspecifiedNatureEntry
    ] = []
    t__240_246__disorders_of_thyroid_gland_entries: List[
        DeathPossibilitiesTaxonomyT240246DisordersOfThyroidGlandEntry
    ] = []
    t__250_259__diseases_of_other_endocrine_glands_entries: List[
        DeathPossibilitiesTaxonomyT250259DiseasesOfOtherEndocrineGlandsEntry
    ] = []
    t__260_269__nutritional_deficiencies_entries: List[
        DeathPossibilitiesTaxonomyT260269NutritionalDeficienciesEntry
    ] = []
    t__270_279__other_metabolic_disorders_and_immunity_disorders_entries: List[
        DeathPossibilitiesTaxonomyT270279OtherMetabolicDisordersAndImmunityDisordersEntry
    ] = []
    t__280_289__diseases_of_blood_and_blood_forming_organs_entries: List[
        DeathPossibilitiesTaxonomyT280289DiseasesOfBloodAndBloodFormingOrgansEntry
    ] = []
    t__290_294__organic_psychotic_conditions_entries: List[
        DeathPossibilitiesTaxonomyT290294OrganicPsychoticConditionsEntry
    ] = []
    t__295_299__other_psychoses_entries: List[DeathPossibilitiesTaxonomyT295299OtherPsychosesEntry] = []
    t__300_316__neurotic_disorders__personality_disorders_and_other_nonpsychotic_mental_disorders_entries: List[
        DeathPossibilitiesTaxonomyT300316NeuroticDisordersPersonalityDisordersAndOtherNonpsychoticMentalDisordersEntry
    ] = []
    t__317_319__mental_retardation_entries: List[DeathPossibilitiesTaxonomyT317319MentalRetardationEntry] = []
    t__320_326__inflammatory_diseases_of_the_central_nervous_system_entries: List[
        DeathPossibilitiesTaxonomyT320326InflammatoryDiseasesOfTheCentralNervousSystemEntry
    ] = []
    t__330_337__hereditary_and_degenerative_diseases_of_the_central_nervous_system_entries: List[
        DeathPossibilitiesTaxonomyT330337HereditaryAndDegenerativeDiseasesOfTheCentralNervousSystemEntry
    ] = []
    t__340_349__other_disorders_of_the_central_nervous_system_entries: List[
        DeathPossibilitiesTaxonomyT340349OtherDisordersOfTheCentralNervousSystemEntry
    ] = []
    t__350_359__disorders_of_the_peripheral_nervous_system_entries: List[
        DeathPossibilitiesTaxonomyT350359DisordersOfThePeripheralNervousSystemEntry
    ] = []
    t__360_379__disorders_of_the_eye_and_adnexa_entries: List[
        DeathPossibilitiesTaxonomyT360379DisordersOfTheEyeAndAdnexaEntry
    ] = []
    t__380_389__diseases_of_the_ear_and_mastoid_process_entries: List[
        DeathPossibilitiesTaxonomyT380389DiseasesOfTheEarAndMastoidProcessEntry
    ] = []
    t__390_392__acute_rheumatic_fever_entries: List[DeathPossibilitiesTaxonomyT390392AcuteRheumaticFeverEntry] = []
    t__393_398__chronic_rheumatic_heart_disease_entries: List[
        DeathPossibilitiesTaxonomyT393398ChronicRheumaticHeartDiseaseEntry
    ] = []
    t__401_405__hypertensive_disease_entries: List[DeathPossibilitiesTaxonomyT401405HypertensiveDiseaseEntry] = []
    t__410_414__ischaemic_heart_disease_entries: List[DeathPossibilitiesTaxonomyT410414IschaemicHeartDiseaseEntry] = []
    t__415_417__diseases_of_pulmonary_circulation_entries: List[
        DeathPossibilitiesTaxonomyT415417DiseasesOfPulmonaryCirculationEntry
    ] = []
    t__420_429__other_forms_of_heart_disease_entries: List[
        DeathPossibilitiesTaxonomyT420429OtherFormsOfHeartDiseaseEntry
    ] = []
    t__430_438__cerebrovascular_disease_entries: List[DeathPossibilitiesTaxonomyT430438CerebrovascularDiseaseEntry] = []
    t__440_448__diseases_of_arteries__arterioles_and_capillaries_entries: List[
        DeathPossibilitiesTaxonomyT440448DiseasesOfArteriesArteriolesAndCapillariesEntry
    ] = []
    t__451_459__diseases_of_veins_and_lymphatics__and_other_diseases_of_circulatory_system_entries: List[
        DeathPossibilitiesTaxonomyT451459DiseasesOfVeinsAndLymphaticsAndOtherDiseasesOfCirculatorySystemEntry
    ] = []
    t__460_466__acute_respiratory_infections_entries: List[
        DeathPossibilitiesTaxonomyT460466AcuteRespiratoryInfectionsEntry
    ] = []
    t__470_478__other_diseases_of_upper_respiratory_tract_entries: List[
        DeathPossibilitiesTaxonomyT470478OtherDiseasesOfUpperRespiratoryTractEntry
    ] = []
    t__480_487__pneumonia_and_influenza_entries: List[DeathPossibilitiesTaxonomyT480487PneumoniaAndInfluenzaEntry] = []
    t__490_496__chronic_obstructive_pulmonary_disease_and_allied_conditions_entries: List[
        DeathPossibilitiesTaxonomyT490496ChronicObstructivePulmonaryDiseaseAndAlliedConditionsEntry
    ] = []
    t__500_508__pneumoconioses_and_other_lung_diseases_due_to_external_agents_entries: List[
        DeathPossibilitiesTaxonomyT500508PneumoconiosesAndOtherLungDiseasesDueToExternalAgentsEntry
    ] = []
    t__510_519__other_diseases_of_respiratory_system_entries: List[
        DeathPossibilitiesTaxonomyT510519OtherDiseasesOfRespiratorySystemEntry
    ] = []
    t__520_529__diseases_of_oral_cavity__salivary_glands_and_jaws_entries: List[
        DeathPossibilitiesTaxonomyT520529DiseasesOfOralCavitySalivaryGlandsAndJawsEntry
    ] = []
    t__530_537__diseases_of_oesophagus__stomach_and_duodenum_entries: List[
        DeathPossibilitiesTaxonomyT530537DiseasesOfOesophagusStomachAndDuodenumEntry
    ] = []
    t__540_543__appendicitis_entries: List[DeathPossibilitiesTaxonomyT540543AppendicitisEntry] = []
    t__550_553__hernia_of_abdominal_cavity_entries: List[
        DeathPossibilitiesTaxonomyT550553HerniaOfAbdominalCavityEntry
    ] = []
    t__555_558__non_infective_enteritis_and_colitis_entries: List[
        DeathPossibilitiesTaxonomyT555558NonInfectiveEnteritisAndColitisEntry
    ] = []
    t__560_569__other_diseases_of_intestines_and_peritoneum_entries: List[
        DeathPossibilitiesTaxonomyT560569OtherDiseasesOfIntestinesAndPeritoneumEntry
    ] = []
    t__570_579__other_diseases_of_digestive_system_entries: List[
        DeathPossibilitiesTaxonomyT570579OtherDiseasesOfDigestiveSystemEntry
    ] = []
    t__580_589__nephritis__nephrotic_syndrome_and_nephrosis_entries: List[
        DeathPossibilitiesTaxonomyT580589NephritisNephroticSyndromeAndNephrosisEntry
    ] = []
    t__590_599__other_diseases_of_urinary_system_entries: List[
        DeathPossibilitiesTaxonomyT590599OtherDiseasesOfUrinarySystemEntry
    ] = []
    t__600_608__diseases_of_male_genital_organs_entries: List[
        DeathPossibilitiesTaxonomyT600608DiseasesOfMaleGenitalOrgansEntry
    ] = []
    t__610_611__disorders_of_breast_entries: List[DeathPossibilitiesTaxonomyT610611DisordersOfBreastEntry] = []
    t__614_616__inflammatory_disease_of_female_pelvic_organs_entries: List[
        DeathPossibilitiesTaxonomyT614616InflammatoryDiseaseOfFemalePelvicOrgansEntry
    ] = []
    t__617_629__other_disorders_of_female_genital_tract_entries: List[
        DeathPossibilitiesTaxonomyT617629OtherDisordersOfFemaleGenitalTractEntry
    ] = []
    t__630_633__ectopic_and_molar_pregnancy_entries: List[
        DeathPossibilitiesTaxonomyT630633EctopicAndMolarPregnancyEntry
    ] = []
    t__634_639__other_pregnancy_with_abortive_outcome_entries: List[
        DeathPossibilitiesTaxonomyT634639OtherPregnancyWithAbortiveOutcomeEntry
    ] = []
    t__640_648__complications_mainly_related_to_pregnancy_entries: List[
        DeathPossibilitiesTaxonomyT640648ComplicationsMainlyRelatedToPregnancyEntry
    ] = []
    t__650_659__normal_delivery_and_other_indications_for_care_in_pregnancy__labour_and_delivery_entries: List[
        DeathPossibilitiesTaxonomyT650659NormalDeliveryAndOtherIndicationsForCareInPregnancyLabourAndDeliveryEntry
    ] = []
    t__660_669__complications_occurring_mainly_in_the_course_of_labour_and_delivery_entries: List[
        DeathPossibilitiesTaxonomyT660669ComplicationsOccurringMainlyInTheCourseOfLabourAndDeliveryEntry
    ] = []
    t__670_677__complications_of_the_puerperium_entries: List[
        DeathPossibilitiesTaxonomyT670677ComplicationsOfThePuerperiumEntry
    ] = []
    t__680_686__infections_of_skin_and_subcutaneous_tissue_entries: List[
        DeathPossibilitiesTaxonomyT680686InfectionsOfSkinAndSubcutaneousTissueEntry
    ] = []
    t__690_698__other_inflammatory_conditions_of_skin_and_subcutaneous_tissue_entries: List[
        DeathPossibilitiesTaxonomyT690698OtherInflammatoryConditionsOfSkinAndSubcutaneousTissueEntry
    ] = []
    t__700_709__other_diseases_of_skin_and_subcutaneous_tissue_entries: List[
        DeathPossibilitiesTaxonomyT700709OtherDiseasesOfSkinAndSubcutaneousTissueEntry
    ] = []
    t__710_719__arthropathies_and_related_disorders_entries: List[
        DeathPossibilitiesTaxonomyT710719ArthropathiesAndRelatedDisordersEntry
    ] = []
    t__720_724__dorsopathies_entries: List[DeathPossibilitiesTaxonomyT720724DorsopathiesEntry] = []
    t__725_729__rheumatism__excluding_the_back_entries: List[
        DeathPossibilitiesTaxonomyT725729RheumatismExcludingTheBackEntry
    ] = []
    t__730_739__osteopathies__chondropathies_and_acquired_musculoskeletal_deformities_entries: List[
        DeathPossibilitiesTaxonomyT730739OsteopathiesChondropathiesAndAcquiredMusculoskeletalDeformitiesEntry
    ] = []
    t__740_759__congenital_anomalies_entries: List[DeathPossibilitiesTaxonomyT740759CongenitalAnomaliesEntry] = []
    t__760_763__maternal_causes_of_perinatal_morbidity_and_mortality_entries: List[
        DeathPossibilitiesTaxonomyT760763MaternalCausesOfPerinatalMorbidityAndMortalityEntry
    ] = []
    t__764_779__other_conditions_originating_in_the_perinatal_period_entries: List[
        DeathPossibilitiesTaxonomyT764779OtherConditionsOriginatingInThePerinatalPeriodEntry
    ] = []
    t__780_789__symptoms_entries: List[DeathPossibilitiesTaxonomyT780789SymptomsEntry] = []
    t__790_796__nonspecific_abnormal_findings_entries: List[
        DeathPossibilitiesTaxonomyT790796NonspecificAbnormalFindingsEntry
    ] = []
    t__797_799__ill_defined_and_unknown_causes_of_morbidity_and_mortality_entries: List[
        DeathPossibilitiesTaxonomyT797799IllDefinedAndUnknownCausesOfMorbidityAndMortalityEntry
    ] = []
    t__800_804__fracture_of_skull_entries: List[DeathPossibilitiesTaxonomyT800804FractureOfSkullEntry] = []
    t__805_809__fracture_of_neck_and_trunk_entries: List[
        DeathPossibilitiesTaxonomyT805809FractureOfNeckAndTrunkEntry
    ] = []
    t__810_819__fracture_of_upper_limb_entries: List[DeathPossibilitiesTaxonomyT810819FractureOfUpperLimbEntry] = []
    t__820_829__fracture_of_lower_limb_entries: List[DeathPossibilitiesTaxonomyT820829FractureOfLowerLimbEntry] = []
    t__830_839__dislocation_entries: List[DeathPossibilitiesTaxonomyT830839DislocationEntry] = []
    t__840_848__sprains_and_strains_of_joints_and_adjacent_muscles_entries: List[
        DeathPossibilitiesTaxonomyT840848SprainsAndStrainsOfJointsAndAdjacentMusclesEntry
    ] = []
    t__850_854__intracranial_injury__excluding_those_with_skull_fracture_entries: List[
        DeathPossibilitiesTaxonomyT850854IntracranialInjuryExcludingThoseWithSkullFractureEntry
    ] = []
    t__860_869__internal_injury_of_chest__abdomen_and_pelvis_entries: List[
        DeathPossibilitiesTaxonomyT860869InternalInjuryOfChestAbdomenAndPelvisEntry
    ] = []
    t__870_879__open_wound_of_head__neck_and_trunk_entries: List[
        DeathPossibilitiesTaxonomyT870879OpenWoundOfHeadNeckAndTrunkEntry
    ] = []
    t__880_887__open_wound_of_upper_limb_entries: List[DeathPossibilitiesTaxonomyT880887OpenWoundOfUpperLimbEntry] = []
    t__890_897__open_wound_of_lower_limb_entries: List[DeathPossibilitiesTaxonomyT890897OpenWoundOfLowerLimbEntry] = []
    t__900_904__injury_to_blood_vessels_entries: List[DeathPossibilitiesTaxonomyT900904InjuryToBloodVesselsEntry] = []
    t__905_909__late_effects_of_injuries__poisonings__toxic_effects_and_other_external_causes_entries: List[
        DeathPossibilitiesTaxonomyT905909LateEffectsOfInjuriesPoisoningsToxicEffectsAndOtherExternalCausesEntry
    ] = []
    t__910_919__superficial_injury_entries: List[DeathPossibilitiesTaxonomyT910919SuperficialInjuryEntry] = []
    t__920_924__contusion_with_intact_skin_surface_entries: List[
        DeathPossibilitiesTaxonomyT920924ContusionWithIntactSkinSurfaceEntry
    ] = []
    t__925_929__crushing_injury_entries: List[DeathPossibilitiesTaxonomyT925929CrushingInjuryEntry] = []
    t__930_939__effects_of_foreign_body_entering_through_orifice_entries: List[
        DeathPossibilitiesTaxonomyT930939EffectsOfForeignBodyEnteringThroughOrificeEntry
    ] = []
    t__940_949__burns_entries: List[DeathPossibilitiesTaxonomyT940949BurnsEntry] = []
    t__950_957__injury_to_nerves_and_spinal_cord_entries: List[
        DeathPossibilitiesTaxonomyT950957InjuryToNervesAndSpinalCordEntry
    ] = []
    t__958_959__certain_traumatic_complications_and_unspecified_injuries_entries: List[
        DeathPossibilitiesTaxonomyT958959CertainTraumaticComplicationsAndUnspecifiedInjuriesEntry
    ] = []
    t__960_979__poisoning_by_drugs__medicaments_and_biological_substances_entries: List[
        DeathPossibilitiesTaxonomyT960979PoisoningByDrugsMedicamentsAndBiologicalSubstancesEntry
    ] = []
    t__980_989__toxic_effects_of_substances_chiefly_nonmedicinal_as_to_source_entries: List[
        DeathPossibilitiesTaxonomyT980989ToxicEffectsOfSubstancesChieflyNonmedicinalAsToSourceEntry
    ] = []
    t__990_995__other_and_unspecified_effects_of_external_causes_entries: List[
        DeathPossibilitiesTaxonomyT990995OtherAndUnspecifiedEffectsOfExternalCausesEntry
    ] = []
    t__996_999__complications_of_surgical_and_medical_care__not_elsewhere_classified_entries: List[
        DeathPossibilitiesTaxonomyT996999ComplicationsOfSurgicalAndMedicalCareNotElsewhereClassifiedEntry
    ] = []
    t__e800_e807__railway_accidents_entries: List[DeathPossibilitiesTaxonomyTE800E807RailwayAccidentsEntry] = []
    t__e810_e819__motor_vehicle_traffic_accidents_entries: List[
        DeathPossibilitiesTaxonomyTE810E819MotorVehicleTrafficAccidentsEntry
    ] = []
    t__e820_e825__motor_vehicle_nontraffic_accidents_entries: List[
        DeathPossibilitiesTaxonomyTE820E825MotorVehicleNontrafficAccidentsEntry
    ] = []
    t__e826_e829__other_road_vehicle_accidents_entries: List[
        DeathPossibilitiesTaxonomyTE826E829OtherRoadVehicleAccidentsEntry
    ] = []
    t__e830_e838__water_transport_accidents_entries: List[
        DeathPossibilitiesTaxonomyTE830E838WaterTransportAccidentsEntry
    ] = []
    t__e840_e845__air_and_space_transport_accidents_entries: List[
        DeathPossibilitiesTaxonomyTE840E845AirAndSpaceTransportAccidentsEntry
    ] = []
    t__e846_e848__vehicle_accidents_not_elsewhere_classifiable_entries: List[
        DeathPossibilitiesTaxonomyTE846E848VehicleAccidentsNotElsewhereClassifiableEntry
    ] = []
    t__e849_e858__accidental_poisoning_by_drugs__medicaments_and_biologicals_entries: List[
        DeathPossibilitiesTaxonomyTE849E858AccidentalPoisoningByDrugsMedicamentsAndBiologicalsEntry
    ] = []
    t__e860_e869__accidental_poisoning_by_other_solid_and_liquid_substances__gases_and_vapours_entries: List[
        DeathPossibilitiesTaxonomyTE860E869AccidentalPoisoningByOtherSolidAndLiquidSubstancesGasesAndVapoursEntry
    ] = []
    t__e870_e876__misadventures_to_patients_during_surgical_and_medical_care_entries: List[
        DeathPossibilitiesTaxonomyTE870E876MisadventuresToPatientsDuringSurgicalAndMedicalCareEntry
    ] = []
    t__e878_e879__surgical_and_medical_procedures_as_the_cause_of_abnormal_reaction_of_patient_or_later_complication__without_mention_of_misadventure_at_the_time_of_procedure_entries: List[
        DeathPossibilitiesTaxonomyTE878E879SurgicalAndMedicalProceduresAsTheCauseOfAbnormalReactionOfPatientOrLaterComplicationWithoutMentionOfMisadventureAtTheTimeOfProcedureEntry
    ] = []
    t__e880_e888__accidental_falls_entries: List[DeathPossibilitiesTaxonomyTE880E888AccidentalFallsEntry] = []
    t__e890_e899__accidents_caused_by_fire_and_flames_entries: List[
        DeathPossibilitiesTaxonomyTE890E899AccidentsCausedByFireAndFlamesEntry
    ] = []
    t__e900_e909__accidents_due_to_natural_and_environmental_factors_entries: List[
        DeathPossibilitiesTaxonomyTE900E909AccidentsDueToNaturalAndEnvironmentalFactorsEntry
    ] = []
    t__e910_e915__accidents_caused_by_submersion__suffocation_and_foreign_bodies_entries: List[
        DeathPossibilitiesTaxonomyTE910E915AccidentsCausedBySubmersionSuffocationAndForeignBodiesEntry
    ] = []
    t__e916_e928__other_accidents_entries: List[DeathPossibilitiesTaxonomyTE916E928OtherAccidentsEntry] = []
    t__e929_e929__late_effects_of_accidental_injury_entries: List[
        DeathPossibilitiesTaxonomyTE929E929LateEffectsOfAccidentalInjuryEntry
    ] = []
    t__e930_e949__drugs__medicaments_and_biological_substances_causing_adverse_effects_in_therapeutic_use_entries: List[
        DeathPossibilitiesTaxonomyTE930E949DrugsMedicamentsAndBiologicalSubstancesCausingAdverseEffectsInTherapeuticUseEntry
    ] = []
    t__e950_e959__suicide_and_self_inflicted_injury_entries: List[
        DeathPossibilitiesTaxonomyTE950E959SuicideAndSelfInflictedInjuryEntry
    ] = []
    t__e960_e969__homicide_and_injury_purposely_inflicted_by_other_persons_entries: List[
        DeathPossibilitiesTaxonomyTE960E969HomicideAndInjuryPurposelyInflictedByOtherPersonsEntry
    ] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
