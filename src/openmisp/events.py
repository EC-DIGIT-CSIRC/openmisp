from datetime import datetime
from typing import Generator, Optional

from pydantic import BaseModel, ConfigDict
from pymisp import (
    MISPAttribute,
    MISPEvent,
    MISPGalaxyCluster,
    MISPObject,
    MISPOrganisation,
    MISPSharingGroup,
    MISPSighting,
    MISPTag,
    PyMISP,
)

from .attributes import AttributeService
from .clusters import ClusterService
from .models import Analysis, Distribution, ThreatLevel
from .objects import ObjectService
from .tags import TagService
from .validators import (
    validate_boolean,
    validate_client,
    validate_criteria_type,
    validate_datetime,
    validate_distribution_sharing_group,
    validate_entity_type,
    validate_required_parameter,
    validate_same_type,
    validate_string,
)


class EventCriteria(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    uuid: str | None = None
    info: str | None = None
    published: bool | None = None
    sharing_group: MISPSharingGroup | None = None
    distribution: Distribution | None = None
    threat_level: ThreatLevel | None = None
    analysis: Analysis | None = None
    organization: MISPOrganisation | None = None
    tags: list[str] | None = None


class EventService:
    """Service for managing MISP events.

    This service provides methods for creating, retrieving, updating, and deleting
    MISP events, as well as linking and unlinking entities to events.

    Attributes:
        _client: The PyMISP client instance.
        _attributes_service: The attributes service instance.
        _objects_service: The objects service instance.
        _tags_service: The tags service instance.
        _clusters_service: The clusters service instance.
    """

    def __init__(self, client: PyMISP):
        validate_client(client, raise_error=True)
        self._client = client
        self._attributes_service = AttributeService(client)
        self._objects_service = ObjectService(client)
        self._tags_service = TagService(client)
        self._clusters_service = ClusterService(client)

    def create(
        self,
        *,
        info: str,
        published: bool,
        distribution: Distribution,
        threat_level: ThreatLevel,
        analysis: Analysis,
        organization: MISPOrganisation | None = None,
        sharing_group: MISPSharingGroup | None = None,
        date: datetime | None = None,
        attributes: list[MISPAttribute] | None = None,
        objects: list[MISPObject] | None = None,
    ) -> MISPEvent:
        """Create a new MISP event.

        Args:
            info: Event description.
            published: Whether the event is published.
            distribution: Distribution level enum.
            threat_level: Threat level enum.
            analysis: Analysis state enum.
            organization: Organization creating the event.
            sharing_group: Sharing group for the event.
            date: Event date.
            attributes: List of attributes to link to the event.
            objects: List of objects to link to the event.

        Returns:
            The created MISP event object.

        Raises:
            MISPValidationError: If the event data is invalid.
            MISPError: If there's an error communicating with the MISP server.
        """
        validate_required_parameter(info, "info")
        validate_required_parameter(published, "published")
        validate_required_parameter(distribution, "distribution")
        validate_required_parameter(threat_level, "threat_level")
        validate_required_parameter(analysis, "analysis")

        validate_string(info, "info", raise_error=True)
        validate_boolean(published, "published", raise_error=True)
        validate_entity_type(distribution, Distribution, "distribution", raise_error=True)
        validate_entity_type(threat_level, ThreatLevel, "threat_level", raise_error=True)
        validate_entity_type(analysis, Analysis, "analysis", raise_error=True)
        validate_entity_type(organization, MISPOrganisation, "organization", raise_error=True)
        validate_entity_type(sharing_group, MISPSharingGroup, "sharing_group", raise_error=True)
        validate_datetime(date, "date", raise_error=True)
        validate_distribution_sharing_group(distribution, sharing_group, raise_error=True)

        event = MISPEvent()
        event.info = info
        event.published = published
        event.distribution = distribution.value
        event.threat_level_id = threat_level.value
        event.analysis = analysis.value
        if organization is not None:
            event.orgc_id = organization.id
        if sharing_group is not None:
            event.sharing_group_id = sharing_group.id
        if date is not None:
            event.date = date

        if attributes:
            for attribute in attributes:
                self._attributes_service._parent_link(event, attribute)

        if objects:
            for obj in objects:
                self._objects_service._parent_link(event, obj)

        return event

    def edit(
        self,
        event: MISPEvent,
        *,
        info: Optional[str] = None,
        published: Optional[bool] = None,
        distribution: Optional[Distribution] = None,
        sharing_group: Optional[MISPSharingGroup] = None,
        threat_level: Optional[ThreatLevel] = None,
        analysis: Optional[Analysis] = None,
        organization: Optional[MISPOrganisation] = None,
        date: Optional[datetime] = None,
    ) -> bool:
        validate_entity_type(event, MISPEvent, "event", raise_error=True)

        validate_string(info, "info", raise_error=True)
        validate_boolean(published, "published", raise_error=True)
        validate_entity_type(distribution, Distribution, "distribution", raise_error=True)
        validate_entity_type(sharing_group, MISPSharingGroup, "sharing_group", raise_error=True)
        validate_entity_type(threat_level, ThreatLevel, "threat_level", raise_error=True)
        validate_entity_type(analysis, Analysis, "analysis", raise_error=True)
        validate_entity_type(organization, MISPOrganisation, "organization", raise_error=True)
        validate_datetime(date, "date", raise_error=True)

        if info is not None:
            event.info = info

        if published is not None:
            event.published = published

        if distribution is not None:
            event.distribution = distribution.value

        if threat_level is not None:
            event.threat_level_id = threat_level.value

        if analysis is not None:
            event.analysis = analysis.value

        if organization is not None:
            event.orgc_id = organization.id

        if sharing_group is not None:
            event.sharing_group_id = sharing_group.id

        if date is not None:
            event.date = date

        if distribution is not None or sharing_group is not None:
            current_distribution = (
                distribution or Distribution(event.distribution) if hasattr(event, "distribution") else None
            )
            current_sharing_group = sharing_group or event.sharing_group if hasattr(event, "sharing_group") else None

            if current_distribution and (current_distribution == Distribution.SHARING_GROUP) != bool(
                current_sharing_group
            ):
                validate_distribution_sharing_group(current_distribution, current_sharing_group, raise_error=True)

        return True

    def link(
        self, event: MISPEvent, entity: MISPAttribute | MISPObject | MISPGalaxyCluster | MISPTag | MISPSighting
    ) -> bool:
        validate_entity_type(event, MISPEvent, "event", raise_error=True)
        validate_entity_type(
            entity, (MISPAttribute, MISPObject, MISPGalaxyCluster, MISPTag, MISPSighting), "entity", raise_error=True
        )

        if isinstance(entity, MISPAttribute):
            return self._attributes_service._parent_link(event, entity)

        if isinstance(entity, MISPObject):
            return self._objects_service._parent_link(event, entity)

        return False

    def unlink(
        self, event: MISPEvent, entity: MISPAttribute | MISPObject | MISPGalaxyCluster | MISPTag | MISPSighting
    ) -> bool:
        validate_entity_type(event, MISPEvent, "event", raise_error=True)
        validate_entity_type(
            entity, (MISPAttribute, MISPObject, MISPGalaxyCluster, MISPTag, MISPSighting), "entity", raise_error=True
        )

        if isinstance(entity, MISPAttribute):
            return self._attributes_service._parent_unlink(event, entity)

        if isinstance(entity, MISPObject):
            return self._objects_service._parent_unlink(event, entity)

        return False

    def _parent_sync(self, current: MISPEvent | None = None, new: MISPEvent | None = None) -> bool:
        if current is None:
            result = self._sync_create(new)
            self._publish(new)
        else:
            result = self._sync_update(current, new)
            self._publish(new)

        return result

    def _sync_create(self, new: MISPEvent) -> bool:
        validate_entity_type(new, MISPEvent, "new", raise_error=True)
        return self._client.add_event(new, pythonify=True)

    def _sync_update(self, current: MISPEvent, new: MISPEvent) -> bool:
        validate_entity_type(current, MISPEvent, "current", raise_error=True)
        validate_entity_type(new, MISPEvent, "new", raise_error=True)
        validate_same_type(current, new, raise_error=True)

        self._attributes_service._parent_sync(current, new)
        self._objects_service._parent_sync(current, new)
        return self._client.update_event(current.uuid, new, pythonify=True)

    def _create(self, event: MISPEvent) -> bool:
        validate_entity_type(event, MISPEvent, "event", raise_error=True)
        return self._sync_create(event)

    def _update(self, event: MISPEvent) -> bool:
        validate_entity_type(event, MISPEvent, "event", raise_error=True)
        return self._client.update_event(event.uuid, event, pythonify=True)

    def _publish(self, event: MISPEvent) -> bool:
        validate_entity_type(event, MISPEvent, "event", raise_error=True)
        return self._client.publish(event.uuid)

    def _list(self, criteria: EventCriteria | None = None) -> Generator[MISPEvent, None, None]:
        if criteria is not None:
            validate_criteria_type(criteria, EventCriteria, raise_error=True)

        parameters = dict(page=1, limit=100, sort="publish_timestamp", pythonify=True)
        if criteria:
            if criteria.info:
                parameters["eventinfo"] = criteria.info
            if criteria.sharing_group:
                parameters["sharing_group_id"] = criteria.sharing_group.id
            if criteria.distribution:
                parameters["distribution"] = criteria.distribution.value
            if criteria.threat_level:
                parameters["threat_level_id"] = criteria.threat_level.value
            if criteria.organization:
                parameters["org"] = criteria.organization.id
            if criteria.tags:
                parameters["tags"] = criteria.tags
            if criteria.published:
                parameters["published"] = criteria.published

        if criteria and criteria.uuid:
            event = self._client.get_event(criteria.uuid, pythonify=True)
            if "errors" in event:
                return

            yield event
            return

        while True:
            events_metadata = self._client.search_index(**parameters)

            if len(events_metadata) == 0:
                break

            for metadata in events_metadata:
                event = self._client.get_event(metadata.uuid, pythonify=True)
                yield event

            parameters["page"] += 1

        return
