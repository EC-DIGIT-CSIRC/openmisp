"""Taxonomy model for ThreatMatch categories for sharing into ThreatMatch and MISP."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ThreatmatchTaxonomyPredicate(str, Enum):
    SECTOR = "sector"
    INCIDENT_TYPE = "incident-type"
    MALWARE_TYPE = "malware-type"
    ALERT_TYPE = "alert-type"


class ThreatmatchTaxonomySectorEntry(str, Enum):
    BANKING___CAPITAL_MARKETS = "Banking & Capital Markets"
    FINANCIAL_SERVICES = "Financial Services"
    INSURANCE = "Insurance"
    PENSION = "Pension"
    GOVERNMENT___PUBLIC_SERVICE = "Government & Public Service"
    DIPLOMATIC_SERVICES = "Diplomatic Services"
    ENERGY__UTILITIES___MINING = "Energy, Utilities & Mining"
    TELECOMMUNICATIONS = "Telecommunications"
    TECHNOLOGY = "Technology"
    ACADEMIC_RESEARCH_INSTITUTES = "Academic/Research Institutes"
    AEROSPACE__DEFENCE___SECURITY = "Aerospace, Defence & Security"
    AGRICULTURE = "Agriculture"
    ASSET___WEALTH_MANAGEMENT = "Asset & Wealth Management"
    AUTOMOTIVE = "Automotive"
    BUSINESS_AND_PROFESSIONAL_SERVICES = "Business and Professional Services"
    CAPITAL_PROJECTS___INFRASTRUCTURE = "Capital Projects & Infrastructure"
    CHARITY_NOT_FOR_PROFIT = "Charity/Not-for-Profit"
    CHEMICALS = "Chemicals"
    COMMERCIAL_AVIATION = "Commercial Aviation"
    COMMODITIES = "Commodities"
    EDUCATION = "Education"
    ENGINEERING___CONSTRUCTION = "Engineering & Construction"
    ENTERTAINMENT___MEDIA = "Entertainment & Media"
    FOREST__PAPER___PACKAGING = "Forest, Paper & Packaging"
    HEALTHCARE = "Healthcare"
    HOSPITALITY___LEISURE = "Hospitality & Leisure"
    INDUSTRIAL_MANUFACTURING = "Industrial Manufacturing"
    IT_INDUSTRY = "IT Industry"
    LEGAL = "Legal"
    METALS = "Metals"
    PHARMACEUTICALS___LIFE_SCIENCES = "Pharmaceuticals & Life Sciences"
    PRIVATE_EQUITY = "Private Equity"
    RETAIL___CONSUMER = "Retail & Consumer"
    SEMICONDUCTORS = "Semiconductors"
    SOVEREIGN_INVESTMENT_FUNDS = "Sovereign Investment Funds"
    TRANSPORT___LOGISTICS = "Transport & Logistics"


class ThreatmatchTaxonomyIncidentTypeEntry(str, Enum):
    ATM_ATTACKS = "ATM Attacks"
    ATM_BREACH = "ATM Breach"
    ATTEMPTED_EXPLOITATION = "Attempted Exploitation"
    BOTNET_ACTIVITY = "Botnet Activity"
    BUSINESS_EMAIL_COMPROMISE = "Business Email Compromise"
    CRYPTO_MINING = "Crypto Mining"
    DATA_BREACH_COMPROMISE = "Data Breach/Compromise"
    DATA_DUMP = "Data Dump"
    DATA_LEAKAGE = "Data Leakage"
    DDO_S = "DDoS"
    DEFACEMENT_ACTIVITY = "Defacement Activity"
    DENIAL_OF_SERVICE__DO_S_ = "Denial of Service (DoS)"
    DISRUPTION_ACTIVITY = "Disruption Activity"
    ESPIONAGE = "Espionage"
    ESPIONAGE_ACTIVITY = "Espionage Activity"
    EXEC_TARGETING_ = "Exec Targeting "
    EXPOSURE_OF_DATA = "Exposure of Data"
    EXTORTION_ACTIVITY = "Extortion Activity"
    FRAUD_ACTIVITY = "Fraud Activity"
    GENERAL_NOTIFICATION = "General Notification"
    HACKTIVISM_ACTIVITY = "Hacktivism Activity"
    MALICIOUS_INSIDER = "Malicious Insider"
    MALWARE_INFECTION = "Malware Infection"
    MAN_IN_THE_MIDDLE_ATTACKS = "Man in the Middle Attacks"
    MFA_ATTACK = "MFA Attack"
    MOBILE_MALWARE = "Mobile Malware"
    PHISHING_ACTIVITY = "Phishing Activity"
    RANSOMWARE_ACTIVITY = "Ransomware Activity"
    SOCIAL_ENGINEERING_ACTIVITY = "Social Engineering Activity"
    SOCIAL_MEDIA_COMPROMISE = "Social Media Compromise"
    SPEAR_PHISHING_ACTIVITY = "Spear-phishing Activity"
    SPYWARE = "Spyware"
    SQL_INJECTION_ACTIVITY = "SQL Injection Activity"
    SUPPLY_CHAIN_COMPROMISE = "Supply Chain Compromise"
    TROJANISED_SOFTWARE = "Trojanised Software"
    VISHING = "Vishing"
    WEBSITE_ATTACK__OTHER_ = "Website Attack (Other)"
    UNKNOWN = "Unknown"


class ThreatmatchTaxonomyMalwareTypeEntry(str, Enum):
    ADWARE = "Adware"
    BACKDOOR = "Backdoor"
    BANKING_TROJAN = "Banking Trojan"
    BOTNET = "Botnet"
    DESTRUCTIVE = "Destructive"
    DOWNLOADER = "Downloader"
    EXPLOIT_KIT = "Exploit Kit"
    FILELESS_MALWARE = "Fileless Malware"
    KEYLOGGER = "Keylogger"
    LEGITIMATE_TOOL = "Legitimate Tool"
    MOBILE_APPLICATION = "Mobile Application"
    MOBILE_MALWARE = "Mobile Malware"
    POINT_OF_SALE__PO_S_ = "Point-of-Sale (PoS)"
    REMOTE_ACCESS_TROJAN = "Remote Access Trojan"
    ROOTKIT = "Rootkit"
    SKIMMER = "Skimmer"
    SPYWARE = "Spyware"
    SURVEILLANCE_TOOL = "Surveillance Tool"
    TROJAN = "Trojan"
    VIRUS = "Virus"
    WORM = "Worm"
    ZERO_DAY = "Zero-day"
    UNKNOWN = "Unknown"


class ThreatmatchTaxonomyAlertTypeEntry(str, Enum):
    ACTOR_CAMPAIGNS = "Actor Campaigns"
    CREDENTIAL_BREACH = "Credential Breach"
    DDO_S = "DDoS"
    EXPLOIT_ALERT = "Exploit Alert"
    GENERAL_NOTIFICATION = "General Notification"
    VULNERABILITY = "Vulnerability"
    INFORMATION_LEAKAGES = "Information Leakages"
    MALWARE = "Malware"
    SUSPICIOUS_DOMAIN = "Suspicious Domain"
    FORUM_MENTION = "Forum Mention"
    PHISHING_ATTEMPTS = "Phishing Attempts"
    SOCIAL_MEDIA_ALERTS = "Social Media Alerts"
    SUPPLY_CHAIN_EVENT = "Supply Chain Event"
    TECHNICAL_EXPOSURE = "Technical Exposure"
    THREAT_ACTOR_UPDATE = "Threat Actor Update"
    DIRECT_TARGETING_ = "Direct Targeting "
    PROTEST_ACTIVITY = "Protest Activity"
    VIOLENT_EVENT = "Violent Event"
    STRATEGIC_EVENT = "Strategic Event"
    INSIDER_THREAT = "Insider Threat"


class ThreatmatchTaxonomy(BaseModel):
    """Model for the ThreatMatch categories for sharing into ThreatMatch and MISP taxonomy."""

    namespace: str = "threatmatch"
    description: str = """The ThreatMatch Sectors, Incident types, Malware types and Alert types are applicable for any ThreatMatch instances and should be used for all CIISI and TIBER Projects."""
    version: int = 3
    exclusive: bool = False
    predicates: List[ThreatmatchTaxonomyPredicate] = []
    sector_entries: List[ThreatmatchTaxonomySectorEntry] = []
    incident_type_entries: List[ThreatmatchTaxonomyIncidentTypeEntry] = []
    malware_type_entries: List[ThreatmatchTaxonomyMalwareTypeEntry] = []
    alert_type_entries: List[ThreatmatchTaxonomyAlertTypeEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
