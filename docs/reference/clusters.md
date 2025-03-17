# Clusters Reference

The Clusters API provides methods for retrieving and managing MISP galaxy clusters, which are specific instances within a galaxy, such as particular threat actors, malware families, or attack techniques.

## Initialization

The `ClusterService` class is accessed through the MISP client:

```python
import os
from openmisp import MISP, ClusterCriteria

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the clusters service
cluster_service = misp.clusters
```

## Methods

### get

Retrieve a cluster by criteria.

```python
# Get cluster from a galaxy
galaxy = misp.galaxies.get(name="threat-actor")
cluster = misp.clusters.get(from=galaxy, name="APT28")

# Get cluster from an event
cluster = misp.clusters.get(from=event, name="APT28")

# Get cluster from an attribute
cluster = misp.clusters.get(from=attribute, name="Emotet")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPGalaxy, MISPEvent, MISPObject, or MISPAttribute | Yes | Parent entity |
| `name` | str | No | Cluster name |
| `**fields` | Various | No | Other cluster fields to match |

### exists

Check if a cluster exists.

```python
# Check if cluster exists in a galaxy
galaxy = misp.galaxies.get(name="threat-actor")
exists = misp.clusters.exists(from=galaxy, name="APT28")

# Check if cluster exists in an event
exists = misp.clusters.exists(from=event, name="APT28")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPGalaxy, MISPEvent, MISPObject, or MISPAttribute | Yes | Parent entity |
| `name` | str | No | Cluster name |
| `**fields` | Various | No | Other cluster fields to match |

### list

List clusters based on criteria.

```python
# List all clusters in a galaxy
galaxy = misp.galaxies.get(name="threat-actor")
for cluster in misp.clusters.list(from=galaxy):
    print(f"Threat Actor: {cluster.name}")

# List clusters with a specific pattern
for cluster in misp.clusters.list(from=galaxy, filter=ClusterCriteria(pattern="APT")):
    print(f"APT Group: {cluster.name}")

# List clusters in an event
for cluster in misp.clusters.list(from=event):
    print(f"Event Cluster: {cluster.name}")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPGalaxy, MISPEvent, MISPObject, or MISPAttribute | Yes | Parent entity |
| `filter` | ClusterCriteria | No | Filter criteria |

## Common Cluster Types

MISP provides several common cluster types within different galaxies:

### Threat Actor Clusters
```python
# Get threat actor galaxy
threat_actor_galaxy = misp.galaxies.get(name="threat-actor")

# List common threat actor clusters
common_threat_actors = [
    "APT28",           # Fancy Bear, Russian military intelligence
    "APT29",           # Cozy Bear, Russian foreign intelligence
    "Lazarus Group",   # North Korean state-sponsored group
    "APT1",            # Chinese PLA Unit 61398
    "FIN7"             # Financial cybercrime group
]

# Link a threat actor to an event
apt28 = misp.clusters.get(from=threat_actor_galaxy, name="APT28")
misp.events.link(event, apt28)
```

### MITRE ATT&CK Technique Clusters
```python
# Get MITRE ATT&CK galaxy
attack_galaxy = misp.galaxies.get(name="mitre-attack-pattern")

# List common ATT&CK techniques
common_techniques = [
    "T1059 - Command and Scripting Interpreter",
    "T1566 - Phishing",
    "T1486 - Data Encrypted for Impact",
    "T1078 - Valid Accounts",
    "T1027 - Obfuscated Files or Information"
]

# Link an attack technique to an attribute
t1059 = misp.clusters.get(from=attack_galaxy, name="T1059 - Command and Scripting Interpreter")
misp.attributes.link(attribute, t1059)
```

### Malware Clusters
```python
# Get malware galaxy
malware_galaxy = misp.galaxies.get(name="malware")

# List common malware families
common_malware = [
    "Emotet",
    "TrickBot",
    "Ryuk",
    "Cobalt Strike",
    "Mimikatz"
]

# Link a malware family to an object
emotet = misp.clusters.get(from=malware_galaxy, name="Emotet")
misp.objects.link(misp_object, emotet)
```
