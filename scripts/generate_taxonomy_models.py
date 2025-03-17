#!/usr/bin/env python3
"""
Script to generate Python models for MISP taxonomies.

This script reads the MISP taxonomies from the misp-taxonomies directory
and generates Python models for each taxonomy in the SDK models/taxonomies directory.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Constants
TAXONOMIES_REPO = "https://github.com/MISP/misp-taxonomies.git"
TAXONOMIES_DIR = Path("misp-taxonomies")
OUTPUT_DIR = Path("src/openmisp/models/taxonomies")
INIT_FILE = OUTPUT_DIR / "__init__.py"


def clone_taxonomies_repo():
    """Clone or update the MISP taxonomies repository."""
    if TAXONOMIES_DIR.exists():
        print(f"Updating existing taxonomies repository in {TAXONOMIES_DIR}...")
        subprocess.run(["git", "-C", str(TAXONOMIES_DIR), "pull"], check=True)
    else:
        print(f"Cloning taxonomies repository to {TAXONOMIES_DIR}...")
        subprocess.run(["git", "clone", TAXONOMIES_REPO, str(TAXONOMIES_DIR)], check=True)


def sanitize_name(name: str) -> str:
    """Sanitize a name to be a valid Python identifier."""
    # Replace non-alphanumeric characters with underscores
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    # Ensure the name starts with a letter
    if not name or not name[0].isalpha():
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


def generate_taxonomy_model(taxonomy_dir: Path) -> Optional[str]:
    """Generate a Python model for a taxonomy."""
    machinetag_file = taxonomy_dir / "machinetag.json"
    if not machinetag_file.exists():
        return None

    try:
        with open(machinetag_file, "r", encoding="utf-8") as f:
            taxonomy = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"Error parsing {machinetag_file}: {e}")
        return None

    namespace = taxonomy.get("namespace", "")
    if not namespace:
        return None

    module_name = sanitize_name(namespace)
    class_name = camel_case(module_name) + "Taxonomy"

    # Generate the Python file content
    content = [
        f'"""Taxonomy model for {taxonomy.get("expanded", namespace)}."""',
        "",
        "from enum import Enum, auto",
        "from typing import Dict, List, Optional, Any, Union",
        "",
        "from pydantic import BaseModel, Field",
        "",
        "",
    ]

    # Check if we have predicates or values
    predicates = taxonomy.get("predicates", [])
    values = taxonomy.get("values", [])

    # Generate predicate enum
    if predicates:
        content.append(f"class {class_name}Predicate(str, Enum):")
        for predicate in predicates:
            value = predicate.get("value", "")
            if not value:
                continue
            enum_name = sanitize_name(value).upper()
            content.append(f'    {enum_name} = "{value}"')
        content.extend(["", ""])

    # Generate entry models for each predicate with entries
    entry_models = []
    if values:
        for value_obj in values:
            predicate = value_obj.get("predicate", "")
            entries = value_obj.get("entry", [])
            if not predicate or not entries:
                continue

            # Format the predicate name properly for the class name
            predicate_class_name = camel_case(predicate)
            entry_class_name = f"{class_name}{predicate_class_name}Entry"
            entry_models.append((predicate, entry_class_name))

            content.append(f"class {entry_class_name}(str, Enum):")
            for entry in entries:
                entry_value = entry.get("value", "")
                if not entry_value:
                    continue
                enum_name = sanitize_name(entry_value).upper()
                content.append(f'    {enum_name} = "{entry_value}"')
            content.extend(["", ""])

    # Generate the main taxonomy class
    content.extend(
        [
            f"class {class_name}(BaseModel):",
            f'    """Model for the {taxonomy.get("expanded", namespace)} taxonomy."""',
            "",
            f'    namespace: str = "{namespace}"',
            f'    description: str = """{taxonomy.get("description", "")}"""',
            f"    version: int = {taxonomy.get('version', 0)}",
            f"    exclusive: bool = {str(taxonomy.get('exclusive', False)).capitalize()}",
        ]
    )

    # Add predicates field if we have predicates
    if predicates:
        content.append(f"    predicates: List[{class_name}Predicate] = []")

    # Add entry fields for each predicate with entries
    for predicate, entry_class_name in entry_models:
        predicate_field = sanitize_name(predicate)
        content.append(f"    {predicate_field}_entries: List[{entry_class_name}] = []")

    # Add methods
    content.extend(
        [
            "",
            "    @classmethod",
            "    def get_tag(cls, predicate: str, entry: Optional[str] = None) -> str:",
            '        """Get the full tag for a predicate and optional entry."""',
            "        if entry:",
            "            return f\"{cls.namespace}:{predicate}='{entry}'\"",
            '        return f"{cls.namespace}:{predicate}"',
            "",
        ]
    )

    return "\n".join(content)


def generate_taxonomy_models():
    """Generate Python models for all taxonomies."""
    # Create the output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read the current __init__.py file
    init_content = []
    if INIT_FILE.exists():
        with open(INIT_FILE, "r", encoding="utf-8") as f:
            init_content = f.readlines()
    else:
        # Create a basic __init__.py if it doesn't exist
        init_content = ['"""MISP taxonomy models."""\n', "\n", "# Import all taxonomy models\n"]

    # Find where to insert the imports
    import_index = -1
    for i, line in enumerate(init_content):
        if "# Import all taxonomy models" in line:
            import_index = i + 1
            break

    # If we didn't find the marker, append to the end
    if import_index == -1:
        init_content.append("\n# Import all taxonomy models\n")
        import_index = len(init_content)

    # Clear any existing imports
    while import_index < len(init_content) and not init_content[import_index].startswith("#"):
        init_content.pop(import_index)

    # Generate models for each taxonomy
    imports = []
    taxonomy_count = 0

    for taxonomy_dir in TAXONOMIES_DIR.iterdir():
        if not taxonomy_dir.is_dir() or taxonomy_dir.name.startswith(".") or taxonomy_dir.name == ".github":
            continue

        content = generate_taxonomy_model(taxonomy_dir)
        if not content:
            continue

        taxonomy_count += 1
        module_name = sanitize_name(taxonomy_dir.name)
        file_path = OUTPUT_DIR / f"{module_name}.py"

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Add import to __init__.py
        class_name = camel_case(module_name) + "Taxonomy"
        import_line = f"from .{module_name} import {class_name}"

        # Add predicate enum if it exists
        if "Predicate(str, Enum)" in content:
            import_line += f", {class_name}Predicate"

        # Add entry enums if they exist
        for line in content.split("\n"):
            if line.startswith("class") and "Entry(str, Enum)" in line:
                entry_class = line.split("class ")[1].split("(")[0].strip()
                import_line += f", {entry_class}"

        imports.append(import_line + "\n")

    # Update __init__.py with imports
    init_content[import_index:import_index] = imports

    with open(INIT_FILE, "w", encoding="utf-8") as f:
        f.writelines(init_content)

    print(f"Generated {taxonomy_count} taxonomy models.")


if __name__ == "__main__":
    # Clone or update the taxonomies repository
    clone_taxonomies_repo()

    # Generate the taxonomy models
    generate_taxonomy_models()
