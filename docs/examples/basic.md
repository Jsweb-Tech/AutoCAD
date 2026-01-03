# Basic Examples

Get started with these simple examples.

## Hello AutoCAD

Your first script:

```python
from AutoCAD import AutoCAD, APoint

cad = AutoCAD()
print("Connected to AutoCAD!")

# Create a circle
circle = cad.add_circle(APoint(10, 10, 0), radius=5)
print("Circle created!")
```

## Create Multiple Shapes

```python
from AutoCAD import AutoCAD, APoint

cad = AutoCAD()

# Create shapes
circle = cad.add_circle(APoint(0, 0, 0), radius=5)
line = cad.add_line(APoint(0, 0, 0), APoint(10, 10, 0))
rect = cad.add_rectangle(APoint(20, 0, 0), APoint(30, 10, 0))

# Zoom to see them all
cad.zoom_extents()

# Save
cad.save()
```

## Work with Layers

```python
from AutoCAD import AutoCAD, APoint, Layer, Color

cad = AutoCAD()

# Create layers
design_layer = Layer("Design", color=Color.BLUE)
construction_layer = Layer("Construction", color=Color.GRAY)

cad.create_layer(design_layer)
cad.create_layer(construction_layer)

# Create objects on layers
circle = cad.add_circle(APoint(10, 10, 0), radius=5)
cad.set_object_layer(circle, "Design")

line = cad.add_line(APoint(0, 0, 0), APoint(20, 20, 0))
cad.set_object_layer(line, "Construction")

cad.save()
```

## Add Text

```python
from AutoCAD import AutoCAD, APoint, Text, Alignment

cad = AutoCAD()

# Create text
text = Text(
    content="Project Name: Building A",
    insertion_point=APoint(0, 0, 0),
    height=2.5,
    alignment=Alignment.LEFT
)

cad.add_text(text)
cad.save()
```

## Draw a Polygon

```python
from AutoCAD import AutoCAD, APoint

cad = AutoCAD()

# Create a square
points = [
    APoint(0, 0, 0),
    APoint(10, 0, 0),
    APoint(10, 10, 0),
    APoint(0, 10, 0),
    APoint(0, 0, 0)  # Close the polygon
]

polyline = cad.add_polyline(points)
cad.save()
```

## Create a Table

```python
from AutoCAD import AutoCAD, APoint, Table

cad = AutoCAD()

# Create table with data
table = Table(
    insertion_point=APoint(0, 0, 0),
    data=[
        ["Item 1", "100"],
        ["Item 2", "200"],
        ["Item 3", "300"]
    ],
    headers=["Description", "Quantity"],
    col_widths=[15, 10],
    row_height=5,
    text_height=2
)

cad.add_table(table)
cad.save()
```

## See Also

- [Advanced Examples](advanced.md)
- [Drawing Metadata Examples](metadata.md)
- [Quick Start](../getting-started/quickstart.md)
