from datetime import datetime
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict
from pymisp import (
    MISPAttribute,
    MISPEvent,
    MISPGalaxyCluster,
    MISPObject,
    MISPObjectAttribute,
    MISPSharingGroup,
    MISPSighting,
    MISPTag,
    PyMISP,
)

from .clusters import ClusterService
from .models import AttributeCategory, AttributeType, Distribution, ObjectRelation
from .sightings import SightingService
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
    validate_type_for_category,
)


class AttributeCriteria(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    uuid: Optional[str] = None
    type: Optional[AttributeType] = None
    value: Optional[str] = None
    comment: Optional[str] = None
    detection: Optional[bool] = None
    correlation: Optional[bool] = None


class AttributeService:
    def __init__(self, client: PyMISP):
        validate_client(client, raise_error=True)

        self._client = client
        self._tags_service = TagService(client)
        self._clusters_service = ClusterService(client)
        self._sightings_service = SightingService(client)

    def create(
        self,
        *,
        type: AttributeType,
        category: AttributeCategory,
        value: str,
        detection: bool,
        correlation: bool = False,
        first_seen: Optional[datetime] = None,
        last_seen: Optional[datetime] = None,
        sharing_group: Optional[MISPSharingGroup] = None,
        distribution: Optional[Distribution] = None,
        comment: Optional[str] = None,
        relation: Optional[ObjectRelation] = None,
    ) -> Union[MISPAttribute, MISPObjectAttribute]:
        validate_required_parameter(type, "type")
        validate_required_parameter(category, "category")
        validate_required_parameter(value, "value")
        validate_required_parameter(detection, "detection")
        validate_required_parameter(correlation, "correlation")

        validate_entity_type(type, AttributeType, "type", raise_error=True)
        validate_entity_type(category, AttributeCategory, "category", raise_error=True)
        validate_entity_type(relation, ObjectRelation, "relation", raise_error=True)
        validate_type_for_category(category, type, raise_error=True)
        validate_string(value, "value", raise_error=True)
        validate_string(comment, "comment", raise_error=True)
        validate_boolean(detection, "detection", raise_error=True)
        validate_boolean(correlation, "correlation", raise_error=True)
        validate_datetime(first_seen, "first_seen", raise_error=True)
        validate_datetime(last_seen, "last_seen", raise_error=True)
        validate_distribution_sharing_group(distribution, sharing_group, raise_error=True)

        if relation is not None and (distribution is not None or sharing_group is not None):
            raise ValueError("Distribution and sharing group must not be set for Object Attributes.")

        if relation is None:
            attribute = MISPAttribute()
        else:
            attribute = MISPObjectAttribute({})
            attribute.object_relation = relation.value

        attribute.type = type.value
        attribute.value = value
        attribute.comment = comment
        attribute.to_ids = detection
        attribute.disable_correlation = not correlation

        if sharing_group is not None and not isinstance(attribute, MISPObjectAttribute):
            attribute.sharing_group_id = sharing_group.id

        if distribution is not None and not isinstance(attribute, MISPObjectAttribute):
            attribute.distribution = distribution.value

        if category:
            attribute.category = category.value

        if first_seen is not None:
            attribute.first_seen = first_seen

        if last_seen is not None:
            attribute.last_seen = last_seen

        return attribute

    def edit(
        self,
        attribute: Union[MISPAttribute, MISPObjectAttribute],
        *,
        type: Optional[AttributeType] = None,
        category: Optional[AttributeCategory] = None,
        value: Optional[str] = None,
        first_seen: Optional[datetime] = None,
        last_seen: Optional[datetime] = None,
        sharing_group: Optional[MISPSharingGroup] = None,
        distribution: Optional[Distribution] = None,
        comment: Optional[str] = None,
        detection: Optional[bool] = None,
        correlation: Optional[bool] = None,
        relation: Optional[ObjectRelation] = None,
    ) -> bool:
        validate_entity_type(attribute, (MISPAttribute, MISPObjectAttribute), "attribute", raise_error=True)
        validate_entity_type(type, AttributeType, "type", raise_error=True)
        validate_entity_type(category, AttributeCategory, "category", raise_error=True)
        validate_entity_type(distribution, Distribution, "distribution", raise_error=True)
        validate_entity_type(sharing_group, MISPSharingGroup, "sharing_group", raise_error=True)
        validate_entity_type(relation, ObjectRelation, "relation", raise_error=True)
        validate_string(value, "value", raise_error=True)
        validate_string(comment, "comment", raise_error=True)
        validate_boolean(detection, "detection", raise_error=True)
        validate_boolean(correlation, "correlation", raise_error=True)
        validate_datetime(first_seen, "first_seen", raise_error=True)
        validate_datetime(last_seen, "last_seen", raise_error=True)

        if isinstance(attribute, MISPObjectAttribute) and (distribution is not None or sharing_group is not None):
            raise ValueError("Distribution and sharing group must not be set for Object Attributes.")

        if isinstance(attribute, MISPAttribute) and (relation is not None):
            raise ValueError("Relation must not be set for Attributes.")

        if relation is not None and isinstance(attribute, MISPObjectAttribute):
            attribute.object_relation = relation.value

        if type is not None:
            attribute.type = type.value

        if category is not None:
            attribute.category = category.value

        if value is not None:
            attribute.value = value

        if first_seen is not None:
            attribute.first_seen = first_seen

        if last_seen is not None:
            attribute.last_seen = last_seen

        if comment is not None:
            attribute.comment = comment

        if detection is not None:
            attribute.to_ids = detection

        if correlation is not None:
            attribute.disable_correlation = not correlation

        if distribution is not None and not isinstance(attribute, MISPObjectAttribute):
            attribute.distribution = distribution.value

        if sharing_group is not None and not isinstance(attribute, MISPObjectAttribute):
            attribute.sharing_group_id = sharing_group.id

        _distribution = None
        if hasattr(attribute, "distribution"):
            _distribution = Distribution(attribute.distribution)

        _sharing_group = None
        if hasattr(attribute, "sharing_group_id"):
            _sharing_group = MISPSharingGroup()
            _sharing_group.id = attribute.sharing_group_id

        validate_distribution_sharing_group(_distribution, _sharing_group, raise_error=True)

        _category = None
        if hasattr(attribute, "category"):
            _category = AttributeCategory(attribute.category)

        _type = None
        if hasattr(attribute, "type"):
            _type = AttributeType(attribute.type)

        if _category and _type:
            validate_type_for_category(_category, _type, raise_error=True)

        return True

    def list(
        self, entity: Union[MISPEvent, MISPObject], criteria: AttributeCriteria
    ) -> List[Union[MISPAttribute, MISPObjectAttribute]]:
        validate_entity_type(entity, (MISPEvent, MISPObject), "entity", raise_error=True, skip_none=False)
        validate_criteria_type(criteria, AttributeCriteria, raise_error=True)

        attributes = []

        for attr in entity.attributes:
            if criteria.type and attr.type != criteria.type.value:
                continue

            if criteria.value and attr.value != criteria.value:
                continue

            if criteria.comment and attr.comment != criteria.comment:
                continue

            if criteria.detection and attr.to_ids != criteria.detection:
                continue

            if criteria.correlation and attr.disable_correlation != criteria.correlation:
                continue

            if criteria.uuid and attr.uuid != criteria.uuid:
                continue

            attributes.append(attr)

        return attributes

    def get(
        self, entity: Union[MISPEvent, MISPObject], criteria: AttributeCriteria
    ) -> Optional[Union[MISPAttribute, MISPObjectAttribute]]:
        validate_entity_type(entity, (MISPEvent, MISPObject), "entity", raise_error=True, skip_none=False)
        validate_criteria_type(criteria, AttributeCriteria, raise_error=True)

        attributes = self.list(entity, criteria)
        if attributes:
            return attributes[0]
        return None

    def exists(self, entity: Union[MISPEvent, MISPObject], criteria: AttributeCriteria) -> bool:
        validate_entity_type(entity, (MISPEvent, MISPObject), "entity", raise_error=True, skip_none=False)
        validate_criteria_type(criteria, AttributeCriteria, raise_error=True)

        return bool(self.get(entity, criteria))

    def link(
        self,
        attribute: Union[MISPAttribute, MISPObjectAttribute],
        entity: Union[MISPGalaxyCluster, MISPTag, MISPSighting],
    ) -> bool:
        validate_entity_type(
            attribute, (MISPAttribute, MISPObjectAttribute), "attribute", raise_error=True, skip_none=False
        )
        validate_entity_type(
            entity, (MISPGalaxyCluster, MISPTag, MISPSighting), "entity", raise_error=True, skip_none=False
        )

        if isinstance(entity, MISPGalaxyCluster):
            return self._clusters_service._parent_link(attribute, entity)

        if isinstance(entity, MISPTag):
            return self._tags_service._parent_link(attribute, entity)

        if isinstance(entity, MISPSighting):
            return self._sightings_service._parent_link(attribute, entity)

        return False

    def unlink(
        self,
        attribute: Union[MISPAttribute, MISPObjectAttribute],
        entity: Union[MISPGalaxyCluster, MISPTag, MISPSighting],
    ) -> bool:
        validate_entity_type(
            attribute, (MISPAttribute, MISPObjectAttribute), "attribute", raise_error=True, skip_none=False
        )
        validate_entity_type(
            entity, (MISPGalaxyCluster, MISPTag, MISPSighting), "entity", raise_error=True, skip_none=False
        )

        if isinstance(entity, MISPGalaxyCluster):
            return self._clusters_service._parent_unlink(attribute, entity)

        if isinstance(entity, MISPTag):
            return self._tags_service._parent_unlink(attribute, entity)

        if isinstance(entity, MISPSighting):
            return self._sightings_service._parent_unlink(attribute, entity)

        return False

    def _parent_link(
        self, entity: Union[MISPEvent, MISPObject], attribute: Union[MISPAttribute, MISPObjectAttribute]
    ) -> bool:
        validate_entity_type(entity, (MISPEvent, MISPObject), "entity", raise_error=True, skip_none=False)
        validate_entity_type(
            attribute, (MISPAttribute, MISPObjectAttribute), "attribute", raise_error=True, skip_none=False
        )

        if isinstance(entity, MISPEvent) and not isinstance(attribute, MISPAttribute):
            raise ValueError("Only Attributes can be linked to Events.")

        if isinstance(entity, MISPObject) and not isinstance(attribute, MISPObjectAttribute):
            raise ValueError("Only Object Attributes can be linked to Objects.")

        self._parent_unlink(entity, attribute)
        entity.attributes.append(attribute)
        entity.edited = True
        return True

    def _parent_unlink(
        self, entity: Union[MISPEvent, MISPObject], attribute: Union[MISPAttribute, MISPObjectAttribute]
    ) -> bool:
        validate_entity_type(entity, (MISPEvent, MISPObject), "entity", raise_error=True, skip_none=False)
        validate_entity_type(
            attribute, (MISPAttribute, MISPObjectAttribute), "attribute", raise_error=True, skip_none=False
        )

        if isinstance(entity, MISPEvent) and not isinstance(attribute, MISPAttribute):
            raise ValueError("Only Attributes can be unlinked from Events.")

        if isinstance(entity, MISPObject) and not isinstance(attribute, MISPObjectAttribute):
            raise ValueError("Only Object Attributes can be unlinked from Objects.")

        for index, _attr in enumerate(entity.attributes):
            if _attr.uuid == attribute.uuid:
                entity.attributes.pop(index)
                entity.edited = True
                return True

        return False

    def _parent_sync(self, current: Union[MISPEvent, MISPObject], new: Union[MISPEvent, MISPObject]) -> None:
        validate_entity_type(current, (MISPEvent, MISPObject), "current", raise_error=True, skip_none=False)
        validate_entity_type(new, (MISPEvent, MISPObject), "new", raise_error=True, skip_none=False)
        validate_same_type(current, new, raise_error=True)

        current_attributes = {attr.uuid: attr for attr in current.attributes}
        new_attributes = {attr.uuid: attr for attr in new.attributes}

        # Delete attributes that are in current but not in new
        for uuid in set(current_attributes.keys()) - set(new_attributes.keys()):
            self._client.delete_attribute(uuid)

        # Update attributes that are in both current and new
        for uuid in set(current_attributes.keys()) & set(new_attributes.keys()):
            self._client.update_attribute(uuid, new_attributes[uuid])

        # Add attributes that are in new but not in current
        for uuid in set(new_attributes.keys()) - set(current_attributes.keys()):
            self._client.add_attribute(current.uuid, new_attributes[uuid], break_on_duplicate=True, pythonify=True)

        # Sync related entities
        for attr in current.attributes:
            if attr.uuid in new_attributes:
                self._tags_service._parent_sync(attr, new_attributes[attr.uuid])
                self._clusters_service._parent_sync(attr, new_attributes[attr.uuid])
                self._sightings_service._parent_sync(attr, new_attributes[attr.uuid])

    def _list(self, criteria: AttributeCriteria) -> List[Union[MISPAttribute, MISPObjectAttribute]]:
        validate_criteria_type(criteria, AttributeCriteria, raise_error=True)

        return self._client.search_attributes(**criteria.dict())
