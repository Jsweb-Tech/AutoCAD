# Object Creation

Create various types of objects in your AutoCAD drawings.

## Circles

Create circular objects:

```python
from AutoCAD import AutoCAD, APoint

cad = AutoCAD()

# Basic circle
center = APoint(10, 10, 0)
circle = cad.add_circle(center, radius=5)
```

## Lines

Draw lines between two points:

```python
# Create a line
start = APoint(0, 0, 0)
end = APoint(10, 10, 0)
line = cad.add_line(start, end)
```

## Rectangles

Create rectangular shapes:

```python
# Rectangle defined by lower-left and upper-right corners
lower_left = APoint(0, 0, 0)
upper_right = APoint(10, 5, 0)
rect = cad.add_rectangle(lower_left, upper_right)
```

## Ellipses

Draw elliptical shapes:

```python
center = APoint(5, 5, 0)
major_axis = APoint(10, 0, 0)
ratio = 0.5  # Minor to major axis ratio
ellipse = cad.add_ellipse(center, major_axis, ratio)
```

## Text

Add text to drawings:

```python
from AutoCAD import Text, Alignment

text = Text(
    content="Hello AutoCAD!",
    insertion_point=APoint(5, 5, 0),
    height=2.5,
    alignment=Alignment.CENTER
)
text_obj = cad.add_text(text)
```

## MText (Paragraph Text)

Create multi-line formatted text:

```python
mtext = cad.add_mtext(
    content="Line 1\\PLine 2\\PLine 3",
    insertion_point=APoint(0, 0, 0),
    width=10,
    height=5
)
```

## Polylines

Create multi-segment lines:

```python
points = [
    APoint(0, 0, 0),
    APoint(10, 0, 0),
    APoint(10, 10, 0),
    APoint(0, 10, 0),
    APoint(0, 0, 0)
]
polyline = cad.add_polyline(points)
```

## Arcs

Draw circular arcs:

```python
arc = cad.add_arc(
    center=APoint(10, 10, 0),
    radius=5,
    start_angle=0,
    end_angle=90
)
```

## Splines

Create smooth curves:

```python
points = [
    APoint(0, 0, 0),
    APoint(5, 10, 0),
    APoint(10, 5, 0),
    APoint(15, 15, 0)
]
spline = cad.add_spline(points)
```

## Points

Add point entities:

```python
point = cad.add_point(APoint(5, 5, 0))
```

## Dimensions

Add dimension annotations:

```python
from AutoCAD import Dimension, DimensionType

dim = Dimension(
    start_point=APoint(0, 0, 0),
    end_point=APoint(10, 0, 0),
    text_point=APoint(5, -2, 0),
    dimension_type=DimensionType.LINEAR
)
cad.add_dimension(dim)
```

## Tables

Create data tables:

```python
from AutoCAD import Table

table = Table(
    insertion_point=APoint(0, 0, 0),
    data=[
        ["Row 1 Col 1", "Row 1 Col 2"],
        ["Row 2 Col 1", "Row 2 Col 2"]
    ],
    headers=["Header 1", "Header 2"],
    col_widths=[10, 10],
    row_height=5,
    text_height=2
)
cad.add_table(table)
```

## See Also

- [Layer Management](layers.md) - Organize objects
- [Block Operations](blocks.md) - Use reusable components
- [Quick Start](../getting-started/quickstart.md) - Get started quickly
