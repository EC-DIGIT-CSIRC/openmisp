"""Utility functions for working with taxonomies."""

import re
from enum import Enum
from typing import Dict, List, Optional, Type, TypeVar

from pydantic import BaseModel

# Type variable for taxonomy classes
T = TypeVar("T", bound=BaseModel)


def sanitize_name(name: str) -> str:
    """Sanitize a name to be a valid Python identifier."""
    # Replace non-alphanumeric characters with underscores
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    # Ensure the name starts with a letter
    if not name[0].isalpha():
        name = "t_" + name
    # Convert to snake_case
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name).lower()
    return name


def camel_case(name: str) -> str:
    """Convert a string to CamelCase."""
    # First convert to snake_case to handle any existing separators
    snake = sanitize_name(name)
    # Then convert to CamelCase
    return "".join(word.capitalize() for word in snake.split("_"))


def get_all_taxonomies() -> List[Type[BaseModel]]:
    """Get all taxonomy classes defined in the package."""
    from . import __dict__ as module_dict

    taxonomies = []
    for name, obj in module_dict.items():
        if (
            isinstance(obj, type)
            and issubclass(obj, BaseModel)
            and obj.__name__.endswith("Taxonomy")
            and obj.__module__.startswith("openmisp.models.taxonomies.")
        ):
            taxonomies.append(obj)

    return taxonomies


def get_taxonomy_by_namespace(namespace: str) -> Type[BaseModel]:
    """Get a taxonomy class by its namespace."""
    for taxonomy_class in get_all_taxonomies():
        if hasattr(taxonomy_class, "namespace") and taxonomy_class.namespace == namespace:
            return taxonomy_class

    raise ValueError(f"Taxonomy with namespace '{namespace}' not found")


def get_taxonomy_from_tag(tag: str) -> Type[BaseModel]:
    """Get a taxonomy class from a tag."""
    if ":" not in tag:
        raise ValueError(f"Invalid tag format: {tag}")

    namespace = tag.split(":", 1)[0]
    return get_taxonomy_by_namespace(namespace)


def parse_tag(tag: str) -> Dict[str, str]:
    """Parse a tag into its namespace, predicate, and optional entry."""
    if ":" not in tag:
        raise ValueError(f"Invalid tag format: {tag}")

    namespace, rest = tag.split(":", 1)

    if "=" in rest:
        predicate, entry = rest.split("=", 1)
        # Remove quotes if present
        if (entry.startswith("'") and entry.endswith("'")) or (entry.startswith('"') and entry.endswith('"')):
            entry = entry[1:-1]
        return {"namespace": namespace, "predicate": predicate, "entry": entry}

    return {"namespace": namespace, "predicate": rest}


def is_valid_tag(tag: str) -> bool:
    """Check if a tag is valid for any taxonomy."""
    try:
        parsed = parse_tag(tag)
        taxonomy_class = get_taxonomy_by_namespace(parsed["namespace"])

        # Check if the predicate is valid
        predicate = parsed["predicate"]
        predicate_valid = False

        # Check in predicate enum if it exists
        predicate_enum = None
        for attr_name in dir(taxonomy_class):
            attr = getattr(taxonomy_class, attr_name)
            if isinstance(attr, type) and issubclass(attr, Enum) and attr.__name__.endswith("Predicate"):
                predicate_enum = attr
                break

        if predicate_enum:
            predicate_valid = any(member.value == predicate for member in predicate_enum)

        if not predicate_valid:
            return False

        # If there's an entry, check if it's valid
        if "entry" in parsed:
            entry = parsed["entry"]
            entry_valid = False

            # Find the entry enum for this predicate
            entry_enum = None
            predicate_class_name = camel_case(predicate)
            entry_class_name = f"{taxonomy_class.__name__}{predicate_class_name}Entry"

            for attr_name in dir(taxonomy_class.__module__):
                if attr_name == entry_class_name:
                    attr = getattr(taxonomy_class.__module__, attr_name)
                    if isinstance(attr, type) and issubclass(attr, Enum):
                        entry_enum = attr
                        break

            if entry_enum:
                entry_valid = any(member.value == entry for member in entry_enum)
                return entry_valid

        return True
    except (ValueError, IndexError):
        return False


def get_predicate_entries(taxonomy_class: Type[BaseModel], predicate: str) -> List[str]:
    """Get all valid entries for a predicate in a taxonomy."""
    # Format the predicate name properly for the class name
    predicate_class_name = camel_case(predicate)
    entry_class_name = f"{taxonomy_class.__name__}{predicate_class_name}Entry"

    # Find the entry enum for this predicate
    entry_enum = None
    for attr_name in dir(taxonomy_class.__module__):
        if attr_name == entry_class_name:
            attr = getattr(taxonomy_class.__module__, attr_name)
            if isinstance(attr, type) and issubclass(attr, Enum):
                entry_enum = attr
                break

    if entry_enum:
        return [member.value for member in entry_enum]

    return []


def build_tag(namespace: str, predicate: str, entry: Optional[str] = None) -> str:
    """Build a tag from its components."""
    if entry:
        return f"{namespace}:{predicate}='{entry}'"
    return f"{namespace}:{predicate}"
