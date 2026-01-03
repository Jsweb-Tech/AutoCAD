# Basic Concepts

Understand the fundamental concepts of the AutoCAD Python Library.

## AutoCAD Instance

The `AutoCAD` class is your main entry point to interact with AutoCAD:

```python
from AutoCAD import AutoCAD

cad = AutoCAD()
```

!!! note
    AutoCAD must be running before you create an instance. The library connects to the running AutoCAD process via COM.

### Properties

```python
# Get the active document
doc = cad.doc

# Get the model space (where objects are drawn)
modelspace = cad.modelspace

# Access drawing properties
props = cad.properties
```

## Points (APoint)

Points represent coordinates in 2D or 3D space:

```python
from AutoCAD import APoint

# Create a point
point = APoint(x=10, y=20, z=0)

# Access coordinates
print(point.x)  # 10
print(point.y)  # 20
print(point.z)  # 0

# Convert to tuple (2D)
tuple_2d = point.to_tuple()  # (10, 20)

# Convert to COM variant
variant = point.to_variant()
```

## Layers

Layers organize objects in your drawing:

```python
from AutoCAD import Layer, Color

# Create a layer
layer = Layer(
    name="MyLayer",
    color=Color.RED,
    visible=True
)

# Available colors
Color.RED
Color.GREEN
Color.BLUE
Color.YELLOW
# ... and many more
```

## Blocks

Blocks are reusable drawing components:

```python
# Insert a block
cad.insert_block(
    block_name="DoorBlock",
    insertion_point=APoint(10, 10, 0),
    scale=1.0,
    rotation=0.0
)

# Get block references
blocks = list(cad.iter_objects("AcDbBlockReference"))
```

## Objects and Entity Types

Everything in AutoCAD is an entity with a type:

```python
# Iterate through objects
for obj in cad.iter_objects():
    print(obj.EntityName)  # e.g., "AcDbCircle"

# Filter by type
circles = list(cad.iter_objects("AcDbCircle"))
lines = list(cad.iter_objects("AcDbLine"))
```

### Common Entity Types

| Type | Python Method |
|------|---------------|
| Circle | `add_circle()` |
| Line | `add_line()` |
| Rectangle | `add_rectangle()` |
| Ellipse | `add_ellipse()` |
| Text | `add_text()` |
| MText | `add_mtext()` |
| Arc | `add_arc()` |
| Polyline | `add_polyline()` |
| Spline | `add_spline()` |
| Point | `add_point()` |
| Dimension | `add_dimension()` |

## Enumerations

Enums provide predefined values for various options:

### Color Enum

```python
from AutoCAD import Color

Color.RED        # 1
Color.YELLOW     # 2
Color.GREEN      # 3
Color.CYAN       # 4
Color.BLUE       # 5
Color.MAGENTA    # 6
Color.WHITE      # 7
Color.GRAY       # 8
Color.ORANGE     # 30
Color.PURPLE     # 40
Color.BROWN      # 41
```

### Alignment Enum

```python
from AutoCAD import Alignment

Alignment.LEFT      # "left"
Alignment.CENTER    # "center"
Alignment.RIGHT     # "right"
```

### LineStyle Enum

```python
from AutoCAD import LineStyle

LineStyle.CONTINUOUS   # "Continuous"
LineStyle.DASHED       # "Dashed"
LineStyle.DOTTED       # "Dotted"
LineStyle.CENTER       # "Center"
LineStyle.HIDDEN       # "Hidden"
# ... and more
```

### DimensionType Enum

```python
from AutoCAD import DimensionType

DimensionType.ALIGNED      # "aligned"
DimensionType.LINEAR       # "linear"
DimensionType.ANGULAR      # "angular"
DimensionType.RADIAL       # "radial"
DimensionType.DIAMETER     # "diameter"
```

## Drawing Properties

Access and modify document metadata:

```python
# General properties
cad.properties.set_title("My Drawing")
cad.properties.set_author("Your Name")
cad.properties.set_subject("Subject")
cad.properties.set_keywords("tag1, tag2")
cad.properties.set_comments("Comments here")

# Summary properties
cad.properties.set_manager("Manager Name")
cad.properties.set_company("Company Name")
cad.properties.set_category("Category")

# Statistics (read-only)
created = cad.properties.get_created_date()
modified = cad.properties.get_modified_date()
edit_time = cad.properties.get_edit_time()

# Custom properties
cad.properties.add_custom_property("ProjectID", "PROJ-001")
value = cad.properties.get_custom_property("ProjectID")
count = cad.properties.get_num_custom_info()
all_custom = cad.properties.get_all_custom_properties()
```

## Error Handling

The library uses custom exceptions:

```python
from AutoCAD import CADException

try:
    cad = AutoCAD()
    circle = cad.add_circle(APoint(0, 0, 0), 5)
except CADException as e:
    print(f"AutoCAD Error: {e}")
```

## Utility Functions

Check AutoCAD status:

```python
from AutoCAD import is_autocad_installed, is_autocad_running

# Check if AutoCAD is installed
if is_autocad_installed():
    print("AutoCAD is installed")

# Check if AutoCAD is running
if is_autocad_running():
    print("AutoCAD is running")
```

## Working with Coordinates

### 2D vs 3D

```python
# 2D point (Z = 0)
point_2d = APoint(10, 20, 0)

# 3D point
point_3d = APoint(10, 20, 5)

# Most operations work in 2D
# Z coordinate is usually 0 for 2D drawings
```

### Units

The library doesn't enforce units. AutoCAD uses drawing units, which can be:
- Millimeters
- Centimeters
- Inches
- Feet
- etc.

Use consistent units throughout your script.

## Next Steps

- 🎨 Learn about [Object Creation](../features/object-creation.md)
- 📑 Explore [Layer Management](../features/layers.md)
- 📊 Understand [Drawing Properties](../features/properties.md)
- 💻 See [API Reference](../api/autocad.md)
