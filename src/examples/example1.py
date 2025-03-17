import os
import sys
from datetime import datetime, timezone

from openmisp import (
    MISP,
    Analysis,
    AttributeCategory,
    AttributeCriteria,
    AttributeType,
    ClusterCriteria,
    # Confidence,
    Distribution,
    EventCriteria,
    GalaxyCriteria,
    ObjectRelation,
    ObjectType,
    OrganizationCriteria,
    SharingGroupCriteria,
    SightingType,
    ThreatLevel,
)

misp = MISP(url=os.getenv("MISP_URL"), key=os.getenv("MISP_KEY"), ssl=False)

galaxy = misp.get(GalaxyCriteria(name="Threat Actor", namespace="misp", value="APT29"))
cluster = misp.get(ClusterCriteria(value="APT29", galaxy=galaxy))
clusters = misp.list(ClusterCriteria(value="APT29", galaxy=galaxy))

sharing_group = misp.get(SharingGroupCriteria(name="Test Sharing Group"))
organization = misp.get(OrganizationCriteria(name="ORGNAME"))
# sharing_group = misp.get(type=SharingGroup, name="Test Sharing Group")
# organization = misp.get(type=Organization, name="ORGNAME")

event = misp.get(EventCriteria(uuid="ca0adec9-9eac-44d8-ba24-c5b7e98bbcb1"))


if not sharing_group or not organization:
    print("Error: This example requires a sharing group named 'Test Sharing Group' and an organization named 'ORGNAME'")
    print("Please create these in your MISP instance first or modify the example to use existing ones.")
    sys.exit(1)

tag_openmisp = misp.tags.create(name="OpenMISP") or misp.tags.create(name="OpenMISPZX") or None
tag_random = misp.tags.create(name="Random")

event = misp.events.create(
    info="Test event",
    published=False,
    sharing_group=sharing_group,
    distribution=Distribution.SHARING_GROUP,
    threat_level=ThreatLevel.MEDIUM,
    analysis=Analysis.ONGOING,
    organization=organization,
)
# misp.utils.confidence.set(event, Confidence.COMPLETELY_CONFIDENT)
misp.sync(event)

misp.events.link(event, tag_openmisp)
misp.sync(event)

misp.events.unlink(event, tag_openmisp)
misp.sync(event)

misp.events.link(event, tag_openmisp)
misp.sync(event)

misp.tags.edit(tag_openmisp, name=tag_openmisp.name + ".v2")
misp.sync(event)

attribute1 = misp.attributes.create(
    type=AttributeType.IP_DST,
    category=AttributeCategory.NETWORK_ACTIVITY,
    value="192.168.1.1",
    detection=True,
    correlation=False,
    distribution=Distribution.YOUR_ORGANIZATION_ONLY,
)
misp.attributes.link(attribute1, tag_openmisp)

misp.events.link(event, attribute1)
misp.sync(event)

misp.attributes.edit(attribute1, value="192.168.1.111")
misp.sync(event)

for attribute in misp.attributes.list(event, criteria=AttributeCriteria(type=AttributeType.IP_DST)):
    attribute.value = "8.8.8.8"

misp.sync(event)

print("Creating attribute 2 ...")
attribute2 = misp.attributes.create(
    type=AttributeType.DOMAIN,
    category=AttributeCategory.NETWORK_ACTIVITY,
    value="example-domain-test.com",
    detection=True,
    correlation=False,
)
misp.attributes.link(attribute2, tag_openmisp)
misp.attributes.link(attribute2, tag_random)
misp.sync(event)

object_attribute1 = misp.attributes.create(
    relation=ObjectRelation.MD5_1,
    type=AttributeType.MD5,
    category=AttributeCategory.PAYLOAD_DELIVERY,
    value="40e556e3039b731ab4ee634c9cfad35a",
    detection=True,
    correlation=False,
)
object_attribute2 = misp.attributes.create(
    relation=ObjectRelation.URL_1,
    type=AttributeType.URL,
    category=AttributeCategory.NETWORK_ACTIVITY,
    value="https://crazy-domain-test.com",
    detection=True,
    correlation=False,
)

object1 = misp.objects.create(type=ObjectType.ARTIFACT)
misp.objects.link(object1, object_attribute1)
misp.objects.link(object1, object_attribute2)
misp.attributes.link(object_attribute2, tag_openmisp)
misp.events.link(event, object1)
misp.sync(event)

misp.attributes.edit(
    attribute=object_attribute1,
    value="3234567890abcdef1234567890abcdef",
)
misp.sync(event)

sighting = misp.sightings.create(
    attribute=object_attribute1,
    source="AlienVault",
    type=SightingType.SIGHTED,
    timestamp=datetime.now(timezone.utc),
)
misp.attributes.link(object_attribute1, sighting)
misp.sync(event)


print("Removing attribute 2 from tag openmisp ...")
misp.attributes.unlink(attribute2, tag_openmisp)

print("Linking attribute 2 ...")
misp.events.link(event, attribute2)
misp.sync(event)

print("Removing attribute 1 ...")
misp.events.unlink(event, attribute1)
misp.sync(event)

print("Linking attribute 2 to tag openmisp ...")
misp.attributes.link(attribute2, tag_openmisp)
misp.sync(event)

print("Performing attribute updates...")
misp.attributes.edit(attribute=attribute1, value="192.168.1.3", correlation=False)
misp.sync(event)

print("Creating final attribute ...")
attribute3 = misp.attributes.create(
    type=AttributeType.DOMAIN,
    category=AttributeCategory.NETWORK_ACTIVITY,
    value="example.com",
    detection=True,
    correlation=False,
)

print("Linking final attribute ...")
misp.events.link(event, attribute3)
misp.attributes.link(attribute3, tag_openmisp)

print("Removing final attribute ...")
misp.events.unlink(event, attribute3)

print("\nExample completed successfully!")
