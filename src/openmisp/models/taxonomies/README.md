# MISP Taxonomy Models

This directory contains Python models for MISP taxonomies. These models are automatically generated from the MISP taxonomies repository.

## Structure

Each taxonomy is represented by two classes:
1. A `<TaxonomyName>Taxonomy` class that contains metadata about the taxonomy
2. A `<TaxonomyName>TaxonomyPredicate` enum that contains the possible predicates for the taxonomy

## Usage

### Importing a specific taxonomy

```python
from openmisp.models.taxonomies.tlp import TlpTaxonomy, TlpTaxonomyPredicate

# Get the namespace
namespace = TlpTaxonomy.namespace  # "tlp"

# Get the description
description = TlpTaxonomy.description

# Get all predicates
predicates = [p.value for p in TlpTaxonomyPredicate]  # ["red", "amber", "amber+strict", "green", "white", "clear", "ex:chr", "unclear"]

# Create a tag
tag = TlpTaxonomy.get_tag(TlpTaxonomyPredicate.RED)  # "tlp:red"
```

### Using the utility functions

```python
from openmisp.models.taxonomies.utils import (
    get_all_taxonomies,
    get_taxonomy_by_namespace,
    get_taxonomy_from_tag,
    is_valid_tag,
    parse_tag,
)

# Get all taxonomies
taxonomies = get_all_taxonomies()

# Get a taxonomy by namespace
tlp_taxonomy = get_taxonomy_by_namespace("tlp")

# Get a taxonomy from a tag
taxonomy = get_taxonomy_from_tag("tlp:red")

# Check if a tag is valid
is_valid = is_valid_tag("tlp:red")  # True
is_valid = is_valid_tag("tlp:invalid")  # False

# Parse a tag
parsed = parse_tag("tlp:red")  # {"namespace": "tlp", "predicate": "red"}
```

## Regenerating the models

The taxonomy models are generated from the MISP taxonomies repository. To regenerate the models, run:

```bash
python scripts/generate_taxonomy_models.py
```

This will read the taxonomies from the `misp-taxonomies` directory and generate the models in this directory. 