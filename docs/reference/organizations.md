# Organizations Reference

The Organizations API provides methods for retrieving and managing MISP organizations, which represent the entities that create and share intelligence within the MISP ecosystem.

## Initialization

The `OrganizationService` class is accessed through the MISP client:

```python
import os
from openmisp import MISP, OrganizationCriteria

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the organizations service
organization_service = misp.organizations
```

## Methods

### get

Retrieve an organization by criteria.

```python
# Get organization by name
organization = misp.organizations.get(name="ACME Inc.")

# Get organization by UUID
organization = misp.organizations.get(uuid="a1b2c3d4-e5f6-7890-abcd-ef1234567890")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | str | No | Organization name |
| `uuid` | str | No | Organization UUID |
| `**fields` | Various | No | Other organization fields to match |

### exists

Check if an organization exists.

```python
# Check if organization exists
exists = misp.organizations.exists(name="ACME Inc.")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | str | No | Organization name |
| `uuid` | str | No | Organization UUID |
| `**fields` | Various | No | Other organization fields to match |

### list

List organizations based on criteria.

```python
# List all organizations
for organization in misp.organizations.list():
    print(f"Organization: {organization.name}")

# List organizations with a specific pattern
for organization in misp.organizations.list(filter=OrganizationCriteria(pattern="CERT")):
    print(f"CERT Organization: {organization.name}")
```

Parameters:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filter` | OrganizationCriteria | No | Filter criteria |

## Working with Organizations

Organizations are used in various contexts within MISP:

### Creating Events with Organizations
```python
# Get an organization
organization = misp.organizations.get(name="ACME Inc.")

# Create an event with the organization
event = misp.events.create(
    info="Suspicious Activity Report",
    published=False,
    distribution=Distribution.YOUR_ORGANIZATION_ONLY,
    threat_level=ThreatLevel.MEDIUM,
    analysis=Analysis.INITIAL,
    organization=organization
)
```

### Filtering Events by Organization
```python
# List events from a specific organization
organization = misp.organizations.get(name="ACME Inc.")
for event in misp.list(EventCriteria(org_id=organization.id)):
    print(f"Event: {event.info}")
```

### Organization Sectors
```python
# Get organization with sector information
organization = misp.organizations.get(name="ACME Inc.")
print(f"Organization: {organization.name}")
print(f"Sector: {organization.sector}")
print(f"Type: {organization.type}")
```
