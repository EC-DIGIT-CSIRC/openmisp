# OpenMISP Documentation

Welcome to the OpenMISP documentation. This SDK provides a powerful and intuitive interface for interacting with MISP (Malware Information Sharing Platform) instances.

## Overview

OpenMISP is a Python library that simplifies the interaction with MISP instances. It provides a clean, modern API for managing MISP events, attributes, objects, and other MISP features.

## Key Features

- **Intuitive API**: Simple and consistent API design for all MISP operations
- **Type Safety**: Strong typing support for better code reliability
- **Modern Python**: Built with modern Python features and best practices

## Quick Example

```python
import os
from openmisp import MISP, EventCriteria, AttributeType

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production
)

# Check server health
healthcheck = misp.server.healthcheck()
print(f"Healthcheck: {healthcheck}")

# List published events
for event in misp.list(EventCriteria(published=True)):
    print(f"Event: {event.info}")

# Create and link attributes
attribute = misp.attributes.create(
    value="8.8.8.8",
    type=AttributeType.IP_DST,
    detection=True,
    correlation=True,
)
misp.events.link(event, attribute)
misp.sync(event)
```

## Quick Access

- [Installation Guide](getting-started/installation.md)
- [Quick Start Guide](getting-started/quickstart.md)
- [CheatSheet](cheatsheet.md)
- [Attribute Reference](reference/attributes.md)
- [Example Usage](examples/basic_usage.md)
