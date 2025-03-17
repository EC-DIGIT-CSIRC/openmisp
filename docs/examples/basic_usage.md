# Basic Usage Examples

This guide provides practical examples of common operations using the OpenMISP.

## Setup

First, import and initialize the MISP client:

```python
import os
from openmisp import (
    MISP,
    Analysis,
    AttributeType,
    Distribution,
    EventCriteria,
    OrganizationCriteria,
    SharingGroupCriteria,
    TagCriteria,
    ThreatLevel,
)

# Initialize client with environment variables
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)
```

## Server Information

Retrieve basic server information:

```python
# Check server health
healthcheck = misp.server.healthcheck()
print(f"Healthcheck: {healthcheck}")

# Get server version
version = misp.server.version()
print(f"Version: {version}")

# Get server settings (commented out as it may return a large amount of data)
# settings = misp.server.settings()
# print(f"Settings: {settings}")
```

## Working with Organizations and Sharing Groups

Retrieve organizations and sharing groups:

```python
# Get a sharing group by name
sharing_group = misp.get(SharingGroupCriteria(name="Test Sharing Group"))

# Get an organization by name
organization = misp.get(OrganizationCriteria(name="ORGNAME"))
```

## Creating and Managing Events

### Listing Events

```python
# List published events
iterator = misp.list(EventCriteria(published=True))
event = next(iterator)
print(f"Event: {event.info}")
```

### Creating Events

```python
# Create a new event
event = misp.events.create(
    published=False,
    info="Suspicious Activity Report",
    organization=organization,  # Link to an organization
    sharing_group=sharing_group,  # Link to a sharing group
    distribution=Distribution.YOUR_ORGANIZATION_ONLY,
    threat_level=ThreatLevel.MEDIUM,
    analysis=Analysis.ONGOING,
)
```

### Updating Events

```python
# Update an existing event
event = misp.events.edit(
    event=event,
    analysis=Analysis.COMPLETED,
)
```

### Publishing Events

```python
# Publish an event
misp.events.edit(
    event=event,
    published=True,
)
```

## Working with Tags

### Creating Tags

```python
# Create a new tag
tag = misp.tags.create(
    name="team:source:feeds",
)
```

### Updating Tags

```python
# Update an existing tag
tag = misp.tags.edit(
    tag=tag,
    name="team:source:MYFEEDS",
)
```

### Linking Tags to Events

```python
# Link a tag to an event
misp.events.link(event, tag)

# Synchronize the event to apply changes
misp.sync(event)
```

### Listing Tags

```python
# List tags matching a pattern
tags = misp.tags.list(event, criteria=TagCriteria(pattern="team:"))
for tag in tags:
    print(f"Tag: {tag.name}")
```

### Batch Updating Tags

```python
# Update multiple tags in a batch
tags = misp.tags.list(event, criteria=TagCriteria(pattern="team:"))
for tag in tags:
    misp.tags.edit(tag=tag, name=f"{tag.name}-v2")
    misp.events.link(event, tag)
```

## Working with Attributes

### Creating Attributes

```python
# Create an IP linkress attribute
attribute = misp.attributes.create(
    value="8.8.8.8",
    type=AttributeType.IP_DST,
    detection=True,
    correlation=True,
)

# Create a domain attribute
attribute = misp.attributes.create(
    value="example.com",
    type=AttributeType.DOMAIN,
    detection=True,
    correlation=False,
)
```

### Updating Attributes

```python
# Update an existing attribute
attribute = misp.attributes.edit(
    attribute=attribute,
    value="8.8.4.4",
)
```

### Linking Attributes to Events

```python
# Link an attribute to an event
misp.events.link(event, attribute)

# Synchronize the event to apply changes
misp.sync(event)
```

### Tagging Attributes

```python
# Create a tag for attributes
tag = misp.tags.create(name="dangerous")

# Link the tag to specific attributes
for attribute in misp.attributes.list(event, criteria=AttributeCriteria(type=AttributeType.IP_DST)):
    misp.attributes.link(attribute, tag)
```

## Synchronization

After making changes to events, attributes, or tags, it's important to synchronize the event to ensure all changes are applied:

```python
# Synchronize an event after making changes
misp.sync(event)
```

