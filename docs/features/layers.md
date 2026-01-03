# Layer Management

Organize and manage layers in your drawings.

## Creating Layers

```python
from AutoCAD import Layer, Color

layer = Layer(
    name="MyLayer",
    color=Color.BLUE,
    visible=True
)
cad.create_layer(layer)
```

## Available Colors

```python
Color.RED
Color.GREEN
Color.BLUE
Color.YELLOW
Color.CYAN
Color.MAGENTA
Color.WHITE
Color.GRAY
Color.ORANGE
Color.PURPLE
Color.BROWN
```

## Layer Operations

```python
# Delete a layer
cad.delete_layer("MyLayer")

# Lock a layer
cad.lock_layer("MyLayer")

# Unlock a layer
cad.unlock_layer("MyLayer")

# Get all layers
layers = cad.get_layers()

# Set object layer
cad.set_object_layer(circle, "MyLayer")
```

## See Also

- [Object Creation](object-creation.md)
- [Quick Start](../getting-started/quickstart.md)
