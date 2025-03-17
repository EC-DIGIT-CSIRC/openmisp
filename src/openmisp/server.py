from pymisp import PyMISP

from .validators import validate_client


class ServerService:
    def __init__(self, client: PyMISP):
        validate_client(client)
        self._client = client

    def healthcheck(self) -> bool:
        return "errors" not in self._client.server_settings()

    def settings(self) -> dict:
        return self._client.server_settings()

    def version(self) -> str:
        return self._client.misp_instance_version.get("version")
