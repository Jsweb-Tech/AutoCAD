# Enums

Reference for enumeration values used in the library.

## Color

Represents colors for objects and layers.

### Values

```python
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

### Usage

```python
from AutoCAD import Color

circle = cad.add_circle(APoint(0, 0, 0), 5)
cad.set_object_color(circle, Color.RED)
```

### from_name() Static Method

Get color value from name string.

```python
value = Color.from_name("RED")  # 1
```

## Alignment

Text alignment options.

### Values

```python
Alignment.LEFT    # "left"
Alignment.CENTER  # "center"
Alignment.RIGHT   # "right"
```

### Usage

```python
from AutoCAD import Text, Alignment

text = Text(
    content="Centered",
    insertion_point=APoint(5, 5, 0),
    height=2.5,
    alignment=Alignment.CENTER
)
```

## DimensionType

Types of dimensions.

### Values

```python
DimensionType.ALIGNED      # "aligned"
DimensionType.LINEAR       # "linear"
DimensionType.ANGULAR      # "angular"
DimensionType.RADIAL       # "radial"
DimensionType.DIAMETER     # "diameter"
```

### Usage

```python
from AutoCAD import Dimension, DimensionType

dimension = Dimension(
    start_point=APoint(0, 0, 0),
    end_point=APoint(10, 0, 0),
    text_point=APoint(5, -2, 0),
    dimension_type=DimensionType.LINEAR
)
cad.add_dimension(dimension)
```

## LineStyle

Line style patterns.

### Values

```python
LineStyle.CONTINUOUS   # "Continuous"     # ────────
LineStyle.DASHED       # "Dashed"         # ─ ─ ─ ─
LineStyle.DOTTED       # "Dotted"         # · · · ·
LineStyle.CENTER       # "Center"         # ─ · ─ ·
LineStyle.HIDDEN       # "Hidden"         # ─ ─ ─ ─
LineStyle.PHANTOM      # "Phantom"        # ─ · · ·
LineStyle.BREAK        # "Break"          # ─   ─  
LineStyle.BORDER       # "Border"         # ─ ─ · ─
LineStyle.DOT2         # "Dot2"           # ·  ·  
LineStyle.DOTX2        # "DotX2"          # ·   ·  
LineStyle.DIVIDE       # "Divide"         # ─  ·  ─
LineStyle.TRACKING     # "Tracking"       # ─ ·  ─ ·
LineStyle.DASHDOT      # "Dashdot"        # ─ · ─ ·
```

### Usage

```python
from AutoCAD import LineStyle

# Apply line style to objects
# (Requires setting line type through object properties)
```

## See Also

- [Data Classes](data-classes.md)
- [AutoCAD Class](autocad.md)
