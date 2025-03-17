"""Taxonomy model for gea-nz-motivators."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GeaNzMotivatorsTaxonomyPredicate(str, Enum):
    PLANS_BUDGET = "plans-budget"
    PLANS_STRATEGY = "plans-strategy"
    PLANS_EFFORT = "plans-effort"
    PLANS_MEASURE = "plans-measure"
    PLANS_RISK = "plans-risk"
    PLANS_SPECIFICATION = "plans-specification"
    CONTROLS_OPERATIONAL = "controls-operational"
    CONTROLS_FINANCE = "controls-finance"
    CONTROLS_INDUSTRY = "controls-industry"
    CONTROLS_TECHNOLOGICAL = "controls-technological"
    CONTROLS_LAW = "controls-law"
    CONTROLS_PERSONAL = "controls-personal"
    CONTROLS_SECURITY = "controls-security"
    CONTRACTS_ARRANGEMENT = "contracts-arrangement"
    CONTRACTS_RIGHTS = "contracts-rights"
    CONTRACTS_OBLIGATION = "contracts-obligation"
    CONTRACTS_JURISDICTION = "contracts-jurisdiction"
    CONTROLS_RISK_GOVERNANCE = "controls-risk-governance"


class GeaNzMotivatorsTaxonomyPlansBudgetEntry(str, Enum):
    CAPITAL = "capital"
    OPERATING = "operating"


class GeaNzMotivatorsTaxonomyPlansStrategyEntry(str, Enum):
    STRATEGIC_DIRECTIVE = "strategic-directive"
    STRATEGIC_GOAL = "strategic-goal"
    STRATEGIC_OBJECTIVE = "strategic-objective"
    STRATEGIC_OUTCOME = "strategic-outcome"
    ROAD_MAP = "road-map"
    CHALLENGE = "challenge"
    OPPORTUNITY = "opportunity"


class GeaNzMotivatorsTaxonomyPlansEffortEntry(str, Enum):
    ACTIVITY = "activity"
    CAMPAIGN = "campaign"
    CARE = "care"
    PROGRAMME = "programme"
    PROJECT = "project"
    ROSTER = "roster"
    SCHEDULE = "schedule"
    TASK = "task"


class GeaNzMotivatorsTaxonomyPlansMeasureEntry(str, Enum):
    INPUT = "input"
    OUTPUT = "output"
    PERFORMANCE = "performance"
    BENEFIT = "benefit"


class GeaNzMotivatorsTaxonomyPlansRiskEntry(str, Enum):
    CONSEQUENCE = "consequence"
    HAZARD = "hazard"
    LIKELIHOOD = "likelihood"
    MITIGATION = "mitigation"
    INFLUENCE = "influence"
    DISRUPTION = "disruption"


class GeaNzMotivatorsTaxonomyPlansSpecificationEntry(str, Enum):
    FUNCTIONAL_REQUIREMENT = "functional-requirement"
    NON_FUNCTIONAL_REQUIREMENT = "non-functional-requirement"
    DESIGN = "design"


class GeaNzMotivatorsTaxonomyControlsOperationalEntry(str, Enum):
    CONVENTION = "convention"
    GUIDELINE = "guideline"
    POLICY = "policy"
    PRINCIPLE = "principle"
    STANDARD = "standard"
    PROCEDURE = "procedure"
    PROCESS = "process"
    CAPABILITY = "capability"
    RULE = "rule"
    EXCEPTION = "exception"
    SCOPE_OF_USE = "scope-of-use"


class GeaNzMotivatorsTaxonomyControlsFinanceEntry(str, Enum):
    FINANCIAL_ASSET = "financial-asset"
    EQUITY = "equity"
    EXPENSE = "expense"
    FEE = "fee"
    INCOME = "income"
    FINANCIAL_LIABILITY = "financial-liability"
    ACQUISITION_METHOD = "acquisition-method"


class GeaNzMotivatorsTaxonomyControlsIndustryEntry(str, Enum):
    BEST_PRACTICE = "best-practice"
    REGULATION = "regulation"
    TERMINOLOGY = "terminology"


class GeaNzMotivatorsTaxonomyControlsTechnologicalEntry(str, Enum):
    ENFORCED_RULES = "enforced-rules"
    CONSTRAINTS = "constraints"


class GeaNzMotivatorsTaxonomyControlsLawEntry(str, Enum):
    COMMON_LAW = "common-law"
    LEGISLATIVE_INSTRUMENT = "legislative-instrument"
    ACT = "act"
    CABINET_MINUTE = "cabinet-minute"


class GeaNzMotivatorsTaxonomyControlsPersonalEntry(str, Enum):
    PERSONAL_DIRECTIVE = "personal-directive"


class GeaNzMotivatorsTaxonomyContractsArrangementEntry(str, Enum):
    MEMORANDUM_OF_UNDERSTANDING = "memorandum-of-understanding"
    OFFER = "offer"
    ORDER = "order"
    AGREEMENT = "agreement"
    REQUEST = "request"
    CONFIDENTIALITY = "confidentiality"
    EMPLOYMENT = "employment"
    SERVICE = "service"
    SUPPLY = "supply"


class GeaNzMotivatorsTaxonomyContractsRightsEntry(str, Enum):
    ELIGIBILITY = "eligibility"
    CREDITS = "credits"
    ACCESS_RIGHT = "access-right"
    AUTHORISATION = "authorisation"
    HUMAN_RIGHT = "human-right"
    EMPLOYMENT_RIGHT = "employment-right"
    PROPERTY_RIGHT = "property-right"
    CONSUMER_RIGHT = "consumer-right"


class GeaNzMotivatorsTaxonomyContractsObligationEntry(str, Enum):
    DUTY_OF_CARE = "duty-of-care"
    FITNESS_FOR_PURPOSE = "fitness-for-purpose"
    WARRANTY = "warranty"
    PRIVACY = "privacy"
    TRUTHFULNESS = "truthfulness"
    ENFORCE_THE_LAW = "enforce-the-law"
    OBEY_THE_LAW = "obey-the-law"
    ACCOUNT_PAYABLE = "account-payable"
    ENFORCE_RULES = "enforce-rules"
    OBEY_RULES = "obey-rules"


class GeaNzMotivatorsTaxonomyContractsJurisdictionEntry(str, Enum):
    NATIONAL = "national"
    INTERNATIONAL = "international"
    LOCAL = "local"
    POLITICAL = "political"
    REGIONAL = "regional"


class GeaNzMotivatorsTaxonomyControlsRiskGovernanceEntry(str, Enum):
    RESIDUAL = "residual"
    ACCEPTANCE = "acceptance"
    ANALYSIS = "analysis"
    ASSESSEMENT = "assessement"
    MANAGEMENT = "management"
    TREATMENT = "treatment"


class GeaNzMotivatorsTaxonomy(BaseModel):
    """Model for the gea-nz-motivators taxonomy."""

    namespace: str = "gea-nz-motivators"
    description: str = """Information relating to authority or governance."""
    version: int = 1
    exclusive: bool = False
    predicates: List[GeaNzMotivatorsTaxonomyPredicate] = []
    plans_budget_entries: List[GeaNzMotivatorsTaxonomyPlansBudgetEntry] = []
    plans_strategy_entries: List[GeaNzMotivatorsTaxonomyPlansStrategyEntry] = []
    plans_effort_entries: List[GeaNzMotivatorsTaxonomyPlansEffortEntry] = []
    plans_measure_entries: List[GeaNzMotivatorsTaxonomyPlansMeasureEntry] = []
    plans_risk_entries: List[GeaNzMotivatorsTaxonomyPlansRiskEntry] = []
    plans_specification_entries: List[GeaNzMotivatorsTaxonomyPlansSpecificationEntry] = []
    controls_operational_entries: List[GeaNzMotivatorsTaxonomyControlsOperationalEntry] = []
    controls_finance_entries: List[GeaNzMotivatorsTaxonomyControlsFinanceEntry] = []
    controls_industry_entries: List[GeaNzMotivatorsTaxonomyControlsIndustryEntry] = []
    controls_technological_entries: List[GeaNzMotivatorsTaxonomyControlsTechnologicalEntry] = []
    controls_law_entries: List[GeaNzMotivatorsTaxonomyControlsLawEntry] = []
    controls_personal_entries: List[GeaNzMotivatorsTaxonomyControlsPersonalEntry] = []
    contracts_arrangement_entries: List[GeaNzMotivatorsTaxonomyContractsArrangementEntry] = []
    contracts_rights_entries: List[GeaNzMotivatorsTaxonomyContractsRightsEntry] = []
    contracts_obligation_entries: List[GeaNzMotivatorsTaxonomyContractsObligationEntry] = []
    contracts_jurisdiction_entries: List[GeaNzMotivatorsTaxonomyContractsJurisdictionEntry] = []
    controls_risk_governance_entries: List[GeaNzMotivatorsTaxonomyControlsRiskGovernanceEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
