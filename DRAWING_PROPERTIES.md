# Drawing Properties Management Feature

This guide covers the Drawing Properties feature - a complete Python interface for managing AutoCAD drawing metadata, equivalent to VBA's `ThisDrawing.SummaryInfo`.

## Overview

The `DrawingProperties` class provides methods to access and modify:
- **General Properties**: Title, Subject, Author, Keywords, Comments
- **Summary Properties**: Manager, Company, Category  
- **Statistics** (Read-only): Creation date, Modification date, Edit time, Revision number
- **Custom Properties**: User-defined property pairs (get, create, remove, list)

This resolves the GitHub issue requesting Python equivalent for VBA's `ThisDrawing.SummaryInfo.NumCustomInfo`.

## Quick Start

```python
from AutoCAD import AutoCAD

# Initialize AutoCAD
autocad = AutoCAD()

# Set properties
autocad.properties.set_title("My Drawing")
autocad.properties.set_author("Jones Peter")

# Add custom properties
autocad.properties.add_custom_property("ProjectID", "PROJ-2026-001")

# Get custom properties count (equivalent to VBA NumCustomInfo)
num_custom = autocad.properties.get_num_custom_info()
print(f"Number of custom properties: {num_custom}")

# Get all custom properties
all_custom = autocad.properties.get_all_custom_properties()
print(all_custom)  # {'ProjectID': 'PROJ-2026-001'}

# Save
autocad.save()
```

## General Properties

### Setting and Getting General Properties

```python
# Title
autocad.properties.set_title("Factory Layout")
title = autocad.properties.get_title()

# Subject
autocad.properties.set_subject("Manufacturing Floor Plan")
subject = autocad.properties.get_subject()

# Author
autocad.properties.set_author("Engineering Team")
author = autocad.properties.get_author()

# Keywords (comma-separated)
autocad.properties.set_keywords("layout, manufacturing, equipment")
keywords = autocad.properties.get_keywords()

# Comments
autocad.properties.set_comments("Updated for Q1 2026 equipment upgrade")
comments = autocad.properties.get_comments()
```

## Summary Properties

```python
# Manager Name
autocad.properties.set_manager("John Smith")
manager = autocad.properties.get_manager()

# Company Name
autocad.properties.set_company("Manufacturing Corp Inc.")
company = autocad.properties.get_company()

# Category
autocad.properties.set_category("Facility Management")
category = autocad.properties.get_category()
```

## Statistics (Read-Only)

These properties provide document information and cannot be modified:

```python
# Creation Date
created = autocad.properties.get_created_date()

# Last Modification Date
modified = autocad.properties.get_modified_date()

# User who last saved the document
saved_by = autocad.properties.get_last_saved_by()

# Total editing time in seconds
edit_time = autocad.properties.get_edit_time()

# Revision Number
revision = autocad.properties.get_revision_number()
```

## Custom Properties

Custom properties allow you to store user-defined metadata.

### Adding Custom Properties

```python
# Add a single custom property
autocad.properties.add_custom_property("ProjectID", "PROJ-2026-001")
autocad.properties.add_custom_property("ClientName", "Acme Corp")
autocad.properties.add_custom_property("DrawingVersion", "1.0")
```

### Getting Custom Properties

```python
# Get a specific custom property
project_id = autocad.properties.get_custom_property("ProjectID")

# Get number of custom properties (Python equivalent of VBA NumCustomInfo)
count = autocad.properties.get_num_custom_info()

# Get all custom properties as a dictionary
all_props = autocad.properties.get_all_custom_properties()
for key, value in all_props.items():
    print(f"{key}: {value}")
```

### Updating and Removing Custom Properties

```python
# Update an existing custom property
autocad.properties.update_custom_property("DrawingVersion", "1.1")

# Remove a single custom property
autocad.properties.remove_custom_property("ClientName")

# Clear all custom properties
autocad.properties.clear_all_custom_properties()
```

## Complete Example

```python
from AutoCAD import AutoCAD
import time

def setup_drawing_metadata():
    """Complete example of setting up drawing metadata"""
    
    autocad = AutoCAD()
    time.sleep(1)
    
    # Set general properties
    autocad.properties.set_title("Warehouse Layout - Phase 2")
    autocad.properties.set_subject("Warehouse Redesign")
    autocad.properties.set_author("Design Team")
    autocad.properties.set_keywords("warehouse, logistics, design")
    autocad.properties.set_comments("Updated layout for increased storage")
    
    # Set summary properties
    autocad.properties.set_manager("Operations Director")
    autocad.properties.set_company("Logistics Solutions Inc.")
    autocad.properties.set_category("Facility Design")
    
    # Add custom properties for project tracking
    project_meta = {
        "ProjectID": "WH-2026-REDESIGN",
        "Location": "Austin, TX - Building C",
        "Budget": "$500,000",
        "StartDate": "2026-01-15",
        "ExpectedCompletion": "2026-06-30",
    }
    
    for property_name, property_value in project_meta.items():
        autocad.properties.add_custom_property(property_name, property_value)
    
    # Display results
    print(f"Title: {autocad.properties.get_title()}")
    print(f"Custom properties: {autocad.properties.get_num_custom_info()}")
    
    # Save
    autocad.save()

setup_drawing_metadata()
```

## VBA to Python Equivalents

| VBA | Python |
|---|---|
| `ThisDrawing.SummaryInfo.Title` | `autocad.properties.set_title()` / `get_title()` |
| `ThisDrawing.SummaryInfo.Subject` | `autocad.properties.set_subject()` / `get_subject()` |
| `ThisDrawing.SummaryInfo.Author` | `autocad.properties.set_author()` / `get_author()` |
| `ThisDrawing.SummaryInfo.Keywords` | `autocad.properties.set_keywords()` / `get_keywords()` |
| `ThisDrawing.SummaryInfo.Comments` | `autocad.properties.set_comments()` / `get_comments()` |
| `ThisDrawing.SummaryInfo.Manager` | `autocad.properties.set_manager()` / `get_manager()` |
| `ThisDrawing.SummaryInfo.Company` | `autocad.properties.set_company()` / `get_company()` |
| `ThisDrawing.SummaryInfo.Category` | `autocad.properties.set_category()` / `get_category()` |
| `ThisDrawing.SummaryInfo.CreateTime` | `autocad.properties.get_created_date()` |
| `ThisDrawing.SummaryInfo.ModTime` | `autocad.properties.get_modified_date()` |
| `ThisDrawing.SummaryInfo.LastSavedBy` | `autocad.properties.get_last_saved_by()` |
| `ThisDrawing.SummaryInfo.EditTime` | `autocad.properties.get_edit_time()` |
| `ThisDrawing.SummaryInfo.NumCustomInfo` | `autocad.properties.get_num_custom_info()` |
| `ThisDrawing.SummaryInfo.SetCustomByKey()` | `autocad.properties.add_custom_property()` |
| `ThisDrawing.SummaryInfo.GetCustomValue()` | `autocad.properties.get_custom_property()` |
| `ThisDrawing.SummaryInfo.RemoveCustomByKey()` | `autocad.properties.remove_custom_property()` |

## API Reference

### General Properties
- `get_title()` → str
- `set_title(value: str)` → None
- `get_subject()` → str
- `set_subject(value: str)` → None
- `get_author()` → str
- `set_author(value: str)` → None
- `get_keywords()` → str
- `set_keywords(value: str)` → None
- `get_comments()` → str
- `set_comments(value: str)` → None

### Summary Properties
- `get_manager()` → str
- `set_manager(value: str)` → None
- `get_company()` → str
- `set_company(value: str)` → None
- `get_category()` → str
- `set_category(value: str)` → None

### Statistics (Read-Only)
- `get_created_date()` → str
- `get_modified_date()` → str
- `get_last_saved_by()` → str
- `get_edit_time()` → int
- `get_revision_number()` → str

### Custom Properties
- `get_num_custom_info()` → int - **Python equivalent of VBA NumCustomInfo**
- `get_all_custom_properties()` → dict
- `add_custom_property(name: str, value: str)` → None
- `get_custom_property(name: str)` → str
- `remove_custom_property(name: str)` → None
- `update_custom_property(name: str, value: str)` → None
- `clear_all_custom_properties()` → None

## Error Handling

All methods include built-in error handling:

```python
from AutoCAD import AutoCAD, CADException

try:
    autocad = AutoCAD()
    autocad.properties.set_title("My Drawing")
    custom_prop = autocad.properties.get_custom_property("NonExistent")
except CADException as e:
    print(f"AutoCAD Error: {e}")
```

## Notes

- All property values are converted to strings when set
- Custom properties must have unique names
- Statistics are read-only and cannot be modified directly
- Changes to properties are not automatically saved; call `autocad.save()` to persist
- The implementation uses COM (Component Object Model) to interact with AutoCAD
- Works with AutoCAD 2010 and later versions

## Testing

Example test functions are provided in `tests/test.py`:

```python
from tests.test import (
    test_general_properties,
    test_summary_properties,
    test_statistics,
    test_custom_properties,
    test_complete_workflow
)

# Run specific tests
test_custom_properties()
test_complete_workflow()
```

## See Also

- [AutoCAD Module Documentation](AutoCAD/AutoCAD_Module.py)
- [Test Examples](tests/test.py)
- [AutoCAD COM Reference](https://help.autodesk.com/view/ACD/latest/ENU/)
