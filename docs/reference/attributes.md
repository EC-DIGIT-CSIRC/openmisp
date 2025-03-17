# Attributes Reference

The Attributes API provides methods for creating, retrieving, updating, and managing MISP attributes, which are the basic building blocks of MISP events, representing individual pieces of information such as IP linkresses, domain names, file hashes, etc.

## Initialization

The `AttributeService` class is accessed through the MISP client:

```python
import os
from openmisp import MISP, AttributeType, AttributeCriteria

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the attributes service
attribute_service = misp.attributes
```

## Methods

### create

Create a new attribute.

```python
# Create a new attribute
attribute = misp.attributes.create(
    type=AttributeType.IP_DST,
    value="192.168.1.1",
    detection=True,
    correlation=True,
    comment="Suspicious IP"
)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `type` | AttributeType | Yes | Attribute type enum |
| `value` | str | Yes | Attribute value |
| `detection` | bool | Yes | Enable detection (IDS flag) |
| `correlation` | bool | Yes | Enable correlation |
| `comment` | str | No | Additional comments |

### edit

Update an existing attribute.

```python
# Update an attribute
attribute = misp.attributes.edit(
    attribute=attribute,
    type=AttributeType.DOMAIN,
    value="suspicious.com",
    detection=True,
    correlation=False,
    comment="Updated comment"
)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `attribute` | MISPAttribute | Yes | Attribute to update |
| `type` | AttributeType | No | New attribute type |
| `value` | str | No | New value |
| `detection` | bool | No | New detection setting |
| `correlation` | bool | No | New correlation setting |
| `comment` | str | No | New comment |

### get

Retrieve an attribute by criteria.

```python
# Get attribute from an event
attribute = misp.attributes.get(event, type=AttributeType.IP_DST, value="192.168.1.1")

# Get attribute from an object
attribute = misp.attributes.get(misp_object, type=AttributeType.DOMAIN)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent or MISPObject | Yes | Parent event or object |
| `**fields` | Various | No | Attribute fields to match |

### exists

Check if an attribute exists.

```python
# Check if attribute exists in an event
exists = misp.attributes.exists(event, type=AttributeType.IP_DST, value="192.168.1.1")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent or MISPObject | Yes | Parent event or object |
| `**fields` | Various | No | Attribute fields to match |

### list

List attributes based on criteria.

```python
# List attributes in an event
for attribute in misp.attributes.list(event, type=AttributeType.IP_DST):
    print(f"IP: {attribute.value}")

# List attributes in an object
for attribute in misp.attributes.list(misp_object, filter=AttributeCriteria(detection=True)):
    print(f"{attribute.type}: {attribute.value}")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `from` | MISPEvent or MISPObject | Yes | Parent event or object |
| `filter` | AttributeCriteria | No | Filter criteria |

### link

Link a tag or cluster to an attribute.

```python
# Link a tag
tag = misp.tags.create(name="tlp:amber")
misp.attributes.link(attribute, tag)

# Link a galaxy cluster
cluster = misp.clusters.get(misp.galaxies.get(name="threat-actor"), name="APT28")
misp.attributes.link(attribute, cluster)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source` | MISPAttribute | Yes | Source attribute |
| `target` | MISPTag or MISPGalaxyCluster | Yes | Target to link |

### unlink

Unlink a tag or cluster from an attribute.

```python
# Unlink a tag
misp.attributes.unlink(attribute, tag)

# Unlink a galaxy cluster
misp.attributes.unlink(attribute, cluster)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source` | MISPAttribute | Yes | Source attribute |
| `target` | MISPTag or MISPGalaxyCluster | Yes | Target to unlink |

## Attribute Types

The SDK provides an `AttributeType` enum for all supported attribute types:

### Network Indicators
```python
AttributeType.IP_DST          # "ip-dst"
AttributeType.IP_SRC          # "ip-src"
AttributeType.DOMAIN          # "domain"
AttributeType.HOSTNAME        # "hostname"
AttributeType.URL            # "url"
AttributeType.EMAIL_SRC      # "email-src"
AttributeType.EMAIL_DST      # "email-dst"
AttributeType.AS             # "AS"
```

### File Indicators
```python
AttributeType.FILENAME       # "filename"
AttributeType.MD5           # "md5"
AttributeType.SHA1          # "sha1"
AttributeType.SHA256        # "sha256"
AttributeType.SIZE_IN_BYTES # "size-in-bytes"
AttributeType.FILE_TYPE     # "file-type"
AttributeType.MIME_TYPE     # "mime-type"
```

### System Indicators
```python
AttributeType.MUTEX         # "mutex"
AttributeType.PROCESS_NAME  # "process-name"
AttributeType.PID           # "pid"
AttributeType.PORT          # "port"
AttributeType.USER_AGENT    # "user-agent"
```

### Other Types
```python
AttributeType.COMMENT       # "comment"
AttributeType.TEXT         # "text"
AttributeType.VULNERABILITY # "vulnerability"
AttributeType.LINK         # "link"
```

