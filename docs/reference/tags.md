# Tags Reference

The Tags API provides methods for creating, retrieving, updating, and managing MISP tags, which are used to categorize and label events, attributes, and objects.

## Initialization

The `TagService` class is accessed through the MISP client:

```python
import os
from openmisp import MISP, TagCriteria

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the tags service
tag_service = misp.tags
```

## Methods

### create

Create a new tag.

```python
# Create a new tag
tag = misp.tags.create(name="tlp:amber")

# Create a tag with a specific color
tag = misp.tags.create(name="internal:investigation", colour="#00FF00")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | str | Yes | Tag name |
| `colour` | str | No | Hexadecimal color code |

### edit

Update an existing tag.

```python
# Update a tag
tag = misp.tags.edit(
    tag=tag,
    name="tlp:red",
    colour="#FF0000"
)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `tag` | MISPTag | Yes | Tag to update |
| `name` | str | No | New tag name |
| `colour` | str | No | New hexadecimal color code |

### get

Retrieve a tag by criteria.

```python
# Get tag by name
tag = misp.tags.get(name="tlp:amber")

# Get tag from an event
tag = misp.tags.get(from=event, name="tlp:amber")

# Get tag from an attribute
tag = misp.tags.get(from=attribute, name="tlp:amber")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent, MISPObject, or MISPAttribute | No | Parent entity |
| `name` | str | No | Tag name |
| `**fields` | Various | No | Other tag fields to match |

### exists

Check if a tag exists.

```python
# Check if tag exists
exists = misp.tags.exists(name="tlp:amber")

# Check if tag exists in an event
exists = misp.tags.exists(from=event, name="tlp:amber")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent, MISPObject, or MISPAttribute | No | Parent entity |
| `name` | str | No | Tag name |
| `**fields` | Various | No | Other tag fields to match |

### list

List tags based on criteria.

```python
# List all tags
for tag in misp.tags.list():
    print(f"Tag: {tag.name}")

# List tags with a specific pattern
for tag in misp.tags.list(filter=TagCriteria(pattern="tlp:")):
    print(f"TLP Tag: {tag.name}")

# List tags in an event
for tag in misp.tags.list(from=event):
    print(f"Event Tag: {tag.name}")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent, MISPObject, or MISPAttribute | No | Parent entity |
| `filter` | TagCriteria | No | Filter criteria |

## Common Tag Namespaces

MISP supports several common tag namespaces:

### Traffic Light Protocol (TLP)
```python
# TLP tags for information sharing restrictions
misp.tags.create(name="tlp:white")   # No restrictions
misp.tags.create(name="tlp:green")   # Limited disclosure
misp.tags.create(name="tlp:amber")   # Limited disclosure, specific organizations
misp.tags.create(name="tlp:red")     # Limited disclosure, specific individuals
```

### MISP Taxonomy
```python
# MISP taxonomy tags
misp.tags.create(name="misp-galaxy:threat-actor=\"APT28\"")
misp.tags.create(name="misp-galaxy:tool=\"Mimikatz\"")
misp.tags.create(name="admiralty-scale:source-reliability=\"a\"")
misp.tags.create(name="adversary:attribution=\"APT28\"")
```

### Custom Tags
```python
# Custom organizational tags
misp.tags.create(name="internal:investigation", colour="#00FF00")
misp.tags.create(name="priority:high", colour="#FF0000")
misp.tags.create(name="status:ongoing", colour="#FFFF00")
```

