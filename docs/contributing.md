# Contributing

We love contributions! Here's how to help.

## Ways to Contribute

- 🐛 **Report Bugs** - Found an issue? Let us know
- ✨ **Suggest Features** - Have an idea? Share it
- 📝 **Improve Documentation** - Help us write better docs
- 💻 **Submit Code** - Fix bugs or add features

## Getting Started

### 1. Fork the Repository

```bash
# Click the Fork button on GitHub
```

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/AutoCAD.git
cd AutoCAD
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 4. Make Changes

Edit files, add features, or fix bugs.

### 5. Test Your Changes

```bash
python -m pytest tests/
```

### 6. Commit Your Changes

```bash
git add .
git commit -m "Description of changes"
```

### 7. Push to GitHub

```bash
git push origin feature/your-feature-name
```

### 8. Create a Pull Request

Go to GitHub and create a pull request with a clear description.

## Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Include type hints

### Example

```python
def add_circle(self, center: APoint, radius: float) -> Circle:
    """
    Adds a circle to the model space.
    
    Args:
        center (APoint): The center point of the circle.
        radius (float): The radius of the circle.
    
    Returns:
        Circle: The created circle object.
    
    Raises:
        CADException: If the circle cannot be added.
    """
    try:
        circle = self.modelspace.AddCircle(center.to_variant(), radius)
        return circle
    except Exception as e:
        raise CADException(f"Error adding circle: {e}")
```

## Documentation

When adding new features:

1. Add docstrings to your code
2. Update relevant documentation files
3. Add examples if applicable

## Reporting Issues

When reporting a bug, include:

- **AutoCAD Version** - Which version are you using?
- **Python Version** - Which Python version?
- **Steps to Reproduce** - How to recreate the issue
- **Error Message** - Full traceback if applicable
- **Code Example** - Minimal example that reproduces the bug

### Example Issue

```
Title: Circle creation fails with certain radius values

AutoCAD Version: 2020
Python Version: 3.9
Error: ValueError: radius must be positive

Code:
cad = AutoCAD()
cad.add_circle(APoint(0,0,0), -5)  # Negative radius

Expected: Should raise CADException with clear error
Actual: ValueError with unclear message
```

## Suggesting Features

When suggesting a feature:

1. **Title** - Clear, concise title
2. **Description** - What feature do you want?
3. **Motivation** - Why do you need it?
4. **Example** - How would you use it?

### Example Suggestion

```
Title: Add support for layers with line type patterns

Description:
Currently, we can't set line types (dashed, dotted, etc.) on layers.

Motivation:
AutoCAD supports line types and it's common to use dashed lines 
for construction geometry.

Example Usage:
from AutoCAD import Layer, LineStyle

layer = Layer("Construction", line_style=LineStyle.DASHED)
cad.create_layer(layer)
```

## Code Review

- Reviewers will provide feedback
- Address comments and make changes
- Keep conversations respectful and professional
- Ask questions if something isn't clear

## Licensing

By contributing, you agree your work is licensed under the MIT License.

## Questions?

- 💬 [GitHub Discussions](https://github.com/Jsweb-Tech/AutoCAD/discussions)
- 📧 [Email](mailto:jonespetersoftware@gmail.com)

## Thank You! 🙏

Thank you for helping make this project better!
