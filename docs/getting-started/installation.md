# Installation

## Requirements

Before installing the AutoCAD Python Library, ensure you have:

- **Python 3.8 or higher**
- **AutoCAD 2010 or later**
- **Windows OS** (COM support is Windows-only)
- **pip** (Python package manager)

## Installation Steps

### 1. Install via pip (Recommended)

```bash
pip install AutoCAD
```

### 2. Verify Installation

```python
from AutoCAD import AutoCAD

# This should initialize without errors
cad = AutoCAD()
print("AutoCAD library installed successfully!")
```

## Dependencies

The library automatically installs these dependencies:

- **pywin32** - For COM (Component Object Model) interface with AutoCAD
- **psutil** - For process management

### Manual Dependency Installation

If you encounter issues, install dependencies manually:

```bash
pip install pywin32
pip install psutil
pip install pythoncom
```

## Troubleshooting

### "Cannot find AutoCAD.Application"

This error means AutoCAD is not installed on your system. You need to:

1. Install AutoCAD from Autodesk
2. Ensure AutoCAD is properly registered in Windows

### "pywin32 not found"

Install it manually:

```bash
pip install pywin32
python -m pip install pywin32
```

### AutoCAD is not running

By default, the library tries to connect to an existing AutoCAD instance. You can check:

```python
from AutoCAD import is_autocad_running

if is_autocad_running():
    print("AutoCAD is running")
else:
    print("Please open AutoCAD first")
```

## Development Installation

To contribute to the project:

```bash
# Clone the repository
git clone https://github.com/Jones-peter/AutoCAD.git
cd AutoCAD

# Install in development mode
pip install -e .

# Install development dependencies
pip install pytest black flake8
```

## Docker (Experimental)

While Docker doesn't support COM directly, you can use WSL2 with Docker:

```dockerfile
FROM python:3.11

WORKDIR /app

RUN pip install AutoCAD

COPY . .

CMD ["python", "your_script.py"]
```

## IDE Setup

### VS Code

Add to your `.vscode/settings.json`:

```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true
    }
}
```

### PyCharm

1. Go to `Settings > Project > Python Interpreter`
2. Click the `+` button
3. Search for "AutoCAD"
4. Install the package

## Next Steps

- 📖 Read the [Quick Start Guide](quickstart.md)
- 🎓 Learn the [Basic Concepts](concepts.md)
- 💻 Check out [Examples](../examples/basic.md)
