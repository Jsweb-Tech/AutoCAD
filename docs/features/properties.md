# Drawing Properties

Manage document metadata including title, author, custom properties, and more.

## Overview

The Drawing Properties feature provides a complete Python interface for managing AutoCAD drawing metadata. This is equivalent to the VBA `ThisDrawing.SummaryInfo` object.

!!! tip
    Access drawing properties via `cad.properties` after initializing AutoCAD.

## General Properties

Set and retrieve basic document information:

=== "Setting Properties"

    ```python
    cad.properties.set_title("My Drawing")
    cad.properties.set_subject("Manufacturing Floor Plan")
    cad.properties.set_author("Engineering Team")
    cad.properties.set_keywords("factory, design, equipment")
    cad.properties.set_comments("Updated for Q1 2026")
    ```

=== "Getting Properties"

    ```python
    title = cad.properties.get_title()
    subject = cad.properties.get_subject()
    author = cad.properties.get_author()
    keywords = cad.properties.get_keywords()
    comments = cad.properties.get_comments()
    ```

## Summary Properties

Additional document metadata:

```python
# Set
cad.properties.set_manager("John Smith")
cad.properties.set_company("Manufacturing Corp")
cad.properties.set_category("Facility Design")

# Get
manager = cad.properties.get_manager()
company = cad.properties.get_company()
category = cad.properties.get_category()
```

## Statistics (Read-Only)

Access document information:

```python
# Creation information
created = cad.properties.get_created_date()
modified = cad.properties.get_modified_date()
saved_by = cad.properties.get_last_saved_by()

# Editing information
edit_time = cad.properties.get_edit_time()  # in seconds
revision = cad.properties.get_revision_number()
```

## Custom Properties

Store user-defined metadata in your drawings:

### Adding Custom Properties

```python
cad.properties.add_custom_property("ProjectID", "PROJ-2026-001")
cad.properties.add_custom_property("Budget", "$500,000")
cad.properties.add_custom_property("StartDate", "2026-01-15")
```

### Getting Custom Properties

```python
# Get specific property
project_id = cad.properties.get_custom_property("ProjectID")

# Get count (Python equivalent of VBA NumCustomInfo)
count = cad.properties.get_num_custom_info()

# Get all as dictionary
all_props = cad.properties.get_all_custom_properties()
for name, value in all_props.items():
    print(f"{name}: {value}")
```

### Updating Custom Properties

```python
cad.properties.update_custom_property("ProjectID", "PROJ-2026-002")
```

### Removing Custom Properties

```python
# Remove one
cad.properties.remove_custom_property("Budget")

# Remove all
cad.properties.clear_all_custom_properties()
```

## Complete Example

```python
from AutoCAD import AutoCAD

def setup_drawing_metadata():
    """Setup complete drawing metadata"""
    
    cad = AutoCAD()
    
    # General properties
    cad.properties.set_title("Warehouse Layout - Phase 2")
    cad.properties.set_author("Design Team")
    cad.properties.set_subject("Warehouse Redesign")
    cad.properties.set_keywords("warehouse, logistics, layout")
    cad.properties.set_comments("Updated for 2026")
    
    # Summary properties
    cad.properties.set_manager("Operations Manager")
    cad.properties.set_company("Logistics Inc.")
    cad.properties.set_category("Facility Design")
    
    # Custom properties
    custom_props = {
        "ProjectID": "WH-2026-REDESIGN",
        "Location": "Austin, TX",
        "Budget": "$500,000",
        "StartDate": "2026-01-15",
        "Deadline": "2026-06-30",
        "Status": "In Progress"
    }
    
    for name, value in custom_props.items():
        cad.properties.add_custom_property(name, value)
    
    # Display results
    print(f"Title: {cad.properties.get_title()}")
    print(f"Custom properties count: {cad.properties.get_num_custom_info()}")
    
    all_custom = cad.properties.get_all_custom_properties()
    print("All custom properties:")
    for name, value in all_custom.items():
        print(f"  {name}: {value}")
    
    # Save
    cad.save()

setup_drawing_metadata()
```

## VBA to Python Mapping

| VBA | Python |
|---|---|
| `NumCustomInfo` | `get_num_custom_info()` |
| `GetCustomByIndex(i)` | `get_all_custom_properties()` |
| `GetCustomValue(name)` | `get_custom_property(name)` |
| `SetCustomByKey(name, val)` | `add_custom_property(name, val)` |
| `RemoveCustomByKey(name)` | `remove_custom_property(name)` |

## API Methods

### General Properties
- `get_title()` → str
- `set_title(value: str)`
- `get_subject()` → str
- `set_subject(value: str)`
- `get_author()` → str
- `set_author(value: str)`
- `get_keywords()` → str
- `set_keywords(value: str)`
- `get_comments()` → str
- `set_comments(value: str)`

### Summary Properties
- `get_manager()` → str
- `set_manager(value: str)`
- `get_company()` → str
- `set_company(value: str)`
- `get_category()` → str
- `set_category(value: str)`

### Statistics (Read-Only)
- `get_created_date()` → str
- `get_modified_date()` → str
- `get_last_saved_by()` → str
- `get_edit_time()` → int
- `get_revision_number()` → str

### Custom Properties
- `get_num_custom_info()` → int
- `get_all_custom_properties()` → dict
- `add_custom_property(name: str, value: str)`
- `get_custom_property(name: str)` → str
- `update_custom_property(name: str, value: str)`
- `remove_custom_property(name: str)`
- `clear_all_custom_properties()`

## Tips & Tricks

!!! tip "Project Tracking"
    Use custom properties to track project metadata:
    ```python
    cad.properties.add_custom_property("ProjectID", "PROJ-001")
    cad.properties.add_custom_property("ClientID", "CLIENT-A")
    cad.properties.add_custom_property("Version", "1.0")
    ```

!!! tip "Batch Updates"
    Update multiple properties efficiently:
    ```python
    props = {
        "Status": "Approved",
        "ApprovedDate": "2026-01-03",
        "ApprovedBy": "John Smith"
    }
    for name, value in props.items():
        cad.properties.add_custom_property(name, value)
    ```

!!! tip "Save After Changes"
    Always save your document after modifying properties:
    ```python
    cad.properties.set_title("New Title")
    cad.save()  # Important!
    ```

## See Also

- [Quick Start](../getting-started/quickstart.md) - Quick example with properties
- [API Reference](../api/properties.md) - Complete API details
- [Examples](../examples/metadata.md) - More examples
