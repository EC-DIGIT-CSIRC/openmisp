# Objects Reference

The Objects API provides methods for creating, retrieving, updating, and managing MISP objects, which are structured collections of attributes that represent more complex data structures.

## Initialization

The `ObjectService` class is accessed through the MISP client:

```python
import os
from openmisp import MISP, ObjectCriteria

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the objects service
object_service = misp.objects
```

## Methods

### create

Create a new MISP object.

```python
# Create a new object
misp_object = misp.objects.create(
    name="file",
    description="Suspicious executable file",
    template_uuid="688c46fb-5edb-40a3-8273-1af7923e2215"
)

# Link attributes to the object
misp.attributes.create(
    type=AttributeType.FILENAME,
    value="malware.exe",
    detection=True,
    correlation=True,
    parent=misp_object
)

misp.attributes.create(
    type=AttributeType.MD5,
    value="d41d8cd98f00b204e9800998ecf8427e",
    detection=True,
    correlation=True,
    parent=misp_object
)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | str | Yes | Object name/type |
| `description` | str | Yes | Object description |
| `template_uuid` | str | No | UUID of the object template |

### edit

Update an existing object.

```python
# Update an object
misp_object = misp.objects.edit(
    object=misp_object,
    name="file",
    description="Updated description for suspicious file"
)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `object` | MISPObject | Yes | Object to update |
| `name` | str | No | New object name/type |
| `description` | str | No | New object description |
| `template_uuid` | str | No | New template UUID |

### get

Retrieve an object by criteria.

```python
# Get object from an event
misp_object = misp.objects.get(from=event, name="file")

# Get object by UUID
misp_object = misp.objects.get(from=event, uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent | Yes | Parent event |
| `**fields` | Various | No | Object fields to match |

### exists

Check if an object exists.

```python
# Check if object exists in an event
exists = misp.objects.exists(from=event, name="file")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent | Yes | Parent event |
| `**fields` | Various | No | Object fields to match |

### list

List objects based on criteria.

```python
# List all objects in an event
for misp_object in misp.objects.list(from=event):
    print(f"Object: {misp_object.name} - {misp_object.description}")

# List objects with specific criteria
for misp_object in misp.objects.list(from=event, filter=ObjectCriteria(name="file")):
    print(f"File object: {misp_object.description}")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent | Yes | Parent event |
| `filter` | ObjectCriteria | No | Filter criteria |

### link

Link a tag, galaxy, or cluster to an object.

```python
# Link a tag
tag = misp.tags.create(name="tlp:amber")
misp.objects.link(misp_object, tag)

# Link a galaxy cluster
cluster = misp.clusters.get(from=misp.galaxies.get(name="threat-actor"), name="APT28")
misp.objects.link(misp_object, cluster)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source` | MISPObject | Yes | Source object |
| `target` | MISPTag, MISPGalaxy, or MISPGalaxyCluster | Yes | Target to link |

### unlink

Unlink a tag, galaxy, or cluster from an object.

```python
# Unlink a tag
misp.objects.unlink(misp_object, tag)

# Unlink a galaxy cluster
misp.objects.unlink(misp_object, cluster)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source` | MISPObject | Yes | Source object |
| `target` | MISPTag, MISPGalaxy, or MISPGalaxyCluster | Yes | Target to unlink |

## Common Object Types

MISP provides templates for many common object types:

### File Objects
```python
# Create a file object
file_object = misp.objects.create(name="file", description="Malicious file")

# Link file attributes
misp.attributes.create(type=AttributeType.FILENAME, value="malware.exe", parent=file_object)
misp.attributes.create(type=AttributeType.MD5, value="d41d8cd98f00b204e9800998ecf8427e", parent=file_object)
misp.attributes.create(type=AttributeType.SHA1, value="da39a3ee5e6b4b0d3255bfef95601890afd80709", parent=file_object)
misp.attributes.create(type=AttributeType.SIZE_IN_BYTES, value="1024", parent=file_object)
```

### Network Objects
```python
# Create a network connection object
network_object = misp.objects.create(name="network-connection", description="Suspicious connection")

# Link network attributes
misp.attributes.create(type=AttributeType.IP_DST, value="192.168.1.1", parent=network_object)
misp.attributes.create(type=AttributeType.PORT_DST, value="443", parent=network_object)
misp.attributes.create(type=AttributeType.HOSTNAME_DST, value="evil.com", parent=network_object)
```
