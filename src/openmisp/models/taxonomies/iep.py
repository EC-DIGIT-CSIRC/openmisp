"""Taxonomy model for iep."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class IepTaxonomyPredicate(str, Enum):
    COMMERCIAL_USE = "commercial-use"
    EXTERNAL_REFERENCE = "external-reference"
    ENCRYPT_IN_TRANSIT = "encrypt-in-transit"
    ENCRYPT_AT_REST = "encrypt-at-rest"
    PERMITTED_ACTIONS = "permitted-actions"
    AFFECTED_PARTY_NOTIFICATIONS = "affected-party-notifications"
    TRAFFIC_LIGHT_PROTOCOL = "traffic-light-protocol"
    PROVIDER_ATTRIBUTION = "provider-attribution"
    OBFUSCATE_AFFECTED_PARTIES = "obfuscate-affected-parties"
    UNMODIFIED_RESALE = "unmodified-resale"
    START_DATE = "start-date"
    END_DATE = "end-date"
    REFERENCE = "reference"
    NAME = "name"
    VERSION = "version"
    ID = "id"


class IepTaxonomyCommercialUseEntry(str, Enum):
    MAY = "MAY"
    MUST_NOT = "MUST NOT"


class IepTaxonomyExternalReferenceEntry(str, Enum):
    T__TEXT = "$text"


class IepTaxonomyEncryptInTransitEntry(str, Enum):
    MUST = "MUST"
    MAY = "MAY"


class IepTaxonomyEncryptAtRestEntry(str, Enum):
    MUST = "MUST"
    MAY = "MAY"


class IepTaxonomyPermittedActionsEntry(str, Enum):
    NONE = "NONE"
    CONTACT_FOR_INSTRUCTION = "CONTACT FOR INSTRUCTION"
    INTERNALLY_VISIBLE_ACTIONS = "INTERNALLY VISIBLE ACTIONS"
    EXTERNALLY_VISIBLE_INDIRECT_ACTIONS = "EXTERNALLY VISIBLE INDIRECT ACTIONS"
    EXTERNALLY_VISIBLE_DIRECT_ACTIONS = "EXTERNALLY VISIBLE DIRECT ACTIONS"


class IepTaxonomyAffectedPartyNotificationsEntry(str, Enum):
    MAY = "MAY"
    MUST_NOT = "MUST NOT"


class IepTaxonomyTrafficLightProtocolEntry(str, Enum):
    RED = "RED"
    AMBER = "AMBER"
    GREEN = "GREEN"
    WHITE = "WHITE"


class IepTaxonomyProviderAttributionEntry(str, Enum):
    MAY = "MAY"
    MUST = "MUST"
    MUST_NOT = "MUST NOT"


class IepTaxonomyObfuscateAffectedPartiesEntry(str, Enum):
    MAY = "MAY"
    MUST = "MUST"
    MUST_NOT = "MUST NOT"


class IepTaxonomyUnmodifiedResaleEntry(str, Enum):
    MAY = "MAY"
    MUST_NOT = "MUST NOT"


class IepTaxonomyStartDateEntry(str, Enum):
    T__TEXT = "$text"


class IepTaxonomyEndDateEntry(str, Enum):
    T__TEXT = "$text"


class IepTaxonomyReferenceEntry(str, Enum):
    T__TEXT = "$text"


class IepTaxonomyNameEntry(str, Enum):
    T__TEXT = "$text"


class IepTaxonomyVersionEntry(str, Enum):
    T__TEXT = "$text"


class IepTaxonomyIdEntry(str, Enum):
    T__TEXT = "$text"


class IepTaxonomy(BaseModel):
    """Model for the iep taxonomy."""

    namespace: str = "iep"
    description: str = (
        """Forum of Incident Response and Security Teams (FIRST) Information Exchange Policy (IEP) framework"""
    )
    version: int = 2
    exclusive: bool = False
    predicates: List[IepTaxonomyPredicate] = []
    commercial_use_entries: List[IepTaxonomyCommercialUseEntry] = []
    external_reference_entries: List[IepTaxonomyExternalReferenceEntry] = []
    encrypt_in_transit_entries: List[IepTaxonomyEncryptInTransitEntry] = []
    encrypt_at_rest_entries: List[IepTaxonomyEncryptAtRestEntry] = []
    permitted_actions_entries: List[IepTaxonomyPermittedActionsEntry] = []
    affected_party_notifications_entries: List[IepTaxonomyAffectedPartyNotificationsEntry] = []
    traffic_light_protocol_entries: List[IepTaxonomyTrafficLightProtocolEntry] = []
    provider_attribution_entries: List[IepTaxonomyProviderAttributionEntry] = []
    obfuscate_affected_parties_entries: List[IepTaxonomyObfuscateAffectedPartiesEntry] = []
    unmodified_resale_entries: List[IepTaxonomyUnmodifiedResaleEntry] = []
    start_date_entries: List[IepTaxonomyStartDateEntry] = []
    end_date_entries: List[IepTaxonomyEndDateEntry] = []
    reference_entries: List[IepTaxonomyReferenceEntry] = []
    name_entries: List[IepTaxonomyNameEntry] = []
    version_entries: List[IepTaxonomyVersionEntry] = []
    id_entries: List[IepTaxonomyIdEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
