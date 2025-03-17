import os

from openmisp import (
    MISP,
    Analysis,
    AttributeCategory,
    AttributeCriteria,
    AttributeType,
    Distribution,
    EventCriteria,
    OrganizationCriteria,
    SharingGroupCriteria,
    TagCriteria,
    ThreatLevel,
)

misp = MISP(url=os.getenv("MISP_URL"), key=os.getenv("MISP_KEY"), ssl=False)

healthcheck = misp.server.healthcheck()
print(f"Healthcheck: {healthcheck}")
version = misp.server.version()
print(f"Version: {version}")

sharing_group = misp.get(SharingGroupCriteria(name="Test Sharing Group"))

organization = misp.get(OrganizationCriteria(name="ORGNAME"))


event = misp.events.create(
    published=False,
    info="nice one",
    organization=organization,
    distribution=Distribution.YOUR_ORGANIZATION_ONLY,
    threat_level=ThreatLevel.MEDIUM,
    analysis=Analysis.ONGOING,
)
misp.events.edit(event=event, analysis=Analysis.COMPLETED)

tag = misp.tags.create(name="team:source:feeds")
misp.tags.edit(tag=tag, name="team:source:MYFEEDS")

misp.events.link(event, tag)
misp.sync(event)

attribute = misp.attributes.create(
    value="8.8.8.8",
    category=AttributeCategory.NETWORK_ACTIVITY,
    type=AttributeType.IP_DST,
    detection=True,
    correlation=False,
)
misp.attributes.edit(attribute=attribute, value="8.8.4.4")

misp.events.link(event, attribute)
misp.sync(event)

misp.attributes.edit(attribute=attribute, value="8.8.3.3")
misp.events.link(event, attribute)

attribute = misp.attributes.create(
    value="example.com",
    category=AttributeCategory.NETWORK_ACTIVITY,
    type=AttributeType.DOMAIN,
    detection=True,
    correlation=False,
)
misp.events.link(event, attribute)

misp.events.edit(event=event, published=True)
misp.sync(event)

tags = misp.tags.list(event, criteria=TagCriteria(pattern="team:"))
for tag in tags:
    misp.tags.edit(tag=tag, name=f"{tag.name}-v2")
    misp.events.link(event, tag)


tag = misp.tags.create(name="dangerous")
for attribute in misp.attributes.list(
    event,
    criteria=AttributeCriteria(type=AttributeType.IP_DST),
):
    misp.attributes.link(attribute, tag)

misp.sync(event)

events = misp.list(EventCriteria(published=True))
print(f"Event: {events[0].info}")
