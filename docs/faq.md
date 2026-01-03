# Frequently Asked Questions

## Installation & Setup

### Q: I get "Cannot find AutoCAD.Application"

**A:** This means AutoCAD is not installed. Make sure to:
1. Install AutoCAD from Autodesk
2. Run AutoCAD at least once to complete registration
3. Ensure you're on Windows (COM support required)

### Q: Do I need a specific Python version?

**A:** Python 3.8 or later is recommended. Earlier versions may work but aren't officially supported.

### Q: Can I use this on macOS or Linux?

**A:** Unfortunately, no. This library uses Windows COM (Component Object Model) which is Windows-only. You'll need Windows with AutoCAD installed.

## Basic Usage

### Q: Does AutoCAD need to be running?

**A:** Yes, AutoCAD must be running before you initialize the library:

```python
from AutoCAD import AutoCAD

cad = AutoCAD()  # AutoCAD must be running
```

### Q: How do I work with multiple drawings?

**A:** The library connects to the active document:

```python
cad = AutoCAD()
document = cad.doc  # Active document
```

Switch to a different document in AutoCAD's UI, then the next operation will use that document.

### Q: Can I create drawings from scratch?

**A:** Yes, but you need to create a new document in AutoCAD first:

```python
# Create new drawing in AutoCAD using File > New
# Then access it via Python:
cad = AutoCAD()
cad.add_circle(APoint(0, 0, 0), 5)
```

## Objects & Layers

### Q: What's the difference between add_circle and add_line?

**A:** They create different geometric objects:

```python
circle = cad.add_circle(center, radius)  # Circular object
line = cad.add_line(start, end)          # Linear object
```

### Q: How do I change an object's properties?

**A:** Use the modify methods:

```python
cad.set_object_color(circle, Color.RED)
cad.set_object_layer(circle, "MyLayer")
cad.modify_object_property(circle, "Radius", 10)
```

### Q: Can I delete objects?

**A:** Yes:

```python
cad.delete_object(circle)
```

## Drawing Properties

### Q: What's the difference between custom and general properties?

**A:** 
- **General Properties**: Title, Subject, Author (built-in)
- **Custom Properties**: User-defined properties you create

```python
# General (predefined)
cad.properties.set_title("My Drawing")

# Custom (you define)
cad.properties.add_custom_property("ProjectID", "PROJ-001")
```

### Q: How do I get the number of custom properties?

**A:** Use `get_num_custom_info()` (Python equivalent of VBA `NumCustomInfo`):

```python
count = cad.properties.get_num_custom_info()
print(f"Custom properties: {count}")
```

### Q: Do I need to save after changing properties?

**A:** Yes, call `save()`:

```python
cad.properties.set_title("New Title")
cad.save()  # Don't forget this!
```

## Coordinates & Points

### Q: What units does the library use?

**A:** The library uses AutoCAD's drawing units. These depend on your drawing setup and can be millimeters, inches, feet, etc. Use consistent units throughout your script.

### Q: What's the difference between 2D and 3D points?

**A:** Both use the same `APoint` class:

```python
# 2D (Z = 0)
point_2d = APoint(10, 20, 0)

# 3D (Z = some value)
point_3d = APoint(10, 20, 5)
```

### Q: How do I convert a point to a tuple?

**A:** Use `to_tuple()`:

```python
point = APoint(10, 20, 0)
x, y = point.to_tuple()  # (10, 20)
```

## Troubleshooting

### Q: My script hangs or doesn't respond

**A:** Possible causes:

1. **AutoCAD is busy** - Wait for AutoCAD to finish current operation
2. **Need user input** - Some operations need user interaction in AutoCAD
3. **Infinite loop** - Check your logic

Add delays if needed:

```python
import time

cad.add_circle(APoint(0, 0, 0), 5)
time.sleep(1)  # Wait 1 second
cad.add_circle(APoint(10, 0, 0), 5)
```

### Q: "CADException: Error..." when creating objects

**A:** Check:

1. **AutoCAD is still running** - It might have crashed
2. **Valid parameters** - Check point coordinates, radius, etc.
3. **Active layer exists** - Object layer must exist
4. **Error handling** - Wrap in try-except:

```python
from AutoCAD import CADException

try:
    cad.add_circle(APoint(0, 0, 0), -5)  # Invalid
except CADException as e:
    print(f"Error: {e}")
```

### Q: Performance is slow with many objects

**A:** Try:

1. **Batch operations** - Group similar operations
2. **Use layers** - Organize objects on layers
3. **Purge drawing** - Remove unused elements:

```python
cad.purge()
```

## Advanced Questions

### Q: Can I access raw COM objects?

**A:** Yes, most objects have COM properties:

```python
circle = cad.add_circle(APoint(0, 0, 0), 5)
radius = circle.Radius  # Direct COM access
circle.Color = 1  # Change color directly
```

### Q: How do I iterate through all objects?

**A:** Use `iter_objects()`:

```python
# All objects
for obj in cad.iter_objects():
    print(obj.EntityName)

# Specific type
for circle in cad.iter_objects("AcDbCircle"):
    print(circle.Radius)
```

### Q: Can I work with blocks?

**A:** Yes:

```python
cad.insert_block("BlockName", APoint(0, 0, 0), scale=1.0)
```

## Still Have Questions?

- 📖 Check the [Complete Documentation](index.md)
- 💬 [GitHub Discussions](https://github.com/Jsweb-Tech/AutoCAD/discussions)
- 🐛 [Report Issues](https://github.com/Jsweb-Tech/AutoCAD/issues)
- 📧 [Email Support](mailto:jonespetersoftware@gmail.com)
