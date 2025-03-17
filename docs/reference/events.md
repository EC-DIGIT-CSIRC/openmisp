# Events Reference

The Events API provides methods for creating, retrieving, updating, and deleting MISP events.

## Initialization

The `EventService` class is accessed through the MISP client:

```python
import os
from openmisp import (
    MISP,
    Analysis,
    Distribution,
    EventCriteria,
    OrganizationCriteria,
    SharingGroupCriteria,
    ThreatLevel,
)

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the events service
event_service = misp.events
```

## Methods

### create

Create a new MISP event.

```python
# Get required objects
organization = misp.get(OrganizationCriteria(name="Your Org"))
sharing_group = misp.get(SharingGroupCriteria(name="Your Group"))

# Create event
event = misp.events.create(
    info="Suspicious Activity Report",
    published=False,
    sharing_group=sharing_group,
    distribution=Distribution.YOUR_ORGANIZATION_ONLY,
    threat_level=ThreatLevel.MEDIUM,
    analysis=Analysis.INITIAL,
    organization=organization
)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `info` | str | Yes | Event description |
| `published` | bool | Yes | Whether the event is published |
| `sharing_group` | MISPSharingGroup | No | Sharing group for the event (required if distribution is SHARING_GROUP) |
| `distribution` | Distribution | Yes | Distribution level enum |
| `threat_level` | ThreatLevel | Yes | Threat level enum |
| `analysis` | Analysis | Yes | Analysis state enum |
| `organization` | MISPOrganisation | No | Organization creating the event |



### edit

Update an existing event.

```python
event = misp.events.edit(
    event=event,
    info="Updated Information",
    threat_level=ThreatLevel.HIGH,
    analysis=Analysis.ONGOING
)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `event` | MISPEvent | Yes | Event to update |
| `info` | str | No | New event description |
| `published` | bool | No | New published state |
| `sharing_group` | MISPSharingGroup | No | New sharing group |
| `distribution` | Distribution | No | New distribution level |
| `threat_level` | ThreatLevel | No | New threat level |
| `analysis` | Analysis | No | New analysis state |
| `organization` | MISPOrganisation | No | New organization |


### link

Link an entity (attribute, object, tag, or cluster) to an event.

```python
# Create and link an attribute
attribute = misp.attributes.create(
    type=AttributeType.IP_DST,
    value="192.168.1.1",
    detection=True,
    correlation=True,
    comment="Suspicious IP"
)
misp.events.link(event, attribute)

# Create and link a tag
tag = misp.tags.create(name="tlp:amber")
misp.events.link(event, tag)
```

### unlink

Unlink an entity from an event.

```python
misp.events.unlink(event, attribute)
misp.events.unlink(event, tag)
```



### sync

Synchronize an event with the MISP server.

```python
# Make changes to event
attribute = misp.attributes.create(
    type=AttributeType.DOMAIN,
    value="suspicious.com",
    detection=True,
    correlation=True
)
misp.events.link(event, attribute)

# Sync changes
misp.sync(event)
```



```python
try:
    # Attempt to get an event
    event = misp.get(EventCriteria(uuid="non-existent-uuid"))
    if event is None:
        print("Event not found")
except Exception as e:
    print(f"An error occurred: {e}")
```



