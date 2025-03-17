"""Taxonomy model for gea-nz-activities."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GeaNzActivitiesTaxonomyPredicate(str, Enum):
    CASES_COMPLIANCE = "cases-compliance"
    CASES_PROCEEDING = "cases-proceeding"
    CASES_EPISODE = "cases-episode"
    CASES_COMMISSION_OF_INQUIRY = "cases-commission-of-inquiry"
    CASES_CLAIM = "cases-claim"
    CASES_REQUEST = "cases-request"
    CASES_ORDER = "cases-order"
    EVENTS_PERSONAL = "events-personal"
    EVENTS_CRISIS = "events-crisis"
    EVENTS_SOCIAL = "events-social"
    EVENTS_BUSINESS = "events-business"
    EVENTS_TRADE = "events-trade"
    EVENTS_TRAVEL = "events-travel"
    EVENTS_ENVIRONMENTAL = "events-environmental"
    EVENTS_UNCONTROLLED = "events-uncontrolled"
    EVENTS_INTERACTION = "events-interaction"
    SERVICES_FRANCE_SOCIETY = "services-france-society"
    SERVICES_INVIDUALS___COMMUNITIES = "services-inviduals-&-communities"
    SERVICES_SERVICES_TO_BUSINESS = "services-services-to-business"
    SERVICES_CIVIC_INFRASTRUCTURE = "services-civic-infrastructure"
    SERVICES_GOVERNMENT_ADMINISTRATION = "services-government-administration"
    SERVICES_SERVICES_FROM_BUSINESS = "services-services-from-business"


class GeaNzActivitiesTaxonomyCasesComplianceEntry(str, Enum):
    ASSESSMENT = "assessment"
    AUDIT = "audit"
    INSPECTION = "inspection"
    INVESTIGATION = "investigation"
    REVIEW = "review"


class GeaNzActivitiesTaxonomyCasesProceedingEntry(str, Enum):
    BREACH = "breach"
    FINE = "fine"
    FRAUD = "fraud"
    OFFENCE = "offence"


class GeaNzActivitiesTaxonomyCasesEpisodeEntry(str, Enum):
    DEFECT = "defect"
    EMERGENCY = "emergency"
    ERROR = "error"
    FAULT = "fault"
    HISTORY = "history"
    INCIDENT = "incident"
    ISSUE = "issue"
    PROBLEM = "problem"
    CRIME = "crime"
    INFRIGEMENT = "infrigement"


class GeaNzActivitiesTaxonomyCasesClaimEntry(str, Enum):
    CLAIM_OF_DEFINITION = "claim-of-definition"
    CLAIM_OF_CAUSE = "claim-of-cause"
    CLAIM_OF_VALUE = "claim-of-value"
    CLAIM_OF_POLICY = "claim-of-policy"
    CLAIM_OF_FACT = "claim-of-fact"


class GeaNzActivitiesTaxonomyCasesRequestEntry(str, Enum):
    REQUEST_FOR_INFORMATION = "request-for-information"
    REQUEST_FOR_PROPOSAL = "request-for-proposal"
    REQUEST_FOR_QUOTATION = "request-for-quotation"
    REQUEST_FOR_TENDER = "request-for-tender"
    REQUEST_FOR_APPROVAL = "request-for-approval"
    REQUEST_FOR_COMMENTS = "request-for-comments"
    ORDER = "order"


class GeaNzActivitiesTaxonomyEventsPersonalEntry(str, Enum):
    BIRTH = "birth"
    STARTING_SCHOOL = "starting-school"
    ADOPTION = "adoption"
    MARRIAGE = "marriage"
    SENIOR_CITIZENSHIP = "senior-citizenship"
    CARE = "care"
    DEATH = "death"
    FOSTERING = "fostering"
    ENROL_TO_VOTE = "enrol-to-vote"
    VOLUNTEERING = "volunteering"
    DRIVER_S_LICENCE = "driver's-licence"


class GeaNzActivitiesTaxonomyEventsCrisisEntry(str, Enum):
    VICTIM_OF_A_CRIME = "victim-of-a-crime"
    WITNESS_OF_A_CRIME = "witness-of-a-crime"
    HEALTH = "health"
    EMERGENCY = "emergency"
    ACCUSED = "accused"
    CONVICTED = "convicted"


class GeaNzActivitiesTaxonomyEventsSocialEntry(str, Enum):
    CEREMONY = "ceremony"
    CONFERENCE = "conference"
    CONCERT = "concert"
    SPORTING_EVENT = "sporting-event"
    PROTEST = "protest"
    FESTIVAL = "festival"


class GeaNzActivitiesTaxonomyEventsBusinessEntry(str, Enum):
    SEED_CAPITAL = "seed-capital"
    START_UP = "start-up"
    HIRING = "hiring"
    TERMINATION_OF_EMPLOYMENT = "termination-of-employment"
    MERGE = "merge"
    DEMERGE = "demerge"
    STOCK_EXCHANGE_LISTING = "stock-exchange-listing"
    STOCK_EXCHANGE_DELISTING = "stock-exchange-delisting"
    CHANGE_NAME = "change-name"
    BANKRUPTCY = "bankruptcy"
    CEASE = "cease"


class GeaNzActivitiesTaxonomyEventsTradeEntry(str, Enum):
    BUYING = "buying"
    SELLING = "selling"
    IMPORTING = "importing"
    EXPORTING = "exporting"
    RENTING = "renting"


class GeaNzActivitiesTaxonomyEventsTravelEntry(str, Enum):
    TRAVELLING_OVERSEAS = "travelling-overseas"
    EXTENDED_STAY_IN_FRANCE = "extended-stay-in-france"


class GeaNzActivitiesTaxonomyEventsEnvironmentalEntry(str, Enum):
    ATMOSPHERIC = "atmospheric"
    ELEMENTAL = "elemental"
    GEOLOGICAL = "geological"
    SEASONAL = "seasonal"


class GeaNzActivitiesTaxonomyEventsUncontrolledEntry(str, Enum):
    ACCIDENT = "accident"
    ATTACK = "attack"
    FAILURE = "failure"
    OTHER = "other"


class GeaNzActivitiesTaxonomyEventsInteractionEntry(str, Enum):
    CHANNEL = "channel"
    MEDIUM = "medium"
    INTERACTION_TYPE = "interaction-type"


class GeaNzActivitiesTaxonomyServicesFranceSocietyEntry(str, Enum):
    BORDER_CONTROL = "border-control"
    CULTURE_AND_HERITAGE = "culture-and-heritage"
    DEFENCE = "defence"
    ECONOMIC_SERVICE = "economic-service"
    ENVIRONMENT = "environment"
    FINANCIAL_TRANSACTION_WITH_GOVERNMENT = "financial-transaction-with-government"
    INTERNATIONAL_RELATIONSHIP = "international-relationship"
    JUSTICE = "justice"
    FRANCE_SOCIETY = "france-society"
    NATURAL_RESOURCES = "natural-resources"
    OPEN_GOVERNMENT = "open-government"
    REGULATORY_COMPLIANCE_AND_ENFORCEMENT = "regulatory-compliance-and-enforcement"
    SCIENCE_AND_RESEARCH = "science-and-research"
    SECURITY = "security"
    STATISTICAL_SERVICES = "statistical-services"


class GeaNzActivitiesTaxonomyServicesInvidualsCommunitiesEntry(str, Enum):
    ADOPTING_AND_FOSTERING = "adopting-and-fostering"
    BIRTHS_DEATHS_AND_MARRIAGES = "births-deaths-and-marriages"
    CITIZENSHIP_AND_IMMIGRATION = "citizenship-and-immigration"
    COMMUNITY_SUPPORT = "community-support"
    EDUCATION_AND_TRAINING = "education-and-training"
    EMERGENCY_AND_DISASTER_PREPAREDNESS = "emergency-and-disaster-preparedness"
    INFORMATION_FROM_CITIZENS = "information-from-citizens"
    HEALTH_CARE = "health-care"
    PASSPORT_TRAVEL_AND_TOURISM = "passport-travel-and-tourism"
    SPORT_AND_RECREATION = "sport-and-recreation"
    WORK_AND_JOBS = "work-and-jobs"


class GeaNzActivitiesTaxonomyServicesServicesToBusinessEntry(str, Enum):
    BUSINESS_DEVELOPMENT = "business-development"
    BUSINESS_SUPPORT = "business-support"
    COMMERCIAL_SPORT = "commercial-sport"
    EMPLOYMENT = "employment"
    PRIMAL_INDUSTRIES = "primal-industries"
    TOURISM = "tourism"
    TRADE = "trade"


class GeaNzActivitiesTaxonomyServicesCivicInfrastructureEntry(str, Enum):
    CIVIC_MANAGEMENT = "civic-management"
    COMMUNICATIONS = "communications"
    ESSENTIAL_SERVICES = "essential-services"
    MARITIME_SERVICES = "maritime-services"
    PUBLIC_HOUSING = "public-housing"
    REGIONAL_DEVELOPMENT = "regional-development"
    TRANSPORT = "transport"


class GeaNzActivitiesTaxonomyServicesGovernmentAdministrationEntry(str, Enum):
    GOVERNMENT_ADMINISTRATION_MANAGEMENT = "government-administration-management"
    GOVERNMENT_BUSINESS_MANAGEMENT = "government-business-management"
    GOVERNMENT_CREDIT_AND_INSURANCE = "government-credit-and-insurance"
    GOVERNMENT_FINANCIAL_MANAGEMENT = "government-financial-management"
    GOVERNMENT_HUMAN_RESSOURCE_MANAGEMENT = "government-human-ressource-management"
    GOVERNMENT_ICT_MANAGEMENT = "government-ict-management"
    GOVERNMENT_INFORMATION_AND_KNOWLEDGE_MANAGEMENT = "government-information-and-knowledge-management"
    GOVERNMENT_STRATEGY_PLANNING_AND_BUDGETING = "government-strategy-planning-and-budgeting"
    MACHINERY_OF_GOVERNMENT = "machinery-of-government"


class GeaNzActivitiesTaxonomyServicesServicesFromBusinessEntry(str, Enum):
    ADVERTISING = "advertising"
    BUSINESS_MANAGEMENT = "business-management"
    INSURANCE = "insurance"
    FINANCIAL_SERVICE = "financial-service"
    REAL_ESTATE_AFFAIRS = "real-estate-affairs"
    BUILDING_CONSTRUCTION = "building-construction"
    TELECOMMUNICATION = "telecommunication"
    TRANSPORTATION = "transportation"
    PACKAGING_AND_STORAGE_OF_GOODS = "packaging-and-storage-of-goods"
    TRAVEL_ARRANGEMENT = "travel-arrangement"
    TREATMENT_OF_MATERIAL = "treatment-of-material"
    PROVIDING_TRAINING = "providing-training"
    ENTERTAINMENT = "entertainment"
    SCIENTIFIC_SERVICE = "scientific-service"
    PROVIDING_FOOD_DRINK_AND_ACCOMODATION = "providing-food-drink-and-accomodation"
    MEDICAL_SERVICE = "medical-service"
    LEGAL_SERVICE = "legal-service"


class GeaNzActivitiesTaxonomy(BaseModel):
    """Model for the gea-nz-activities taxonomy."""

    namespace: str = "gea-nz-activities"
    description: str = """Information needed to track or monitor moments, periods or events that occur over time. This type of information is focused on occurrences that must be tracked for business reasons or represent a specific point in the evolution of ‘The Business’."""
    version: int = 1
    exclusive: bool = False
    predicates: List[GeaNzActivitiesTaxonomyPredicate] = []
    cases_compliance_entries: List[GeaNzActivitiesTaxonomyCasesComplianceEntry] = []
    cases_proceeding_entries: List[GeaNzActivitiesTaxonomyCasesProceedingEntry] = []
    cases_episode_entries: List[GeaNzActivitiesTaxonomyCasesEpisodeEntry] = []
    cases_claim_entries: List[GeaNzActivitiesTaxonomyCasesClaimEntry] = []
    cases_request_entries: List[GeaNzActivitiesTaxonomyCasesRequestEntry] = []
    events_personal_entries: List[GeaNzActivitiesTaxonomyEventsPersonalEntry] = []
    events_crisis_entries: List[GeaNzActivitiesTaxonomyEventsCrisisEntry] = []
    events_social_entries: List[GeaNzActivitiesTaxonomyEventsSocialEntry] = []
    events_business_entries: List[GeaNzActivitiesTaxonomyEventsBusinessEntry] = []
    events_trade_entries: List[GeaNzActivitiesTaxonomyEventsTradeEntry] = []
    events_travel_entries: List[GeaNzActivitiesTaxonomyEventsTravelEntry] = []
    events_environmental_entries: List[GeaNzActivitiesTaxonomyEventsEnvironmentalEntry] = []
    events_uncontrolled_entries: List[GeaNzActivitiesTaxonomyEventsUncontrolledEntry] = []
    events_interaction_entries: List[GeaNzActivitiesTaxonomyEventsInteractionEntry] = []
    services_france_society_entries: List[GeaNzActivitiesTaxonomyServicesFranceSocietyEntry] = []
    services_inviduals___communities_entries: List[GeaNzActivitiesTaxonomyServicesInvidualsCommunitiesEntry] = []
    services_services_to_business_entries: List[GeaNzActivitiesTaxonomyServicesServicesToBusinessEntry] = []
    services_civic_infrastructure_entries: List[GeaNzActivitiesTaxonomyServicesCivicInfrastructureEntry] = []
    services_government_administration_entries: List[GeaNzActivitiesTaxonomyServicesGovernmentAdministrationEntry] = []
    services_services_from_business_entries: List[GeaNzActivitiesTaxonomyServicesServicesFromBusinessEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
