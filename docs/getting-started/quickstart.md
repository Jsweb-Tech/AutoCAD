# Quick Start

Get started with the AutoCAD Python Library in 5 minutes!

## Your First Script

### 1. Open AutoCAD

Make sure AutoCAD is running on your computer before running any Python scripts.

### 2. Initialize the Library

```python
from AutoCAD import AutoCAD, APoint

# Create an AutoCAD instance
cad = AutoCAD()
print("Connected to AutoCAD!")
```

### 3. Create Your First Object

```python
# Create a circle
center = APoint(10, 10, 0)  # x, y, z coordinates
radius = 5

circle = cad.add_circle(center, radius)
print("Circle created successfully!")
```

## Common Tasks

### Drawing Basic Shapes

```python
from AutoCAD import AutoCAD, APoint

cad = AutoCAD()

# Circle
circle = cad.add_circle(APoint(0, 0, 0), radius=5)

# Line
line = cad.add_line(APoint(0, 0, 0), APoint(10, 10, 0))

# Rectangle
rect = cad.add_rectangle(APoint(0, 0, 0), APoint(10, 5, 0))

# Ellipse
ellipse = cad.add_ellipse(
    center=APoint(20, 20, 0),
    major_axis=APoint(30, 0, 0),
    ratio=0.5
)
```

### Working with Layers

```python
from AutoCAD import AutoCAD, Layer, Color

cad = AutoCAD()

# Create a new layer
layer = Layer(name="MyLayer", color=Color.RED, visible=True)
cad.create_layer(layer)

# Set objects to a layer
cad.set_object_layer(circle, "MyLayer")

# Lock a layer
cad.lock_layer("MyLayer")
```

### Adding Text

```python
from AutoCAD import AutoCAD, APoint, Text, Alignment

cad = AutoCAD()

# Create text
text_obj = Text(
    content="Hello AutoCAD!",
    insertion_point=APoint(5, 5, 0),
    height=2.5,
    alignment=Alignment.CENTER
)

created_text = cad.add_text(text_obj)
```

### Managing Drawing Properties

```python
# Set document metadata
cad.properties.set_title("My Drawing")
cad.properties.set_author("Your Name")
cad.properties.set_company("Your Company")

# Add custom properties
cad.properties.add_custom_property("ProjectID", "PROJ-001")
cad.properties.add_custom_property("Version", "1.0")

# Get custom properties
all_props = cad.properties.get_all_custom_properties()
print(all_props)  # {'ProjectID': 'PROJ-001', 'Version': '1.0'}

# Get count
count = cad.properties.get_num_custom_info()
print(f"Total custom properties: {count}")
```

### User Input

```python
# Get a point from user
point = cad.request_point("Click a point in the drawing")
print(f"You selected: {point}")

# Get text input
name = cad.request_string("Enter object name")
print(f"Name: {name}")

# Get number input
value = cad.request_int("Enter a value")
print(f"Value: {value}")
```

### Iterating Objects

```python
# Iterate all objects in model space
for obj in cad.iter_objects():
    print(f"Found object: {obj.EntityName}")

# Iterate only circles
for circle in cad.iter_objects("AcDbCircle"):
    print(f"Circle radius: {circle.Radius}")
```

### Saving Your Work

```python
# Save the current drawing
cad.save()

# Save as a new file
cad.save_as("D:/path/to/new_drawing.dwg")
```

## A Complete Example

Here's a complete example that creates a simple drawing with multiple objects:

```python
from AutoCAD import AutoCAD, APoint, Layer, Color, Text, Alignment
import time

def create_sample_drawing():
    """Create a sample drawing with various objects"""
    
    # Initialize
    cad = AutoCAD()
    time.sleep(1)
    
    # Create a layer
    layer = Layer("Design", color=Color.BLUE, visible=True)
    cad.create_layer(layer)
    
    # Add a circle
    circle = cad.add_circle(APoint(10, 10, 0), 5)
    cad.set_object_layer(circle, "Design")
    
    # Add a rectangle
    rect = cad.add_rectangle(APoint(20, 5, 0), APoint(35, 15, 0))
    cad.set_object_layer(rect, "Design")
    
    # Add text
    text = Text("Sample Drawing", APoint(15, 20, 0), 3)
    cad.add_text(text)
    
    # Set drawing properties
    cad.properties.set_title("Sample Drawing")
    cad.properties.set_author("Python Script")
    cad.properties.add_custom_property("CreatedBy", "AutoCAD Python")
    
    # Zoom to see everything
    cad.zoom_extents()
    
    # Save
    cad.save()
    
    print("Sample drawing created successfully!")

# Run the example
create_sample_drawing()
```

## Next Steps

- 📖 Learn the [Basic Concepts](concepts.md)
- 🎨 Explore all [Features](../features/object-creation.md)
- 📚 Check the [API Reference](../api/autocad.md)
- 💡 See more [Examples](../examples/basic.md)

## Getting Help

- 🤔 Check the [FAQ](../faq.md)
- 🐛 [Report Issues](https://github.com/Jones-peter/AutoCAD/issues)
- 💬 [Ask Questions](https://github.com/Jones-peter/AutoCAD/discussions)
