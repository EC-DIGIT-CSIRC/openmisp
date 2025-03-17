# MISP Reference

The `MISP` class is the main entry point for interacting with a MISP instance through the OpenMISP.

## Initialization

```python
import os
from openmisp import MISP

# Initialize with direct parameters
misp = MISP(
    url="https://your-misp-instance.com",
    key="your-api-key",
    ssl=True  # Enable/disable SSL verification
)

# Or initialize with environment variables
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False  # Set to True in production environments
)
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `client` | PyMISP | The underlying PyMISP client |
| `events` | EventService | Service for managing MISP events |
| `objects` | ObjectService | Service for managing MISP objects |
| `attributes` | AttributeService | Service for managing MISP attributes |
| `tags` | TagService | Service for managing MISP tags |
| `galaxies` | GalaxyService | Service for managing MISP galaxies |
| `clusters` | ClusterService | Service for managing galaxy clusters |
| `organizations` | OrganizationService | Service for managing organizations |
| `sharing_groups` | SharingGroupService | Service for managing sharing groups |
| `server` | ServerService | Service for server-related operations |

## Methods

### list

```python
from openmisp import EventCriteria, AttributeCriteria, TagCriteria

# List published events
criteria = EventCriteria(published=True)

for event in misp.list(criteria):
    print(f"Event: {event.info}")


# List attributes of a specific type
criteria = AttributeCriteria(type=AttributeType.IP_DST)

for attribute in misp.list(criteria):
    print(f"Attribute: {attribute.value}")


# List tags matching a pattern
criteria = TagCriteria(pattern="tlp:")

for tag in misp.list(criteria):
    print(f"Tag: {tag.name}")
```

### get

```python
from openmisp import EventCriteria, OrganizationCriteria, SharingGroupCriteria

# Get an event by UUID
criteria = EventCriteria(uuid="event-uuid")
event = misp.get(criteria)


# Get an organization by name
criteria = OrganizationCriteria(name="ORGNAME")
organization = misp.get(criteria)


# Get a sharing group by name
criteria = SharingGroupCriteria(name="Test Sharing Group")
sharing_group = misp.get(criteria)
```

### sync

```python
# After making changes to an event
misp.sync(event)
```

## Enums

The SDK provides several enums for standardized values:

### Distribution
```python
from openmisp import Distribution

Distribution.YOUR_ORGANIZATION_ONLY      # 0
Distribution.COMMUNITY_ONLY        # 1
Distribution.CONNECTED_COMMUNITIES # 2
Distribution.ALL_COMMUNITIES      # 3
Distribution.SHARING_GROUP        # 4
```

### ThreatLevel
```python
from openmisp import ThreatLevel

ThreatLevel.HIGH      # 1
ThreatLevel.MEDIUM    # 2
ThreatLevel.LOW       # 3
ThreatLevel.UNDEFINED # 4
```

### Analysis
```python
from openmisp import Analysis

Analysis.INITIAL    # 0
Analysis.ONGOING    # 1
Analysis.COMPLETED  # 2
```

### AttributeType
```python
from openmisp import AttributeType

AttributeType.IP_DST          # "ip-dst"
AttributeType.DOMAIN          # "domain"
AttributeType.HOSTNAME        # "hostname"
AttributeType.URL            # "url"
AttributeType.MD5            # "md5"
AttributeType.SHA1           # "sha1"
AttributeType.SHA256         # "sha256"
AttributeType.FILENAME       # "filename"
AttributeType.EMAIL          # "email"
AttributeType.TEXT           # "text"
AttributeType.DATETIME       # "datetime"
AttributeType.REGKEY         # "regkey"
AttributeType.SIZE_IN_BYTES  # "size-in-bytes"
# ... and many more
```

## Error Handling

The client may raise various exceptions:

```python
try:
    # Attempt operations
    event = misp.get(EventCriteria(uuid="non-existent-uuid"))
    if event is None:
        print("Event not found")
except Exception as e:
    print(f"An error occurred: {e}")
```

