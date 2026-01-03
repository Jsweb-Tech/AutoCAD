![AutoCAD Library](https://github.com/Jsweb-Tech/AutoCAD/blob/master/images/new_banner.png?raw=true)

# AutoCAD Python Library

[![GitHub](https://img.shields.io/badge/GitHub-Jsweb--Tech-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Jsweb-Tech)
[![Instagram](https://img.shields.io/badge/Instagram-jones__peter__-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/jones_peter__/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Jones--Peter-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jones-peter-121157221/)
[![Website](https://img.shields.io/badge/Website-jonespeter.site-0078D4?style=for-the-badge&logo=google-chrome&logoColor=white)](https://jonespeter.site)

[![PyPI version](https://img.shields.io/pypi/v/AutoCAD)](https://pypi.org/project/AutoCAD/)
[![Downloads](https://static.pepy.tech/badge/AutoCAD)](https://pepy.tech/project/AutoCAD)
[![License](https://img.shields.io/github/license/Jsweb-Tech/AutoCAD)](https://github.com/Jsweb-Tech/AutoCAD/blob/master/LICENSE)

## About

The `AutoCAD` Python library provides a comprehensive interface for automating AutoCAD tasks. It leverages the COM client to interact with AutoCAD, allowing for efficient manipulation of drawings and objects directly from Python.

## Quick Installation

```bash
pip install AutoCAD
```

## Quick Start

```python
from AutoCAD import AutoCAD, APoint

# Initialize AutoCAD connection
cad = AutoCAD()

# Create a circle
center = APoint(10, 10, 0)
circle = cad.add_circle(center, radius=5)
```

## Documentation

For comprehensive guides, API reference, examples, and more, visit the full documentation:

**[AutoCAD Python Library Documentation](https://jsweb-tech.github.io/AutoCAD/)**

## Key Features

- Object Creation (circles, lines, rectangles, ellipses, text, tables, etc.)
- Layer Management
- Block Operations
- Group Management
- Drawing Properties Management
- User Interaction & Input
- View Management
- Error Handling

## Requirements

- Python 3.8+
- AutoCAD 2010 or later
- Windows OS (for COM support)
- pywin32

## Contributing

Want to contribute? Check out our [Contributing Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions, issues, or suggestions:
- Open an [Issue](https://github.com/Jsweb-Tech/AutoCAD/issues)
- Start a [Discussion](https://github.com/Jsweb-Tech/AutoCAD/discussions)
- Email: jonespetersoftware@gmail.com

## Credits

Built on the shoulders of:
- [AutoCAD by manufino](https://github.com/manufino/AutoCAD)
- [pyautocad by reclosedev](https://github.com/reclosedev/pyautocad)

---

> **Note**: This project is not affiliated with Autodesk AutoCAD in any way.