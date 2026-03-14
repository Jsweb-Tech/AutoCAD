# Block Operations

Insert, export, query, and manage blocks and their attributes in your drawings.

## Listing User-Defined Blocks

Retrieve all user-defined block names in the current drawing (excludes layout blocks and internal blocks starting with `*`).

```python
blocks = cad.get_user_defined_blocks()
print(blocks)  # ['DoorBlock', 'WindowBlock', 'TitleBlock']
```

## Inserting Blocks

### From Current Drawing

Insert a block that already exists in the drawing's block table.

```python
from AutoCAD import APoint, BlockReference

block = BlockReference(
    name="DoorBlock",
    insertion_point=APoint(10, 10, 0),
    scale=1.0,
    rotation=0.0
)
block_ref = cad.insert_block(block)
```

### From External File

Insert a block from an external `.dwg` file into the current drawing.

```python
block_ref = cad.insert_block_from_file(
    file_path=r"C:\Blocks\MyBlock.dwg",
    insertion_point=APoint(50, 50, 0),
    scale=2.0,
    rotation=0.0
)
```

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `file_path` | `str` | Path to the `.dwg` file containing the block definition |
| `insertion_point` | `APoint` | The point where the block will be inserted |
| `scale` | `float` | Scale factor (default: `1.0`) |
| `rotation` | `float` | Rotation angle in radians (default: `0.0`) |

## Exporting Blocks

Export one or more block definitions from the current drawing to a `.dwg` file.

```python
cad.export_blocks_to_file(
    block_names=["DoorBlock", "WindowBlock"],
    file_path=r"C:\Exports\exported_blocks.dwg"
)
```

If the target file already exists, the blocks are merged into it. If it doesn't exist, a new file is created.

!!! note
    This method temporarily inserts block instances at a safe far-away point, exports them via `Wblock`, then cleans up. The source drawing is closed without saving after export.

## Querying Block Information

### Get Block Extents

Get the bounding box (minimum and maximum points) of a block reference.

```python
min_pt, max_pt = cad.get_block_extents("DoorBlock")
print(f"Min: {min_pt}, Max: {max_pt}")
```

### Get Block Coordinates

Get the insertion points of all references of a specific block in the drawing.

```python
coordinates = cad.get_block_coordinates("DoorBlock")
for pt in coordinates:
    print(f"Block at: ({pt.x}, {pt.y}, {pt.z})")
```

## Repeating Blocks

Fill a horizontal span by repeating a block at regular intervals.

```python
cad.repeat_block_horizontally(
    block_name="BrickBlock",
    total_length=100.0,
    block_length=10.0,
    insertion_point=APoint(0, 0, 0)
)
# Inserts 10 copies of "BrickBlock" side by side
```

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `block_name` | `str` | Name of the block to repeat |
| `total_length` | `float` | Total length to fill |
| `block_length` | `float` | Length of a single block |
| `insertion_point` | `APoint` | Starting insertion point |

## Block Attributes

### Modify an Attribute

Change the value of a specific attribute by its tag.

```python
# Get a block reference (e.g., from iterating model space)
for entity in cad.iter_objects("AcDbBlockReference"):
    if entity.Name == "TitleBlock":
        cad.modify_block_attribute(entity, "TITLE", "New Drawing Title")
        cad.modify_block_attribute(entity, "AUTHOR", "Jones Peter")
```

### Modify Attribute by Old Value

Only update an attribute if its current value matches an expected value.

```python
cad.modify_block_attribute_by_old_value(
    block_ref=entity,
    tag="STATUS",
    old_value="DRAFT",
    new_value="FINAL"
)
```

This is useful for conditional updates — the attribute is only changed if it currently holds `old_value`.

### Delete an Attribute

Remove an attribute from a block reference by its tag.

```python
cad.delete_block_attribute(entity, "OBSOLETE_TAG")
```

## Complete Example

```python
from AutoCAD import AutoCAD, APoint, BlockReference

cad = AutoCAD()

# List all blocks in the drawing
blocks = cad.get_user_defined_blocks()
print(f"Found blocks: {blocks}")

# Insert a block
block_ref = cad.insert_block(
    BlockReference("TitleBlock", APoint(0, 0, 0), scale=1.0, rotation=0.0)
)

# Set attributes on the inserted block
cad.modify_block_attribute(block_ref, "TITLE", "Floor Plan - Level 1")
cad.modify_block_attribute(block_ref, "DATE", "2026-03-14")

# Find all instances of a block
coords = cad.get_block_coordinates("DoorBlock")
print(f"Found {len(coords)} door blocks")

# Get bounding box of a block
min_pt, max_pt = cad.get_block_extents("DoorBlock")
width = max_pt.x - min_pt.x
height = max_pt.y - min_pt.y
print(f"Door block size: {width} x {height}")

# Insert a block from an external file
cad.insert_block_from_file(
    r"C:\Blocks\FurnitureBlock.dwg",
    APoint(20, 30, 0),
    scale=1.5
)

# Export blocks to a separate file
cad.export_blocks_to_file(
    ["TitleBlock", "DoorBlock"],
    r"C:\Exports\project_blocks.dwg"
)

cad.save()
```

## API Reference

| Method | Description |
|---|---|
| `get_user_defined_blocks()` | List all user-defined block names |
| `insert_block(block)` | Insert a block from the block table |
| `insert_block_from_file(file_path, insertion_point, scale, rotation)` | Insert a block from an external `.dwg` file |
| `export_blocks_to_file(block_names, file_path)` | Export blocks to a `.dwg` file |
| `get_block_extents(block_name)` | Get bounding box of a block reference |
| `get_block_coordinates(block_name)` | Get insertion points of all block references |
| `repeat_block_horizontally(block_name, total_length, block_length, insertion_point)` | Repeat a block to fill a length |
| `modify_block_attribute(block_ref, tag, new_value)` | Modify an attribute value |
| `modify_block_attribute_by_old_value(block_ref, tag, old_value, new_value)` | Conditionally modify an attribute |
| `delete_block_attribute(block_ref, tag)` | Delete an attribute from a block |

## See Also

- [Object Creation](object-creation.md)
- [Group Management](groups.md)
- [Layer Management](layers.md)
