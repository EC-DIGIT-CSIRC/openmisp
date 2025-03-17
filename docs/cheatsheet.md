# Methods Overview

This page provides a comprehensive overview of all available methods in the OpenMISP SDK, organized by service.

## MISP

All these actions will be on the MISP server directly.

| Method | Description | Example |
|--------|-------------|---------|
| `misp.sync(entity)` | Synchronize an entity with the MISP server | `misp.sync(event)` |
| `misp.delete(entity)` | Delete an entity from the MISP server | `misp.delete(event)` |
| `misp.get(criteria)` | Get a single entity matching criteria | `misp.get(EventCriteria(uuid="..."))` |
| `misp.exists(criteria)` | Check if an entity exists | `misp.exists(EventCriteria(uuid="..."))` |
| `misp.list(criteria)` | List entities matching criteria | `misp.list(EventCriteria(published=True))` |

## Server

All these actions will be on the MISP server directly.

| Method | Description | Example |
|--------|-------------|---------|
| `misp.server.healthcheck()` | Check if the MISP server is running | `health = misp.server.healthcheck()` |
| `misp.server.settings()` | Get server settings | `settings = misp.server.settings()` |
| `misp.server.version()` | Get server version information | `version = misp.server.version()` |

## Events

All these actions will only be local until a `misp.sync(...)` is called.

| Method | Description | Example |
|--------|-------------|---------|
| `misp.events.create(...)` | Create a new event | `event = misp.events.create(info="...", distribution=...)` |
| `misp.events.edit(event, ...)` | Edit an existing event | `misp.events.edit(event, info="Updated info")` |
| `misp.events.link(event, target)` | Link an entity to an event | `misp.events.link(event, attribute)` |
| `misp.events.unlink(event, target)` | Unlink an entity from an event | `misp.events.unlink(event, attribute)` |

## Attributes

All these actions will only be local until a `misp.sync(...)` is called.

| Method | Description | Example |
|--------|-------------|---------|
| `misp.attributes.create(...)` | Create a new attribute | `attribute = misp.attributes.create(type=AttributeType.IP_DST, value="...")` |
| `misp.attributes.edit(attribute, ...)` | Edit an existing attribute | `misp.attributes.edit(attribute, value="...")` |
| `misp.attributes.get(from, ...)` | Get an attribute by criteria | `attribute = misp.attributes.get(from=event, type=AttributeType.IP_DST)` |
| `misp.attributes.exists(from, ...)` | Check if an attribute exists | `exists = misp.attributes.exists(from=event, value="...")` |
| `misp.attributes.list(from, ...)` | List attributes matching criteria | `for attr in misp.attributes.list(from=event): ...` |
| `misp.attributes.link(attribute, target)` | Link an entity to an attribute | `misp.attributes.link(attribute, tag)` |
| `misp.attributes.unlink(attribute, target)` | Unlink an entity from an attribute | `misp.attributes.unlink(attribute, tag)` |

## Objects

All these actions will only be local until a `misp.sync(...)` is called.

| Method | Description | Example |
|--------|-------------|---------|
| `misp.objects.create(...)` | Create a new object | `obj = misp.objects.create(name="file", description="...")` |
| `misp.objects.edit(object, ...)` | Edit an existing object | `misp.objects.edit(obj, description="...")` |
| `misp.objects.get(from, ...)` | Get an object by criteria | `obj = misp.objects.get(from=event, name="file")` |
| `misp.objects.exists(from, ...)` | Check if an object exists | `exists = misp.objects.exists(from=event, name="file")` |
| `misp.objects.list(from, ...)` | List objects matching criteria | `for obj in misp.objects.list(from=event): ...` |
| `misp.objects.link(object, target)` | Link an entity to an object | `misp.objects.link(obj, tag)` |
| `misp.objects.unlink(object, target)` | Unlink an entity from an object | `misp.objects.unlink(obj, tag)` |

## Tags

All these actions will only be local until a `misp.sync(...)` is called.

| Method | Description | Example |
|--------|-------------|---------|
| `misp.tags.create(...)` | Create a new tag | `tag = misp.tags.create(name="tlp:amber")` |
| `misp.tags.edit(tag, ...)` | Edit an existing tag | `misp.tags.edit(tag, colour="#FF0000")` |
| `misp.tags.get(...)` | Get a tag by criteria | `tag = misp.tags.get(name="tlp:amber")` |
| `misp.tags.exists(...)` | Check if a tag exists | `exists = misp.tags.exists(name="tlp:amber")` |
| `misp.tags.list(...)` | List tags matching criteria | `for tag in misp.tags.list(): ...` |

## Galaxies

All these actions will only be local until a `misp.sync(...)` is called.

| Method | Description | Example |
|--------|-------------|---------|
| `misp.galaxies.get(...)` | Get a galaxy by criteria | `galaxy = misp.galaxies.get(name="threat-actor")` |
| `misp.galaxies.exists(...)` | Check if a galaxy exists | `exists = misp.galaxies.exists(name="threat-actor")` |
| `misp.galaxies.list(...)` | List galaxies matching criteria | `for galaxy in misp.galaxies.list(): ...` |

## Clusters

All these actions will only be local until a `misp.sync(...)` is called.

| Method | Description | Example |
|--------|-------------|---------|
| `misp.clusters.get(from, ...)` | Get a cluster by criteria | `cluster = misp.clusters.get(from=galaxy, name="APT28")` |
| `misp.clusters.exists(from, ...)` | Check if a cluster exists | `exists = misp.clusters.exists(from=galaxy, name="APT28")` |
| `misp.clusters.list(from, ...)` | List clusters matching criteria | `for cluster in misp.clusters.list(from=galaxy): ...` |

## Criterias

These criterias are used to filter the entities returned by the methods `get`, `exists`, `list`.

| Method | Description | Example |
|--------|-------------|---------|
| `EventCriteria(...)` | Event criteria | `criteria = EventCriteria(published=True)` |
| `ObjectCriteria(...)` | Object criteria | `criteria = ObjectCriteria(name="file")` |
| `AttributeCriteria(...)` | Attribute criteria | `criteria = AttributeCriteria(type=AttributeType.IP_DST)` |
| `TagCriteria(...)` | Tag criteria | `criteria = TagCriteria(name="tlp:amber")` |
| `GalaxyCriteria(...)` | Galaxy criteria | `criteria = GalaxyCriteria(name="threat-actor")` |
| `ClusterCriteria(...)` | Cluster criteria | `criteria = ClusterCriteria(name="APT28")` |
| `OrganizationCriteria(...)` | Organization criteria | `criteria = OrganizationCriteria(name="ACME Inc.")` |
| `SharingGroupCriteria(...)` | Sharing group criteria | `criteria = SharingGroupCriteria(name="Financial Sector")` |
