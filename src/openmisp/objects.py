from typing import List, Optional

from pydantic import BaseModel, ConfigDict
from pymisp import MISPEvent, MISPObject, MISPObjectAttribute, PyMISP

from .attributes import AttributeService
from .clusters import ClusterService
from .models import Distribution, ObjectType
from .tags import TagService
from .validators import validate_entity_type, validate_string


class ObjectCriteria(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: Optional[str] = None


class ObjectService:
    def __init__(self, client: PyMISP):
        self._client = client
        self._attributes_service = AttributeService(client)
        self._tags_service = TagService(client)
        self._clusters_service = ClusterService(client)

    def create(
        self,
        *,
        type: ObjectType,
        description: Optional[str] = None,
        distribution: Optional[Distribution] = None,
    ) -> MISPObject:
        """Create a new MISP object."""
        validate_entity_type(type, ObjectType, "type", raise_error=True)
        if description is not None:
            validate_string(description)
        if distribution is not None:
            validate_entity_type(distribution, Distribution)

        obj = MISPObject(name=type.value, strict=True, standalone=False)
        if description is not None:
            obj.description = description
        if distribution is not None:
            obj.distribution = distribution.value
        return obj

    def list(self, entity: MISPEvent, criteria: ObjectCriteria) -> List[MISPObject]:
        """List MISP objects."""
        validate_entity_type(entity, MISPEvent, "entity", raise_error=True, skip_none=False)
        validate_entity_type(criteria, ObjectCriteria, "criteria", raise_error=True)

        objects = []
        for obj in entity.objects:
            if criteria.name and obj.name != criteria.name:
                continue
            objects.append(obj)
        return objects

    def get(self, entity: MISPEvent, criteria: ObjectCriteria) -> Optional[MISPObject]:
        """Get a MISP object."""
        validate_entity_type(entity, MISPEvent, "entity", raise_error=True, skip_none=False)
        validate_entity_type(criteria, ObjectCriteria, "criteria", raise_error=True)

        objects = self.list(entity, criteria)
        if objects:
            return objects[0]
        return None

    def exists(self, entity: MISPEvent, criteria: ObjectCriteria) -> bool:
        """Check if a MISP object exists."""
        validate_entity_type(entity, MISPEvent, "entity", raise_error=True, skip_none=False)
        validate_entity_type(criteria, ObjectCriteria, "criteria", raise_error=True)

        return bool(self.get(entity, criteria))

    def link(self, obj: MISPObject, entity: MISPObjectAttribute) -> bool:
        """Link an entity to an object."""
        validate_entity_type(obj, MISPObject, "obj", raise_error=True, skip_none=False)
        validate_entity_type(entity, MISPObjectAttribute, "entity", raise_error=True, skip_none=False)

        return self._attributes_service._parent_link(obj, entity)

    def unlink(self, obj: MISPObject, entity: MISPObjectAttribute) -> bool:
        """Unlink an entity from an object."""
        validate_entity_type(obj, MISPObject, "obj", raise_error=True, skip_none=False)
        validate_entity_type(entity, MISPObjectAttribute, "entity", raise_error=True, skip_none=False)

        return self._attributes_service._parent_unlink(obj, entity)

    def _parent_link(self, entity: MISPEvent, obj: MISPObject) -> bool:
        validate_entity_type(obj, MISPObject, "obj", raise_error=True)
        validate_entity_type(entity, MISPEvent, "entity", raise_error=True)

        self._parent_unlink(entity, obj)
        entity.objects.append(obj)
        entity.edited = True
        return True

    def _parent_unlink(self, entity: MISPEvent, obj: MISPObject) -> bool:
        validate_entity_type(obj, MISPObject, "obj", raise_error=True)
        validate_entity_type(entity, MISPEvent, "entity", raise_error=True)

        for index, _attr in enumerate(entity.objects):
            if _attr.uuid == obj.uuid:
                entity.objects.pop(index)
                entity.edited = True
                return True

        return False

    def _parent_sync(self, current: MISPEvent, new: MISPEvent) -> bool:
        validate_entity_type(current, MISPEvent, "current", raise_error=True)
        validate_entity_type(new, MISPEvent, "new", raise_error=True)

        current_obj_uuids = {obj.uuid for obj in current.objects}
        new_obj_uuids = {obj.uuid for obj in new.objects}

        for current_obj in current.objects:
            if current_obj.uuid not in new_obj_uuids:
                self._client.delete_object(current_obj.uuid)
                continue

            new_obj = next(new_obj for new_obj in new.objects if new_obj.uuid == current_obj.uuid)

            self._attributes_service._parent_sync(current_obj, new_obj)
            self._client.update_object(current_obj.uuid, new_obj, pythonify=True)

        for new_obj in new.objects:
            if new_obj.uuid not in current_obj_uuids:
                self._client.add_object(new, new_obj, break_on_duplicate=True, pythonify=True)

    def _list(self, criteria: ObjectCriteria) -> List[MISPObject]:
        validate_entity_type(criteria, ObjectCriteria, "criteria", raise_error=True)

        return self._client.search_objects(**criteria.dict())
