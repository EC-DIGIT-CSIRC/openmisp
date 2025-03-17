from typing import Generator

from pydantic import BaseModel
from pymisp import MISPSharingGroup, PyMISP

from .validators import validate_client, validate_entity_type


class SharingGroupCriteria(BaseModel):
    name: str | None = None


class SharingGroupService:
    def __init__(self, client: PyMISP):
        validate_client(client)
        self.client = client

    def _list(self, criteria: SharingGroupCriteria) -> Generator[MISPSharingGroup, None, None]:
        validate_entity_type(criteria, SharingGroupCriteria)

        sharing_groups = self.client.sharing_groups(pythonify=True)

        for sharing_group in sharing_groups:
            if criteria.name and sharing_group.name != criteria.name:
                continue
            yield sharing_group

        yield
