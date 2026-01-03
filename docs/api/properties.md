# Drawing Properties API

Complete API reference for drawing properties.

## DrawingProperties Class

Access via `cad.properties`.

## General Properties

### get_title() → str

Get the document title.

### set_title(value: str) → None

Set the document title.

### get_subject() → str

Get the document subject.

### set_subject(value: str) → None

Set the document subject.

### get_author() → str

Get the document author.

### set_author(value: str) → None

Set the document author.

### get_keywords() → str

Get document keywords.

### set_keywords(value: str) → None

Set document keywords.

### get_comments() → str

Get document comments.

### set_comments(value: str) → None

Set document comments.

## Summary Properties

### get_manager() → str

Get the manager name.

### set_manager(value: str) → None

Set the manager name.

### get_company() → str

Get the company name.

### set_company(value: str) → None

Set the company name.

### get_category() → str

Get the category.

### set_category(value: str) → None

Set the category.

## Statistics (Read-Only)

### get_created_date() → str

Get creation date and time.

### get_modified_date() → str

Get last modification date and time.

### get_last_saved_by() → str

Get the user who last saved the document.

### get_edit_time() → int

Get total editing time in seconds.

### get_revision_number() → str

Get the revision number.

## Custom Properties

### get_num_custom_info() → int

Get the number of custom properties.

**Python equivalent of VBA `NumCustomInfo`**

### get_all_custom_properties() → dict

Get all custom properties as a dictionary.

```python
all_props = cad.properties.get_all_custom_properties()
# {'ProjectID': 'PROJ-001', 'Version': '1.0'}
```

### add_custom_property(name: str, value: str) → None

Add or update a custom property.

```python
cad.properties.add_custom_property("ProjectID", "PROJ-001")
```

### get_custom_property(name: str) → str

Get the value of a specific custom property.

```python
project_id = cad.properties.get_custom_property("ProjectID")
```

### remove_custom_property(name: str) → None

Remove a custom property.

```python
cad.properties.remove_custom_property("ProjectID")
```

### update_custom_property(name: str, new_value: str) → None

Update an existing custom property.

```python
cad.properties.update_custom_property("ProjectID", "PROJ-002")
```

### clear_all_custom_properties() → None

Remove all custom properties.

```python
cad.properties.clear_all_custom_properties()
```

## Example

```python
# Set various properties
cad.properties.set_title("My Drawing")
cad.properties.set_author("Your Name")

# Add custom properties
cad.properties.add_custom_property("ProjectID", "PROJ-001")
cad.properties.add_custom_property("Version", "1.0")

# Get properties
count = cad.properties.get_num_custom_info()
all_custom = cad.properties.get_all_custom_properties()

# Save
cad.save()
```

## See Also

- [Drawing Properties Feature Guide](../features/properties.md)
- [AutoCAD Class](autocad.md)
