"""Taxonomies models for the OpenMISP SDK.

This package contains the models for the taxonomies used in MISP.
The models are dynamically generated from the MISP taxonomies repository.
"""

# Import all taxonomy models
from .access_method import AccessMethodTaxonomy, AccessMethodTaxonomyPredicate
from .accessnow import AccessnowTaxonomy, AccessnowTaxonomyPredicate
from .acs_marking import (
    AcsMarkingTaxonomy,
    AcsMarkingTaxonomyCaveatEntry,
    AcsMarkingTaxonomyClassificationEntry,
    AcsMarkingTaxonomyEntityEntry,
    AcsMarkingTaxonomyFormalDeterminationEntry,
    AcsMarkingTaxonomyPredicate,
    AcsMarkingTaxonomyPrivilegeActionEntry,
    AcsMarkingTaxonomySensitivityEntry,
    AcsMarkingTaxonomyShareabilityEntry,
)
from .action_taken import ActionTakenTaxonomy, ActionTakenTaxonomyPredicate
from .admiralty_scale import (
    AdmiraltyScaleTaxonomy,
    AdmiraltyScaleTaxonomyInformationCredibilityEntry,
    AdmiraltyScaleTaxonomyPredicate,
    AdmiraltyScaleTaxonomySourceReliabilityEntry,
)
from .adversary import (
    AdversaryTaxonomy,
    AdversaryTaxonomyInfrastructureActionEntry,
    AdversaryTaxonomyInfrastructureStateEntry,
    AdversaryTaxonomyInfrastructureStatusEntry,
    AdversaryTaxonomyInfrastructureTypeEntry,
    AdversaryTaxonomyPredicate,
)
from .ais_marking import (
    AisMarkingTaxonomy,
    AisMarkingTaxonomyAisconsentEntry,
    AisMarkingTaxonomyAismarkingEntry,
    AisMarkingTaxonomyCisaProprietaryEntry,
    AisMarkingTaxonomyPredicate,
    AisMarkingTaxonomyTlpmarkingEntry,
)
from .analyst_assessment import (
    AnalystAssessmentTaxonomy,
    AnalystAssessmentTaxonomyBinaryReversingArchEntry,
    AnalystAssessmentTaxonomyBinaryReversingExperienceEntry,
    AnalystAssessmentTaxonomyCryptoExperienceEntry,
    AnalystAssessmentTaxonomyExperienceEntry,
    AnalystAssessmentTaxonomyOsEntry,
    AnalystAssessmentTaxonomyPredicate,
    AnalystAssessmentTaxonomyWebEntry,
    AnalystAssessmentTaxonomyWebExperienceEntry,
)
from .approved_category_of_action import ApprovedCategoryOfActionTaxonomy, ApprovedCategoryOfActionTaxonomyPredicate
from .artificial_satellites import (
    ArtificialSatellitesTaxonomy,
    ArtificialSatellitesTaxonomyDisasterMonitoringEntry,
    ArtificialSatellitesTaxonomyEarthRessourcesEntry,
    ArtificialSatellitesTaxonomyEducationEntry,
    ArtificialSatellitesTaxonomyEngineeringEntry,
    ArtificialSatellitesTaxonomyGeoEntry,
    ArtificialSatellitesTaxonomyGeodeticEntry,
    ArtificialSatellitesTaxonomyGnssEntry,
    ArtificialSatellitesTaxonomyIndianSpaceResearchEntry,
    ArtificialSatellitesTaxonomyMeteorologicalAndEarthObservationEntry,
    ArtificialSatellitesTaxonomyPredicate,
    ArtificialSatellitesTaxonomySearchRescueEntry,
    ArtificialSatellitesTaxonomySpaceEarthScienceEntry,
    ArtificialSatellitesTaxonomyTrackingEntry,
)
from .aviation import (
    AviationTaxonomy,
    AviationTaxonomyCertaintyEntry,
    AviationTaxonomyCriticalityEntry,
    AviationTaxonomyImpactEntry,
    AviationTaxonomyLikelihoodEntry,
    AviationTaxonomyPredicate,
    AviationTaxonomyTargetEntry,
    AviationTaxonomyTargetSubSystemsEntry,
    AviationTaxonomyTargetSystemsEntry,
)
from .binary_class import BinaryClassTaxonomy, BinaryClassTaxonomyPredicate, BinaryClassTaxonomyTypeEntry
from .cccs import (
    CccsTaxonomy,
    CccsTaxonomyDisclosureTypeEntry,
    CccsTaxonomyDomainCategoryEntry,
    CccsTaxonomyEmailTypeEntry,
    CccsTaxonomyEventEntry,
    CccsTaxonomyExploitationTechniqueEntry,
    CccsTaxonomyIpCategoryEntry,
    CccsTaxonomyMaliciousnessEntry,
    CccsTaxonomyMalwareCategoryEntry,
    CccsTaxonomyMisusageTypeEntry,
    CccsTaxonomyMitigationTypeEntry,
    CccsTaxonomyOriginEntry,
    CccsTaxonomyOriginatingOrganizationEntry,
    CccsTaxonomyPredicate,
    CccsTaxonomyScanTypeEntry,
    CccsTaxonomySeverityEntry,
    CccsTaxonomyThreatVectorEntry,
)
from .cert_xlm import (
    CertXlmTaxonomy,
    CertXlmTaxonomyAbusiveContentEntry,
    CertXlmTaxonomyAvailabilityEntry,
    CertXlmTaxonomyConformityEntry,
    CertXlmTaxonomyFraudEntry,
    CertXlmTaxonomyInformationContentSecurityEntry,
    CertXlmTaxonomyInformationGatheringEntry,
    CertXlmTaxonomyIntrusionAttemptsEntry,
    CertXlmTaxonomyIntrusionEntry,
    CertXlmTaxonomyMaliciousCodeEntry,
    CertXlmTaxonomyOtherEntry,
    CertXlmTaxonomyPredicate,
    CertXlmTaxonomyVulnerableEntry,
)
from .circl import (
    CirclTaxonomy,
    CirclTaxonomyIncidentClassificationEntry,
    CirclTaxonomyPredicate,
    CirclTaxonomyTopicEntry,
)
from .cnsd import (
    CnsdTaxonomy,
    CnsdTaxonomyContenidoAbusivoEntry,
    CnsdTaxonomyDisponibilidadEntry,
    CnsdTaxonomyFraudeEntry,
    CnsdTaxonomyFugaDeInformaciNEntry,
    CnsdTaxonomyIntentosDeIntrusiNEntry,
    CnsdTaxonomyIntrusiNEntry,
    CnsdTaxonomyMalwareEntry,
    CnsdTaxonomyOtrosEntry,
    CnsdTaxonomyPredicate,
    CnsdTaxonomyRecopilaciNDeInformaciNEntry,
)
from .coa import (
    CoaTaxonomy,
    CoaTaxonomyDeceiveEntry,
    CoaTaxonomyDegradeEntry,
    CoaTaxonomyDenyEntry,
    CoaTaxonomyDestroyEntry,
    CoaTaxonomyDetectEntry,
    CoaTaxonomyDiscoverEntry,
    CoaTaxonomyDisruptEntry,
    CoaTaxonomyPredicate,
)
from .collaborative_intelligence import (
    CollaborativeIntelligenceTaxonomy,
    CollaborativeIntelligenceTaxonomyPredicate,
    CollaborativeIntelligenceTaxonomyRequestEntry,
)
from .common_taxonomy import (
    CommonTaxonomyTaxonomy,
    CommonTaxonomyTaxonomyAbusiveContentEntry,
    CommonTaxonomyTaxonomyAvailabilityEntry,
    CommonTaxonomyTaxonomyFraudEntry,
    CommonTaxonomyTaxonomyInformationGatheringEntry,
    CommonTaxonomyTaxonomyInformationSecurityEntry,
    CommonTaxonomyTaxonomyIntrusionAttemptEntry,
    CommonTaxonomyTaxonomyIntrusionEntry,
    CommonTaxonomyTaxonomyMalwareEntry,
    CommonTaxonomyTaxonomyOtherEntry,
    CommonTaxonomyTaxonomyPredicate,
)
from .copine_scale import CopineScaleTaxonomy, CopineScaleTaxonomyPredicate
from .course_of_action import (
    CourseOfActionTaxonomy,
    CourseOfActionTaxonomyActiveEntry,
    CourseOfActionTaxonomyPassiveEntry,
    CourseOfActionTaxonomyPredicate,
)
from .crowdsec import (
    CrowdsecTaxonomy,
    CrowdsecTaxonomyBehaviorEntry,
    CrowdsecTaxonomyClassificationEntry,
    CrowdsecTaxonomyFalsePositiveEntry,
    CrowdsecTaxonomyPredicate,
)
from .cryptocurrency_threat import CryptocurrencyThreatTaxonomy, CryptocurrencyThreatTaxonomyPredicate
from .csirt_americas import CsirtAmericasTaxonomy, CsirtAmericasTaxonomyPredicate
from .csirt_case_classification import (
    CsirtCaseClassificationTaxonomy,
    CsirtCaseClassificationTaxonomyCriticalityClassificationEntry,
    CsirtCaseClassificationTaxonomyIncidentCategoryEntry,
    CsirtCaseClassificationTaxonomyPredicate,
    CsirtCaseClassificationTaxonomySensitivityClassificationEntry,
)
from .cssa import (
    CssaTaxonomy,
    CssaTaxonomyOriginEntry,
    CssaTaxonomyPredicate,
    CssaTaxonomyReportEntry,
    CssaTaxonomySharingClassEntry,
)
from .cti import CtiTaxonomy, CtiTaxonomyPredicate
from .current_event import (
    CurrentEventTaxonomy,
    CurrentEventTaxonomyElectionEntry,
    CurrentEventTaxonomyPandemicEntry,
    CurrentEventTaxonomyPredicate,
)
from .cyber_threat_framework import (
    CyberThreatFrameworkTaxonomy,
    CyberThreatFrameworkTaxonomyEffectConsequenceEntry,
    CyberThreatFrameworkTaxonomyEngagementEntry,
    CyberThreatFrameworkTaxonomyPredicate,
    CyberThreatFrameworkTaxonomyPreparationEntry,
    CyberThreatFrameworkTaxonomyPresenceEntry,
)
from .cycat import CycatTaxonomy, CycatTaxonomyPredicate, CycatTaxonomyScopeEntry, CycatTaxonomyTypeEntry
from .cytomic_orion import CytomicOrionTaxonomy, CytomicOrionTaxonomyActionEntry, CytomicOrionTaxonomyPredicate
from .dark_web import (
    DarkWebTaxonomy,
    DarkWebTaxonomyContentEntry,
    DarkWebTaxonomyMotivationEntry,
    DarkWebTaxonomyPredicate,
    DarkWebTaxonomyServiceEntry,
    DarkWebTaxonomyStructureEntry,
    DarkWebTaxonomyTopicEntry,
)
from .data_classification import DataClassificationTaxonomy, DataClassificationTaxonomyPredicate
from .dcso_sharing import DcsoSharingTaxonomy, DcsoSharingTaxonomyEventTypeEntry, DcsoSharingTaxonomyPredicate
from .ddos import DdosTaxonomy, DdosTaxonomyPredicate, DdosTaxonomyTypeEntry
from .de_vs import DeVsTaxonomy, DeVsTaxonomyEinstufungEntry, DeVsTaxonomyPredicate, DeVsTaxonomySchutzwortEntry
from .death_possibilities import (
    DeathPossibilitiesTaxonomy,
    DeathPossibilitiesTaxonomyPredicate,
    DeathPossibilitiesTaxonomyT001009IntestinalInfectiousDiseasesEntry,
    DeathPossibilitiesTaxonomyT010018TuberculosisEntry,
    DeathPossibilitiesTaxonomyT020027ZoonoticBacterialDiseasesEntry,
    DeathPossibilitiesTaxonomyT030041OtherBacterialDiseasesEntry,
    DeathPossibilitiesTaxonomyT042042HumanImmunodeficiencyVirusHivInfectionEntry,
    DeathPossibilitiesTaxonomyT045049PoliomyelitisAndOtherNonArthropodBorneViralDiseasesOfCentralNervousSystemEntry,
    DeathPossibilitiesTaxonomyT050057ViralDiseasesAccompaniedByExanthemEntry,
    DeathPossibilitiesTaxonomyT060066ArthropodBorneViralDiseasesEntry,
    DeathPossibilitiesTaxonomyT070079OtherDiseasesDueToVirusesAndChlamydiaeEntry,
    DeathPossibilitiesTaxonomyT080088RickettsiosesAndOtherArthropodBorneDiseasesEntry,
    DeathPossibilitiesTaxonomyT090099SyphilisAndOtherVenerealDiseasesEntry,
    DeathPossibilitiesTaxonomyT100104OtherSpirochaetalDiseasesEntry,
    DeathPossibilitiesTaxonomyT110118MycosesEntry,
    DeathPossibilitiesTaxonomyT120129HelminthiasesEntry,
    DeathPossibilitiesTaxonomyT130136OtherInfectiousAndParasiticDiseasesEntry,
    DeathPossibilitiesTaxonomyT137139LateEffectsOfInfectiousAndParasiticDiseasesEntry,
    DeathPossibilitiesTaxonomyT140149MalignantNeoplasmOfLipOralCavityAndPharynxEntry,
    DeathPossibilitiesTaxonomyT150159MalignantNeoplasmOfDigestiveOrgansAndPeritoneumEntry,
    DeathPossibilitiesTaxonomyT160165MalignantNeoplasmOfRespiratoryAndIntrathoracicOrgansEntry,
    DeathPossibilitiesTaxonomyT170176MalignantNeoplasmOfBoneConnectiveTissueSkinAndBreastEntry,
    DeathPossibilitiesTaxonomyT179189MalignantNeoplasmOfGenitoUrinaryOrgansEntry,
    DeathPossibilitiesTaxonomyT190199MalignantNeoplasmOfOtherAndUnspecifiedSitesEntry,
    DeathPossibilitiesTaxonomyT200208MalignantNeoplasmOfLymphaticAndHaematopoieticTissueEntry,
    DeathPossibilitiesTaxonomyT210229BenignNeoplasmsEntry,
    DeathPossibilitiesTaxonomyT230234CarcinomaInSituEntry,
    DeathPossibilitiesTaxonomyT235238NeoplasmsOfUncertainBehaviourEntry,
    DeathPossibilitiesTaxonomyT239239NeoplasmsOfUnspecifiedNatureEntry,
    DeathPossibilitiesTaxonomyT240246DisordersOfThyroidGlandEntry,
    DeathPossibilitiesTaxonomyT250259DiseasesOfOtherEndocrineGlandsEntry,
    DeathPossibilitiesTaxonomyT260269NutritionalDeficienciesEntry,
    DeathPossibilitiesTaxonomyT270279OtherMetabolicDisordersAndImmunityDisordersEntry,
    DeathPossibilitiesTaxonomyT280289DiseasesOfBloodAndBloodFormingOrgansEntry,
    DeathPossibilitiesTaxonomyT290294OrganicPsychoticConditionsEntry,
    DeathPossibilitiesTaxonomyT295299OtherPsychosesEntry,
    DeathPossibilitiesTaxonomyT300316NeuroticDisordersPersonalityDisordersAndOtherNonpsychoticMentalDisordersEntry,
    DeathPossibilitiesTaxonomyT317319MentalRetardationEntry,
    DeathPossibilitiesTaxonomyT320326InflammatoryDiseasesOfTheCentralNervousSystemEntry,
    DeathPossibilitiesTaxonomyT330337HereditaryAndDegenerativeDiseasesOfTheCentralNervousSystemEntry,
    DeathPossibilitiesTaxonomyT340349OtherDisordersOfTheCentralNervousSystemEntry,
    DeathPossibilitiesTaxonomyT350359DisordersOfThePeripheralNervousSystemEntry,
    DeathPossibilitiesTaxonomyT360379DisordersOfTheEyeAndAdnexaEntry,
    DeathPossibilitiesTaxonomyT380389DiseasesOfTheEarAndMastoidProcessEntry,
    DeathPossibilitiesTaxonomyT390392AcuteRheumaticFeverEntry,
    DeathPossibilitiesTaxonomyT393398ChronicRheumaticHeartDiseaseEntry,
    DeathPossibilitiesTaxonomyT401405HypertensiveDiseaseEntry,
    DeathPossibilitiesTaxonomyT410414IschaemicHeartDiseaseEntry,
    DeathPossibilitiesTaxonomyT415417DiseasesOfPulmonaryCirculationEntry,
    DeathPossibilitiesTaxonomyT420429OtherFormsOfHeartDiseaseEntry,
    DeathPossibilitiesTaxonomyT430438CerebrovascularDiseaseEntry,
    DeathPossibilitiesTaxonomyT440448DiseasesOfArteriesArteriolesAndCapillariesEntry,
    DeathPossibilitiesTaxonomyT451459DiseasesOfVeinsAndLymphaticsAndOtherDiseasesOfCirculatorySystemEntry,
    DeathPossibilitiesTaxonomyT460466AcuteRespiratoryInfectionsEntry,
    DeathPossibilitiesTaxonomyT470478OtherDiseasesOfUpperRespiratoryTractEntry,
    DeathPossibilitiesTaxonomyT480487PneumoniaAndInfluenzaEntry,
    DeathPossibilitiesTaxonomyT490496ChronicObstructivePulmonaryDiseaseAndAlliedConditionsEntry,
    DeathPossibilitiesTaxonomyT500508PneumoconiosesAndOtherLungDiseasesDueToExternalAgentsEntry,
    DeathPossibilitiesTaxonomyT510519OtherDiseasesOfRespiratorySystemEntry,
    DeathPossibilitiesTaxonomyT520529DiseasesOfOralCavitySalivaryGlandsAndJawsEntry,
    DeathPossibilitiesTaxonomyT530537DiseasesOfOesophagusStomachAndDuodenumEntry,
    DeathPossibilitiesTaxonomyT540543AppendicitisEntry,
    DeathPossibilitiesTaxonomyT550553HerniaOfAbdominalCavityEntry,
    DeathPossibilitiesTaxonomyT555558NonInfectiveEnteritisAndColitisEntry,
    DeathPossibilitiesTaxonomyT560569OtherDiseasesOfIntestinesAndPeritoneumEntry,
    DeathPossibilitiesTaxonomyT570579OtherDiseasesOfDigestiveSystemEntry,
    DeathPossibilitiesTaxonomyT580589NephritisNephroticSyndromeAndNephrosisEntry,
    DeathPossibilitiesTaxonomyT590599OtherDiseasesOfUrinarySystemEntry,
    DeathPossibilitiesTaxonomyT600608DiseasesOfMaleGenitalOrgansEntry,
    DeathPossibilitiesTaxonomyT610611DisordersOfBreastEntry,
    DeathPossibilitiesTaxonomyT614616InflammatoryDiseaseOfFemalePelvicOrgansEntry,
    DeathPossibilitiesTaxonomyT617629OtherDisordersOfFemaleGenitalTractEntry,
    DeathPossibilitiesTaxonomyT630633EctopicAndMolarPregnancyEntry,
    DeathPossibilitiesTaxonomyT634639OtherPregnancyWithAbortiveOutcomeEntry,
    DeathPossibilitiesTaxonomyT640648ComplicationsMainlyRelatedToPregnancyEntry,
    DeathPossibilitiesTaxonomyT650659NormalDeliveryAndOtherIndicationsForCareInPregnancyLabourAndDeliveryEntry,
    DeathPossibilitiesTaxonomyT660669ComplicationsOccurringMainlyInTheCourseOfLabourAndDeliveryEntry,
    DeathPossibilitiesTaxonomyT670677ComplicationsOfThePuerperiumEntry,
    DeathPossibilitiesTaxonomyT680686InfectionsOfSkinAndSubcutaneousTissueEntry,
    DeathPossibilitiesTaxonomyT690698OtherInflammatoryConditionsOfSkinAndSubcutaneousTissueEntry,
    DeathPossibilitiesTaxonomyT700709OtherDiseasesOfSkinAndSubcutaneousTissueEntry,
    DeathPossibilitiesTaxonomyT710719ArthropathiesAndRelatedDisordersEntry,
    DeathPossibilitiesTaxonomyT720724DorsopathiesEntry,
    DeathPossibilitiesTaxonomyT725729RheumatismExcludingTheBackEntry,
    DeathPossibilitiesTaxonomyT730739OsteopathiesChondropathiesAndAcquiredMusculoskeletalDeformitiesEntry,
    DeathPossibilitiesTaxonomyT740759CongenitalAnomaliesEntry,
    DeathPossibilitiesTaxonomyT760763MaternalCausesOfPerinatalMorbidityAndMortalityEntry,
    DeathPossibilitiesTaxonomyT764779OtherConditionsOriginatingInThePerinatalPeriodEntry,
    DeathPossibilitiesTaxonomyT780789SymptomsEntry,
    DeathPossibilitiesTaxonomyT790796NonspecificAbnormalFindingsEntry,
    DeathPossibilitiesTaxonomyT797799IllDefinedAndUnknownCausesOfMorbidityAndMortalityEntry,
    DeathPossibilitiesTaxonomyT800804FractureOfSkullEntry,
    DeathPossibilitiesTaxonomyT805809FractureOfNeckAndTrunkEntry,
    DeathPossibilitiesTaxonomyT810819FractureOfUpperLimbEntry,
    DeathPossibilitiesTaxonomyT820829FractureOfLowerLimbEntry,
    DeathPossibilitiesTaxonomyT830839DislocationEntry,
    DeathPossibilitiesTaxonomyT840848SprainsAndStrainsOfJointsAndAdjacentMusclesEntry,
    DeathPossibilitiesTaxonomyT850854IntracranialInjuryExcludingThoseWithSkullFractureEntry,
    DeathPossibilitiesTaxonomyT860869InternalInjuryOfChestAbdomenAndPelvisEntry,
    DeathPossibilitiesTaxonomyT870879OpenWoundOfHeadNeckAndTrunkEntry,
    DeathPossibilitiesTaxonomyT880887OpenWoundOfUpperLimbEntry,
    DeathPossibilitiesTaxonomyT890897OpenWoundOfLowerLimbEntry,
    DeathPossibilitiesTaxonomyT900904InjuryToBloodVesselsEntry,
    DeathPossibilitiesTaxonomyT905909LateEffectsOfInjuriesPoisoningsToxicEffectsAndOtherExternalCausesEntry,
    DeathPossibilitiesTaxonomyT910919SuperficialInjuryEntry,
    DeathPossibilitiesTaxonomyT920924ContusionWithIntactSkinSurfaceEntry,
    DeathPossibilitiesTaxonomyT925929CrushingInjuryEntry,
    DeathPossibilitiesTaxonomyT930939EffectsOfForeignBodyEnteringThroughOrificeEntry,
    DeathPossibilitiesTaxonomyT940949BurnsEntry,
    DeathPossibilitiesTaxonomyT950957InjuryToNervesAndSpinalCordEntry,
    DeathPossibilitiesTaxonomyT958959CertainTraumaticComplicationsAndUnspecifiedInjuriesEntry,
    DeathPossibilitiesTaxonomyT960979PoisoningByDrugsMedicamentsAndBiologicalSubstancesEntry,
    DeathPossibilitiesTaxonomyT980989ToxicEffectsOfSubstancesChieflyNonmedicinalAsToSourceEntry,
    DeathPossibilitiesTaxonomyT990995OtherAndUnspecifiedEffectsOfExternalCausesEntry,
    DeathPossibilitiesTaxonomyT996999ComplicationsOfSurgicalAndMedicalCareNotElsewhereClassifiedEntry,
    DeathPossibilitiesTaxonomyTE800E807RailwayAccidentsEntry,
    DeathPossibilitiesTaxonomyTE810E819MotorVehicleTrafficAccidentsEntry,
    DeathPossibilitiesTaxonomyTE820E825MotorVehicleNontrafficAccidentsEntry,
    DeathPossibilitiesTaxonomyTE826E829OtherRoadVehicleAccidentsEntry,
    DeathPossibilitiesTaxonomyTE830E838WaterTransportAccidentsEntry,
    DeathPossibilitiesTaxonomyTE840E845AirAndSpaceTransportAccidentsEntry,
    DeathPossibilitiesTaxonomyTE846E848VehicleAccidentsNotElsewhereClassifiableEntry,
    DeathPossibilitiesTaxonomyTE849E858AccidentalPoisoningByDrugsMedicamentsAndBiologicalsEntry,
    DeathPossibilitiesTaxonomyTE860E869AccidentalPoisoningByOtherSolidAndLiquidSubstancesGasesAndVapoursEntry,
    DeathPossibilitiesTaxonomyTE870E876MisadventuresToPatientsDuringSurgicalAndMedicalCareEntry,
    DeathPossibilitiesTaxonomyTE878E879SurgicalAndMedicalProceduresAsTheCauseOfAbnormalReactionOfPatientOrLaterComplicationWithoutMentionOfMisadventureAtTheTimeOfProcedureEntry,
    DeathPossibilitiesTaxonomyTE880E888AccidentalFallsEntry,
    DeathPossibilitiesTaxonomyTE890E899AccidentsCausedByFireAndFlamesEntry,
    DeathPossibilitiesTaxonomyTE900E909AccidentsDueToNaturalAndEnvironmentalFactorsEntry,
    DeathPossibilitiesTaxonomyTE910E915AccidentsCausedBySubmersionSuffocationAndForeignBodiesEntry,
    DeathPossibilitiesTaxonomyTE916E928OtherAccidentsEntry,
    DeathPossibilitiesTaxonomyTE929E929LateEffectsOfAccidentalInjuryEntry,
    DeathPossibilitiesTaxonomyTE930E949DrugsMedicamentsAndBiologicalSubstancesCausingAdverseEffectsInTherapeuticUseEntry,
    DeathPossibilitiesTaxonomyTE950E959SuicideAndSelfInflictedInjuryEntry,
    DeathPossibilitiesTaxonomyTE960E969HomicideAndInjuryPurposelyInflictedByOtherPersonsEntry,
)
from .deception import (
    DeceptionTaxonomy,
    DeceptionTaxonomyCausalityEntry,
    DeceptionTaxonomyEssenceEntry,
    DeceptionTaxonomyParticipantEntry,
    DeceptionTaxonomyPredicate,
    DeceptionTaxonomyQualityEntry,
    DeceptionTaxonomySpaceEntry,
    DeceptionTaxonomySpeechActTheoryEntry,
    DeceptionTaxonomyTimeEntry,
)
from .detection_engineering import (
    DetectionEngineeringTaxonomy,
    DetectionEngineeringTaxonomyPatternMatchingEntry,
    DetectionEngineeringTaxonomyPredicate,
)
from .dfrlab_dichotomies_of_disinformation import (
    DfrlabDichotomiesOfDisinformationTaxonomy,
    DfrlabDichotomiesOfDisinformationTaxonomyContentLanguageEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyContentTopicEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyDisinformantCategoryEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyDisinformantConcurrentEventsEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyDisinformantIntentEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyMethodsNarrativeTechniquesEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyMethodsTacticsEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyPlatformsEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyPlatformsMessagingEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyPlatformsOpenWebEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyPlatformsSocialMediaEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyPredicate,
    DfrlabDichotomiesOfDisinformationTaxonomyPrimaryDisinformantEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyPrimaryTargetEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyTargetCategoryEntry,
    DfrlabDichotomiesOfDisinformationTaxonomyTargetConcurrentEventsEntry,
)
from .dga import DgaTaxonomy, DgaTaxonomyGenerationSchemeEntry, DgaTaxonomyPredicate, DgaTaxonomySeedingEntry
from .dhs_ciip_sectors import (
    DhsCiipSectorsTaxonomy,
    DhsCiipSectorsTaxonomyDhsCriticalSectorsEntry,
    DhsCiipSectorsTaxonomyPredicate,
)
from .diamond_model import DiamondModelTaxonomy, DiamondModelTaxonomyPredicate
from .diamond_model_for_influence_operations import (
    DiamondModelForInfluenceOperationsTaxonomy,
    DiamondModelForInfluenceOperationsTaxonomyPredicate,
)
from .dml import DmlTaxonomy, DmlTaxonomyPredicate
from .dni_ism import (
    DniIsmTaxonomy,
    DniIsmTaxonomyAtomicenergymarkingsEntry,
    DniIsmTaxonomyClassificationAllEntry,
    DniIsmTaxonomyClassificationUsEntry,
    DniIsmTaxonomyCompliesWithEntry,
    DniIsmTaxonomyDissemEntry,
    DniIsmTaxonomyNonicEntry,
    DniIsmTaxonomyNonuscontrolsEntry,
    DniIsmTaxonomyNoticeEntry,
    DniIsmTaxonomyPredicate,
    DniIsmTaxonomyScicontrolsEntry,
)
from .domain_abuse import (
    DomainAbuseTaxonomy,
    DomainAbuseTaxonomyDomainAccessMethodEntry,
    DomainAbuseTaxonomyDomainStatusEntry,
    DomainAbuseTaxonomyPredicate,
)
from .doping_substances import (
    DopingSubstancesTaxonomy,
    DopingSubstancesTaxonomyAnabolicAgentsEntry,
    DopingSubstancesTaxonomyBeta2AgonistsEntry,
    DopingSubstancesTaxonomyBetaBlockersEntry,
    DopingSubstancesTaxonomyCannabinoidsEntry,
    DopingSubstancesTaxonomyDiureticsAndMaskingAgentsEntry,
    DopingSubstancesTaxonomyGlucocorticoidsEntry,
    DopingSubstancesTaxonomyHormoneAndMetabolicModulatorsEntry,
    DopingSubstancesTaxonomyNarcoticsEntry,
    DopingSubstancesTaxonomyPeptideHormonesGrowthFactorsRelatedSubstancesAndMimeticsEntry,
    DopingSubstancesTaxonomyPredicate,
    DopingSubstancesTaxonomyStimulantsEntry,
)
from .drugs import (
    DrugsTaxonomy,
    DrugsTaxonomyAlkaloidsAndDerivativesEntry,
    DrugsTaxonomyBenzenoidsEntry,
    DrugsTaxonomyHomogeneousMetalCompoundsEntry,
    DrugsTaxonomyHomogeneousNonMetalCompoundsEntry,
    DrugsTaxonomyHydrocarbonDerivativesEntry,
    DrugsTaxonomyHydrocarbonsEntry,
    DrugsTaxonomyLignansNeolignansAndRelatedCompoundsEntry,
    DrugsTaxonomyLipidsAndLipidLikeMoleculesEntry,
    DrugsTaxonomyMixedMetalNonMetalCompoundsEntry,
    DrugsTaxonomyNucleosidesNucleotidesAndAnaloguesEntry,
    DrugsTaxonomyOrganic13DipolarCompoundsEntry,
    DrugsTaxonomyOrganicAcidsAndDerivativesEntry,
    DrugsTaxonomyOrganicAcidsEntry,
    DrugsTaxonomyOrganicNitrogenCompoundsEntry,
    DrugsTaxonomyOrganicOxygenCompoundsEntry,
    DrugsTaxonomyOrganicPolymersEntry,
    DrugsTaxonomyOrganicSaltsEntry,
    DrugsTaxonomyOrganohalogenCompoundsEntry,
    DrugsTaxonomyOrganoheterocyclicCompoundsEntry,
    DrugsTaxonomyOrganometallicCompoundsEntry,
    DrugsTaxonomyOrganophosphorusCompoundsEntry,
    DrugsTaxonomyOrganosulfurCompoundsEntry,
    DrugsTaxonomyPhenylpropanoidsAndPolyketidesEntry,
    DrugsTaxonomyPredicate,
)
from .economical_impact import (
    EconomicalImpactTaxonomy,
    EconomicalImpactTaxonomyGainEntry,
    EconomicalImpactTaxonomyLossEntry,
    EconomicalImpactTaxonomyPredicate,
)
from .ecsirt import (
    EcsirtTaxonomy,
    EcsirtTaxonomyAbusiveContentEntry,
    EcsirtTaxonomyAvailabilityEntry,
    EcsirtTaxonomyFraudEntry,
    EcsirtTaxonomyInformationContentSecurityEntry,
    EcsirtTaxonomyInformationGatheringEntry,
    EcsirtTaxonomyIntrusionAttemptsEntry,
    EcsirtTaxonomyIntrusionsEntry,
    EcsirtTaxonomyMaliciousCodeEntry,
    EcsirtTaxonomyOtherEntry,
    EcsirtTaxonomyPredicate,
    EcsirtTaxonomyTestEntry,
    EcsirtTaxonomyVulnerableEntry,
)
from .enisa import (
    EnisaTaxonomy,
    EnisaTaxonomyDisasterEntry,
    EnisaTaxonomyEavesdroppingInterceptionHijackingEntry,
    EnisaTaxonomyFailuresMalfunctionEntry,
    EnisaTaxonomyLegalEntry,
    EnisaTaxonomyNefariousActivityAbuseEntry,
    EnisaTaxonomyOutagesEntry,
    EnisaTaxonomyPhysicalAttackEntry,
    EnisaTaxonomyPredicate,
    EnisaTaxonomyUnintentionalDamageEntry,
)
from .estimative_language import (
    EstimativeLanguageTaxonomy,
    EstimativeLanguageTaxonomyConfidenceInAnalyticJudgmentEntry,
    EstimativeLanguageTaxonomyLikelihoodProbabilityEntry,
    EstimativeLanguageTaxonomyPredicate,
)
from .eu_marketop_and_publicadmin import (
    EuMarketopAndPublicadminTaxonomy,
    EuMarketopAndPublicadminTaxonomyCriticalInfraOperatorsEntry,
    EuMarketopAndPublicadminTaxonomyInfoServicesEntry,
    EuMarketopAndPublicadminTaxonomyPredicate,
    EuMarketopAndPublicadminTaxonomyPublicAdminEntry,
)
from .eu_nis_sector_and_subsectors import (
    EuNisSectorAndSubsectorsTaxonomy,
    EuNisSectorAndSubsectorsTaxonomyEuNisDspEntry,
    EuNisSectorAndSubsectorsTaxonomyEuNisOesEnergyEntry,
    EuNisSectorAndSubsectorsTaxonomyEuNisOesEntry,
    EuNisSectorAndSubsectorsTaxonomyEuNisOesTransportEntry,
    EuNisSectorAndSubsectorsTaxonomyPredicate,
)
from .euci import EuciTaxonomy, EuciTaxonomyPredicate
from .europol_event import EuropolEventTaxonomy, EuropolEventTaxonomyPredicate
from .europol_incident import (
    EuropolIncidentTaxonomy,
    EuropolIncidentTaxonomyAbusiveContentEntry,
    EuropolIncidentTaxonomyAvailabilityEntry,
    EuropolIncidentTaxonomyFraudEntry,
    EuropolIncidentTaxonomyInformationGatheringEntry,
    EuropolIncidentTaxonomyInformationSecurityEntry,
    EuropolIncidentTaxonomyIntrusionAttemptEntry,
    EuropolIncidentTaxonomyIntrusionEntry,
    EuropolIncidentTaxonomyMalwareEntry,
    EuropolIncidentTaxonomyOtherEntry,
    EuropolIncidentTaxonomyPredicate,
)
from .event_assessment import (
    EventAssessmentTaxonomy,
    EventAssessmentTaxonomyAlternativePointsOfViewProcessEntry,
    EventAssessmentTaxonomyPredicate,
)
from .event_classification import (
    EventClassificationTaxonomy,
    EventClassificationTaxonomyEventClassEntry,
    EventClassificationTaxonomyPredicate,
)
from .exercise import (
    ExerciseTaxonomy,
    ExerciseTaxonomyCyberCoalitionEntry,
    ExerciseTaxonomyCyberEuropeEntry,
    ExerciseTaxonomyCyberSopexEntry,
    ExerciseTaxonomyCyberStormEntry,
    ExerciseTaxonomyGenericEntry,
    ExerciseTaxonomyLockedShieldsEntry,
    ExerciseTaxonomyLukexEntry,
    ExerciseTaxonomyPaceEntry,
    ExerciseTaxonomyPredicate,
)
from .extended_event import (
    ExtendedEventTaxonomy,
    ExtendedEventTaxonomyChunkedEventEntry,
    ExtendedEventTaxonomyCompetitiveAnalysisEntry,
    ExtendedEventTaxonomyExtendedAnalysisEntry,
    ExtendedEventTaxonomyPredicate,
)
from .failure_mode_in_machine_learning import (
    FailureModeInMachineLearningTaxonomy,
    FailureModeInMachineLearningTaxonomyIntentionallyMotivatedFailuresSummaryEntry,
    FailureModeInMachineLearningTaxonomyPredicate,
    FailureModeInMachineLearningTaxonomyUnintendedFailuresSummaryEntry,
)
from .false_positive import (
    FalsePositiveTaxonomy,
    FalsePositiveTaxonomyConfirmedEntry,
    FalsePositiveTaxonomyPredicate,
    FalsePositiveTaxonomyRiskEntry,
)
from .file_type import FileTypeTaxonomy, FileTypeTaxonomyPredicate, FileTypeTaxonomyTypeEntry
from .financial import (
    FinancialTaxonomy,
    FinancialTaxonomyCategoriesAndTypesOfServicesEntry,
    FinancialTaxonomyGeographicalFootprintEntry,
    FinancialTaxonomyOnlineExpositionEntry,
    FinancialTaxonomyPhysicalPresenceEntry,
    FinancialTaxonomyPredicate,
    FinancialTaxonomyServicesEntry,
)
from .flesch_reading_ease import (
    FleschReadingEaseTaxonomy,
    FleschReadingEaseTaxonomyPredicate,
    FleschReadingEaseTaxonomyScoreEntry,
)
from .fpf import (
    FpfTaxonomy,
    FpfTaxonomyAnonymousDataEntry,
    FpfTaxonomyDeIdentifiedDataEntry,
    FpfTaxonomyDegreesOfIdentifiabilityEntry,
    FpfTaxonomyPredicate,
    FpfTaxonomyPseudonymousDataEntry,
)
from .fr_classif import (
    FrClassifTaxonomy,
    FrClassifTaxonomyClassifieesEntry,
    FrClassifTaxonomyNonClassifieesEntry,
    FrClassifTaxonomyPredicate,
    FrClassifTaxonomySpecialFranceEntry,
)
from .gdpr import GdprTaxonomy, GdprTaxonomyPredicate, GdprTaxonomySpecialCategoriesEntry
from .gea_nz_activities import (
    GeaNzActivitiesTaxonomy,
    GeaNzActivitiesTaxonomyCasesClaimEntry,
    GeaNzActivitiesTaxonomyCasesComplianceEntry,
    GeaNzActivitiesTaxonomyCasesEpisodeEntry,
    GeaNzActivitiesTaxonomyCasesProceedingEntry,
    GeaNzActivitiesTaxonomyCasesRequestEntry,
    GeaNzActivitiesTaxonomyEventsBusinessEntry,
    GeaNzActivitiesTaxonomyEventsCrisisEntry,
    GeaNzActivitiesTaxonomyEventsEnvironmentalEntry,
    GeaNzActivitiesTaxonomyEventsInteractionEntry,
    GeaNzActivitiesTaxonomyEventsPersonalEntry,
    GeaNzActivitiesTaxonomyEventsSocialEntry,
    GeaNzActivitiesTaxonomyEventsTradeEntry,
    GeaNzActivitiesTaxonomyEventsTravelEntry,
    GeaNzActivitiesTaxonomyEventsUncontrolledEntry,
    GeaNzActivitiesTaxonomyPredicate,
    GeaNzActivitiesTaxonomyServicesCivicInfrastructureEntry,
    GeaNzActivitiesTaxonomyServicesFranceSocietyEntry,
    GeaNzActivitiesTaxonomyServicesGovernmentAdministrationEntry,
    GeaNzActivitiesTaxonomyServicesInvidualsCommunitiesEntry,
    GeaNzActivitiesTaxonomyServicesServicesFromBusinessEntry,
    GeaNzActivitiesTaxonomyServicesServicesToBusinessEntry,
)
from .gea_nz_entities import (
    GeaNzEntitiesTaxonomy,
    GeaNzEntitiesTaxonomyItemsApplicationIctServicesEntry,
    GeaNzEntitiesTaxonomyItemsFinancialEntry,
    GeaNzEntitiesTaxonomyItemsGoodsEntry,
    GeaNzEntitiesTaxonomyItemsIctInfrastructureEntry,
    GeaNzEntitiesTaxonomyItemsItemUsageEntry,
    GeaNzEntitiesTaxonomyItemsNaturalEntry,
    GeaNzEntitiesTaxonomyItemsRegulatoryEntry,
    GeaNzEntitiesTaxonomyItemsUrbanInfrastructureEntry,
    GeaNzEntitiesTaxonomyPartiesPartyEntry,
    GeaNzEntitiesTaxonomyPartiesPartyRelationshipEntry,
    GeaNzEntitiesTaxonomyPartiesQualificationEntry,
    GeaNzEntitiesTaxonomyPartiesRoleEntry,
    GeaNzEntitiesTaxonomyPlacesAddressEntry,
    GeaNzEntitiesTaxonomyPlacesAddressTypeEntry,
    GeaNzEntitiesTaxonomyPlacesLocationTypeEntry,
    GeaNzEntitiesTaxonomyPlacesPurposeOfLocationEntry,
    GeaNzEntitiesTaxonomyPredicate,
)
from .gea_nz_motivators import (
    GeaNzMotivatorsTaxonomy,
    GeaNzMotivatorsTaxonomyContractsArrangementEntry,
    GeaNzMotivatorsTaxonomyContractsJurisdictionEntry,
    GeaNzMotivatorsTaxonomyContractsObligationEntry,
    GeaNzMotivatorsTaxonomyContractsRightsEntry,
    GeaNzMotivatorsTaxonomyControlsFinanceEntry,
    GeaNzMotivatorsTaxonomyControlsIndustryEntry,
    GeaNzMotivatorsTaxonomyControlsLawEntry,
    GeaNzMotivatorsTaxonomyControlsOperationalEntry,
    GeaNzMotivatorsTaxonomyControlsPersonalEntry,
    GeaNzMotivatorsTaxonomyControlsRiskGovernanceEntry,
    GeaNzMotivatorsTaxonomyControlsTechnologicalEntry,
    GeaNzMotivatorsTaxonomyPlansBudgetEntry,
    GeaNzMotivatorsTaxonomyPlansEffortEntry,
    GeaNzMotivatorsTaxonomyPlansMeasureEntry,
    GeaNzMotivatorsTaxonomyPlansRiskEntry,
    GeaNzMotivatorsTaxonomyPlansSpecificationEntry,
    GeaNzMotivatorsTaxonomyPlansStrategyEntry,
    GeaNzMotivatorsTaxonomyPredicate,
)
from .gray_zone import (
    GrayZoneTaxonomy,
    GrayZoneTaxonomyAdversaryEmulationEntry,
    GrayZoneTaxonomyAdversaryTakedownsEntry,
    GrayZoneTaxonomyBeaconsEntry,
    GrayZoneTaxonomyDeceptionEntry,
    GrayZoneTaxonomyDeterrenceEntry,
    GrayZoneTaxonomyIntelligenceAndCounterintelligenceEntry,
    GrayZoneTaxonomyPredicate,
    GrayZoneTaxonomyRansomwareEntry,
    GrayZoneTaxonomyRescueMissionsEntry,
    GrayZoneTaxonomySanctionsIndictmentsTradeRemediesEntry,
    GrayZoneTaxonomyTarpitsSandboxesAndHoneypotsEntry,
)
from .gsma_attack_category import GsmaAttackCategoryTaxonomy, GsmaAttackCategoryTaxonomyPredicate
from .gsma_fraud import (
    GsmaFraudTaxonomy,
    GsmaFraudTaxonomyBusinessEntry,
    GsmaFraudTaxonomyDistributionEntry,
    GsmaFraudTaxonomyPredicate,
    GsmaFraudTaxonomyPrepaidEntry,
    GsmaFraudTaxonomySubscriptionEntry,
    GsmaFraudTaxonomyTechnicalEntry,
)
from .gsma_network_technology import (
    GsmaNetworkTechnologyTaxonomy,
    GsmaNetworkTechnologyTaxonomyEndDevicesAndComponentsEntry,
    GsmaNetworkTechnologyTaxonomyPredicate,
)
from .honeypot_basic import (
    HoneypotBasicTaxonomy,
    HoneypotBasicTaxonomyCommunicationInterfaceEntry,
    HoneypotBasicTaxonomyContainmentEntry,
    HoneypotBasicTaxonomyDataCaptureEntry,
    HoneypotBasicTaxonomyDistributionAppearanceEntry,
    HoneypotBasicTaxonomyInteractionLevelEntry,
    HoneypotBasicTaxonomyPredicate,
    HoneypotBasicTaxonomyRoleEntry,
)
from .ics import (
    IcsTaxonomy,
    IcsTaxonomyOtCommunicationInterfaceEntry,
    IcsTaxonomyOtComponentsCategoryEntry,
    IcsTaxonomyOtNetworkDataTransmissionProtocolsAutomaticAutomobileVehicleAviationEntry,
    IcsTaxonomyOtNetworkDataTransmissionProtocolsAutomaticMeterReadingEntry,
    IcsTaxonomyOtNetworkDataTransmissionProtocolsBuildingAutomationEntry,
    IcsTaxonomyOtNetworkDataTransmissionProtocolsIndustrialControlSystemEntry,
    IcsTaxonomyOtNetworkDataTransmissionProtocolsPowerSystemAutomationEntry,
    IcsTaxonomyOtNetworkDataTransmissionProtocolsProcessAutomationEntry,
    IcsTaxonomyOtOperatingSystemsEntry,
    IcsTaxonomyOtSecurityIssuesEntry,
    IcsTaxonomyPredicate,
)
from .iep import (
    IepTaxonomy,
    IepTaxonomyAffectedPartyNotificationsEntry,
    IepTaxonomyCommercialUseEntry,
    IepTaxonomyEncryptAtRestEntry,
    IepTaxonomyEncryptInTransitEntry,
    IepTaxonomyEndDateEntry,
    IepTaxonomyExternalReferenceEntry,
    IepTaxonomyIdEntry,
    IepTaxonomyNameEntry,
    IepTaxonomyObfuscateAffectedPartiesEntry,
    IepTaxonomyPermittedActionsEntry,
    IepTaxonomyPredicate,
    IepTaxonomyProviderAttributionEntry,
    IepTaxonomyReferenceEntry,
    IepTaxonomyStartDateEntry,
    IepTaxonomyTrafficLightProtocolEntry,
    IepTaxonomyUnmodifiedResaleEntry,
    IepTaxonomyVersionEntry,
)
from .iep2_policy import (
    Iep2PolicyTaxonomy,
    Iep2PolicyTaxonomyAffectedPartyNotificationsEntry,
    Iep2PolicyTaxonomyAttributionEntry,
    Iep2PolicyTaxonomyDescriptionEntry,
    Iep2PolicyTaxonomyEncryptInTransitEntry,
    Iep2PolicyTaxonomyEndDateEntry,
    Iep2PolicyTaxonomyExternalReferenceEntry,
    Iep2PolicyTaxonomyIdEntry,
    Iep2PolicyTaxonomyIepVersionEntry,
    Iep2PolicyTaxonomyNameEntry,
    Iep2PolicyTaxonomyPermittedActionsEntry,
    Iep2PolicyTaxonomyPredicate,
    Iep2PolicyTaxonomyStartDateEntry,
    Iep2PolicyTaxonomyTlpEntry,
    Iep2PolicyTaxonomyUnmodifiedResaleEntry,
)
from .iep2_reference import (
    Iep2ReferenceTaxonomy,
    Iep2ReferenceTaxonomyIdRefEntry,
    Iep2ReferenceTaxonomyIepVersionEntry,
    Iep2ReferenceTaxonomyPredicate,
    Iep2ReferenceTaxonomyUrlEntry,
)
from .ifx_vetting import (
    IfxVettingTaxonomy,
    IfxVettingTaxonomyPredicate,
    IfxVettingTaxonomyScoreEntry,
    IfxVettingTaxonomyVettedEntry,
)
from .incident_disposition import (
    IncidentDispositionTaxonomy,
    IncidentDispositionTaxonomyDuplicateEntry,
    IncidentDispositionTaxonomyIncidentEntry,
    IncidentDispositionTaxonomyNotAnIncidentEntry,
    IncidentDispositionTaxonomyPredicate,
)
from .infoleak import (
    InfoleakTaxonomy,
    InfoleakTaxonomyAnalystDetectionEntry,
    InfoleakTaxonomyAutomaticDetectionEntry,
    InfoleakTaxonomyCertaintyEntry,
    InfoleakTaxonomyConfirmedEntry,
    InfoleakTaxonomyOutputFormatEntry,
    InfoleakTaxonomyPredicate,
    InfoleakTaxonomySourceEntry,
    InfoleakTaxonomySubmissionEntry,
)
from .information_origin import InformationOriginTaxonomy, InformationOriginTaxonomyPredicate
from .information_security_data_source import (
    InformationSecurityDataSourceTaxonomy,
    InformationSecurityDataSourceTaxonomyIntegrabilityFormatEntry,
    InformationSecurityDataSourceTaxonomyIntegrabilityInterfaceEntry,
    InformationSecurityDataSourceTaxonomyOriginalityEntry,
    InformationSecurityDataSourceTaxonomyPredicate,
    InformationSecurityDataSourceTaxonomyTimelinessSharingBehaviorEntry,
    InformationSecurityDataSourceTaxonomyTrustworthinessCreditabililyEntry,
    InformationSecurityDataSourceTaxonomyTrustworthinessFeedbackMechanismEntry,
    InformationSecurityDataSourceTaxonomyTrustworthinessTraceabilityEntry,
    InformationSecurityDataSourceTaxonomyTypeOfInformationEntry,
    InformationSecurityDataSourceTaxonomyTypeOfSourceEntry,
)
from .information_security_indicators import (
    InformationSecurityIndicatorsTaxonomy,
    InformationSecurityIndicatorsTaxonomyIdbEntry,
    InformationSecurityIndicatorsTaxonomyIexEntry,
    InformationSecurityIndicatorsTaxonomyImfEntry,
    InformationSecurityIndicatorsTaxonomyImpEntry,
    InformationSecurityIndicatorsTaxonomyIwhEntry,
    InformationSecurityIndicatorsTaxonomyPredicate,
    InformationSecurityIndicatorsTaxonomyVbhEntry,
    InformationSecurityIndicatorsTaxonomyVcfEntry,
    InformationSecurityIndicatorsTaxonomyVorEntry,
    InformationSecurityIndicatorsTaxonomyVswEntry,
    InformationSecurityIndicatorsTaxonomyVtcEntry,
)
from .interactive_cyber_training_audience import (
    InteractiveCyberTrainingAudienceTaxonomy,
    InteractiveCyberTrainingAudienceTaxonomyPredicate,
    InteractiveCyberTrainingAudienceTaxonomyProficiencyLevelEntry,
    InteractiveCyberTrainingAudienceTaxonomyPurposeEntry,
    InteractiveCyberTrainingAudienceTaxonomySectorEntry,
    InteractiveCyberTrainingAudienceTaxonomyTargetAudienceEntry,
)
from .interactive_cyber_training_technical_setup import (
    InteractiveCyberTrainingTechnicalSetupTaxonomy,
    InteractiveCyberTrainingTechnicalSetupTaxonomyDeploymentEntry,
    InteractiveCyberTrainingTechnicalSetupTaxonomyEnvironmentStructureEntry,
    InteractiveCyberTrainingTechnicalSetupTaxonomyOrchestrationEntry,
    InteractiveCyberTrainingTechnicalSetupTaxonomyPredicate,
)
from .interactive_cyber_training_training_environment import (
    InteractiveCyberTrainingTrainingEnvironmentTaxonomy,
    InteractiveCyberTrainingTrainingEnvironmentTaxonomyPredicate,
    InteractiveCyberTrainingTrainingEnvironmentTaxonomyScenarioEntry,
    InteractiveCyberTrainingTrainingEnvironmentTaxonomyTrainingTypeEntry,
)
from .interactive_cyber_training_training_setup import (
    InteractiveCyberTrainingTrainingSetupTaxonomy,
    InteractiveCyberTrainingTrainingSetupTaxonomyCustomizationLevelEntry,
    InteractiveCyberTrainingTrainingSetupTaxonomyPredicate,
    InteractiveCyberTrainingTrainingSetupTaxonomyRolesEntry,
    InteractiveCyberTrainingTrainingSetupTaxonomyScoringEntry,
    InteractiveCyberTrainingTrainingSetupTaxonomyTrainingModeEntry,
)
from .interception_method import InterceptionMethodTaxonomy, InterceptionMethodTaxonomyPredicate
from .ioc import IocTaxonomy, IocTaxonomyArtifactStateEntry, IocTaxonomyPredicate
from .iot import IotTaxonomy, IotTaxonomyDslEntry, IotTaxonomyPredicate, IotTaxonomySslEntry, IotTaxonomyTcomEntry
from .kill_chain import KillChainTaxonomy, KillChainTaxonomyPredicate
from .maec_delivery_vectors import (
    MaecDeliveryVectorsTaxonomy,
    MaecDeliveryVectorsTaxonomyMaecDeliveryVectorEntry,
    MaecDeliveryVectorsTaxonomyPredicate,
)
from .maec_malware_behavior import (
    MaecMalwareBehaviorTaxonomy,
    MaecMalwareBehaviorTaxonomyMaecMalwareBehaviorEntry,
    MaecMalwareBehaviorTaxonomyPredicate,
)
from .maec_malware_capabilities import (
    MaecMalwareCapabilitiesTaxonomy,
    MaecMalwareCapabilitiesTaxonomyMaecMalwareCapabilityEntry,
    MaecMalwareCapabilitiesTaxonomyPredicate,
)
from .maec_malware_obfuscation_methods import (
    MaecMalwareObfuscationMethodsTaxonomy,
    MaecMalwareObfuscationMethodsTaxonomyMaecObfuscationMethodsEntry,
    MaecMalwareObfuscationMethodsTaxonomyPredicate,
)
from .malware_classification import (
    MalwareClassificationTaxonomy,
    MalwareClassificationTaxonomyMalwareCategoryEntry,
    MalwareClassificationTaxonomyMemoryClassificationEntry,
    MalwareClassificationTaxonomyObfuscationTechniqueEntry,
    MalwareClassificationTaxonomyPayloadClassificationEntry,
    MalwareClassificationTaxonomyPredicate,
)
from .misinformation_website_label import (
    MisinformationWebsiteLabelTaxonomy,
    MisinformationWebsiteLabelTaxonomyExtremeBiasEntry,
    MisinformationWebsiteLabelTaxonomyHateNewsEntry,
    MisinformationWebsiteLabelTaxonomyPredicate,
    MisinformationWebsiteLabelTaxonomyRumorEntry,
    MisinformationWebsiteLabelTaxonomySatireEntry,
)
from .misp import (
    MispTaxonomy,
    MispTaxonomyApiEntry,
    MispTaxonomyAutomationLevelEntry,
    MispTaxonomyConfidenceLevelEntry,
    MispTaxonomyContributorEntry,
    MispTaxonomyEventTypeEntry,
    MispTaxonomyExpansionEntry,
    MispTaxonomyIdsEntry,
    MispTaxonomyMisp2yaraEntry,
    MispTaxonomyPredicate,
    MispTaxonomyThreatLevelEntry,
    MispTaxonomyToolEntry,
    MispTaxonomyUiEntry,
)
from .misp_workflow import (
    MispWorkflowTaxonomy,
    MispWorkflowTaxonomyActionTakenEntry,
    MispWorkflowTaxonomyAnalysisEntry,
    MispWorkflowTaxonomyMutabilityEntry,
    MispWorkflowTaxonomyPredicate,
    MispWorkflowTaxonomyRunEntry,
)
from .monarc_threat import (
    MonarcThreatTaxonomy,
    MonarcThreatTaxonomyCompromiseOfFunctionsEntry,
    MonarcThreatTaxonomyCompromiseOfInformationEntry,
    MonarcThreatTaxonomyLossOfEssentialServicesEntry,
    MonarcThreatTaxonomyPhysicalDamageEntry,
    MonarcThreatTaxonomyPredicate,
    MonarcThreatTaxonomyTechnicalFailuresEntry,
    MonarcThreatTaxonomyUnauthorisedActionsEntry,
)
from .ms_caro_malware import (
    MsCaroMalwareTaxonomy,
    MsCaroMalwareTaxonomyMalwarePlatformEntry,
    MsCaroMalwareTaxonomyMalwareTypeEntry,
    MsCaroMalwareTaxonomyPredicate,
)
from .ms_caro_malware_full import (
    MsCaroMalwareFullTaxonomy,
    MsCaroMalwareFullTaxonomyMalwareFamilyEntry,
    MsCaroMalwareFullTaxonomyMalwarePlatformEntry,
    MsCaroMalwareFullTaxonomyMalwareTypeEntry,
    MsCaroMalwareFullTaxonomyPredicate,
)
from .mwdb import MwdbTaxonomy, MwdbTaxonomyFamilyEntry, MwdbTaxonomyLocationTypeEntry, MwdbTaxonomyPredicate
from .nato import NatoTaxonomy, NatoTaxonomyClassificationEntry, NatoTaxonomyPredicate
from .nis import (
    NisTaxonomy,
    NisTaxonomyImpactOutlookEntry,
    NisTaxonomyImpactSectorsImpactedEntry,
    NisTaxonomyImpactSeverityEntry,
    NisTaxonomyNatureRootCauseEntry,
    NisTaxonomyNatureSeverityEntry,
    NisTaxonomyPredicate,
    NisTaxonomyTestEntry,
)
from .nis2 import (
    Nis2Taxonomy,
    Nis2TaxonomyImpactOutlookEntry,
    Nis2TaxonomyImpactSectorsImpactedEntry,
    Nis2TaxonomyImpactSeverityEntry,
    Nis2TaxonomyImpactSubsectorsImpactedEntry,
    Nis2TaxonomyImpactSubsectorsImportantEntitiesEntry,
    Nis2TaxonomyImportantEntitiesEntry,
    Nis2TaxonomyNatureRootCauseEntry,
    Nis2TaxonomyNatureSeverityEntry,
    Nis2TaxonomyPredicate,
    Nis2TaxonomyTestEntry,
)
from .open_threat import (
    OpenThreatTaxonomy,
    OpenThreatTaxonomyPredicate,
    OpenThreatTaxonomyThreatCategoryEntry,
    OpenThreatTaxonomyThreatNameEntry,
)
from .organizational_cyber_harm import (
    OrganizationalCyberHarmTaxonomy,
    OrganizationalCyberHarmTaxonomyEconomicEntry,
    OrganizationalCyberHarmTaxonomyPhysicalDigitalEntry,
    OrganizationalCyberHarmTaxonomyPredicate,
    OrganizationalCyberHarmTaxonomyPsychologicalEntry,
    OrganizationalCyberHarmTaxonomyReputationalEntry,
    OrganizationalCyberHarmTaxonomySocialSocietalEntry,
)
from .osint import (
    OsintTaxonomy,
    OsintTaxonomyCertaintyEntry,
    OsintTaxonomyLifetimeEntry,
    OsintTaxonomyPredicate,
    OsintTaxonomySourceTypeEntry,
)
from .pandemic import PandemicTaxonomy, PandemicTaxonomyCovid19Entry, PandemicTaxonomyPredicate
from .pap import PapTaxonomy, PapTaxonomyPredicate
from .passivetotal import (
    PassivetotalTaxonomy,
    PassivetotalTaxonomyClassEntry,
    PassivetotalTaxonomyDynamicDnsEntry,
    PassivetotalTaxonomyEverCompromisedEntry,
    PassivetotalTaxonomyPredicate,
    PassivetotalTaxonomySinkholedEntry,
)
from .pentest import (
    PentestTaxonomy,
    PentestTaxonomyApproachEntry,
    PentestTaxonomyExploitEntry,
    PentestTaxonomyNetworkEntry,
    PentestTaxonomyPostExploitationEntry,
    PentestTaxonomyPredicate,
    PentestTaxonomyScanEntry,
    PentestTaxonomySocialEngineeringEntry,
    PentestTaxonomyVulnerabilityEntry,
    PentestTaxonomyWebEntry,
)
from .pfc import PfcTaxonomy, PfcTaxonomyPredicate
from .phishing import (
    PhishingTaxonomy,
    PhishingTaxonomyActionEntry,
    PhishingTaxonomyDistributionEntry,
    PhishingTaxonomyPredicate,
    PhishingTaxonomyPrincipleOfPersuasionEntry,
    PhishingTaxonomyPsychologicalAcceptabilityEntry,
    PhishingTaxonomyReportOriginEntry,
    PhishingTaxonomyReportTypeEntry,
    PhishingTaxonomyStateEntry,
    PhishingTaxonomyTechniquesEntry,
)
from .poison_taxonomy import (
    PoisonTaxonomyTaxonomy,
    PoisonTaxonomyTaxonomyPoisonousFungusEntry,
    PoisonTaxonomyTaxonomyPredicate,
)
from .political_spectrum import (
    PoliticalSpectrumTaxonomy,
    PoliticalSpectrumTaxonomyIdeologyEntry,
    PoliticalSpectrumTaxonomyLeftRightSpectrumEntry,
    PoliticalSpectrumTaxonomyPredicate,
)
from .priority_level import PriorityLevelTaxonomy, PriorityLevelTaxonomyPredicate
from .pyoti import (
    PyotiTaxonomy,
    PyotiTaxonomyAbuseipdbEntry,
    PyotiTaxonomyCheckdmarcEntry,
    PyotiTaxonomyCirclHashlookupEntry,
    PyotiTaxonomyEmailrepioEntry,
    PyotiTaxonomyGooglesafebrowsingEntry,
    PyotiTaxonomyGreynoiseRiotEntry,
    PyotiTaxonomyIrisInvestigateEntry,
    PyotiTaxonomyPredicate,
    PyotiTaxonomyReputationBlockListEntry,
    PyotiTaxonomyVirustotalEntry,
)
from .ransomware import (
    RansomwareTaxonomy,
    RansomwareTaxonomyCommunicationEntry,
    RansomwareTaxonomyComplexityLevelEntry,
    RansomwareTaxonomyElementEntry,
    RansomwareTaxonomyInfectionEntry,
    RansomwareTaxonomyMaliciousActionEntry,
    RansomwareTaxonomyPredicate,
    RansomwareTaxonomyPurposeEntry,
    RansomwareTaxonomyTargetEntry,
    RansomwareTaxonomyTypeEntry,
)
from .ransomware_roles import RansomwareRolesTaxonomy, RansomwareRolesTaxonomyPredicate
from .retention import RetentionTaxonomy, RetentionTaxonomyPredicate
from .rsit import (
    RsitTaxonomy,
    RsitTaxonomyAbusiveContentEntry,
    RsitTaxonomyAvailabilityEntry,
    RsitTaxonomyFraudEntry,
    RsitTaxonomyInformationContentSecurityEntry,
    RsitTaxonomyInformationGatheringEntry,
    RsitTaxonomyIntrusionAttemptsEntry,
    RsitTaxonomyIntrusionsEntry,
    RsitTaxonomyMaliciousCodeEntry,
    RsitTaxonomyOtherEntry,
    RsitTaxonomyPredicate,
    RsitTaxonomyTestEntry,
    RsitTaxonomyVulnerableEntry,
)
from .rt_event_status import (
    RtEventStatusTaxonomy,
    RtEventStatusTaxonomyEventStatusEntry,
    RtEventStatusTaxonomyPredicate,
)
from .runtime_packer import (
    RuntimePackerTaxonomy,
    RuntimePackerTaxonomyDexEntry,
    RuntimePackerTaxonomyElfEntry,
    RuntimePackerTaxonomyMachoEntry,
    RuntimePackerTaxonomyPeEntry,
    RuntimePackerTaxonomyPredicate,
)
from .scrippsco2_fgc import Scrippsco2FgcTaxonomy, Scrippsco2FgcTaxonomyPredicate
from .scrippsco2_fgi import Scrippsco2FgiTaxonomy, Scrippsco2FgiTaxonomyPredicate
from .scrippsco2_sampling_stations import (
    Scrippsco2SamplingStationsTaxonomy,
    Scrippsco2SamplingStationsTaxonomyPredicate,
)
from .sentinel_threattype import SentinelThreattypeTaxonomy, SentinelThreattypeTaxonomyPredicate
from .smart_airports_threats import (
    SmartAirportsThreatsTaxonomy,
    SmartAirportsThreatsTaxonomyHumanErrorsEntry,
    SmartAirportsThreatsTaxonomyMaliciousActionsEntry,
    SmartAirportsThreatsTaxonomyNaturalAndSocialPhenomenaEntry,
    SmartAirportsThreatsTaxonomyPredicate,
    SmartAirportsThreatsTaxonomySystemFailuresEntry,
    SmartAirportsThreatsTaxonomyThirdPartyFailuresEntry,
)
from .social_engineering_attack_vectors import (
    SocialEngineeringAttackVectorsTaxonomy,
    SocialEngineeringAttackVectorsTaxonomyNonTechnicalEntry,
    SocialEngineeringAttackVectorsTaxonomyPredicate,
    SocialEngineeringAttackVectorsTaxonomyTechnicalEntry,
)
from .srbcert import (
    SrbcertTaxonomy,
    SrbcertTaxonomyIncidentCriticalityLevelEntry,
    SrbcertTaxonomyIncidentTypeEntry,
    SrbcertTaxonomyPredicate,
)
from .state_responsibility import StateResponsibilityTaxonomy, StateResponsibilityTaxonomyPredicate
from .stealth_malware import StealthMalwareTaxonomy, StealthMalwareTaxonomyPredicate, StealthMalwareTaxonomyTypeEntry
from .stix_ttp import StixTtpTaxonomy, StixTtpTaxonomyPredicate, StixTtpTaxonomyVictimTargetingEntry
from .targeted_threat_index import (
    TargetedThreatIndexTaxonomy,
    TargetedThreatIndexTaxonomyPredicate,
    TargetedThreatIndexTaxonomyTargetingSophisticationBaseValueEntry,
    TargetedThreatIndexTaxonomyTechnicalSophisticationMultiplierEntry,
)
from .thales_group import (
    ThalesGroupTaxonomy,
    ThalesGroupTaxonomyDistributionEntry,
    ThalesGroupTaxonomyIocConfidenceEntry,
    ThalesGroupTaxonomyPredicate,
)
from .threatmatch import (
    ThreatmatchTaxonomy,
    ThreatmatchTaxonomyAlertTypeEntry,
    ThreatmatchTaxonomyIncidentTypeEntry,
    ThreatmatchTaxonomyMalwareTypeEntry,
    ThreatmatchTaxonomyPredicate,
    ThreatmatchTaxonomySectorEntry,
)
from .threats_to_dns import (
    ThreatsToDnsTaxonomy,
    ThreatsToDnsTaxonomyDnsAbuseOrMisuseEntry,
    ThreatsToDnsTaxonomyDnsProtocolAttacksEntry,
    ThreatsToDnsTaxonomyDnsServerAttacksEntry,
    ThreatsToDnsTaxonomyPredicate,
)
from .tlp import TlpTaxonomy, TlpTaxonomyPredicate
from .tor import TorTaxonomy, TorTaxonomyPredicate, TorTaxonomyTorRelayTypeEntry
from .trust import (
    TrustTaxonomy,
    TrustTaxonomyFrequencyEntry,
    TrustTaxonomyPredicate,
    TrustTaxonomyTrustEntry,
    TrustTaxonomyValidEntry,
)
from .type import TypeTaxonomy, TypeTaxonomyPredicate
from .unified_kill_chain import (
    UnifiedKillChainTaxonomy,
    UnifiedKillChainTaxonomyActionOnObjectivesEntry,
    UnifiedKillChainTaxonomyInitialFootholdEntry,
    UnifiedKillChainTaxonomyNetworkPropagationEntry,
    UnifiedKillChainTaxonomyPredicate,
)
from .unified_ransomware_kill_chain import (
    UnifiedRansomwareKillChainTaxonomy,
    UnifiedRansomwareKillChainTaxonomyPredicate,
)
from .use_case_applicability import UseCaseApplicabilityTaxonomy, UseCaseApplicabilityTaxonomyPredicate
from .veris import (
    VerisTaxonomy,
    VerisTaxonomyActionEnvironmentalVarietyEntry,
    VerisTaxonomyActionErrorVarietyEntry,
    VerisTaxonomyActionErrorVectorEntry,
    VerisTaxonomyActionHackingResultEntry,
    VerisTaxonomyActionHackingVarietyEntry,
    VerisTaxonomyActionHackingVectorEntry,
    VerisTaxonomyActionMalwareResultEntry,
    VerisTaxonomyActionMalwareVarietyEntry,
    VerisTaxonomyActionMalwareVectorEntry,
    VerisTaxonomyActionMisuseResultEntry,
    VerisTaxonomyActionMisuseVarietyEntry,
    VerisTaxonomyActionMisuseVectorEntry,
    VerisTaxonomyActionPhysicalResultEntry,
    VerisTaxonomyActionPhysicalVarietyEntry,
    VerisTaxonomyActionPhysicalVectorEntry,
    VerisTaxonomyActionSocialResultEntry,
    VerisTaxonomyActionSocialTargetEntry,
    VerisTaxonomyActionSocialVarietyEntry,
    VerisTaxonomyActionSocialVectorEntry,
    VerisTaxonomyActionUnknownResultEntry,
    VerisTaxonomyActorExternalCountryEntry,
    VerisTaxonomyActorExternalMotiveEntry,
    VerisTaxonomyActorExternalVarietyEntry,
    VerisTaxonomyActorInternalJobChangeEntry,
    VerisTaxonomyActorInternalMotiveEntry,
    VerisTaxonomyActorInternalVarietyEntry,
    VerisTaxonomyActorPartnerCountryEntry,
    VerisTaxonomyActorPartnerMotiveEntry,
    VerisTaxonomyAssetAccessibilityEntry,
    VerisTaxonomyAssetAssetsVarietyEntry,
    VerisTaxonomyAssetCloudEntry,
    VerisTaxonomyAssetCountryEntry,
    VerisTaxonomyAssetGovernanceEntry,
    VerisTaxonomyAssetHostingEntry,
    VerisTaxonomyAssetManagementEntry,
    VerisTaxonomyAssetOwnershipEntry,
    VerisTaxonomyAttributeAvailabilityDurationUnitEntry,
    VerisTaxonomyAttributeAvailabilityVarietyEntry,
    VerisTaxonomyAttributeConfidentialityDataDisclosureEntry,
    VerisTaxonomyAttributeConfidentialityDataVarietyEntry,
    VerisTaxonomyAttributeConfidentialityDataVictimEntry,
    VerisTaxonomyAttributeConfidentialityStateEntry,
    VerisTaxonomyAttributeIntegrityVarietyEntry,
    VerisTaxonomyConfidenceEntry,
    VerisTaxonomyCostCorrectiveActionEntry,
    VerisTaxonomyDiscoveryMethodEntry,
    VerisTaxonomyImpactIsoCurrencyCodeEntry,
    VerisTaxonomyImpactLossRatingEntry,
    VerisTaxonomyImpactLossVarietyEntry,
    VerisTaxonomyImpactOverallRatingEntry,
    VerisTaxonomyPredicate,
    VerisTaxonomySecurityIncidentEntry,
    VerisTaxonomyTargetedEntry,
    VerisTaxonomyTimelineCompromiseUnitEntry,
    VerisTaxonomyTimelineContainmentUnitEntry,
    VerisTaxonomyTimelineDiscoveryUnitEntry,
    VerisTaxonomyTimelineExfiltrationUnitEntry,
    VerisTaxonomyVictimCountryEntry,
    VerisTaxonomyVictimEmployeeCountEntry,
    VerisTaxonomyVictimRevenueIsoCurrencyCodeEntry,
)
from .vmray import (
    VmrayTaxonomy,
    VmrayTaxonomyArtifactEntry,
    VmrayTaxonomyPredicate,
    VmrayTaxonomyVerdictEntry,
    VmrayTaxonomyVtiAnalysisScoreEntry,
)
from .vocabulaire_des_probabilites_estimatives import (
    VocabulaireDesProbabilitesEstimativesTaxonomy,
    VocabulaireDesProbabilitesEstimativesTaxonomyDegrDeProbabilitEntry,
    VocabulaireDesProbabilitesEstimativesTaxonomyPredicate,
)
from .vulnerability import (
    VulnerabilityTaxonomy,
    VulnerabilityTaxonomyExploitabilityEntry,
    VulnerabilityTaxonomyInformationEntry,
    VulnerabilityTaxonomyPredicate,
    VulnerabilityTaxonomySightingEntry,
)
from .workflow import WorkflowTaxonomy, WorkflowTaxonomyPredicate, WorkflowTaxonomyStateEntry, WorkflowTaxonomyTodoEntry
# This will be populated by the taxonomy generator
