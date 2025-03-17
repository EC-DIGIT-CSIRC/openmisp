import logging

import urllib3
from pymisp import (
    MISPAttribute,
    MISPEvent,
    MISPGalaxy,
    MISPObject,
    MISPOrganisation,
    MISPSharingGroup,
    MISPSighting,
    MISPTag,
    PyMISP,
)

from .attributes import AttributeCriteria, AttributeService
from .clusters import ClusterCriteria, ClusterService
from .events import EventCriteria, EventService
from .galaxies import GalaxyCriteria, GalaxyService
from .objects import ObjectCriteria, ObjectService
from .organizations import OrganizationCriteria, OrganizationService
from .server import ServerService
from .sharing_groups import SharingGroupCriteria, SharingGroupService
from .sightings import SightingCriteria, SightingService
from .tags import TagCriteria, TagService
from .validators import validate_entity_type

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)
logging.getLogger("pymisp").addHandler(logging.NullHandler())


class MISP:
    def __init__(self, url: str, key: str, ssl: bool):
        self.client = PyMISP(url=url, key=key, ssl=ssl)
        self.events = EventService(self.client)
        self.objects = ObjectService(self.client)
        self.attributes = AttributeService(self.client)
        self.tags = TagService(self.client)
        self.galaxies = GalaxyService(self.client)
        self.clusters = ClusterService(self.client)
        self.organizations = OrganizationService(self.client)
        self.sharing_groups = SharingGroupService(self.client)
        self.sightings = SightingService(self.client)
        self.server = ServerService(self.client)

    def sync(self, event: MISPEvent) -> bool:
        validate_entity_type(event, MISPEvent)
        criteria = EventCriteria(uuid=event.uuid)
        current_event = self.get(criteria)
        return self.events._parent_sync(current_event, event)

    def delete(self, event: MISPEvent) -> bool:
        validate_entity_type(event, MISPEvent)
        self.client.delete_event(event.uuid)

    def list(
        self,
        criteria: EventCriteria
        | ObjectCriteria
        | AttributeCriteria
        | GalaxyCriteria
        | ClusterCriteria
        | TagCriteria
        | SharingGroupCriteria
        | OrganizationCriteria
        | SightingCriteria
        | None = None,
    ) -> list[
        MISPEvent
        | MISPObject
        | MISPAttribute
        | MISPGalaxy
        | MISPTag
        | MISPSharingGroup
        | MISPOrganisation
        | MISPSighting
    ]:
        if criteria is None:
            return list(self.events._list())

        if isinstance(criteria, EventCriteria):
            return list(self.events._list(criteria))
        elif isinstance(criteria, ObjectCriteria):
            return list(self.objects._list(criteria))
        elif isinstance(criteria, AttributeCriteria):
            return list(self.attributes._list(criteria))
        elif isinstance(criteria, ClusterCriteria):
            return list(self.clusters._list(criteria))
        elif isinstance(criteria, GalaxyCriteria):
            return list(self.galaxies._list(criteria))
        elif isinstance(criteria, TagCriteria):
            return list(self.tags._list(criteria))
        elif isinstance(criteria, SharingGroupCriteria):
            return list(self.sharing_groups._list(criteria))
        elif isinstance(criteria, OrganizationCriteria):
            return list(self.organizations._list(criteria))
        elif isinstance(criteria, SightingCriteria):
            return list(self.sightings._list(criteria))
        else:
            raise ValueError("Invalid criteria type.")

    def get(
        self,
        criteria: EventCriteria
        | ObjectCriteria
        | AttributeCriteria
        | GalaxyCriteria
        | ClusterCriteria
        | TagCriteria
        | SharingGroupCriteria
        | OrganizationCriteria
        | SightingCriteria,
    ) -> (
        MISPEvent
        | MISPObject
        | MISPAttribute
        | MISPGalaxy
        | MISPTag
        | MISPSharingGroup
        | MISPOrganisation
        | MISPSighting
        | None
    ):
        results = self.list(criteria)
        if isinstance(results, list):
            return results[0] if results else None
        return next(iter(results), None)

    def exists(
        self,
        criteria: EventCriteria
        | ObjectCriteria
        | AttributeCriteria
        | ClusterCriteria
        | TagCriteria
        | SharingGroupCriteria
        | OrganizationCriteria
        | SightingCriteria,
    ) -> bool:
        return self.get(criteria) is not None
