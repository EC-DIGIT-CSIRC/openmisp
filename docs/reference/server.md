# Server Reference

The Server API provides methods for interacting with the MISP server itself, allowing you to check server status, retrieve settings, and get version information.

## Initialization

The `ServerService` class is accessed through the MISP client:

```python
import os
from openmisp import MISP

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# Access the server service
server_service = misp.server
```

## Methods

### healthcheck

Check if the MISP server is running and accessible.

```python
# Check server health
health_status = misp.server.healthcheck()
print(f"Server is healthy: {health_status['status'] == 'ok'}")
```

Parameters: None

Returns:
- `dict`: A dictionary containing the server health status information.

### settings

Retrieve the current settings of the MISP server.

```python
# Get server settings
server_settings = misp.server.settings()
print(f"MISP version: {server_settings['version']}")
print(f"Base URL: {server_settings['baseurl']}")
```

Parameters: None

Returns:
- `dict`: A dictionary containing the server settings.

### version

Get the version information of the MISP server.

```python
# Get MISP version information
version = misp.server.version()
print(f"MISP version: {version['version']}")
print(f"PHP version: {version['php_version']}")
print(f"PyMISP version: {version['pymisp_version']}")
```

Parameters: None

Returns:
- `dict`: A dictionary containing version information.

## Use Cases

### Server Health Monitoring

```python
def check_misp_health(misp_client):
    """Monitor the health of a MISP server."""
    try:
        health = misp_client.server.healthcheck()
        if health['status'] == 'ok':
            print("MISP server is healthy")
            return True
        else:
            print(f"MISP server health check failed: {health}")
            return False
    except Exception as e:
        print(f"Error checking MISP server health: {e}")
        return False
```

### Version Compatibility Check

```python
def check_version_compatibility(misp_client, min_version="2.4.0"):
    """Check if the MISP server version is compatible."""
    try:
        version_info = misp_client.server.version()
        server_version = version_info['version']
        
        # Simple version comparison (you might want to use packaging.version for proper comparison)
        if server_version >= min_version:
            print(f"MISP server version {server_version} is compatible")
            return True
        else:
            print(f"MISP server version {server_version} is below minimum required {min_version}")
            return False
    except Exception as e:
        print(f"Error checking MISP server version: {e}")
        return False
```
