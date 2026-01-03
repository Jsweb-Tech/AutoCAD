# Utilities

Utility functions for working with AutoCAD.

## is_autocad_installed()

Check if AutoCAD is installed on the system.

```python
from AutoCAD import is_autocad_installed

if is_autocad_installed():
    print("AutoCAD is installed")
else:
    print("AutoCAD is not installed")
```

### Returns

`bool` - True if AutoCAD is found, False otherwise

## is_autocad_running()

Check if an AutoCAD process is currently running.

```python
from AutoCAD import is_autocad_running

if is_autocad_running():
    print("AutoCAD is running")
    cad = AutoCAD()  # Safe to initialize
else:
    print("Please open AutoCAD first")
```

### Returns

`bool` - True if AutoCAD process is running, False otherwise

## CADException

Custom exception for AutoCAD-related errors.

```python
from AutoCAD import CADException

try:
    cad = AutoCAD()
    circle = cad.add_circle(APoint(0, 0, 0), 5)
except CADException as e:
    print(f"Error: {e}")
```

### Constructor

```python
raise CADException("Error message here")
```

## See Also

- [AutoCAD Class](autocad.md)
- [Error Handling](../getting-started/concepts.md#error-handling)
