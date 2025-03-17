from pydantic import BaseModel
from pymisp import MISPTaxonomy, PyMISP

from .models.taxonomies.utils import get_all_taxonomies
from .validators import validate_criteria_type


class TaxonomyCriteria(BaseModel):
    name: str | None = None
    namespace: str | None = None


class TaxonomyService:
    def __init__(self, client: PyMISP):
        self._client = client
        self._taxonomies = get_all_taxonomies()

    def _list(self, criteria: TaxonomyCriteria | None = None) -> list[MISPTaxonomy]:
        validate_criteria_type(criteria, TaxonomyCriteria, raise_error=True)

        taxonomies = self._client.taxonomies(pythonify=True)
        if criteria is None:
            return taxonomies
        for taxonomy in taxonomies:
            if taxonomy.name == criteria.name and taxonomy.namespace == criteria.namespace:
                yield taxonomy
