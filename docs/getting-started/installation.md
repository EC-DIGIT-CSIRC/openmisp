# Installation Guide

This guide will help you install and set up the OpenMISP in your environment.

## Installation Methods

### Using pip

The recommended way to install OpenMISP is using pip:

```bash
pip install openmisp
```

### From Source

To install from source:

```bash
git clone https://github.com/ec-digit-csirc/openmisp
cd openmisp
uv sync
```

## Configuration

### Environment Variables

OpenMISP can be configured using environment variables:

```bash
export MISP_URL="https://your-misp-instance.com"
export MISP_KEY="your-api-key"
```

Alternatively, you can create a `.env` file:

```plaintext
MISP_URL=https://your-misp-instance.com
MISP_KEY=your-api-key
```

### Verifying Installation

You can verify your installation by running:

```python
import os
from openmisp import MISP

# Initialize the MISP client
misp = MISP(
    url=os.getenv("MISP_URL"),
    key=os.getenv("MISP_KEY"),
    ssl=False,  # Set to True in production environments
)

# This should print your MISP instance version
version = misp.server.version()
print(f"MISP Version: {version}")
```

## Next Steps

- Check out the [Quick Start Guide](quickstart.md) to begin using OpenMISP
- Review the [API Reference](../reference/misp.md) for detailed information about available features
- Try the [Basic Usage Examples](../examples/basic_usage.md)
