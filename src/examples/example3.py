import os
import sys

from openmisp import (
    MISP,
    Analysis,
    AttributeCategory,
    AttributeType,
    Distribution,
    EventCriteria,
    OrganizationCriteria,
    SharingGroupCriteria,
    ThreatLevel,
)

print("Initializing MISP client...")
misp = MISP(url=os.getenv("MISP_URL"), key=os.getenv("MISP_KEY"), ssl=False)

example = misp.get(criteria=EventCriteria(uuid="9729f023-41e1-40d3-8863-223908dcfba9"))

print("Getting sharing group and organization...")
sharing_group = misp.get(criteria=SharingGroupCriteria(name="Test Sharing Group"))
organization = misp.get(criteria=OrganizationCriteria(name="ORGNAME"))

if not sharing_group or not organization:
    print("Error: This example requires a sharing group named 'Test Sharing Group' and an organization named 'ORGNAME'")
    print("Please create these in your MISP instance first or modify the example to use existing ones.")
    sys.exit(1)

print("Creating tag...")
tag_openmisp = misp.tags.create(name="OpenMISP")
tag_random = misp.tags.create(name="Random")

print("Creating event...")
event = misp.events.create(
    info="Test event",
    published=False,
    sharing_group=sharing_group,
    distribution=Distribution.SHARING_GROUP,
    threat_level=ThreatLevel.MEDIUM,
    analysis=Analysis.ONGOING,
    organization=organization,
)
misp.sync(event)
misp.events.link(event, tag_openmisp)
misp.sync(event)

# print("Getting malware and actor...")
# malware = misp.malware.get(name="Cobalt Strike")
# actor = misp.actors.get(name="APT29")

# print("Linking malware and actor to event...")
# misp.events.link(event, malware)
# misp.events.link(event, actor)

print("Creating attribute 1 ...")
attribute1 = misp.attributes.create(
    type=AttributeType.IP_DST,
    category=AttributeCategory.NETWORK_ACTIVITY,
    value="192.168.1.1",
    detection=True,
)
misp.attributes.link(attribute1, tag_openmisp)
print("Linking attribute 1 ...")
misp.events.link(event, attribute1)
misp.sync(event)

# Now that we have an attribute, we can publish the event
event.published = True
misp.sync(event)

print("Creating attribute 2 ...")
attribute2 = misp.attributes.create(
    type=AttributeType.DOMAIN,
    category=AttributeCategory.NETWORK_ACTIVITY,
    value="example-domain-test.com",
    detection=True,
)
misp.attributes.link(attribute2, tag_openmisp)
misp.attributes.link(attribute2, tag_random)
misp.sync(event)

print("Unlinking attribute 2 from tag openmisp ...")
misp.attributes.unlink(attribute2, tag_openmisp)

print("Linking attribute 2 ...")
misp.events.link(event, attribute2)
misp.sync(event)

print("Unlinking attribute 1 ...")
misp.events.unlink(event, attribute1)
misp.sync(event)

print("Linking attribute 2 to tag openmisp ...")
misp.attributes.link(attribute2, tag_openmisp)
misp.sync(event)

print("Performing attribute updates...")
misp.attributes.edit(attribute=attribute1, value="192.168.1.2")
misp.sync(event)

print("Creating final attribute ...")
attribute3 = misp.attributes.create(
    type=AttributeType.DOMAIN,
    category=AttributeCategory.NETWORK_ACTIVITY,
    value="example.com",
    detection=True,
)

print("Linking final attribute ...")
misp.events.link(event, attribute3)
misp.attributes.link(attribute3, tag_openmisp)

print("Unlinking final attribute ...")
misp.events.unlink(event, attribute3)
misp.sync(event)

input("Press Enter to delete the event...")
misp.delete(event)

print("\nExample completed successfully!")
