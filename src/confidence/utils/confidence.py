from pymisp import MISPAttribute, MISPEvent, PyMISP

from ..models.confidence import Confidence
from ..tags import TagService
from ..validators import validate_client, validate_entity_type


class ConfidenceService:
    def __init__(self, client: PyMISP):
        validate_client(client)
        self._client = client
        self._tag_service = TagService(client)

    def set(self, entity: MISPEvent | MISPAttribute, confidence: Confidence):
        validate_entity_type(entity, (MISPEvent, MISPAttribute))
        validate_entity_type(confidence, Confidence)

        for tag in entity.tags:
            if tag.name.startswith('misp:confidence-level="'):
                self._tag_service._parent_unlink(entity, tag)
                break

        self._tag_service._parent_link(entity, confidence.value)
