# AutoCAD Python Library

<p align="center">
  <img src="https://github.com/Jsweb-Tech/AutoCAD/blob/master/images/new_banner.png?raw=true" alt="JsWeb Logo" width="900">
</p>

## Overview

The **AutoCAD Python Library** is a comprehensive interface for interacting with AutoCAD through Python. It leverages COM (Component Object Model) to automate tasks within AutoCAD, allowing for efficient manipulation of drawings, objects, and metadata.

Whether you're new to AutoCAD automation or an experienced VBA developer, this library provides a Pythonic way to work with AutoCAD without the need for VBA or any complex setup.

## Key Features

- Object Creation - Create circles, lines, rectangles, ellipses, text, dimensions, polylines, and more
- Layer Management - Create, delete, lock/unlock, and manage layers
- Block Operations - Insert, export, and modify blocks and their attributes
- Group Management - Create and manage groups of objects
- Drawing Properties - Access and modify document metadata (title, author, custom properties)
- View Control - Zoom, pan, and navigate your drawings
- User Interaction - Request input from users directly
- Robust Error Handling - Custom exception handling for AutoCAD-specific errors

## Quick Start

=== "Installation"

    ```bash
    pip install AutoCAD
    ```

=== "Basic Usage"

    ```python
    from AutoCAD import AutoCAD, APoint

    # Initialize AutoCAD
    cad = AutoCAD()

    # Create a circle
    center = APoint(10, 10, 0)
    circle = cad.add_circle(center, radius=5)

    # Add custom property
    cad.properties.add_custom_property("ProjectID", "PROJ-001")

    # Save the drawing
    cad.save()
    ```

## Documentation Structure

- Getting Started - Installation, setup, and basic concepts
- Features - Detailed feature guides
- API Reference - Complete API documentation
- Examples - Code examples and use cases

## VBA to Python

Coming from VBA? We've got you covered! Check out our [Drawing Properties](features/properties.md) guide for Python equivalents of VBA SummaryInfo methods.

| VBA | Python |
|---|---|
| `ThisDrawing.SummaryInfo.NumCustomInfo` | `cad.properties.get_num_custom_info()` |
| `ThisDrawing.SummaryInfo.SetCustomByKey()` | `cad.properties.add_custom_property()` |
| `ThisDrawing.ModelSpace.AddCircle()` | `cad.add_circle()` |

## Why Use This Library?

- Pythonic API - Familiar Python conventions instead of VBA
- Easy to Use - Simple, intuitive interface
- Well Documented - Comprehensive guides and examples
- Type Hints - Full type hints for better IDE support
- Error Handling - Clear, actionable error messages
- Active Development - Regular updates and improvements

## Contributing

Contributions are welcome! Whether it's:
- Bug reports
- Feature requests
- Documentation improvements
- Code contributions

Check out our [Contributing Guide](contributing.md) to get started.

## Requirements

- Python 3.8+
- AutoCAD 2010 or later
- Windows OS (for COM support)
- `pywin32` - For COM interface

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Jsweb-Tech/AutoCAD/blob/master/LICENSE) file for details.

## Author

**Jones Peter**

- GitHub: [jones-peter](https://github.com/jones-peter)
- LinkedIn: [Jones Peter](https://www.linkedin.com/in/jones-peter-121157221/)
- Instagram: [@jones_peter__](https://www.instagram.com/jones_peter__/)
- Website: [jonespeter.site](https://jonespeter.site)

## Credits

This project builds upon the work from:

- [AutoCAD by manufino](https://github.com/manufino/AutoCAD)
- [pyautocad by reclosedev](https://github.com/reclosedev/pyautocad)

> **Note**: This project is not affiliated with Autodesk AutoCAD in any way.

## Support

- Check the [FAQ](faq.md)
- [Report Issues](https://github.com/Jsweb-Tech/AutoCAD/issues)
- [Discussions](https://github.com/Jsweb-Tech/AutoCAD/discussions)
