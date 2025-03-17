# Sharing Groups Reference

The Sharing Groups API provides methods for retrieving and managing MISP sharing groups, which define custom sets of organizations for selective sharing of threat intelligence.

## Initialization

The `SharingGroupService` class is accessed through the MISP client:

```python
import os
from openmisp import MISP, SharingGroupCriteria, Distribution

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the sharing groups service
sharing_group_service = misp.sharing_groups
```

## Methods

### create

Create a new sharing group.

```python
# Create a new sharing group
sharing_group = misp.sharing_groups.create(
    name="Financial Sector Group",
    description="Sharing group for financial sector organizations",
    releasability="TLP:AMBER"
)

# Link organizations to the sharing group
org1 = misp.organizations.get(name="ACME Bank")
org2 = misp.organizations.get(name="Financial CERT")
misp.sharing_groups.link_organization(sharing_group, org1)
misp.sharing_groups.link_organization(sharing_group, org2)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | str | Yes | Sharing group name |
| `description` | str | No | Description of the sharing group |
| `releasability` | str | No | Releasability statement (e.g., TLP level) |
| `active` | bool | No | Whether the sharing group is active |

### edit

Update an existing sharing group.

```python
# Update a sharing group
sharing_group = misp.sharing_groups.edit(
    sharing_group=sharing_group,
    name="Updated Financial Sector Group",
    description="Updated description for financial sector sharing",
    releasability="TLP:RED"
)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `sharing_group` | MISPSharingGroup | Yes | Sharing group to update |
| `name` | str | No | New sharing group name |
| `description` | str | No | New description |
| `releasability` | str | No | New releasability statement |
| `active` | bool | No | New active status |

### get

Retrieve a sharing group by criteria.

```python
# Get sharing group by name
sharing_group = misp.sharing_groups.get(name="Financial Sector Group")

# Get sharing group by UUID
sharing_group = misp.sharing_groups.get(uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | str | No | Sharing group name |
| `uuid` | str | No | Sharing group UUID |
| `**fields` | Various | No | Other sharing group fields to match |

### exists

Check if a sharing group exists.

```python
# Check if sharing group exists
exists = misp.sharing_groups.exists(name="Financial Sector Group")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | str | No | Sharing group name |
| `uuid` | str | No | Sharing group UUID |
| `**fields` | Various | No | Other sharing group fields to match |

### list

List sharing groups based on criteria.

```python
# List all sharing groups
for sharing_group in misp.sharing_groups.list():
    print(f"Sharing Group: {sharing_group.name}")

# List sharing groups with a specific pattern
for sharing_group in misp.sharing_groups.list(filter=SharingGroupCriteria(pattern="CERT")):
    print(f"CERT Sharing Group: {sharing_group.name}")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filter` | SharingGroupCriteria | No | Filter criteria |

### link_organization

Link an organization to a sharing group.

```python
# Link an organization to a sharing group
organization = misp.organizations.get(name="New Financial Org")
misp.sharing_groups.link_organization(sharing_group, organization)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `sharing_group` | MISPSharingGroup | Yes | Sharing group to modify |
| `organization` | MISPOrganisation | Yes | Organization to link |
| `extend` | bool | No | Whether the organization can extend the sharing group |

### unlink_organization

Unlink an organization from a sharing group.

```python
# Unlink an organization from a sharing group
organization = misp.organizations.get(name="Old Financial Org")
misp.sharing_groups.unlink_organization(sharing_group, organization)
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `sharing_group` | MISPSharingGroup | Yes | Sharing group to modify |
| `organization` | MISPOrganisation | Yes | Organization to unlink |

## Using Sharing Groups

Sharing groups are used when creating or updating events with a distribution level of `SHARING_GROUP`:

```python
# Get a sharing group
sharing_group = misp.sharing_groups.get(name="Financial Sector Group")

# Create an event with the sharing group
event = misp.events.create(
    info="Financial Sector Threat Intelligence",
    published=False,
    distribution=Distribution.SHARING_GROUP,
    sharing_group=sharing_group,
    threat_level=ThreatLevel.MEDIUM,
    analysis=Analysis.INITIAL,
    organization=misp.organizations.get(name="ACME Bank")
)
```

