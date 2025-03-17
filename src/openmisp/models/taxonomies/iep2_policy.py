"""Taxonomy model for iep2-policy."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Iep2PolicyTaxonomyPredicate(str, Enum):
    ID = "id"
    NAME = "name"
    DESCRIPTION = "description"
    IEP_VERSION = "iep_version"
    START_DATE = "start_date"
    END_DATE = "end_date"
    ENCRYPT_IN_TRANSIT = "encrypt_in_transit"
    PERMITTED_ACTIONS = "permitted_actions"
    AFFECTED_PARTY_NOTIFICATIONS = "affected_party_notifications"
    TLP = "tlp"
    ATTRIBUTION = "attribution"
    UNMODIFIED_RESALE = "unmodified_resale"
    EXTERNAL_REFERENCE = "external_reference"


class Iep2PolicyTaxonomyIdEntry(str, Enum):
    T__TEXT = "$text"


class Iep2PolicyTaxonomyNameEntry(str, Enum):
    T__TEXT = "$text"


class Iep2PolicyTaxonomyDescriptionEntry(str, Enum):
    T__TEXT = "$text"


class Iep2PolicyTaxonomyIepVersionEntry(str, Enum):
    T_2_0 = "2.0"


class Iep2PolicyTaxonomyStartDateEntry(str, Enum):
    T__TEXT = "$text"


class Iep2PolicyTaxonomyEndDateEntry(str, Enum):
    T__TEXT = "$text"


class Iep2PolicyTaxonomyEncryptInTransitEntry(str, Enum):
    MUST = "must"
    MAY = "may"


class Iep2PolicyTaxonomyPermittedActionsEntry(str, Enum):
    NONE = "none"
    CONTACT_FOR_INSTRUCTION = "contact-for-instruction"
    INTERNALLY_VISIBLE_ACTIONS = "internally-visible-actions"
    EXTERNALLY_VISIBLE_INDIRECT_ACTIONS = "externally-visible-indirect-actions"
    EXTERNALLY_VISIBLE_DIRECT_ACTIONS = "externally-visible-direct-actions"


class Iep2PolicyTaxonomyAffectedPartyNotificationsEntry(str, Enum):
    MAY = "may"
    MUST_NOT = "must-not"


class Iep2PolicyTaxonomyTlpEntry(str, Enum):
    RED = "red"
    AMBER = "amber"
    GREEN = "green"
    WHITE = "white"


class Iep2PolicyTaxonomyAttributionEntry(str, Enum):
    MAY = "may"
    MUST = "must"
    MUST_NOT = "must-not"


class Iep2PolicyTaxonomyUnmodifiedResaleEntry(str, Enum):
    MAY = "may"
    MUST_NOT = "must-not"


class Iep2PolicyTaxonomyExternalReferenceEntry(str, Enum):
    T__TEXT = "$text"


class Iep2PolicyTaxonomy(BaseModel):
    """Model for the iep2-policy taxonomy."""

    namespace: str = "iep2-policy"
    description: str = (
        """Forum of Incident Response and Security Teams (FIRST) Information Exchange Policy (IEP) v2.0 Policy"""
    )
    version: int = 1
    exclusive: bool = False
    predicates: List[Iep2PolicyTaxonomyPredicate] = []
    id_entries: List[Iep2PolicyTaxonomyIdEntry] = []
    name_entries: List[Iep2PolicyTaxonomyNameEntry] = []
    description_entries: List[Iep2PolicyTaxonomyDescriptionEntry] = []
    iep_version_entries: List[Iep2PolicyTaxonomyIepVersionEntry] = []
    start_date_entries: List[Iep2PolicyTaxonomyStartDateEntry] = []
    end_date_entries: List[Iep2PolicyTaxonomyEndDateEntry] = []
    encrypt_in_transit_entries: List[Iep2PolicyTaxonomyEncryptInTransitEntry] = []
    permitted_actions_entries: List[Iep2PolicyTaxonomyPermittedActionsEntry] = []
    affected_party_notifications_entries: List[Iep2PolicyTaxonomyAffectedPartyNotificationsEntry] = []
    tlp_entries: List[Iep2PolicyTaxonomyTlpEntry] = []
    attribution_entries: List[Iep2PolicyTaxonomyAttributionEntry] = []
    unmodified_resale_entries: List[Iep2PolicyTaxonomyUnmodifiedResaleEntry] = []
    external_reference_entries: List[Iep2PolicyTaxonomyExternalReferenceEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
