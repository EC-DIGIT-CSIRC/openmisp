"""Taxonomy model for Domain Name Abuse."""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DomainAbuseTaxonomyPredicate(str, Enum):
    DOMAIN_STATUS = "domain-status"
    DOMAIN_ACCESS_METHOD = "domain-access-method"


class DomainAbuseTaxonomyDomainStatusEntry(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    NOT_REGISTERED = "not-registered"
    NOT_REGISTRABLE = "not-registrable"
    GRACE_PERIOD = "grace-period"


class DomainAbuseTaxonomyDomainAccessMethodEntry(str, Enum):
    CRIMINAL_REGISTRATION = "criminal-registration"
    COMPROMISED_WEBSERVER = "compromised-webserver"
    COMPROMISED_DNS = "compromised-dns"
    SINKHOLE = "sinkhole"
    COMPROMISED_DOMAIN_NAME_REGISTRAR = "compromised-domain-name-registrar"
    COMPROMISED_DOMAIN_NAME_REGISTRY = "compromised-domain-name-registry"


class DomainAbuseTaxonomy(BaseModel):
    """Model for the Domain Name Abuse taxonomy."""

    namespace: str = "domain-abuse"
    description: str = """Domain Name Abuse - taxonomy to tag domain names used for cybercrime."""
    version: int = 2
    exclusive: bool = False
    predicates: List[DomainAbuseTaxonomyPredicate] = []
    domain_status_entries: List[DomainAbuseTaxonomyDomainStatusEntry] = []
    domain_access_method_entries: List[DomainAbuseTaxonomyDomainAccessMethodEntry] = []

    @classmethod
    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:
        """Get the full tag for a predicate and optional entry."""
        if entry:
            return f"{cls.namespace}:{predicate}='{entry}'"
        return f"{cls.namespace}:{predicate}"
