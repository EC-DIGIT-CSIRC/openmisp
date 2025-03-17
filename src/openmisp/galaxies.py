from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict
from pymisp import MISPAttribute, MISPEvent, MISPGalaxy, MISPObject, PyMISP

from .validators import validate_client, validate_entity_type


class GalaxyCriteria(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: Optional[str] = None
    namespace: Optional[str] = None


class GalaxyService:
    def __init__(self, client: PyMISP):
        validate_client(client)
        self._client = client

    def list(self, entity: Union[MISPEvent, MISPObject, MISPAttribute], criteria: GalaxyCriteria) -> List[MISPGalaxy]:
        validate_entity_type(entity, (MISPEvent, MISPObject, MISPAttribute))
        validate_entity_type(criteria, GalaxyCriteria)

        galaxies = []
        for galaxy in entity.galaxies:
            if criteria.name and galaxy.name != criteria.name:
                continue
            if criteria.namespace and galaxy.namespace != criteria.namespace:
                continue
            galaxies.append(galaxy)
        return galaxies

    def get(
        self, entity: Union[MISPEvent, MISPObject, MISPAttribute], criteria: GalaxyCriteria
    ) -> Optional[MISPGalaxy]:
        """Get a galaxy based on criteria."""
        galaxies = self.list(entity, criteria)
        if galaxies:
            return galaxies[0]
        return None

    def exists(self, entity: Union[MISPEvent, MISPObject, MISPAttribute], criteria: GalaxyCriteria) -> bool:
        """Check if a galaxy exists based on criteria."""
        return bool(self.get(entity, criteria))

    def _list(self, criteria: Optional[GalaxyCriteria] = None) -> List[MISPGalaxy]:
        """Internal method to list galaxies."""
        if criteria is None:
            return self._client.galaxies(pythonify=True)

        validate_entity_type(criteria, GalaxyCriteria)

        galaxies = []
        for galaxy in self._client.galaxies(pythonify=True):
            if criteria.name and galaxy.name != criteria.name:
                continue
            if criteria.namespace and galaxy.namespace != criteria.namespace:
                continue
            galaxies.append(galaxy)

        return galaxies
