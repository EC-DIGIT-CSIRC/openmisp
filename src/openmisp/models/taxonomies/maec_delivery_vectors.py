"""Taxonomy model for maec-delivery-vectors."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class MaecDeliveryVectorsTaxonomyPredicate(str, Enum):
    MAEC_DELIVERY_VECTOR = "maec-delivery-vector"


class MaecDeliveryVectorsTaxonomyMaecDeliveryVectorEntry(str, Enum):
    ACTIVE_ATTACKER = "active-attacker"
    AUTO_EXECUTING_MEDIA = "auto-executing-media"
    DOWNLOADER = "downloader"
    DROPPER = "dropper"
    EMAIL_ATTACHMENT = "email-attachment"
    EXPLOIT_KIT_LANDING_PAGE = "exploit-kit-landing-page"
    FAKE_WEBSITE = "fake-website"
    JANITOR_ATTACK = "janitor-attack"
    MALICIOUS_IFRAMES = "malicious-iframes"
    MALVERTISING = "malvertising"
    MEDIA_BAITING = "media-baiting"
    PHARMING = "pharming"
    PHISHING = "phishing"
    TROJANIZED_LINK = "trojanized-link"
    TROJANIZED_SOFTWARE = "trojanized-software"
    USB_CABLE_SYNCING = "usb-cable-syncing"
    WATERING_HOLE = "watering-hole"


class MaecDeliveryVectorsTaxonomy(BaseModel):
    """Model for the maec-delivery-vectors taxonomy."""

    namespace: str = "maec-delivery-vectors"
    description: str = """Vectors used to deliver malware based on MAEC 5.0"""
    version: int = 1
    exclusive: bool = False
    predicates: List[MaecDeliveryVectorsTaxonomyPredicate] = []
    maec_delivery_vector_entries: List[MaecDeliveryVectorsTaxonomyMaecDeliveryVectorEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
