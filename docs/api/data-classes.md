# Data Classes

Reference for data classes used in the library.

## APoint

Represents a 3D point in AutoCAD.

### Constructor

```python
point = APoint(x: float, y: float, z: float)
```

### Properties

- `x: float` - X coordinate
- `y: float` - Y coordinate  
- `z: float` - Z coordinate

### Methods

#### to_tuple() → Tuple[float, float]

Convert to 2D tuple.

```python
point = APoint(10, 20, 0)
x, y = point.to_tuple()  # (10, 20)
```

#### to_variant()

Convert to COM VARIANT for AutoCAD.

### Example

```python
from AutoCAD import APoint

point = APoint(10, 20, 0)
print(point.x)  # 10
print(point.y)  # 20
print(point.z)  # 0
```

## Text

Represents a text object to be added to AutoCAD.

### Constructor

```python
from AutoCAD import Text, Alignment

text = Text(
    content: str,
    insertion_point: APoint,
    height: float,
    alignment: Alignment = Alignment.LEFT
)
```

### Properties

- `content: str` - Text content
- `insertion_point: APoint` - Where to place the text
- `height: float` - Text height
- `alignment: Alignment` - Text alignment

### Example

```python
text = Text(
    content="Hello World",
    insertion_point=APoint(5, 5, 0),
    height=2.5,
    alignment=Alignment.CENTER
)
cad.add_text(text)
```

## Dimension

Represents a dimension object.

### Constructor

```python
from AutoCAD import Dimension, DimensionType

dimension = Dimension(
    start_point: APoint,
    end_point: APoint,
    text_point: APoint,
    dimension_type: DimensionType = DimensionType.ALIGNED
)
```

### Properties

- `start_point: APoint` - Start point
- `end_point: APoint` - End point
- `text_point: APoint` - Text location
- `dimension_type: DimensionType` - Type of dimension

## Table

Represents a table to be drawn in AutoCAD.

### Constructor

```python
from AutoCAD import Table

table = Table(
    insertion_point: APoint,
    data: List[List[str]],
    headers: List[str] = None,
    col_widths: List[float] = None,
    row_height: float = 8.0,
    text_height: float = 2.5,
    text_style: str = None
)
```

### Properties

- `insertion_point: APoint` - Table top-left position
- `data: List[List[str]]` - Table body data
- `headers: List[str]` - Header row
- `col_widths: List[float]` - Column widths
- `row_height: float` - Row height
- `text_height: float` - Text height in cells
- `text_style: str` - Text style name

### Example

```python
table = Table(
    insertion_point=APoint(0, 0, 0),
    data=[
        ["John", "30"],
        ["Jane", "28"]
    ],
    headers=["Name", "Age"],
    col_widths=[10, 10],
    row_height=5,
    text_height=2
)
cad.add_table(table)
```

## Layer

Represents a layer to be created in AutoCAD.

### Constructor

```python
from AutoCAD import Layer, Color

layer = Layer(
    name: str,
    color: Color = Color.WHITE,
    visible: bool = True
)
```

### Properties

- `name: str` - Layer name
- `color: Color` - Layer color
- `visible: bool` - Layer visibility

### Example

```python
layer = Layer(
    name="Design",
    color=Color.BLUE,
    visible=True
)
cad.create_layer(layer)
```

## BlockReference

Represents a block reference (insertion).

### Constructor

```python
from AutoCAD import BlockReference

block = BlockReference(
    name: str,
    insertion_point: APoint,
    scale: float = 1.0,
    rotation: float = 0.0
)
```

### Properties

- `name: str` - Block name
- `insertion_point: APoint` - Insertion point
- `scale: float` - Scale factor
- `rotation: float` - Rotation angle in radians

## See Also

- [AutoCAD Class](autocad.md)
- [Enums](enums.md)
