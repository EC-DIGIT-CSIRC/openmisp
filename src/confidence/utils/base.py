from pymisp import PyMISP

from ..validators import validate_client
from .confidence import ConfidenceService


class UtilsService:
    def __init__(self, client: PyMISP):
        validate_client(client)
        self._client = client
        self.confidence = ConfidenceService(self._client)
