import subprocess
import psutil
import pythoncom
import win32com.client
from enum import Enum

# project by jones peter
class Color(Enum):
    """Enum to represent common colors in AutoCAD."""
    RED = 1
    YELLOW = 2
    GREEN = 3
    CYAN = 4
    BLUE = 5
    MAGENTA = 6
    WHITE = 7
    GRAY = 8
    ORANGE = 30
    PURPLE = 40
    BROWN = 41

    @staticmethod
    def from_name(name):
        """
        Gets the color value from its string name.
        Args:
            name (str): The name of the color (e.g., 'RED').
        Returns:
            int: The integer value of the color.
        Raises:
            ValueError: If the color name is not valid.
        """
        try:
            return Color[name.upper()].value
        except KeyError:
            raise ValueError(f"Color '{name}' is not a valid color name")


class Alignment(Enum):
    """Enum to represent text alignments in AutoCAD."""
    LEFT = 'left'
    CENTER = 'center'
    RIGHT = 'right'


class DimensionType(Enum):
    """Enum to represent dimension types in AutoCAD."""
    ALIGNED = 'aligned'
    LINEAR = 'linear'
    ANGULAR = 'angular'
    RADIAL = 'radial'
    DIAMETER = 'diameter'


class LineStyle(Enum):
    """Enum to represent common line styles in AutoCAD."""
    CONTINUOUS = 'Continuous'  # ------------
    DASHED = 'Dashed'  # - - - - - -
    DOTTED = 'Dotted'  # . . . . . .
    CENTER = 'Center'  # - . - . - .
    HIDDEN = 'Hidden'  # - - - - - -
    PHANTOM = 'Phantom'  # - . . - . .
    BREAK = 'Break'  # -     -
    BORDER = 'Border'  # - - - . - -
    DOT2 = 'Dot2'  # .  .  .  .
    DOTX2 = 'DotX2'  # .   .   .
    DIVIDE = 'Divide'  # -  .  -  .
    TRACKING = 'Tracking'  # - .  - .
    DASHDOT = 'Dashdot'  # - . - . -


class APoint:
    """Represents a 3D point in AutoCAD."""
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        """
        Initializes a 3D point.
        Args:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
            z (float): The z-coordinate.
        """
        self.x = x
        self.y = y
        self.z = z

    def to_variant(self):
        """
        Converts the point to a COM VARIANT object for AutoCAD.
        Returns:
            win32com.client.VARIANT: The point as a variant array.
        """
        return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, [self.x, self.y, self.z])

    def to_tuple(self):
        """
        Converts the point to a 2D tuple (x, y).
        Returns:
            tuple: A tuple containing the x and y coordinates.
        """
        return self.x, self.y

    def __repr__(self):
        return f"APoint({self.x}, {self.y}, {self.z})"


class Layer:
    """Represents an AutoCAD layer."""
    def __init__(self, name, color=Color.WHITE, visible=True):
        """
        Initializes a layer.
        Args:
            name (str): The name of the layer.
            color (Color): The color of the layer.
            visible (bool): The visibility state of the layer.
        """
        self.name = name
        self.color = color
        self.visible = visible

    def __repr__(self):
        return f"Layer(name='{self.name}', color={self.color}, visible={self.visible})"


class BlockReference:
    """Represents an AutoCAD block reference (insertion)."""
    def __init__(self, name, insertion_point, scale=1.0, rotation=0.0):
        """
        Initializes a block reference.

        Args:
            name (str): The name of the block definition.
            insertion_point (APoint): The point where the block is inserted.
            scale (float): The scale factor for the block.
            rotation (float): The rotation angle in radians.
        """
        self.name = name
        self.insertion_point = insertion_point
        self.scale = scale
        self.rotation = rotation

    def __repr__(self):
        return f"BlockReference(name='{self.name}', insertion_point={self.insertion_point}, scale={self.scale}, rotation={self.rotation})"


class Table:
    """Represents a data table to be drawn in AutoCAD."""

    def __init__(self, insertion_point: APoint, data: list[list[str]], headers: list[str] = None,
                 col_widths: list[float] = None, row_height: float = 8.0, text_height: float = 2.5, text_style: str = None):
        """
        Initializes a table data object.
        Args:
            insertion_point (APoint): The top-left insertion point for the table.
            data (list[list[str]]): A list of lists representing the table's body data.
            headers (list[str], optional): A list of strings for the header row. Defaults to None.
            col_widths (list[float], optional): A list of widths for each column.
            row_height (float): The height for each row.
            text_height (float): The default text height for cells.
            text_style (str, optional): The text style to use. Defaults to None (use default).
        """
        self.insertion_point = insertion_point
        self.data = data
        self.headers = headers
        self.col_widths = col_widths
        self.row_height = row_height
        self.text_height = text_height
        self.text_style = text_style

    def __repr__(self):
        return f"Table(rows={len(self.data)}, cols={len(self.data[0]) if self.data else 0}, text_style={self.text_style})"


class Text:
    """Represents a text object in AutoCAD."""
    def __init__(self, content, insertion_point, height, alignment=Alignment.LEFT):
        """
        Initializes a text object.

        Args:
            content (str): The text string to display.
            insertion_point (APoint): The insertion point for the text.
            height (float): The height of the text.
            alignment (Alignment): The alignment of the text.
        """
        self.content = content
        self.insertion_point = insertion_point
        self.height = height
        self.alignment = alignment

    def __repr__(self):
        return f"Text(content='{self.content}', insertion_point={self.insertion_point}, height={self.height}, alignment='{self.alignment}')"


class Dimension:
    """Represents a dimension object in AutoCAD."""
    def __init__(self, start_point, end_point, text_point, dimension_type=DimensionType.ALIGNED):
        """
        Initializes a dimension.

        Args:
            start_point (APoint): The starting point of the dimension.
            end_point (APoint): The ending point of the dimension.
            text_point (APoint): The location for the dimension text.
            dimension_type (DimensionType): The type of dimension.
        """
        self.start_point = start_point
        self.end_point = end_point
        self.text_point = text_point
        self.dimension_type = dimension_type

    def __repr__(self):
        return f"Dimension(start_point={self.start_point}, end_point={self.end_point}, text_point={self.text_point}, dimension_type='{self.dimension_type}')"


class CADException(Exception):
    """Custom exception class for handling AutoCAD-related errors."""
    def __init__(self, message):
        """
        Initializes the custom AutoCAD exception.
        Args:
            message (str): The error message.
        """
        super().__init__(message)
        print(f"AutoCAD Error: {message}")


def is_autocad_installed():
    """
    Checks if AutoCAD is installed by querying the system's product list.
    Returns:
        bool: True if AutoCAD is found, False otherwise.
    """
    try:
        output = subprocess.check_output('wmic product get name', shell=True, stderr=subprocess.DEVNULL, text=True)
        return "AutoCAD" in output
    except subprocess.CalledProcessError:
        return False


def is_autocad_running():
    """
    Checks if an AutoCAD process is currently running on the system.

    Returns:
        bool: True if an AutoCAD process is running, False otherwise.
    """
    autocad_processes = ['acad.exe', 'AutoCAD', 'acad']
    for process in psutil.process_iter(['name']):
        if any(autocad_process.lower() in process.info['name'].lower() for autocad_process in autocad_processes):
            return True
    return False


class DrawingProperties:
    """
    Manages AutoCAD Drawing Properties (Summary, Statistics, and Custom Properties).
    Provides a Pythonic interface to access and modify document metadata.
    
    This class wraps the COM SummaryInfo object to handle:
    - General properties (Title, Subject, Author, Keywords, Comments)
    - Summary properties (Manager, Company, Category)
    - Statistics (Read-only: Creation date, Modification date, Edit time)
    - Custom properties (Add, Get, Remove, List all custom properties)
    """
    
    def __init__(self, document):
        """
        Initializes the DrawingProperties manager.
        
        Args:
            document: The AutoCAD Document object (ThisDrawing equivalent).
            
        Raises:
            CADException: If the document is invalid.
        """
        try:
            self.doc = document
            self.summary_info = document.SummaryInfo
        except Exception as e:
            raise CADException(f"Error initializing DrawingProperties: {e}")
    
    # ==================== GENERAL PROPERTIES ====================
    
    def get_title(self):
        """
        Gets the document title.
        
        Returns:
            str: The document title.
        """
        try:
            return self.summary_info.Title
        except Exception as e:
            raise CADException(f"Error getting title: {e}")
    
    def set_title(self, value):
        """
        Sets the document title.
        
        Args:
            value (str): The new title.
            
        Raises:
            CADException: If the title cannot be set.
        """
        try:
            self.summary_info.Title = str(value)
        except Exception as e:
            raise CADException(f"Error setting title: {e}")
    
    def get_subject(self):
        """
        Gets the document subject.
        
        Returns:
            str: The document subject.
        """
        try:
            return self.summary_info.Subject
        except Exception as e:
            raise CADException(f"Error getting subject: {e}")
    
    def set_subject(self, value):
        """
        Sets the document subject.
        
        Args:
            value (str): The new subject.
            
        Raises:
            CADException: If the subject cannot be set.
        """
        try:
            self.summary_info.Subject = str(value)
        except Exception as e:
            raise CADException(f"Error setting subject: {e}")
    
    def get_author(self):
        """
        Gets the document author.
        
        Returns:
            str: The document author.
        """
        try:
            return self.summary_info.Author
        except Exception as e:
            raise CADException(f"Error getting author: {e}")
    
    def set_author(self, value):
        """
        Sets the document author.
        
        Args:
            value (str): The new author.
            
        Raises:
            CADException: If the author cannot be set.
        """
        try:
            self.summary_info.Author = str(value)
        except Exception as e:
            raise CADException(f"Error setting author: {e}")
    
    def get_keywords(self):
        """
        Gets the document keywords.
        
        Returns:
            str: The document keywords (comma-separated).
        """
        try:
            return self.summary_info.Keywords
        except Exception as e:
            raise CADException(f"Error getting keywords: {e}")
    
    def set_keywords(self, value):
        """
        Sets the document keywords.
        
        Args:
            value (str): The new keywords (comma-separated).
            
        Raises:
            CADException: If the keywords cannot be set.
        """
        try:
            self.summary_info.Keywords = str(value)
        except Exception as e:
            raise CADException(f"Error setting keywords: {e}")
    
    def get_comments(self):
        """
        Gets the document comments.
        
        Returns:
            str: The document comments.
        """
        try:
            return self.summary_info.Comments
        except Exception as e:
            raise CADException(f"Error getting comments: {e}")
    
    def set_comments(self, value):
        """
        Sets the document comments.
        
        Args:
            value (str): The new comments.
            
        Raises:
            CADException: If the comments cannot be set.
        """
        try:
            self.summary_info.Comments = str(value)
        except Exception as e:
            raise CADException(f"Error setting comments: {e}")
    
    # ==================== SUMMARY PROPERTIES ====================
    
    def get_manager(self):
        """
        Gets the document manager name.
        
        Returns:
            str: The manager name.
        """
        try:
            return self.summary_info.Manager
        except Exception as e:
            raise CADException(f"Error getting manager: {e}")
    
    def set_manager(self, value):
        """
        Sets the document manager name.
        
        Args:
            value (str): The new manager name.
            
        Raises:
            CADException: If the manager cannot be set.
        """
        try:
            self.summary_info.Manager = str(value)
        except Exception as e:
            raise CADException(f"Error setting manager: {e}")
    
    def get_company(self):
        """
        Gets the company name.
        
        Returns:
            str: The company name.
        """
        try:
            return self.summary_info.Company
        except Exception as e:
            raise CADException(f"Error getting company: {e}")
    
    def set_company(self, value):
        """
        Sets the company name.
        
        Args:
            value (str): The new company name.
            
        Raises:
            CADException: If the company cannot be set.
        """
        try:
            self.summary_info.Company = str(value)
        except Exception as e:
            raise CADException(f"Error setting company: {e}")
    
    def get_category(self):
        """
        Gets the document category.
        
        Returns:
            str: The document category.
        """
        try:
            return self.summary_info.Category
        except Exception as e:
            raise CADException(f"Error getting category: {e}")
    
    def set_category(self, value):
        """
        Sets the document category.
        
        Args:
            value (str): The new category.
            
        Raises:
            CADException: If the category cannot be set.
        """
        try:
            self.summary_info.Category = str(value)
        except Exception as e:
            raise CADException(f"Error setting category: {e}")
    
    # ==================== STATISTICS (READ-ONLY) ====================
    
    def get_created_date(self):
        """
        Gets the document creation date.
        
        Returns:
            str: The creation date and time.
        """
        try:
            return self.summary_info.CreateTime
        except Exception as e:
            raise CADException(f"Error getting creation date: {e}")
    
    def get_modified_date(self):
        """
        Gets the document last modification date.
        
        Returns:
            str: The last modification date and time.
        """
        try:
            return self.summary_info.ModTime
        except Exception as e:
            raise CADException(f"Error getting modification date: {e}")
    
    def get_last_saved_by(self):
        """
        Gets the name of the user who last saved the document.
        
        Returns:
            str: The last user who saved the document.
        """
        try:
            return self.summary_info.LastSavedBy
        except Exception as e:
            raise CADException(f"Error getting last saved by: {e}")
    
    def get_edit_time(self):
        """
        Gets the total editing time for the document.
        
        Returns:
            int: The total editing time in seconds.
        """
        try:
            return self.summary_info.EditTime
        except Exception as e:
            raise CADException(f"Error getting edit time: {e}")
    
    def get_revision_number(self):
        """
        Gets the document revision number.
        
        Returns:
            str: The revision number.
        """
        try:
            return self.summary_info.RevisionNumber
        except Exception as e:
            raise CADException(f"Error getting revision number: {e}")
    
    # ==================== CUSTOM PROPERTIES ====================
    
    def get_num_custom_info(self):
        """
        Gets the number of custom properties in the document.
        Python equivalent of VBA: ThisDrawing.SummaryInfo.NumCustomInfo
        
        Returns:
            int: The number of custom properties.
        """
        try:
            return self.summary_info.NumCustomInfo
        except Exception as e:
            raise CADException(f"Error getting custom properties count: {e}")
    
    def get_all_custom_properties(self):
        """
        Retrieves all custom properties as a dictionary.
        
        Returns:
            dict: A dictionary where keys are property names and values are property values.
        """
        try:
            custom_props = {}
            num_custom = self.get_num_custom_info()
            
            for i in range(1, num_custom + 1):
                prop_name = self.summary_info.GetCustomByIndex(i - 1)
                prop_value = self.summary_info.GetCustomValue(prop_name)
                custom_props[prop_name] = prop_value
            
            return custom_props
        except Exception as e:
            raise CADException(f"Error getting all custom properties: {e}")
    
    def add_custom_property(self, property_name, value):
        """
        Adds or updates a custom property in the document.
        
        Args:
            property_name (str): The name of the custom property.
            value (str): The value of the custom property.
            
        Raises:
            CADException: If the property cannot be added.
        """
        try:
            self.summary_info.SetCustomByKey(property_name, str(value))
        except Exception as e:
            raise CADException(f"Error adding custom property '{property_name}': {e}")
    
    def get_custom_property(self, property_name):
        """
        Retrieves the value of a specific custom property.
        
        Args:
            property_name (str): The name of the custom property.
            
        Returns:
            str: The value of the custom property.
            
        Raises:
            CADException: If the property does not exist or cannot be retrieved.
        """
        try:
            return self.summary_info.GetCustomValue(property_name)
        except Exception as e:
            raise CADException(f"Error getting custom property '{property_name}': {e}")
    
    def remove_custom_property(self, property_name):
        """
        Removes a custom property from the document.
        
        Args:
            property_name (str): The name of the custom property to remove.
            
        Raises:
            CADException: If the property cannot be removed.
        """
        try:
            self.summary_info.RemoveCustomByKey(property_name)
        except Exception as e:
            raise CADException(f"Error removing custom property '{property_name}': {e}")
    
    def update_custom_property(self, property_name, new_value):
        """
        Updates an existing custom property value.
        
        Args:
            property_name (str): The name of the custom property.
            new_value (str): The new value for the property.
            
        Raises:
            CADException: If the property cannot be updated.
        """
        try:
            # First check if it exists
            existing_value = self.get_custom_property(property_name)
            # If we get here, it exists, so update it
            self.add_custom_property(property_name, new_value)
        except Exception as e:
            raise CADException(f"Error updating custom property '{property_name}': {e}")
    
    def clear_all_custom_properties(self):
        """
        Removes all custom properties from the document.
        
        Raises:
            CADException: If properties cannot be cleared.
        """
        try:
            num_custom = self.get_num_custom_info()
            # Iterate backwards to avoid index shifting during deletion
            for i in range(num_custom, 0, -1):
                prop_name = self.summary_info.GetCustomByIndex(i - 1)
                self.remove_custom_property(prop_name)
        except Exception as e:
            raise CADException(f"Error clearing custom properties: {e}")


class AutoCAD:
    """Main class for interacting with the AutoCAD application via COM."""
    def __init__(self):
        """
        Initializes the AutoCAD application object.

        Raises:
            CADException: If AutoCAD application cannot be initialized.
        """
        try:
            self.acad = win32com.client.Dispatch("AutoCAD.Application")
            self.acad.Visible = True
        except Exception as e:
            raise CADException(f"Error initializing AutoCAD: {e}")

    @property
    def doc(self):
        """ Returns `ActiveDocument` of current :attr:`Application`"""
        return self.acad.ActiveDocument

    @property
    def modelspace(self):
        """ Returns `ActiveDocument` of current :attr:`Application`"""
        return self.doc.ModelSpace

    @property
    def properties(self):
        """
        Returns a DrawingProperties object for managing document metadata.
        
        This allows easy access to document properties like:
        - Title, Subject, Author, Keywords, Comments
        - Manager, Company, Category
        - Statistics (creation date, modification date, edit time)
        - Custom properties (add, get, remove, list)
        
        Example:
            >>> autocad = AutoCAD()
            >>> autocad.properties.set_title("My Drawing")
            >>> autocad.properties.add_custom_property("ProjectID", "12345")
            >>> all_custom = autocad.properties.get_all_custom_properties()
        
        Returns:
            DrawingProperties: A properties manager for the active document.
        """
        return DrawingProperties(self.doc)

    def purge(self):
        """
        Purges all unused elements (e.g., layers, blocks) in the active document.
        Raises:
            CADException: If an error occurs during the purge operation.
        """
        try:
            self.doc.PurgeAll()
            print("Successfully purged the document.")
        except Exception as e:
            raise CADException(f"Error purging AutoCAD document: {e}")

    def iter_objects(self, object_type=None):
        """
        Iterates over objects in the model space.

        Args:
            object_type (str, optional): The type of AutoCAD object to filter by (e.g., 'AcDbCircle').
                                         If None, iterates over all objects. Defaults to None.

        Yields:
            The AutoCAD object.
        """
        for obj in self.modelspace:
            if object_type is None or obj.EntityName == object_type:
                yield obj

    def add_circle(self, center, radius):
        """
        Adds a circle to the model space.
        Args:
            center (APoint): The center point of the circle.
            radius (float): The radius of the circle.
        Returns:
            The created circle object.
        Raises:
            CADException: If the circle cannot be added.
        """
        try:
            circle = self.modelspace.AddCircle(center.to_variant(), radius)
            return circle
        except Exception as e:
            raise CADException(f"Error adding circle: {e}")

    def add_line(self, start_point, end_point):
        """
        Adds a line to the model space.
        Args:
            start_point (APoint): The starting point of the line.
            end_point (APoint): The ending point of the line.
        Returns:
            The created line object.
        Raises:
            CADException: If the line cannot be added.
        """
        try:
            line = self.modelspace.AddLine(start_point.to_variant(), end_point.to_variant())
            return line
        except Exception as e:
            raise CADException(f"Error adding line: {e}")

    def add_rectangle(self, lower_left, upper_right):
        """
        Adds a rectangle (as a closed polyline) to the model space.
        Args:
            lower_left (APoint): The lower-left corner of the rectangle.
            upper_right (APoint): The upper-right corner of the rectangle.
        Returns:
            The created polyline object representing the rectangle.
        Raises:
            CADException: If the rectangle cannot be added.
        """
        try:
            x1, y1 = lower_left.to_tuple()
            x2, y2 = upper_right.to_tuple()
            points = [
                x1, y1,
                x2, y1,
                x2, y2,
                x1, y2,
                x1, y1
            ]
            points_variant = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, points)
            polyline = self.modelspace.AddLightweightPolyline(points_variant)
            return polyline
        except Exception as e:
            raise CADException(f"Error adding rectangle: {e}")

    def add_ellipse(self, center, major_axis, ratio):
        """
        Adds an ellipse to the model space.
        Args:
            center (APoint): The center point of the ellipse.
            major_axis (APoint): A point defining the major axis from the center.
            ratio (float): The ratio of the minor axis to the major axis.
        Returns:
            The created ellipse object.
        Raises:
            CADException: If the ellipse cannot be added.
        """
        try:
            ellipse = self.modelspace.AddEllipse(center.to_variant(), major_axis.to_variant(), ratio)
            return ellipse
        except Exception as e:
            raise CADException(f"Error adding ellipse: {e}")

    def add_text(self, text):
        """
        Adds a text object to the model space.
        Args:
            text (Text): A Text object containing the content, insertion point, and height.
        Returns:
            The created text object.
        Raises:
            CADException: If the text cannot be added.
        """
        try:
            text_obj = self.modelspace.AddText(text.content, text.insertion_point.to_variant(), text.height)
            return text_obj
        except Exception as e:
            raise CADException(f"Error adding text: {e}")

    def add_dimension(self, dimension):
        """
        Adds a dimension to the model space.
        Args:
            dimension (Dimension): A Dimension object containing points and type.
        Returns:
            The created dimension object.
        Raises:
            CADException: If the dimension cannot be added.
        """
        try:
            dimension_obj = None
            if dimension.dimension_type == DimensionType.ALIGNED:
                dimension_obj = self.modelspace.AddDimAligned(dimension.start_point.to_variant(),
                                                              dimension.end_point.to_variant(),
                                                              dimension.text_point.to_variant())
            elif dimension.dimension_type == DimensionType.LINEAR:
                dimension_obj = self.modelspace.AddDimLinear(dimension.start_point.to_variant(),
                                                             dimension.end_point.to_variant(),
                                                             dimension.text_point.to_variant())
            elif dimension.dimension_type == DimensionType.ANGULAR:
                dimension_obj = self.modelspace.AddDimAngular(dimension.start_point.to_variant(),
                                                              dimension.end_point.to_variant(),
                                                              dimension.text_point.to_variant())
            elif dimension.dimension_type == DimensionType.RADIAL:
                dimension_obj = self.modelspace.AddDimRadial(dimension.start_point.to_variant(),
                                                             dimension.end_point.to_variant(),
                                                             dimension.text_point.to_variant())
            elif dimension.dimension_type == DimensionType.DIAMETER:
                dimension_obj = self.modelspace.AddDimDiameter(dimension.start_point.to_variant(),
                                                               dimension.end_point.to_variant(),
                                                               dimension.text_point.to_variant())
            return dimension_obj
        except Exception as e:
            raise CADException(f"Error adding dimension: {e}")

    def add_point(self, point):
        """
        Adds a point object to the model space.
        Args:
            point (APoint): The point to add.
        Returns:
            The created point object.
        Raises:
            CADException: If the point cannot be added.
        """
        try:
            point_obj = self.modelspace.AddPoint(point.to_variant())
            return point_obj
        except Exception as e:
            raise CADException(f"Error adding point: {e}")

    def add_polyline(self, points):
        """
        Adds a lightweight polyline to the model space.
        Args:
            points (list[APoint]): A list of APoint objects defining the vertices.
        Returns:
            The created polyline object.
        Raises:
            CADException: If the polyline cannot be added.
        """
        try:
            points_variant = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8,
                                                     [coord for point in points for coord in point.to_tuple()])
            polyline = self.modelspace.AddLightweightPolyline(points_variant)
            return polyline
        except Exception as e:
            raise CADException(f"Error adding polyline: {e}")

    def add_spline(self, points):
        """
        Adds a spline to the model space.
        Args:
            points (list[APoint]): A list of APoint objects defining the control points.
        Returns:
            The created spline object.
        Raises:
            CADException: If the spline cannot be added.
        """
        try:
            points_variant = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8,
                                                     [coord for point in points for coord in point.to_variant()])
            spline = self.modelspace.AddSpline(points_variant)
            return spline
        except Exception as e:
            raise CADException(f"Error adding spline: {e}")

    def add_arc(self, center, radius, start_angle, end_angle):
        """
        Adds an arc to the model space.
        Args:
            center (APoint): The center point of the arc.
            radius (float): The radius of the arc.
            start_angle (float): The starting angle in radians.
            end_angle (float): The ending angle in radians.
        Returns:
            The created arc object.
        Raises:
            CADException: If the arc cannot be added.
        """
        try:
            arc = self.modelspace.AddArc(center.to_variant(), radius, start_angle, end_angle)
            return arc
        except Exception as e:
            raise CADException(f"Error adding arc: {e}")

    def explode_object(self, obj):
        """
        Explodes a complex object (like a block or polyline) into its constituent parts.
        Args:
            obj: The AutoCAD object to explode.
        Returns:
            list: A list of the exploded objects.
        Raises:
            CADException: If the object cannot be exploded.
        """
        try:
            exploded_items = obj.Explode()
            return exploded_items
        except Exception as e:
            raise CADException(f"Error exploding object: {e}")


    def get_block_extents(self, block_name):
        """
        Gets the geometric extents (bounding box) of a block reference.
        Args:
            block_name (str): The name of the block.
        Returns:
            tuple(APoint, APoint): A tuple containing the minimum and maximum points of the extents.
        Raises:
            CADException: If the block extents cannot be retrieved.
        """
        try:
            for entity in self.iter_objects("AcDbBlockReference"):
                if entity.Name == block_name:
                    print(entity.GetBoundingBox)
                    min_pt, max_pt = entity.GetBoundingBox()
                    return APoint(*min_pt), APoint(*max_pt)
        except Exception as e:
            raise CADException(f"Error getting extents of block '{block_name}': {e}")

    def get_entity_extents(self, entity):
        """
        Returns the bounding box (min and max APoint) of any AutoCAD entity using GetBoundingBox.

        Args:
            entity: The AutoCAD COM object (line, block, polyline, etc.)
        Returns:
            tuple(APoint, APoint): Min and Max APoint
        Raises:
            CADException: If bounding box can't be computed
        """
        try:
            min_pt, max_pt = entity.GetBoundingBox()
            return APoint(*min_pt), APoint(*max_pt)
        except Exception as e:
            raise CADException(f"Cannot get bounding box for entity: {e}")

    def add_overall_dimensions(self, entity):
        """
        Adds overall horizontal and vertical dimensions to an entity based on its bounding box.
        Args:
            entity: The AutoCAD object to dimension.
        Raises:
            CADException: If dimensions cannot be added.
        """
        try:
            min_point, max_point = self.get_entity_extents(entity)

            self.add_dimension(Dimension(
                min_point,
                APoint(max_point.x, min_point.y, min_point.z),
                APoint((min_point.x + max_point.x) / 2, min_point.y - 5, min_point.z),
                DimensionType.ALIGNED
            ))

            self.add_dimension(Dimension(
                min_point,
                APoint(min_point.x, max_point.y, min_point.z),
                APoint(min_point.x - 5, (min_point.y + max_point.y) / 2, min_point.z),
                DimensionType.ALIGNED
            ))

        except Exception as e:
            raise CADException(f"Failed to add overall dimensions: {e}")

    def get_user_defined_blocks(self):
        """
        Retrieves a list of all user-defined block names in the document.
        Returns:
            list[str]: A list of block names.
        Raises:
            CADException: If the block list cannot be retrieved.
        """
        try:
            blocks = self.doc.Blocks
            user_defined_blocks = [block.Name for block in blocks
                                   if not block.IsLayout and not block.Name.startswith('*') and block.Name != 'GENAXEH']
            return user_defined_blocks
        except Exception as e:
            raise CADException(f"Error getting user-defined blocks: {e}")

    def create_layer(self, layer):
        """
        Creates a new layer in the document.
        Args:
            layer (Layer): A Layer object with name and color properties.
        Returns:
            The created layer object.
        Raises:
            CADException: If the layer cannot be created.
        """
        try:
            layers = self.doc.Layers
            new_layer = layers.Add(layer.name)
            new_layer.Color = layer.color.value
            return new_layer
        except Exception as e:
            raise CADException(f"Error creating layer '{layer.name}': {e}")

    def set_active_layer(self, layer_name):
        """
        Sets the specified layer as the active layer for new objects.
        Args:
            layer_name (str): The name of the layer to activate.
        Raises:
            CADException: If the layer cannot be set as active.
        """
        try:
            self.doc.ActiveLayer = self.doc.Layers.Item(layer_name)
        except Exception as e:
            raise CADException(f"Error setting active layer '{layer_name}': {e}")

    def insert_block(self, block):
        """
        Inserts a block reference into the model space.
        Args:
            block (BlockReference): A BlockReference object with name, insertion point, scale, and rotation.
        Returns:
            The created block reference object.
        Raises:
            CADException: If the block cannot be inserted.
        """
        try:
            block_ref = self.modelspace.InsertBlock(block.insertion_point.to_variant(), block.name, block.scale,
                                                    block.scale, block.scale, block.rotation)
            return block_ref
        except Exception as e:
            raise CADException(f"Error inserting block '{block.name}': {e}")

    def save_as(self, file_path):
        """
        Saves the active document to a new file path.
        Args:
            file_path (str): The full path to save the new file.
        Raises:
            CADException: If the document cannot be saved.
        """
        try:
            self.doc.SaveAs(file_path)
        except Exception as e:
            raise CADException(f"Error saving document as '{file_path}': {e}")

    def save(self):
        """
        Saves the active document.
        Raises:
            CADException: If an error occurs during saving.
        """
        try:
            self.doc.Save()
            print("Document saved successfully.")
        except Exception as e:
            raise CADException(f"Error saving AutoCAD document: {e}")

    def close(self, save_changes=True):
        """
        Closes the active document.
        Args:
            save_changes (bool): If True, save changes before closing. Defaults to True.
        Raises:
            CADException: If an error occurs during closing.
        """
        try:
            self.doc.Close(SaveChanges=save_changes)
            print("Document closed successfully.")
        except Exception as e:
            raise CADException(f"Error closing AutoCAD document: {e}")

    def open_file(self, file_path):
        """
        Opens an existing drawing file.
        Args:
            file_path (str): The full path to the file to open.
        Raises:
            CADException: If the file cannot be opened.
        """
        try:
            self.acad.Documents.Open(file_path)
        except Exception as e:
            raise CADException(f"Error opening file '{file_path}': {e}")

    def get_block_coordinates(self, block_name):
        """
        Gets the insertion coordinates of all references of a specific block.
        Args:
            block_name (str): The name of the block to find.
        Returns:
            list[APoint]: A list of APoint objects for each block reference found.
        Raises:
            CADException: If an error occurs while retrieving coordinates.
        """
        try:
            block_references = []
            for entity in self.iter_objects("AcDbBlockReference"):
                if entity.Name == block_name:
                    insertion_point = entity.InsertionPoint
                    block_references.append(APoint(insertion_point[0], insertion_point[1], insertion_point[2]))
            return block_references
        except Exception as e:
            raise CADException(f"Error getting coordinates of block '{block_name}': {e}")

    def delete_object(self, obj):
        """
        Deletes a specified object from the model space.
        Args:
            obj: The AutoCAD object to delete.
        Raises:
            CADException: If the object cannot be deleted.
        """
        try:
            obj.Delete()
        except Exception as e:
            raise CADException(f"Error deleting object: {e}")

    def clone_object(self, obj, new_insertion_point):
        """
        Creates a copy of an object at a new location.
        Args:
            obj: The AutoCAD object to clone.
            new_insertion_point (APoint): The insertion point for the cloned object.
        Returns:
            The newly created cloned object.
        Raises:
            CADException: If the object cannot be cloned.
        """
        try:
            cloned_obj = obj.Copy(new_insertion_point.to_variant())
            return cloned_obj
        except Exception as e:
            raise CADException(f"Error cloning object: {e}")

    def modify_object_property(self, obj, property_name, new_value):
        """
        Modifies a property of a given object.
        Args:
            obj: The AutoCAD object to modify.
            property_name (str): The name of the property to change (e.g., 'Color').
            new_value: The new value for the property.
        Raises:
            CADException: If the property cannot be modified.
        """
        try:
            setattr(obj, property_name, new_value)
        except Exception as e:
            raise CADException(f"Error modifying property '{property_name}' of object: {e}")

    def repeat_block_horizontally(self, block_name, total_length, block_length, insertion_point):
        """
        Repeats a block horizontally to fill a specified total length.
        Args:
            block_name (str): The name of the block to repeat.
            total_length (float): The total length to fill.
            block_length (float): The length of a single block.
            insertion_point (APoint): The starting insertion point.
        Raises:
            CADException: If an error occurs during the operation.
        """
        try:
            x, y, z = insertion_point.x, insertion_point.y, insertion_point.z
            num_blocks = total_length // block_length

            for i in range(int(num_blocks)):
                new_insertion_point = APoint(x + i * block_length, y, z)
                self.insert_block(BlockReference(block_name, new_insertion_point))
        except Exception as e:
            raise CADException(f"Error repeating block '{block_name}' horizontally: {e}")

    def set_layer_visibility(self, layer_name, visible=True):
        """
        Sets the visibility of a layer.
        Args:
            layer_name (str): The name of the layer.
            visible (bool): True to make the layer visible, False to hide it.
        Raises:
            CADException: If the layer visibility cannot be changed.
        """
        try:
            layer = self.doc.Layers.Item(layer_name)
            layer.LayerOn = visible
        except Exception as e:
            raise CADException(f"Error setting visibility of layer '{layer_name}': {e}")

    def lock_layer(self, layer_name, lock=True):
        """
        Locks or unlocks a layer.
        Args:
            layer_name (str): The name of the layer.
            lock (bool): True to lock the layer, False to unlock it.
        Raises:
            CADException: If the layer lock state cannot be changed.
        """
        try:
            layer = self.doc.Layers.Item(layer_name)
            layer.Lock = lock
        except Exception as e:
            raise CADException(f"Error locking/unlocking layer '{layer_name}': {e}")

    def delete_layer(self, layer_name):
        """
        Deletes a layer from the document.
        Args:
            layer_name (str): The name of the layer to delete.
        Raises:
            CADException: If the layer cannot be deleted.
        """
        try:
            layer = self.doc.Layers.Item(layer_name)
            layer.Delete()
        except Exception as e:
            raise CADException(f"Error deleting layer '{layer_name}': {e}")

    def change_layer_color(self, layer_name, color):
        """
        Changes the color of a layer.
        Args:
            layer_name (str): The name of the layer.
            color (Color): The new color for the layer.
        Raises:
            CADException: If the layer color cannot be changed.
        """
        try:
            layer = self.doc.Layers.Item(layer_name)
            layer.color = color.value
        except Exception as e:
            raise CADException(f"Error changing color of layer '{layer_name}': {e}")

    def set_layer_linetype(self, layer_name, linetype_name):
        """
        Sets the linetype for a specific layer. If the linetype is not loaded,
        it will be loaded from the default '.lin' file.
        Args:
            layer_name (str): The name of the layer to modify.
            linetype_name (str): The name of the linetype to apply (e.g., 'DASHED', 'CENTER').
        Raises:
            CADException: If the linetype cannot be set for the layer.
        """
        try:
            layer = self.doc.Layers.Item(layer_name)
            linetypes = self.doc.Linetypes
            if linetype_name not in linetypes:
                self.doc.Linetypes.Load(linetype_name, linetype_name)
            layer.Linetype = linetype_name
        except Exception as e:
            raise CADException(f"Error setting linetype of layer '{layer_name}': {e}")

    def move_object(self, obj, new_insertion_point):
        """
        Moves an object from its current position to a new insertion point.
        Args:
            obj: The AutoCAD object to move.
            new_insertion_point (APoint): The target point to move the object to.
        Raises:
            CADException: If the object does not support the Move() method or an error occurs.
        """
        try:
            if not hasattr(obj, "Move"):
                raise CADException("The object does not support Move().")
            try:
                from_point = win32com.client.VARIANT(
                    pythoncom.VT_ARRAY | pythoncom.VT_R8, list(obj.InsertionPoint)
                )
            except AttributeError:
                from_point = win32com.client.VARIANT(
                    pythoncom.VT_ARRAY | pythoncom.VT_R8, list(obj.GeometricExtents.MinPoint)
                )
            to_point = new_insertion_point.to_variant()
            obj.Move(from_point, to_point)
        except Exception as e:
            raise CADException(f"Error moving object (type: {obj.EntityName}): {e}")

    def scale_object(self, obj, base_point, scale_factor):
        """
        Scales an object by a given factor relative to a base point.
        Args:
            obj: The AutoCAD object to scale.
            base_point (APoint): The base point for the scaling operation.
            scale_factor (float): The factor by which to scale the object.
        Raises:
            CADException: If an error occurs during scaling.
        """
        try:
            obj.ScaleEntity(base_point.to_variant(), scale_factor)
        except Exception as e:
            raise CADException(f"Error scaling object: {e}")

    def rotate_object(self, obj, base_point, rotation_angle):
        """
        Rotates an object around a base point.
        Args:
            obj: The AutoCAD object to rotate.
            base_point (APoint): The base point for the rotation.
            rotation_angle (float): The angle of rotation in radians.
        Raises:
            CADException: If an error occurs during rotation.
        """
        try:
            obj.Rotate(base_point.to_variant(), rotation_angle)
        except Exception as e:
            raise CADException(f"Error rotating object: {e}")

    def align_objects(self, objects, alignment=Alignment.LEFT):
        """
        Aligns a list of objects horizontally.
        Args:
            objects (list): A list of AutoCAD objects to align.
            alignment (Alignment): The alignment type (LEFT, RIGHT, or CENTER).
        Raises:
            CADException: If an error occurs during alignment.
        """
        try:
            if not objects:
                return
            if alignment == Alignment.LEFT:
                min_x = min(obj.InsertionPoint[0] for obj in objects)
                for obj in objects:
                    self.move_object(obj, APoint(min_x, obj.InsertionPoint[1], obj.InsertionPoint[2]))
            elif alignment == Alignment.RIGHT:
                max_x = max(obj.InsertionPoint[0] for obj in objects)
                for obj in objects:
                    self.move_object(obj, APoint(max_x, obj.InsertionPoint[1], obj.InsertionPoint[2]))
            elif alignment == Alignment.CENTER:
                center_x = (min(obj.InsertionPoint[0] for obj in objects) + max(
                    obj.InsertionPoint[0] for obj in objects)) / 2
                for obj in objects:
                    self.move_object(obj, APoint(center_x, obj.InsertionPoint[1], obj.InsertionPoint[2]))
        except Exception as e:
            raise CADException(f"Error aligning objects: {e}")

    def distribute_objects(self, objects, spacing):
        """
        Distributes objects horizontally with a specified spacing.
        Args:
            objects (list): A list of AutoCAD objects to distribute.
            spacing (float): The horizontal distance between the insertion points of adjacent objects.
        Raises:
            CADException: If an error occurs during distribution.
        """
        try:
            if not objects:
                return
            objects.sort(key=lambda obj: obj.InsertionPoint[0])
            for i in range(1, len(objects)):
                new_x = objects[i - 1].InsertionPoint[0] + spacing
                self.move_object(objects[i], APoint(new_x, objects[i].InsertionPoint[1], objects[i].InsertionPoint[2]))
        except Exception as e:
            raise CADException(f"Error distributing objects: {e}")

    def insert_block_from_file(self, file_path, insertion_point, scale=1.0, rotation=0.0):
        """
        Inserts a block into the current drawing from an external file.
        Args:
            file_path (str): The path to the .dwg file containing the block definition.
            insertion_point (APoint): The point where the block will be inserted.
            scale (float): The scale factor for the block.
            rotation (float): The rotation angle in radians.
        Returns:
            The created block reference object.
        Raises:
            CADException: If the block cannot be inserted from the file.
        """
        try:
            block_name = self.doc.Blocks.Import(file_path, file_path)
            block_ref = self.modelspace.InsertBlock(insertion_point.to_variant(), block_name, scale, scale, scale,
                                                    rotation)
            return block_ref
        except Exception as e:
            raise CADException(f"Error inserting block from file '{file_path}': {e}")

    def export_block_to_file(self, block_name, file_path):
        """
        Exports a block definition from the current drawing to a new .dwg file.
        Args:
            block_name (str): The name of the block to export.
            file_path (str): The destination path for the new .dwg file.
        Raises:
            CADException: If the block cannot be exported.
        """
        try:
            block = self.doc.Blocks.Item(block_name)
            block.Export(file_path)
        except Exception as e:
            raise CADException(f"Error exporting block '{block_name}' to '{file_path}': {e}")

    def modify_block_attribute(self, block_ref, tag, new_value):
        """
        Modifies the value of a specific attribute within a block reference.
        Args:
            block_ref: The block reference object containing the attribute.
            tag (str): The tag string of the attribute to modify.
            new_value (str): The new text value for the attribute.
        Raises:
            CADException: If the attribute cannot be modified.
        """
        try:
            for attribute in block_ref.GetAttributes():
                if attribute.TagString == tag:
                    attribute.TextString = new_value
        except Exception as e:
            raise CADException(f"Error modifying block attribute '{tag}': {e}")

    def modify_block_attribute_by_old_value(self, block_ref, tag, old_value, new_value):
        """
        Modifies a block attribute only if its current value matches a specific value.
        Args:
            block_ref: The block reference object.
            tag (str): The tag string of the attribute.
            old_value (str): The expected current value of the attribute.
            new_value (str): The new value to set if the old value matches.
        Raises:
            CADException: If an error occurs during modification.
        """
        try:
            for attribute in block_ref.GetAttributes():
                if attribute.TagString == tag:
                    if attribute.TextString == old_value:
                        attribute.TextString = new_value
        except Exception as e:
            raise CADException(f"Error modifying block attribute '{tag}': {e}")

    def delete_block_attribute(self, block_ref, tag):
        """
        Deletes an attribute from a block reference.
        Args:
            block_ref: The block reference object.
            tag (str): The tag string of the attribute to delete.
        Raises:
            CADException: If the attribute cannot be deleted.
        """
        try:
            for attribute in block_ref.GetAttributes():
                if attribute.TagString == tag:
                    attribute.Delete()
        except Exception as e:
            raise CADException(f"Error deleting block attribute '{tag}': {e}")

    def get_user_input_point(self, prompt="Select a point"):
        """
        Prompts the user to select a point in the AutoCAD drawing area.
        Args:
            prompt (str): The message to display to the user.
        Returns:
            APoint: The point selected by the user.
        Raises:
            CADException: If the user cancels or an error occurs.
        """
        try:
            point = self.doc.Utility.GetPoint(None, prompt)
            return APoint(point[0], point[1], point[2])
        except Exception as e:
            raise CADException(f"Error getting point input from user: {e}")

    def get_user_input_string(self, prompt="Enter a string"):
        """
        Prompts the user to enter a string in the command line.
        Args:
            prompt (str): The message to display to the user.
        Returns:
            str: The string entered by the user.
        Raises:
            CADException: If the user cancels or an error occurs.
        """
        try:
            return self.doc.Utility.GetString(False, prompt)
        except Exception as e:
            raise CADException(f"Error getting string input from user: {e}")

    def get_user_input_integer(self, prompt="Enter an integer"):
        """
        Prompts the user to enter an integer in the command line.
        Args:
            prompt (str): The message to display to the user.
        Returns:
            int: The integer entered by the user.
        Raises:
            CADException: If the user cancels or an error occurs.
        """
        try:
            return self.doc.Utility.GetInteger(prompt)
        except Exception as e:
            raise CADException(f"Error getting integer input from user: {e}")

    def show_message(self, message):
        """
        Displays a message in the AutoCAD command line.
        Args:
            message (str): The message to display.
        Raises:
            CADException: If the message cannot be displayed.
        """
        try:
            self.doc.Utility.Prompt(message + "\n")
        except Exception as e:
            raise CADException(f"Error displaying message: {e}")

    def create_group(self, group_name, objects):
        """
        Creates a new group containing the specified objects.
        Args:
            group_name (str): The name for the new group.
            objects (list): A list of AutoCAD objects to include in the group.
        Returns:
            The created group object.
        Raises:
            CADException: If the group cannot be created.
        """
        try:
            group = self.doc.Groups.Add(group_name)
            for obj in objects:
                group.AppendItems([obj])
            return group
        except Exception as e:
            raise CADException(f"Error creating group '{group_name}': {e}")

    def add_to_group(self, group_name, objects):
        """
        Adds objects to an existing group.
        Args:
            group_name (str): The name of the group to add to.
            objects (list): A list of AutoCAD objects to add.

        Raises:
            CADException: If objects cannot be added to the group.
        """
        try:
            group = self.doc.Groups.Item(group_name)
            for obj in objects:
                group.AppendItems([obj])
        except Exception as e:
            raise CADException(f"Error adding objects to group '{group_name}': {e}")

    def remove_from_group(self, group_name, objects):
        """
        Removes objects from a group.
        Args:
            group_name (str): The name of the group to remove from.
            objects (list): A list of AutoCAD objects to remove.

        Raises:
            CADException: If objects cannot be removed from the group.
        """
        try:
            group = self.doc.Groups.Item(group_name)
            for obj in objects:
                group.RemoveItems([obj])
        except Exception as e:
            raise CADException(f"Error removing objects from group '{group_name}': {e}")

    def select_group(self, group_name):
        """
        Retrieves all objects within a specified group.
        Args:
            group_name (str): The name of the group to select.
        Returns:
            list: A list of the objects contained within the group.
        Raises:
            CADException: If the group cannot be found or selected.
        """
        try:
            group = self.doc.Groups.Item(group_name)
            return [item for item in group.GetItems()]
        except Exception as e:
            raise CADException(f"Error selecting group '{group_name}': {e}")

    def add_mtext(self, content: str, insertion_point: APoint, width: float, height: float, text_style: str = None,
                  attachment_point: int = 1):
        """
        Adds a multiline text (MText) object to the model space with specified alignment.

        Args:
            content (str): The text string to display. Can include newlines.
            insertion_point (APoint): The insertion point for the text, relative to the alignment.
            width (float): The width of the MText bounding box.
            height (float): The height of the text characters.
            text_style (str, optional): The name of the text style to use. Defaults to None (use default).
            attachment_point (int): The COM constant for the attachment point (e.g., 1 for TopLeft, 5 for MiddleCenter).

        Returns:
            The created MText object.

        Raises:
            CADException: If the MText object cannot be added.
        """
        try:
            temp_point = APoint(0, 0, 0)
            mtext_obj = self.modelspace.AddMText(temp_point.to_variant(), width, content)
            mtext_obj.Height = height

            mtext_obj.AttachmentPoint = attachment_point
            if text_style:
                text_styles = self.doc.TextStyles
                style_exists = False
                for style in text_styles:
                    if style.Name.lower() == text_style.lower():
                        style_exists = True
                        break

                if style_exists:
                    try:
                        mtext_obj.StyleName = text_style
                    except Exception as e:
                        print(f"Error setting TextStyle '{text_style}': {e}. Using default.")
                        mtext_obj.StyleName = "Standard"
                else:
                    print(f"Warning: TextStyle '{text_style}' not found in drawing. Using 'Standard' style.")
                    mtext_obj.StyleName = "Standard"

            mtext_obj.InsertionPoint = insertion_point.to_variant()

            return mtext_obj
        except Exception as e:
            raise CADException(f"Error adding MText: {e}")

    def zoom_extents(self):
        """
        Zooms the active viewport to display all objects in the drawing (Zoom Extents).
        Raises:
            CADException: If the zoom operation fails.
        """
        try:
            self.acad.ZoomExtents()
        except Exception as e:
            raise CADException(f"Error performing Zoom Extents: {e}")

    def zoom_to_object(self, obj):
        """
        Zooms the active viewport to fit a specific object using GetBoundingBox.
        Args:
            obj: The AutoCAD object to zoom to.
        Raises:
            CADException: If the zoom operation fails.
        """
        try:
            min_pt, max_pt = obj.GetBoundingBox()
            min_point_variant = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, min_pt)
            max_point_variant = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, max_pt)

            self.acad.ZoomWindow(min_point_variant, max_point_variant)

        except Exception as e:
            raise CADException(f"Error zooming to object: {e}")

    def add_table(self, table_obj: Table):
        """
        Adds a table to the model space by manually drawing lines and text.
        This version is optimized for tables with headers and data only (no title)
        and provides precise text alignment within each cell.

        Args:
            table_obj (Table): The Table data object to draw.
        Raises:
            CADException: If the table cannot be created or data is inconsistent.
        """
        try:
            if not table_obj.data or not isinstance(table_obj.data[0], list):
                raise ValueError("Input 'data' must be a non-empty list of lists.")
            num_cols = len(table_obj.data[0])
            if num_cols == 0:
                raise ValueError("Input 'data' must contain at least one column.")
            if table_obj.headers and len(table_obj.headers) != num_cols:
                raise ValueError("Number of headers must match the number of columns in data.")
            if not table_obj.col_widths or len(table_obj.col_widths) != num_cols:
                raise ValueError("A list of column widths matching the number of columns is required for manual creation.")

            ip = table_obj.insertion_point
            col_widths = table_obj.col_widths
            row_height = table_obj.row_height
            total_width = sum(col_widths)

            num_data_rows = len(table_obj.data)
            num_header_rows = 1 if table_obj.headers else 0
            num_total_rows = num_header_rows + num_data_rows
            total_height = num_total_rows * row_height

            current_y = ip.y
            for _ in range(num_total_rows + 1):
                self.add_line(APoint(ip.x, current_y), APoint(ip.x + total_width, current_y))
                current_y -= row_height

            current_x = ip.x
            for width in col_widths:
                self.add_line(APoint(current_x, ip.y), APoint(current_x, ip.y - total_height))
                current_x += width
            self.add_line(APoint(ip.x + total_width, ip.y), APoint(ip.x + total_width, ip.y - total_height))

            acAttachmentPointMiddleCenter = 5

            current_y = ip.y

            # Header Row
            if table_obj.headers:
                current_x = ip.x
                for col_idx, header_text in enumerate(table_obj.headers):
                    cell_width = col_widths[col_idx]

                    cell_center_x = current_x + (cell_width / 2)
                    cell_center_y = current_y - (row_height / 2)

                    mtext_obj = self.add_mtext(
                        content=str(header_text),
                        insertion_point=APoint(cell_center_x, cell_center_y),
                        width=cell_width * 0.95,
                        height=table_obj.text_height,
                        text_style=table_obj.text_style,
                        attachment_point=acAttachmentPointMiddleCenter
                    )
                    mtext_obj.AttachmentPoint = acAttachmentPointMiddleCenter
                    current_x += cell_width
                current_y -= row_height

            for data_row in table_obj.data:
                current_x = ip.x
                for col_idx, cell_text in enumerate(data_row):
                    cell_width = col_widths[col_idx]

                    cell_center_x = current_x + (cell_width / 2)
                    cell_center_y = current_y - (row_height / 2)

                    mtext_obj = self.add_mtext(
                        content=str(cell_text),
                        insertion_point=APoint(cell_center_x, cell_center_y),
                        width=cell_width * 0.95,
                        height=table_obj.text_height,
                        text_style=table_obj.text_style,
                        attachment_point=acAttachmentPointMiddleCenter  # Pass alignment directly
                    )
                    mtext_obj.AttachmentPoint = acAttachmentPointMiddleCenter
                    current_x += cell_width
                current_y -= row_height

        except ValueError as ve:
            raise CADException(f"Invalid input for manual table creation: {ve}")
        except Exception as e:
            raise CADException(f"Error during manual table creation: {e}")

    def send_command(self, command_string):
        """
        Sends a single command string to the AutoCAD command line.
        Note: This is an asynchronous operation. The script may continue
        before the command is fully executed in AutoCAD. For commands that
        require user input or have long processing times, consider adding delays
        or using other methods to ensure completion.
        Args:
            command_string (str): The command string to send. It should be
                                  formatted as if typed in the command line.
                                  Crucially, end the command with a space ' ' or a
                                  newline '\\r' to simulate pressing Enter.
                                  Example: "LINE 0,0 100,100  " (two spaces for Enter twice)
        Raises:
            CADException: If the command cannot be sent.
        """
        try:
            self.doc.SendCommand(command_string)
        except Exception as e:
            raise CADException(f"Error sending command '{command_string}': {e}")

    def send_commands(self, commands):
        """
        Sends a sequence of command strings to the AutoCAD command line.
        Args:
            commands (list[str]): A list of command strings to send in sequence.
        Raises:
            CADException: If any command in the sequence fails.
        """
        try:
            for command in commands:
                self.send_command(command)
        except Exception as e:
            raise CADException(f"Error sending command sequence: {e}")
