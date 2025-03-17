# Galaxies Reference

The Galaxies API provides methods for retrieving and managing MISP galaxies, which are knowledge bases of threat actors, tools, malware, and other intelligence items.

## Initialization

The `GalaxyService` class is accessed through the MISP client:

```python
import os
from openmisp import MISP, GalaxyCriteria

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the galaxies service
galaxy_service = misp.galaxies
```

## Methods

### get

Retrieve a galaxy by criteria.

```python
# Get galaxy by name
galaxy = misp.galaxies.get(name="threat-actor")

# Get galaxy from an event
galaxy = misp.galaxies.get(from=event, name="threat-actor")

# Get galaxy from an attribute
galaxy = misp.galaxies.get(from=attribute, name="tool")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent, MISPObject, or MISPAttribute | No | Parent entity |
| `name` | str | No | Galaxy name |
| `**fields` | Various | No | Other galaxy fields to match |

### exists

Check if a galaxy exists.

```python
# Check if galaxy exists
exists = misp.galaxies.exists(name="threat-actor")

# Check if galaxy exists in an event
exists = misp.galaxies.exists(from=event, name="threat-actor")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent, MISPObject, or MISPAttribute | No | Parent entity |
| `name` | str | No | Galaxy name |
| `**fields` | Various | No | Other galaxy fields to match |

### list

List galaxies based on criteria.

```python
# List all galaxies
for galaxy in misp.galaxies.list():
    print(f"Galaxy: {galaxy.name}")

# List galaxies with a specific pattern
for galaxy in misp.galaxies.list(filter=GalaxyCriteria(pattern="mitre-")):
    print(f"MITRE Galaxy: {galaxy.name}")

# List galaxies in an event
for galaxy in misp.galaxies.list(from=event):
    print(f"Event Galaxy: {galaxy.name}")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent, MISPObject, or MISPAttribute | No | Parent entity |
| `filter` | GalaxyCriteria | No | Filter criteria |

## Common Galaxy Types

MISP provides several common galaxy types:

### Threat Actors
```python
# Get threat actor galaxy
threat_actor_galaxy = misp.galaxies.get(name="threat-actor")

# Get specific threat actor cluster
apt28_cluster = misp.clusters.get(from=threat_actor_galaxy, name="APT28")

# Link threat actor to an event
misp.events.link(event, apt28_cluster)
```

### Attack Patterns (MITRE ATT&CK)
```python
# Get MITRE ATT&CK galaxy
attack_galaxy = misp.galaxies.get(name="mitre-attack-pattern")

# Get specific attack pattern cluster
t1059_cluster = misp.clusters.get(from=attack_galaxy, name="T1059 - Command and Scripting Interpreter")

# Link attack pattern to an attribute
misp.attributes.link(attribute, t1059_cluster)
```

### Malware
```python
# Get malware galaxy
malware_galaxy = misp.galaxies.get(name="malware")

# Get specific malware cluster
emotet_cluster = misp.clusters.get(from=malware_galaxy, name="Emotet")

# Link malware to an object
misp.objects.link(misp_object, emotet_cluster)
```
