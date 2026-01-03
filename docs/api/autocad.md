# AutoCAD Class

The main class for interacting with AutoCAD.

## Initialization

```python
from AutoCAD import AutoCAD

cad = AutoCAD()
```

## Properties

### `doc`

Returns the active document.

```python
document = cad.doc
```

### `modelspace`

Returns the model space where objects are drawn.

```python
ms = cad.modelspace
for obj in ms:
    print(obj.EntityName)
```

### `properties`

Returns a DrawingProperties object for managing document metadata.

```python
cad.properties.set_title("My Drawing")
```

## Methods

### Object Creation

- `add_circle(center: APoint, radius: float)` → Circle object
- `add_line(start: APoint, end: APoint)` → Line object
- `add_rectangle(lower_left: APoint, upper_right: APoint)` → Polyline object
- `add_ellipse(center: APoint, major_axis: APoint, ratio: float)` → Ellipse object
- `add_text(text: Text)` → Text object
- `add_mtext(content: str, insertion_point: APoint, width: float, height: float)` → MText object
- `add_arc(center: APoint, radius: float, start_angle: float, end_angle: float)` → Arc object
- `add_polyline(points: List[APoint])` → Polyline object
- `add_spline(points: List[APoint])` → Spline object
- `add_point(point: APoint)` → Point object
- `add_dimension(dimension: Dimension)` → Dimension object
- `add_table(table: Table)` → Table object

### Layer Management

- `create_layer(layer: Layer)` → None
- `delete_layer(layer_name: str)` → None
- `lock_layer(layer_name: str)` → None
- `unlock_layer(layer_name: str)` → None
- `get_layers()` → List of layers

### Block Operations

- `insert_block(block_name: str, insertion_point: APoint, scale: float, rotation: float)` → Block reference
- `get_block_extents(block_name: str)` → Tuple[min_point, max_point]

### Object Manipulation

- `move_object(obj, new_position: APoint)` → None
- `copy_object(obj, displacement: APoint)` → None
- `delete_object(obj)` → None
- `set_object_color(obj, color: Color)` → None
- `set_object_layer(obj, layer_name: str)` → None
- `modify_object_property(obj, property_name: str, new_value)` → None

### View Management

- `zoom_extents()` → None
- `zoom_to_object(obj)` → None

### Iteration

- `iter_objects(object_type: str = None)` → Iterator

### File Operations

- `open_file(filepath: str)` → None
- `save()` → None
- `save_as(filepath: str)` → None
- `purge()` → None

## See Also

- [Quick Start](../getting-started/quickstart.md)
- [Complete API Reference](properties.md)
