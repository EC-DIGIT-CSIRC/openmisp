from datetime import datetime
from typing import List, Optional, Union
from uuid import uuid4

from pydantic import BaseModel, ConfigDict
from pymisp import MISPAttribute, MISPObjectAttribute, MISPOrganisation, MISPSighting, PyMISP

from .models import SightingType
from .validators import validate_client, validate_datetime, validate_entity_type, validate_same_type, validate_string


class SightingCriteria(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    value: Optional[str] = None
    uuid: Optional[str] = None
    source: Optional[str] = None
    type: Optional[SightingType] = None


class SightingService:
    def __init__(self, client: PyMISP):
        validate_client(client)
        self._client = client

    def create(
        self,
        *,
        attribute: MISPAttribute,
        type: SightingType,
        timestamp: datetime,
        source: str,
    ) -> MISPSighting:
        validate_entity_type(attribute, MISPAttribute)
        validate_string(source)
        validate_entity_type(type, SightingType)
        validate_datetime(timestamp, require_timezone=True)

        sighting = MISPSighting()
        sighting.uuid = str(uuid4())
        sighting.value = attribute.value
        sighting.attribute_uuid = attribute.uuid
        sighting.type = type.value
        sighting.date_sighting = int(timestamp.timestamp())
        sighting.source = source

        return sighting

    def edit(
        self,
        sighting: MISPSighting,
        *,
        attribute: Optional[MISPAttribute] = None,
        type: Optional[SightingType] = None,
        timestamp: Optional[datetime] = None,
        source: Optional[MISPOrganisation] = None,
    ) -> bool:
        validate_entity_type(sighting, MISPSighting)

        if attribute is not None:
            sighting.attribute_uuid = attribute.uuid
        if source is not None:
            sighting.source = source.name
        if type is not None:
            sighting.type = type.value
        if timestamp is not None:
            validate_datetime(timestamp)
            sighting.date_sighting = int(timestamp.timestamp())

        return True

    def list(
        self, attribute: Union[MISPAttribute, MISPObjectAttribute], criteria: SightingCriteria
    ) -> List[MISPSighting]:
        validate_entity_type(attribute, (MISPAttribute, MISPObjectAttribute))
        validate_entity_type(criteria, SightingCriteria)

        if not hasattr(attribute, "Sighting") or not attribute.Sighting:
            return []

        sightings = attribute.Sighting

        if criteria.value:
            sightings = [s for s in sightings if s.value == criteria.value]

        if criteria.uuid:
            sightings = [s for s in sightings if s.uuid == criteria.uuid]

        if criteria.source:
            sightings = [s for s in sightings if s.source == criteria.source]

        if criteria.type:
            sightings = [s for s in sightings if s.type == criteria.type]

        return sightings

    def get(
        self, attribute: Union[MISPAttribute, MISPObjectAttribute], criteria: SightingCriteria
    ) -> Optional[MISPSighting]:
        validate_entity_type(attribute, (MISPAttribute, MISPObjectAttribute))
        return next((sighting for sighting in self.list(attribute, criteria)), None)

    def exists(self, attribute: Union[MISPAttribute, MISPObjectAttribute], criteria: SightingCriteria) -> bool:
        validate_entity_type(attribute, (MISPAttribute, MISPObjectAttribute))
        return self.get(attribute, criteria) is not None

    def _parent_link(self, entity: Union[MISPObjectAttribute, MISPAttribute], sighting: MISPSighting) -> bool:
        validate_entity_type(entity, (MISPObjectAttribute, MISPAttribute))
        validate_entity_type(sighting, MISPSighting)

        self._parent_unlink(entity, sighting)

        entity.sightings.append(sighting)
        entity.edited = True
        return True

    def _parent_unlink(self, entity: Union[MISPObjectAttribute, MISPAttribute], sighting: MISPSighting) -> bool:
        validate_entity_type(entity, (MISPObjectAttribute, MISPAttribute))
        validate_entity_type(sighting, MISPSighting)

        for index, _sighting in enumerate(entity.sightings):
            if _sighting.uuid == sighting.uuid:
                entity.sightings.pop(index)
                entity.edited = True
                return True

        return False

    def _parent_sync(
        self, current: Union[MISPObjectAttribute, MISPAttribute], new: Union[MISPObjectAttribute, MISPAttribute]
    ) -> bool:
        validate_same_type(current, new)
        validate_entity_type(current, (MISPObjectAttribute, MISPAttribute))
        validate_entity_type(new, (MISPObjectAttribute, MISPAttribute))

        current_sighting_uuids = {sighting.uuid for sighting in current.sightings}
        new_sighting_uuids = {sighting.uuid for sighting in new.sightings}

        for current_sighting in current.sightings:
            if current_sighting.uuid not in new_sighting_uuids:
                self._client.delete_sighting(current_sighting)

        for sighting in new.sightings:
            if sighting.uuid not in current_sighting_uuids:
                self._client.add_sighting(sighting)

    def _list(self, criteria: Optional[SightingCriteria] = None) -> List[MISPSighting]:
        validate_entity_type(criteria, SightingCriteria)

        search_params = {}

        if criteria.value:
            search_params["value"] = criteria.value

        if criteria.uuid:
            search_params["uuid"] = criteria.uuid

        if criteria.source:
            search_params["source"] = criteria.source

        if criteria.type:
            search_params["type"] = criteria.type

        try:
            return self._client.search_sightings(search_params)
        except Exception:
            return []
