"""Taxonomy model for gea-nz-entities."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class GeaNzEntitiesTaxonomyPredicate(str, Enum):
    PARTIES_PARTY = "parties-party"
    PARTIES_QUALIFICATION = "parties-qualification"
    PARTIES_ROLE = "parties-role"
    PARTIES_PARTY_RELATIONSHIP = "parties-party-relationship"
    PLACES_ADDRESS = "places-address"
    PLACES_LOCATION_TYPE = "places-location-type"
    PLACES_ADDRESS_TYPE = "places-address-type"
    PLACES_PURPOSE_OF_LOCATION = "places-purpose-of-location"
    ITEMS_APPLICATION___ICT_SERVICES = "items-application-&-ict-services"
    ITEMS_ICT_INFRASTRUCTURE = "items-ict-infrastructure"
    ITEMS_NATURAL = "items-natural"
    ITEMS_FINANCIAL = "items-financial"
    ITEMS_GOODS = "items-goods"
    ITEMS_REGULATORY = "items-regulatory"
    ITEMS_URBAN_INFRASTRUCTURE = "items-urban-infrastructure"
    ITEMS_ACCOMMODATION = "items-accommodation"
    ITEMS_DWELLING_TYPE = "items-dwelling-type"
    ITEMS_ARTEFACT = "items-artefact"
    ITEMS_WASTE = "items-waste"
    ITEMS_ITEM_USAGE = "items-item-usage"
    ITEMS_OTHER_ITEM = "items-other-item"


class GeaNzEntitiesTaxonomyPartiesPartyEntry(str, Enum):
    ORGANISATION = "organisation"
    INDIVIDUAL = "individual"


class GeaNzEntitiesTaxonomyPartiesQualificationEntry(str, Enum):
    COMPETENCE = "competence"
    EDUCATION = "education"
    INDUSTRY = "industry"
    OCCUPATION = "occupation"


class GeaNzEntitiesTaxonomyPartiesRoleEntry(str, Enum):
    COMMERCE = "commerce"
    LEGAL = "legal"
    OF_INTEREST = "of-interest"
    SOCIAL = "social"


class GeaNzEntitiesTaxonomyPartiesPartyRelationshipEntry(str, Enum):
    MEMBERSHIP = "membership"
    EMPLOYER = "employer"
    PROVIDER = "provider"
    DELEGATION = "delegation"


class GeaNzEntitiesTaxonomyPlacesAddressEntry(str, Enum):
    ELECTRONIC_ADDRESS = "electronic-address"
    PHYSICAL_ADDRESS = "physical-address"


class GeaNzEntitiesTaxonomyPlacesLocationTypeEntry(str, Enum):
    GEOPOLITICAL = "geopolitical"
    GEOSPATIAL = "geospatial"


class GeaNzEntitiesTaxonomyPlacesAddressTypeEntry(str, Enum):
    NZ_STANDARD_ADDRESSS = "nz-standard-addresss"
    PO_BOX = "po-box"
    RURAL_DELIVERY_ADDRESS = "rural-delivery-address"
    OVEARSEAS_ADDRESS = "ovearseas-address"
    LOCATION_ADDRESSS = "location-addresss"


class GeaNzEntitiesTaxonomyPlacesPurposeOfLocationEntry(str, Enum):
    RESIDENCY = "residency"
    DELIVERY = "delivery"
    BILLING = "billing"
    PLACE_OF_BIRTH = "place-of-birth"
    CONSULTATION = "consultation"
    REFERRAL = "referral"
    ADMISSION = "admission"
    TREATMENT = "treatment"
    WORK_PLACE = "work-place"
    FACILITY_LOCATION = "facility-location"
    STORAGE = "storage"
    PLACE_OF_EVENT = "place-of-event"


class GeaNzEntitiesTaxonomyItemsApplicationIctServicesEntry(str, Enum):
    CORPORATE_APPLICATION = "corporate-application"
    COMMON_LINE_OF_BUSINESS_APPLICATION = "common-line-of-business-application"
    END_USER_COMPUTING = "end-user-computing"
    DATA_AND_INFORMATION_MANAGEMENT = "data-and-information-management"
    IDENTITY_AND_ACCESD_MANAGEMENT = "identity-and-accesd-management"
    SECURITY_SERVICE = "security-service"
    ICT_COMPONENTS_SERVICES_AND_TOOLS = "ict-components-services-and-tools"
    INTERFACE_AND_INTEGRATION = "interface-and-integration"


class GeaNzEntitiesTaxonomyItemsIctInfrastructureEntry(str, Enum):
    PLATFORM = "platform"
    NETWORK = "network"
    FACILITY = "facility"
    END_USER_EQUIPMENT = "end-user-equipment"


class GeaNzEntitiesTaxonomyItemsNaturalEntry(str, Enum):
    AIR = "air"
    FAUNA = "fauna"
    FLORA = "flora"
    LAND = "land"
    MINERALS = "minerals"
    WATER = "water"
    ENERGY = "energy"


class GeaNzEntitiesTaxonomyItemsFinancialEntry(str, Enum):
    ALLOWANCE = "allowance"
    AWARD = "award"
    BENEFIT = "benefit"
    BONUS = "bonus"
    COMPENSATION = "compensation"
    CONCESSION = "concession"
    GRANT = "grant"
    PENSION = "pension"
    SUBSIDY = "subsidy"
    WAGE = "wage"
    BOND = "bond"
    DUTY = "duty"
    EXCISE = "excise"
    INSURANCE = "insurance"
    LOAN = "loan"
    TAX = "tax"


class GeaNzEntitiesTaxonomyItemsGoodsEntry(str, Enum):
    CHEMICAL = "chemical"
    PAINT = "paint"
    BLEACH = "bleach"
    INDUSTRIAL_OIL = "industrial-oil"
    PHARMACEUTICAL_PREPARATION = "pharmaceutical-preparation"
    COMMON_METAL = "common-metal"
    MACHINE = "machine"
    HAND_TOOL = "hand-tool"
    SCIENTIFIC_APPARATUS_AND_INSTRUMENT = "scientific-apparatus-and-instrument"
    MEDICAL_APPARATUS_AND_INSTRUMENT = "medical-apparatus-and-instrument"
    ELECTRICAL_APPARATUS = "electrical-apparatus"
    VEHICLE = "vehicle"
    FIREARM = "firearm"
    PRECIOUS_METAL = "precious-metal"
    MUSICAL_INSTRUMENT = "musical-instrument"
    PAPER = "paper"
    RUBBER_GOOD = "rubber-good"
    LEATHER = "leather"
    BUILDING_MATERIAL = "building-material"
    FURNITURE = "furniture"
    HOUSEHOLD_UTENSIL = "household-utensil"
    ROPE = "rope"
    YARN = "yarn"
    TEXTILE = "textile"
    CLOTHING = "clothing"
    LACE = "lace"
    CARPET = "carpet"
    TOY = "toy"
    FOOD = "food"
    LIQUID_FOOD = "liquid-food"
    AGRICULTURAL_PRODUCT = "agricultural-product"
    BEVERAGES = "beverages"
    ALCOHOLIC_BEVERAGE = "alcoholic-beverage"
    TOBACCO = "tobacco"


class GeaNzEntitiesTaxonomyItemsRegulatoryEntry(str, Enum):
    CERTIFICATE = "certificate"
    LICENSE = "license"
    PERMIT = "permit"
    REGISTRATION = "registration"
    DECLARATION = "declaration"


class GeaNzEntitiesTaxonomyItemsUrbanInfrastructureEntry(str, Enum):
    WATER_SUPPLY_SYSTEM = "water-supply-system"
    ELECTRIC_POWER_SYSTEM = "electric-power-system"
    TRANSPORT_NETWORK = "transport-network"
    SANITATION_SYSTEM = "sanitation-system"
    COMMUNICATION_SYSTEM = "communication-system"


class GeaNzEntitiesTaxonomyItemsItemUsageEntry(str, Enum):
    PRODUCT = "product"
    RESOURCE = "resource"


class GeaNzEntitiesTaxonomy(BaseModel):
    """Model for the gea-nz-entities taxonomy."""

    namespace: str = "gea-nz-entities"
    description: str = """Information relating to instances of entities or things."""
    version: int = 1
    exclusive: bool = False
    predicates: List[GeaNzEntitiesTaxonomyPredicate] = []
    parties_party_entries: List[GeaNzEntitiesTaxonomyPartiesPartyEntry] = []
    parties_qualification_entries: List[GeaNzEntitiesTaxonomyPartiesQualificationEntry] = []
    parties_role_entries: List[GeaNzEntitiesTaxonomyPartiesRoleEntry] = []
    parties_party_relationship_entries: List[GeaNzEntitiesTaxonomyPartiesPartyRelationshipEntry] = []
    places_address_entries: List[GeaNzEntitiesTaxonomyPlacesAddressEntry] = []
    places_location_type_entries: List[GeaNzEntitiesTaxonomyPlacesLocationTypeEntry] = []
    places_address_type_entries: List[GeaNzEntitiesTaxonomyPlacesAddressTypeEntry] = []
    places_purpose_of_location_entries: List[GeaNzEntitiesTaxonomyPlacesPurposeOfLocationEntry] = []
    items_application___ict_services_entries: List[GeaNzEntitiesTaxonomyItemsApplicationIctServicesEntry] = []
    items_ict_infrastructure_entries: List[GeaNzEntitiesTaxonomyItemsIctInfrastructureEntry] = []
    items_natural_entries: List[GeaNzEntitiesTaxonomyItemsNaturalEntry] = []
    items_financial_entries: List[GeaNzEntitiesTaxonomyItemsFinancialEntry] = []
    items_goods_entries: List[GeaNzEntitiesTaxonomyItemsGoodsEntry] = []
    items_regulatory_entries: List[GeaNzEntitiesTaxonomyItemsRegulatoryEntry] = []
    items_urban_infrastructure_entries: List[GeaNzEntitiesTaxonomyItemsUrbanInfrastructureEntry] = []
    items_item_usage_entries: List[GeaNzEntitiesTaxonomyItemsItemUsageEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
