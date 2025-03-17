from typing import Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict
from pymisp import MISPAttribute, MISPEvent, MISPGalaxy, MISPGalaxyCluster, MISPObject, PyMISP

from openmisp.galaxies import GalaxyCriteria, GalaxyService

from .validators import validate_client, validate_criteria_type, validate_entity_type, validate_same_type


class ClusterCriteria(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    value: Optional[str] = None
    meta: Optional[Dict[str, str]] = None
    galaxy: Optional[MISPGalaxy] = None
    fulltext: bool = False


class ClusterService:
    def __init__(self, client: PyMISP):
        validate_client(client, raise_error=True)
        self._client = client
        self._galaxy_service = GalaxyService(client)

    def list(
        self, entity: Union[MISPEvent, MISPObject, MISPAttribute], criteria: Optional[ClusterCriteria] = None
    ) -> List[MISPGalaxyCluster]:
        validate_entity_type(entity, (MISPAttribute, MISPEvent, MISPObject), raise_error=True)

        if criteria and criteria.galaxy:
            clusters = [
                _cluster
                for _galaxy in entity.galaxies
                for _cluster in _galaxy.clusters
                if _galaxy.uuid == criteria.galaxy.uuid
            ]
        else:
            clusters = [cluster for cluster in entity.tags if cluster.name.startswith("misp-galaxy:")]

        if criteria and criteria.value:
            clusters = [
                cluster for cluster in clusters if criteria.value == cluster.value or criteria.value in cluster.synonyms
            ]

        return clusters

    def get(
        self, entity: Union[MISPEvent, MISPObject, MISPAttribute], criteria: ClusterCriteria
    ) -> Optional[MISPGalaxyCluster]:
        validate_entity_type(entity, (MISPAttribute, MISPEvent, MISPObject), raise_error=True)
        validate_criteria_type(criteria, ClusterCriteria, raise_error=True)

        clusters = self.list(entity, criteria)
        if clusters:
            return clusters[0]
        return None

    def exists(self, entity: Union[MISPEvent, MISPObject, MISPAttribute], criteria: ClusterCriteria) -> bool:
        validate_entity_type(entity, (MISPAttribute, MISPEvent, MISPObject), raise_error=True)
        validate_criteria_type(criteria, ClusterCriteria, raise_error=True)

        return bool(self.get(entity, criteria))

    def _parent_link(self, entity: Union[MISPAttribute, MISPEvent, MISPObject], cluster: MISPGalaxyCluster) -> bool:
        validate_entity_type(cluster, MISPGalaxyCluster, raise_error=True)
        validate_entity_type(entity, (MISPAttribute, MISPEvent, MISPObject), raise_error=True)

        self._parent_unlink(entity, cluster)

        entity.add_tag(cluster)
        entity.edited = True
        return True

    def _parent_unlink(self, entity: Union[MISPAttribute, MISPEvent, MISPObject], cluster: MISPGalaxyCluster) -> bool:
        validate_entity_type(cluster, MISPGalaxyCluster, raise_error=True)
        validate_entity_type(entity, (MISPAttribute, MISPEvent, MISPObject), raise_error=True)

        for index, tag in enumerate(entity.tags):
            if tag.value == cluster.value:
                entity.tags.pop(index)
                entity.edited = True
                return True

        return False

    def _parent_sync(
        self, current: Union[MISPEvent, MISPObject, MISPAttribute], new: Union[MISPEvent, MISPObject, MISPAttribute]
    ) -> bool:
        validate_same_type(current, new, raise_error=True)
        validate_entity_type(current, (MISPEvent, MISPObject, MISPAttribute), raise_error=True)
        validate_entity_type(new, (MISPEvent, MISPObject, MISPAttribute), raise_error=True)

        for current_cluster in self.list(current):
            for cluster in self.list(new):
                if current_cluster.value == cluster.value:
                    break
            else:
                self._client.untag(current.uuid, current_cluster)

    def _list(self, criteria: ClusterCriteria) -> List[MISPGalaxyCluster]:
        validate_criteria_type(criteria, ClusterCriteria, raise_error=True)

        clusters = dict()

        galaxy_criteria = GalaxyCriteria()
        if criteria.galaxy:
            galaxy_criteria = GalaxyCriteria(name=criteria.galaxy.name, namespace=criteria.galaxy.namespace)

        for galaxy in self._galaxy_service._list(galaxy_criteria):
            _clusters = self._client.search_galaxy_clusters(searchall=criteria.value, galaxy=galaxy, pythonify=True)

            if _clusters is None:
                continue

            for _cluster in _clusters:
                if criteria.fulltext is True:
                    clusters[_cluster.uuid] = _cluster

                if criteria.value == _cluster.value:
                    clusters[_cluster.uuid] = _cluster

                if hasattr(_cluster, "synonyms") and criteria.value in _cluster.synonyms:
                    clusters[_cluster.uuid] = _cluster

        return list(clusters.values())
