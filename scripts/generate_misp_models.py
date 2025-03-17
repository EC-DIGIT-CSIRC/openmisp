#!/usr/bin/env python3
"""
Script to generate models and mappings from MISP data.

This script generates:
1. Enums:
   - ObjectType enum from pymisp data/misp-objects/objects directory
   - ObjectRelation enum from pymisp data/misp-objects/objects directory
   - AttributeCategory enum from pymisp data/describeTypes.json
   - AttributeType enum from pymisp data/describeTypes.json

2. Mappings:
   - CATEGORY_TYPE_MAPPING dictionary from pymisp data/describeTypes.json
   - OBJECT_RELATION_ATTRIBUTE_MAPPING dictionary from pymisp data/misp-objects/objects

These generated models and mappings are used by the OpenMISP SDK to provide
type safety and validation when working with MISP data.
"""

import json
import os
import re
from collections import Counter
from pathlib import Path

import pymisp

MODELS_DIR = Path("src/openmisp/models")
OBJECTS_FILE = MODELS_DIR / "objects.py"
ATTRIBUTES_FILE = MODELS_DIR / "attributes.py"
OBJECTS_DIR = Path(pymisp.__path__[0]) / "data/misp-objects/objects"
DESCRIBE_TYPES_FILE = Path(pymisp.__path__[0]) / "data/describeTypes.json"


def format_enum_name(name):
    """Format a string to be a valid enum name in SCREAMING_SNAKE_CASE."""
    # Replace spaces and special characters with underscores
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    # Convert to uppercase
    name = name.upper()
    # Ensure it starts with a letter or underscore
    if name and name[0].isdigit():
        name = f"_{name}"
    return name


def generate_enum_file(file_path, enum_definitions, imports=None, header_comment=None):
    """Generate a file with one or more enum definitions."""
    with open(file_path, "w") as f:
        # Write header comment if provided
        if header_comment:
            f.write(f"# {header_comment}\n\n")

        # Write imports
        if imports:
            for import_line in imports:
                f.write(f"{import_line}\n")
            f.write("\n\n")
        else:
            f.write("from enum import Enum\n\n\n")

        for enum_name, enum_values in enum_definitions.items():
            f.write(f"class {enum_name}(Enum):\n")

            for enum_key, value in sorted(enum_values.items()):
                f.write(f'    {enum_key} = "{value}"\n')

            if enum_name != list(enum_definitions.keys())[-1]:
                f.write("\n\n")


def generate_object_enums():
    """Generate ObjectType and ObjectRelation enums from MISP data."""
    print("Generating ObjectType and ObjectRelation enums...")

    object_types = [d.name for d in OBJECTS_DIR.iterdir() if d.is_dir()]
    object_enum = {"ObjectType": {format_enum_name(obj_type): obj_type for obj_type in object_types}}

    # Collect all unique object relations
    all_relations = set()

    # Iterate through all object directories to collect relations
    for obj_dir in OBJECTS_DIR.iterdir():
        if not obj_dir.is_dir():
            continue

        definition_file = obj_dir / "definition.json"
        if not definition_file.exists():
            continue

        # Read the definition.json file
        with open(definition_file) as f:
            try:
                definition = json.load(f)
            except json.JSONDecodeError:
                continue

        # Get the attributes
        attributes = definition.get("attributes", {})
        if not attributes:
            continue

        # Add each relation to the set of all relations
        for relation in attributes.keys():
            all_relations.add(relation)

    # Create a mapping from relation to enum key
    relation_to_enum_key = {}
    enum_key_counter = Counter()

    # First pass: generate enum keys and handle duplicates
    relation_enum_values = {}

    for relation in sorted(all_relations):
        # Generate the enum key
        enum_key = format_enum_name(relation)

        # If this enum key has been used before, add a suffix
        if enum_key_counter[enum_key] > 0:
            enum_key = f"{enum_key}_{enum_key_counter[enum_key]}"

        # Store the mapping and increment the counter
        relation_to_enum_key[relation] = enum_key
        relation_enum_values[enum_key] = relation
        enum_key_counter[format_enum_name(relation)] += 1

    relation_enum = {"ObjectRelation": relation_enum_values}

    # Combine the enums
    object_enums = {**object_enum, **relation_enum}

    # Define imports for objects.py
    imports = ["from enum import Enum", "from typing import Dict", "from .attributes import AttributeType"]

    # Generate the file with header comment and imports
    generate_enum_file(
        OBJECTS_FILE,
        object_enums,
        imports=imports,
        header_comment="This mapping is automatically generated from MISP data",
    )

    print(f"ObjectType enum saved to {OBJECTS_FILE} ({len(object_types)} types)")
    print(f"ObjectRelation enum saved to {OBJECTS_FILE} ({len(relation_enum_values)} relations)")

    # Generate object relation to attribute type mappings
    generate_object_mappings(relation_to_enum_key)


def generate_object_mappings(relation_to_enum_key):
    """Generate object relation to attribute type mappings from MISP data."""
    print("Generating object relation to attribute type mappings...")

    # Dictionary to store the mappings
    object_mappings = {}

    # Iterate through all object directories
    for obj_dir in OBJECTS_DIR.iterdir():
        if not obj_dir.is_dir():
            continue

        obj_name = obj_dir.name
        definition_file = obj_dir / "definition.json"

        if not definition_file.exists():
            print(f"Warning: No definition.json found for {obj_name}")
            continue

        # Read the definition.json file
        with open(definition_file) as f:
            try:
                definition = json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Invalid JSON in definition.json for {obj_name}")
                continue

        # Get the attributes
        attributes = definition.get("attributes", {})
        if not attributes:
            print(f"Warning: No attributes found for {obj_name}")
            continue

        # Create the mapping for this object
        object_mappings[obj_name] = {}

        # Add each relation and its attribute type to the mapping
        for relation, attr_def in attributes.items():
            misp_type = attr_def.get("misp-attribute")
            if misp_type:
                object_mappings[obj_name][relation] = misp_type

    # Add the mappings to the objects.py file
    with open(OBJECTS_FILE, "a") as f:
        f.write("\n\n# Object relation to attribute type mappings\n")
        f.write("OBJECT_RELATION_ATTRIBUTE_MAPPING: Dict[ObjectType, Dict[ObjectRelation, AttributeType]] = {\n")

        for obj_name, relations in sorted(object_mappings.items()):
            obj_enum_name = format_enum_name(obj_name)
            f.write(f"    ObjectType.{obj_enum_name}: {{\n")

            for relation, attr_type in sorted(relations.items()):
                # Use the pre-computed enum key for this relation
                relation_enum_name = relation_to_enum_key.get(relation)
                if not relation_enum_name:
                    print(f"Warning: No enum key found for relation '{relation}' in object '{obj_name}'")
                    continue

                attr_enum_name = format_enum_name(attr_type)
                f.write(f"        ObjectRelation.{relation_enum_name}: AttributeType.{attr_enum_name},\n")

            f.write("    },\n")

        f.write("}\n")

    print(f"Object relation to attribute type mappings added to {OBJECTS_FILE}")
    print(f"Generated mappings for {len(object_mappings)} object types")


def generate_attribute_enums():
    """Generate AttributeCategory and AttributeType enums from MISP data."""
    print("Generating AttributeCategory and AttributeType enums...")

    with open(DESCRIBE_TYPES_FILE, "r") as f:
        describe_data = json.load(f)

    result = describe_data.get("result", {})
    categories = result.get("categories", [])
    types = result.get("types", [])
    category_type_mappings = result.get("category_type_mappings", {})

    attribute_enums = {
        "AttributeCategory": {format_enum_name(cat): cat for cat in categories},
        "AttributeType": {format_enum_name(attr_type): attr_type for attr_type in types},
    }

    # Define imports for attributes.py
    imports = ["from enum import Enum", "from typing import Dict, Set"]

    # Generate the file with header comment and imports
    generate_enum_file(
        ATTRIBUTES_FILE,
        attribute_enums,
        imports=imports,
        header_comment="This mapping is automatically generated from MISP data",
    )

    # Add CATEGORY_TYPE_MAPPING dictionary
    with open(ATTRIBUTES_FILE, "a") as f:
        f.write("\n\n# Category to type mappings\n")
        f.write("CATEGORY_TYPE_MAPPING: Dict[AttributeCategory, Set[AttributeType]] = {\n")

        for category, types_list in sorted(category_type_mappings.items()):
            category_enum_name = format_enum_name(category)
            f.write(f"    AttributeCategory.{category_enum_name}: {{\n")

            for attr_type in sorted(types_list):
                type_enum_name = format_enum_name(attr_type)
                f.write(f"        AttributeType.{type_enum_name},\n")

            f.write("    },\n")

        f.write("}\n")

    print(
        f"AttributeCategory and AttributeType enums saved to {ATTRIBUTES_FILE} "
        f"({len(categories)} categories, {len(types)} types)"
    )
    print(f"CATEGORY_TYPE_MAPPING dictionary added to {ATTRIBUTES_FILE}")


def main():
    """Generate all models and mappings from MISP data."""
    os.makedirs(MODELS_DIR, exist_ok=True)

    generate_object_enums()
    generate_attribute_enums()

    print("Done!")


if __name__ == "__main__":
    main()
