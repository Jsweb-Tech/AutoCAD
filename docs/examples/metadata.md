# Drawing Metadata Examples

Examples of working with drawing properties.

## Set All Properties

Complete example setting all types of properties:

```python
from AutoCAD import AutoCAD

cad = AutoCAD()

# General properties
cad.properties.set_title("Manufacturing Floor Plan")
cad.properties.set_subject("Facility Layout")
cad.properties.set_author("Engineering Department")
cad.properties.set_keywords("manufacturing, floor, layout")
cad.properties.set_comments("Q1 2026 update")

# Summary properties
cad.properties.set_manager("Plant Manager")
cad.properties.set_company("Manufacturing Corp")
cad.properties.set_category("Facility Design")

# Custom properties
cad.properties.add_custom_property("ProjectID", "MFG-2026-001")
cad.properties.add_custom_property("Location", "Plant A")
cad.properties.add_custom_property("Status", "Active")

# Save
cad.save()
```

## Project Tracking with Custom Properties

```python
from AutoCAD import AutoCAD
from datetime import datetime

cad = AutoCAD()

# Project metadata
project_info = {
    "ProjectID": "PROJ-2026-001",
    "ClientName": "Acme Corporation",
    "ProjectManager": "John Smith",
    "Budget": "$500,000",
    "StartDate": "2026-01-15",
    "Deadline": "2026-06-30",
    "Status": "In Progress",
    "CreatedDate": datetime.now().strftime("%Y-%m-%d")
}

# Add all properties
for key, value in project_info.items():
    cad.properties.add_custom_property(key, str(value))

cad.properties.set_title(f"Project {project_info['ProjectID']}")
cad.save()
```

## Update Properties

```python
from AutoCAD import AutoCAD

cad = AutoCAD()

# Get current properties
current_version = cad.properties.get_custom_property("Version")
print(f"Current version: {current_version}")

# Update to new version
new_version = "1.1"
cad.properties.update_custom_property("Version", new_version)

# Add review information
cad.properties.add_custom_property("ReviewedBy", "Jane Doe")
cad.properties.add_custom_property("ReviewDate", "2026-01-03")
cad.properties.add_custom_property("ApprovalStatus", "Approved")

cad.save()
```

## Read and Display Properties

```python
from AutoCAD import AutoCAD

cad = AutoCAD()

# Display general information
print("=== General Information ===")
print(f"Title: {cad.properties.get_title()}")
print(f"Author: {cad.properties.get_author()}")
print(f"Company: {cad.properties.get_company()}")

# Display statistics
print("\n=== Statistics ===")
print(f"Created: {cad.properties.get_created_date()}")
print(f"Modified: {cad.properties.get_modified_date()}")
print(f"Saved By: {cad.properties.get_last_saved_by()}")

# Display custom properties
print("\n=== Custom Properties ===")
all_custom = cad.properties.get_all_custom_properties()
for name, value in all_custom.items():
    print(f"{name}: {value}")

print(f"\nTotal custom properties: {cad.properties.get_num_custom_info()}")
```

## Batch Property Updates

```python
from AutoCAD import AutoCAD

def update_drawing_version(cad, new_version):
    """Update drawing to new version"""
    cad.properties.update_custom_property("Version", new_version)
    cad.properties.update_custom_property("LastModified", "2026-01-03")
    cad.properties.update_custom_property("Status", "Updated")
    cad.save()

# Usage
cad = AutoCAD()
update_drawing_version(cad, "2.0")
```

## Property Validation

```python
from AutoCAD import AutoCAD

cad = AutoCAD()

# Check if required properties exist
required_props = ["ProjectID", "ClientName", "Budget"]
existing_props = cad.properties.get_all_custom_properties()

missing = [p for p in required_props if p not in existing_props]

if missing:
    print(f"Missing properties: {missing}")
    # Add missing properties
    for prop in missing:
        cad.properties.add_custom_property(prop, "TBD")
else:
    print("All required properties present")

cad.save()
```

## See Also

- [Drawing Properties Feature](../features/properties.md)
- [Basic Examples](basic.md)
- [Advanced Examples](advanced.md)
