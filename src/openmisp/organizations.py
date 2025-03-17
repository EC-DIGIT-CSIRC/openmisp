from typing import Generator

from pydantic import BaseModel
from pymisp import MISPOrganisation, PyMISP

from .validators import validate_client, validate_entity_type


class OrganizationCriteria(BaseModel):
    name: str | None = None


class OrganizationService:
    def __init__(self, client: PyMISP):
        validate_client(client)
        self._client = client

    def _list(self, criteria: OrganizationCriteria) -> Generator[MISPOrganisation, None, None]:
        validate_entity_type(criteria, OrganizationCriteria)

        organizations = self._client.organisations(pythonify=True)

        for organization in organizations:
            if criteria.name and organization.name != criteria.name:
                continue
            yield organization

        yield
