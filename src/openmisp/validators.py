from typing import Any, List, Optional, Type, Union

from pydantic import BaseModel, ValidationError
from pymisp import MISPObject, MISPObjectAttribute, MISPSharingGroup, PyMISP

from .models import AttributeCategory, AttributeType, Distribution, ObjectRelation, ObjectType
from .models.attributes import CATEGORY_TYPE_MAPPING
from .models.objects import OBJECT_RELATION_ATTRIBUTE_MAPPING


def validate_client(client: Any, raise_error: bool = False) -> bool:
    """
    Validate that the client is an instance of PyMISP.

    Args:
        client: The client to validate
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the client is valid, False otherwise

    Raises:
        ValueError: If the client is not an instance of PyMISP and raise_error is True
    """
    is_valid = isinstance(client, PyMISP)
    if not is_valid and raise_error:
        raise ValueError("Client must be an instance of PyMISP.")
    return is_valid


def validate_type_for_category(category: AttributeCategory, type: AttributeType, raise_error: bool = False) -> bool:
    """
    Validate that an attribute type is allowed for a specific category.

    Args:
        category: The attribute category to validate against
        type: The attribute type to validate
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the type is valid for the category, False otherwise

    Raises:
        ValueError: If the type is not valid for the category and raise_error is True
    """
    if category not in CATEGORY_TYPE_MAPPING:
        if raise_error:
            raise ValueError(f"Category {category.value} is not valid.")
        return False

    is_valid = type in CATEGORY_TYPE_MAPPING[category]
    if not is_valid and raise_error:
        raise ValueError(f"Type {type.value} is not valid for category {category.value}.")
    return is_valid


def validate_relation_type_for_object(
    object_type: ObjectType, relation: ObjectRelation, attribute_type: AttributeType, raise_error: bool = False
) -> bool:
    """
    Validate that the given relation and attribute type are valid for the object type.

    Args:
        object_type: The object type to validate against
        relation: The relation to validate
        attribute_type: The attribute type to validate
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the relation and attribute type are valid for the object type, False otherwise

    Raises:
        ValueError: If the relation and attribute type are not valid for the object type and raise_error is True
    """
    if object_type not in OBJECT_RELATION_ATTRIBUTE_MAPPING:
        if raise_error:
            raise ValueError(f"Object type {object_type.value} is not valid.")
        return False

    object_relations = OBJECT_RELATION_ATTRIBUTE_MAPPING[object_type]
    if relation not in object_relations:
        if raise_error:
            raise ValueError(f"Relation {relation.value} is not valid for object type {object_type.value}.")
        return False

    is_valid = object_relations[relation] == attribute_type
    if not is_valid and raise_error:
        raise ValueError(
            f"Relation {relation.value} with type {attribute_type.value} is not valid for object type {object_type.value}."
        )
    return is_valid


def validate_entity_type(
    entity: Any,
    expected_types: Union[Type, List[Type]],
    param_name: str = "entity",
    skip_none: bool = True,
    raise_error: bool = False,
) -> bool:
    """
    Validate that an entity is of the expected type(s).

    Args:
        entity: The entity to validate
        expected_types: The expected type(s) of the entity
        param_name: The name of the parameter to use in the error message
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the entity is of the expected type(s), False otherwise

    Raises:
        TypeError: If the entity is not of the expected type(s) and raise_error is True
    """
    if not isinstance(expected_types, (list, tuple)):
        expected_types = [expected_types]

    type_names = " or ".join(t.__name__ for t in expected_types)

    if entity is None:
        if skip_none:
            return True

        if raise_error:
            raise TypeError(f"{param_name} must be an instance of {type_names}.")

        return False

    is_valid = any(isinstance(entity, t) for t in expected_types)

    if not is_valid:
        if raise_error:
            raise TypeError(f"{param_name} must be an instance of {type_names}.")

        return False

    return True


def validate_model(model: BaseModel, raise_error: bool = False) -> bool:
    """
    Validate that a model is valid according to its Pydantic schema.

    Args:
        model: The model to validate
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the model is valid, False otherwise

    Raises:
        ValidationError: If the model is not valid and raise_error is True
    """
    if model is None:
        return True

    try:
        model.validate(model.dict())
        return True
    except ValidationError as e:
        if raise_error:
            raise e
        return False


def validate_distribution_sharing_group(
    distribution: Distribution,
    sharing_group: Optional[MISPSharingGroup] = None,
    raise_error: bool = False,
) -> bool:
    """
    Validate that the distribution and sharing group are compatible.

    Args:
        distribution: The distribution to validate
        sharing_group: The sharing group to validate
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the distribution and sharing group are compatible, False otherwise

    Raises:
        ValueError: If the distribution and sharing group are not compatible and raise_error is True
    """
    if distribution is None:
        return True

    # If distribution is set to sharing group, a sharing group must be provided
    if distribution == Distribution.SHARING_GROUP and sharing_group is None:
        if raise_error:
            raise ValueError("Sharing group must be provided when distribution is set to sharing group.")
        return False

    # If distribution is not set to sharing group, a sharing group should not be provided
    if distribution != Distribution.SHARING_GROUP and (sharing_group is not None and sharing_group.id != 0):
        if raise_error:
            raise ValueError("Sharing group should not be provided when distribution is not set to sharing group.")
        return False

    return True


def validate_required_parameter(param: Any, param_name: str, raise_error: bool = True) -> bool:
    """
    Validate that a required parameter is not None.

    Args:
        param: The parameter to validate
        param_name: The name of the parameter to use in the error message
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the parameter is not None, False otherwise

    Raises:
        ValueError: If the parameter is None and raise_error is True
    """
    is_valid = param is not None
    if not is_valid and raise_error:
        raise ValueError(f"{param_name} is required.")
    return is_valid


def validate_criteria_type(
    criteria: Any, expected_type: Type, criteria_name: str = "criteria", raise_error: bool = False
) -> bool:
    """
    Validate that a criteria object is of the expected type.

    Args:
        criteria: The criteria to validate
        expected_type: The expected type of the criteria
        criteria_name: The name of the criteria to use in the error message
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the criteria is of the expected type, False otherwise

    Raises:
        ValueError: If the criteria is not of the expected type and raise_error is True
    """
    if criteria is None:
        return True

    is_valid = isinstance(criteria, expected_type)
    if not is_valid and raise_error:
        raise ValueError(f"{criteria_name} must be an instance of {expected_type.__name__}.")
    return is_valid


def validate_same_type(current: Any, new: Any, error_message: Optional[str] = None, raise_error: bool = False) -> bool:
    """
    Validate that two objects are of the same type.

    Args:
        current: The current object
        new: The new object
        error_message: Optional custom error message
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the objects are of the same type, False otherwise

    Raises:
        ValueError: If the objects are not of the same type and raise_error is True
    """
    if current is None or new is None:
        return True

    is_valid = isinstance(current, type(new))
    if not is_valid and raise_error:
        if error_message:
            raise ValueError(error_message)
        else:
            raise ValueError(f"Cannot sync {type(current).__name__} with {type(new).__name__}.")
    return is_valid


def validate_datetime(
    dt: Any, param_name: str = "datetime", require_timezone: bool = True, raise_error: bool = False
) -> bool:
    """
    Validate that a parameter is a valid datetime object.

    Args:
        dt: The datetime to validate
        param_name: The name of the parameter to use in the error message
        require_timezone: Whether to require the datetime to have a timezone
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the parameter is a valid datetime object, False otherwise

    Raises:
        ValueError: If the parameter is not a valid datetime object and raise_error is True
    """
    if dt is None:
        return True

    from datetime import datetime

    is_valid_type = isinstance(dt, datetime)
    if not is_valid_type:
        if raise_error:
            raise ValueError(f"{param_name} must be a datetime object.")
        return False

    has_timezone = dt.tzinfo is not None
    if require_timezone and not has_timezone:
        if raise_error:
            raise ValueError(f"{param_name} must have a timezone.")
        return False

    return True


def validate_string(value: Any, param_name: str = "string", raise_error: bool = False) -> bool:
    """
    Validate that a parameter is a string.

    Args:
        value: The value to validate
        param_name: The name of the parameter to use in the error message
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the parameter is a string, False otherwise

    Raises:
        ValueError: If the parameter is not a string and raise_error is True
    """
    if value is None:
        return True

    is_valid = isinstance(value, str)
    if not is_valid and raise_error:
        raise ValueError(f"{param_name} must be a string.")
    return is_valid


def validate_boolean(value: Any, param_name: str = "boolean", raise_error: bool = False) -> bool:
    """
    Validate that a parameter is a boolean.

    Args:
        value: The value to validate
        param_name: The name of the parameter to use in the error message
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the parameter is a boolean, False otherwise

    Raises:
        ValueError: If the parameter is not a boolean and raise_error is True
    """
    if value is None:
        return True

    is_valid = isinstance(value, bool)
    if not is_valid and raise_error:
        raise ValueError(f"{param_name} must be a boolean.")
    return is_valid


def validate_list_item_types(
    items: List[Any], expected_type: Type, list_name: str = "list", raise_error: bool = False
) -> bool:
    """
    Validate that all items in a list are of the expected type.

    Args:
        items: The list of items to validate
        expected_type: The expected type of the items
        list_name: The name of the list to use in the error message
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if all items in the list are of the expected type, False otherwise

    Raises:
        ValueError: If any item in the list is not of the expected type and raise_error is True
    """
    if items is None:
        return True

    for i, item in enumerate(items):
        if not isinstance(item, expected_type):
            if raise_error:
                raise ValueError(f"Item at index {i} in {list_name} must be an instance of {expected_type.__name__}.")
            return False

    return True


def validate_attribute_relation_for_object_type(
    attribute: MISPObjectAttribute, obj: MISPObject, raise_error: bool = False
) -> bool:
    """
    Validate that an attribute's relation is valid for an object's type.

    Args:
        attribute: The attribute to validate
        obj: The object to validate against
        raise_error: Whether to raise an error if validation fails

    Returns:
        True if the attribute's relation is valid for the object's type, False otherwise

    Raises:
        ValueError: If the attribute's relation is not valid for the object's type and raise_error is True
    """
    if attribute is None or obj is None:
        return True

    if (
        hasattr(obj, "name")
        and obj.name
        and hasattr(attribute, "relation")
        and attribute.relation
        and hasattr(attribute, "type")
        and attribute.type
    ):
        try:
            object_type = ObjectType(obj.name)
            relation = ObjectRelation(attribute.relation)
            attribute_type = AttributeType(attribute.type)

            return validate_relation_type_for_object(object_type, relation, attribute_type, raise_error)
        except (ValueError, KeyError):
            # If any of the conversions fail, skip validation
            return True

    return True


# Legacy functions for backward compatibility
def validate_client_or_raise(client: Any) -> None:
    """Legacy function for backward compatibility."""
    validate_client(client, raise_error=True)


def validate_entity_type_or_raise(
    entity: Any, expected_types: Union[Type, List[Type]], param_name: str = "entity"
) -> None:
    """Legacy function for backward compatibility."""
    validate_entity_type(entity, expected_types, param_name, raise_error=True)


def validate_model_or_raise(model: BaseModel) -> None:
    """Legacy function for backward compatibility."""
    validate_model(model, raise_error=True)


def validate_distribution_sharing_group_or_raise(
    distribution: Distribution, sharing_group: Optional[MISPSharingGroup] = None
) -> None:
    """Legacy function for backward compatibility."""
    validate_distribution_sharing_group(distribution, sharing_group, raise_error=True)
