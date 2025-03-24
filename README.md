# OpenMISP SDK

OpenMISP is a Python SDK built on top of [pymisp](https://github.com/MISP/PyMISP) to provide a more intuitive and analyst-friendly interface to interact with MISP. It abstracts analysts from the complexities of the underlying REST API by offering a clean, Pythonic interface with strong typing, comprehensive documentation, and simplified workflows. The SDK handles common MISP operations like managing events, attributes, tags and sharing groups while taking care of pymisp quirks.

## Installation

```bash
pip install git+https://github.com/ec-digit-csirc/openmisp.git@v0.0.1
```

## Usage

```python
# --- Create a client ---
from openmisp import MISPClient

misp = MISPClient(url="https://misp.example.com", api_key="your-api-key")


# --- Get a sharing group and organization ---
from openmisp import SharingGroupCriteria, OrganizationCriteria

sharing_group = misp.get(SharingGroupCriteria(name="Test Sharing Group"))
organization = misp.get(OrganizationCriteria(name="ORGNAME"))


# --- Create an event ---
from openmisp import Distribution, ThreatLevel, Analysis

event = misp.events.create(
    info="Test event",
    published=False,
    sharing_group=sharing_group,
    distribution=Distribution.SHARING_GROUP,
    threat_level=ThreatLevel.MEDIUM,
    analysis=Analysis.ONGOING,
    organization=organization,
)


# --- Create a tag ---
tag = misp.tags.create(name="OpenMISP")


# --- Link the tag to the event ---
misp.events.link(event, tag)


# --- Create an attribute ---
attribute1 = misp.attributes.create(
    type=AttributeType.IP_DST,
    category=AttributeCategory.NETWORK_ACTIVITY,
    value="192.168.1.1",
    detection=True,
    correlation=False,
    distribution=Distribution.YOUR_ORGANIZATION_ONLY,
)


# --- Link the tag to the attribute ---
misp.attributes.link(attribute1, tag)


# --- Link the attribute to the event ---
misp.events.link(event, attribute1)


# --- Sync the event ---
misp.sync(event)
```

## Development

### Setup

```bash
# Fork the repository
git clone https://github.com/your-username/openmisp.git
cd openmisp
make sync

source .venv/bin/activate
```
