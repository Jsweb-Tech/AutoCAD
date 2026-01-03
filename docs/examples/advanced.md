# Advanced Examples

More complex examples and patterns.

## Batch Operations

Process multiple objects:

```python
from AutoCAD import AutoCAD, APoint, Color

cad = AutoCAD()

# Create multiple circles
for i in range(5):
    center = APoint(i * 15, 0, 0)
    circle = cad.add_circle(center, radius=5)
    cad.set_object_color(circle, Color.BLUE)

cad.zoom_extents()
cad.save()
```

## Copy and Transform

```python
from AutoCAD import AutoCAD, APoint

cad = AutoCAD()

# Create original
original = cad.add_circle(APoint(0, 0, 0), radius=5)

# Copy multiple times
for i in range(3):
    displacement = APoint(20 * (i + 1), 0, 0)
    cad.copy_object(original, displacement)

cad.save()
```

## Selective Object Manipulation

```python
from AutoCAD import AutoCAD, Color

cad = AutoCAD()

# Process all circles in the drawing
for circle in cad.iter_objects("AcDbCircle"):
    # Change color based on size
    radius = circle.Radius
    if radius < 5:
        cad.set_object_color(circle, Color.GREEN)
    elif radius < 10:
        cad.set_object_color(circle, Color.BLUE)
    else:
        cad.set_object_color(circle, Color.RED)

cad.save()
```

## Dynamic Grid Creation

```python
from AutoCAD import AutoCAD, APoint

cad = AutoCAD()

# Create a grid of circles
spacing = 10
rows, cols = 5, 5

for row in range(rows):
    for col in range(cols):
        center = APoint(col * spacing, row * spacing, 0)
        cad.add_circle(center, radius=2)

cad.zoom_extents()
cad.save()
```

## Dimension Multiple Objects

```python
from AutoCAD import AutoCAD, APoint, Dimension, DimensionType

cad = AutoCAD()

# Create a line
line = cad.add_line(APoint(0, 0, 0), APoint(10, 0, 0))

# Add dimension
dimension = Dimension(
    start_point=APoint(0, 0, 0),
    end_point=APoint(10, 0, 0),
    text_point=APoint(5, -2, 0),
    dimension_type=DimensionType.LINEAR
)
cad.add_dimension(dimension)

cad.save()
```

## See Also

- [Basic Examples](basic.md)
- [Drawing Metadata](metadata.md)
- [Features](../features/object-creation.md)
