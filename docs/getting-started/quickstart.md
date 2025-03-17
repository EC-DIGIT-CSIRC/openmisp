# Quick Start Guide

This guide will help you get started with OpenMISP by walking through some common use cases.

## Basic Setup

First, import and initialize the MISP client:

```python
import os
from openmisp import (
    MISP,
    Analysis,
    AttributeType,
    Distribution,
    EventCriteria,
    ThreatLevel,
)

# Initialize the client with environment variables
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)
```

## Server Information

```python
# Check server health
healthcheck = misp.server.healthcheck()
print(f"Healthcheck: {healthcheck}")

# Get server version
version = misp.server.version()
print(f"Version: {version}")
```

## Working with Events

### Listing Events

```python
# List published events
iterator = misp.list(EventCriteria(published=True))
event = next(iterator)
print(f"Event: {event.info}")

# Iterate through all published events
for event in misp.list(EventCriteria(published=True)):
    print(f"Event: {event.info}")
```

### Creating Events

```python
# Create a new event
event = misp.events.create(
    published=False,
    info="Suspicious Activity Report",
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

# Publish an event
misp.events.edit(
    event=event,
    published=True,
)
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

## Working with Tags

### Creating and Updating Tags

```python
# Create a new tag
tag = misp.tags.create(
    name="team:source:feeds",
)

# Update an existing tag
tag = misp.tags.edit(
    tag=tag,
    name="team:source:MYFEEDS",
)
```

### Linking Tags

```python
# Link a tag to an event
misp.events.link(event, tag)

# Link a tag to an attribute
misp.attributes.link(attribute, tag)

# Synchronize the event to apply changes
misp.sync(event)
```

### Searching Tags

```python
# List tags matching a pattern
tags = misp.tags.list(event, criteria=TagCriteria(pattern="team:"))
for tag in tags:
    print(f"Tag: {tag.name}")
```

## Synchronization

After making changes to events, attributes, or tags, it's important to synchronize the event to ensure all changes are applied:

```python
# Synchronize an event after making changes
misp.sync(event)
```

## Error Handling

```python
try:
    # Attempt to perform an operation
    event = misp.get(EventCriteria(uuid="non-existent-uuid"))
    if event is None:
        print("Event not found")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Next Steps

- Check out the [API Reference](../reference/misp.md) for detailed information about all available features
- Look at more complex [Examples](../examples/basic_usage.md)
- Learn about [Advanced Features](../reference/events.md) like working with galaxies and sharing groups
