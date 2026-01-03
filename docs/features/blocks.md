# Block Operations

Insert and manage blocks in your drawings.

## Inserting Blocks

```python
from AutoCAD import APoint

cad.insert_block(
    block_name="DoorBlock",
    insertion_point=APoint(10, 10, 0),
    scale=1.0,
    rotation=0.0
)
```

## Block Attributes

```python
# Set attribute values
cad.set_block_attribute(block, "DoorID", "D-001")
cad.set_block_attribute(block, "DoorType", "Sliding")
```

## See Also

- [Object Creation](object-creation.md)
- [Group Management](groups.md)
