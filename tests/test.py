import time

from AutoCAD import AutoCAD, APoint

# =====================================================================
# EXISTING TESTS (Original Code)
# =====================================================================

# acad = AutoCAD()
# time.sleep(1)
# acad.open_file("D:/jones/Jones/test.DWG")
# time.sleep(1)
# # Collect all block references
# blocks = list(acad.iter_objects("AcDbBlockReference"))
#
# # Print details about the blocks
# for block in blocks:
#     print(f"Block Name: {block.Name}, Insertion Point: {block.InsertionPoint}")
#     time.sleep(1)
#     if not block.Name == "A$C625fddc0":
#         acad.move_object(block, APoint(150, 150, 0))
#         time.sleep(1)
#         min_point, max_point = acad.get_block_extents(block.Name)
#         print(f"min : {min_point} max : {max_point}")
#         acad.add_rectangle(max_point, min_point)
#         acad.add_overall_dimensions(block)
#         acad.zoom_to_object(block)


# =====================================================================
# NEW TESTS: DRAWING PROPERTIES MANAGEMENT
# =====================================================================

def test_general_properties():
    """Test General Properties: Title, Subject, Author, Keywords, Comments"""
    print("\n=== Testing General Properties ===")
    
    acad = AutoCAD()
    time.sleep(0.5)
    
    # Set general properties
    acad.properties.set_title("My AutoCAD Drawing")
    acad.properties.set_subject("Technical Drawing")
    acad.properties.set_author("Jones Peter")
    acad.properties.set_keywords("python, autocad, drawing")
    acad.properties.set_comments("This is a test drawing created with Python")
    
    # Get and display general properties
    print(f"Title: {acad.properties.get_title()}")
    print(f"Subject: {acad.properties.get_subject()}")
    print(f"Author: {acad.properties.get_author()}")
    print(f"Keywords: {acad.properties.get_keywords()}")
    print(f"Comments: {acad.properties.get_comments()}")


def test_summary_properties():
    """Test Summary Properties: Manager, Company, Category"""
    print("\n=== Testing Summary Properties ===")
    
    acad = AutoCAD()
    time.sleep(0.5)
    
    # Set summary properties
    acad.properties.set_manager("Project Manager Name")
    acad.properties.set_company("My Company Inc.")
    acad.properties.set_category("Engineering")
    
    # Get and display summary properties
    print(f"Manager: {acad.properties.get_manager()}")
    print(f"Company: {acad.properties.get_company()}")
    print(f"Category: {acad.properties.get_category()}")


def test_statistics():
    """Test Statistics (Read-only): Creation date, Modification date, Edit time"""
    print("\n=== Testing Statistics ===")
    
    acad = AutoCAD()
    time.sleep(0.5)
    
    # Get and display statistics
    print(f"Created Date: {acad.properties.get_created_date()}")
    print(f"Modified Date: {acad.properties.get_modified_date()}")
    print(f"Last Saved By: {acad.properties.get_last_saved_by()}")
    print(f"Edit Time (seconds): {acad.properties.get_edit_time()}")
    print(f"Revision Number: {acad.properties.get_revision_number()}")


def test_custom_properties():
    """Test Custom Properties: Add, Get, Remove, List all"""
    print("\n=== Testing Custom Properties ===")
    
    acad = AutoCAD()
    time.sleep(0.5)
    
    # Add custom properties
    print("Adding custom properties...")
    acad.properties.add_custom_property("ProjectID", "PROJ-2026-001")
    acad.properties.add_custom_property("ClientName", "Acme Corporation")
    acad.properties.add_custom_property("DrawingVersion", "1.0")
    acad.properties.add_custom_property("ApprovedBy", "John Doe")
    
    # Get the count of custom properties (Python equivalent of VBA: NumCustomInfo)
    num_custom = acad.properties.get_num_custom_info()
    print(f"\nNumber of custom properties: {num_custom}")
    
    # Get a specific custom property
    print(f"\nGetting specific custom property:")
    print(f"ProjectID: {acad.properties.get_custom_property('ProjectID')}")
    print(f"ClientName: {acad.properties.get_custom_property('ClientName')}")
    
    # Get all custom properties as a dictionary
    print(f"\nAll custom properties:")
    all_props = acad.properties.get_all_custom_properties()
    for key, value in all_props.items():
        print(f"  {key}: {value}")
    
    # Update a custom property
    print(f"\nUpdating custom property 'DrawingVersion' to '1.1'...")
    acad.properties.update_custom_property("DrawingVersion", "1.1")
    print(f"Updated DrawingVersion: {acad.properties.get_custom_property('DrawingVersion')}")
    
    # Remove a specific custom property
    print(f"\nRemoving custom property 'ApprovedBy'...")
    acad.properties.remove_custom_property("ApprovedBy")
    
    # Verify removal
    remaining_props = acad.properties.get_all_custom_properties()
    print(f"Custom properties after removal: {remaining_props}")


def test_complete_workflow():
    """Complete workflow: Set all properties at once"""
    print("\n=== Complete Workflow Test ===")
    
    acad = AutoCAD()
    time.sleep(0.5)
    
    # Set all general properties
    print("Setting general properties...")
    acad.properties.set_title("Factory Layout Drawing")
    acad.properties.set_subject("Manufacturing Floor Plan")
    acad.properties.set_author("Engineering Team")
    acad.properties.set_keywords("layout, manufacturing, floor plan")
    acad.properties.set_comments("Updated layout for new equipment installation")
    
    # Set summary properties
    print("Setting summary properties...")
    acad.properties.set_manager("Factory Manager")
    acad.properties.set_company("Manufacturing Corp")
    acad.properties.set_category("Facility Management")
    
    # Add multiple custom properties at once
    print("Adding custom properties...")
    custom_data = {
        "ProjectID": "PROJ-2026-FACTORY",
        "Location": "Building A, Floor 2",
        "Reviewed": "Yes",
        "SafetyApproved": "Pending",
        "LastReviewDate": "2026-01-03"
    }
    
    for prop_name, prop_value in custom_data.items():
        acad.properties.add_custom_property(prop_name, prop_value)
    
    # Display all properties
    print("\n--- General Properties ---")
    print(f"Title: {acad.properties.get_title()}")
    print(f"Subject: {acad.properties.get_subject()}")
    print(f"Author: {acad.properties.get_author()}")
    
    print("\n--- Summary Properties ---")
    print(f"Company: {acad.properties.get_company()}")
    print(f"Manager: {acad.properties.get_manager()}")
    print(f"Category: {acad.properties.get_category()}")
    
    print("\n--- Statistics ---")
    print(f"Created: {acad.properties.get_created_date()}")
    print(f"Modified: {acad.properties.get_modified_date()}")
    
    print("\n--- Custom Properties ---")
    all_custom = acad.properties.get_all_custom_properties()
    print(f"Total custom properties: {acad.properties.get_num_custom_info()}")
    for key, value in all_custom.items():
        print(f"  {key}: {value}")
    
    # Save the document
    print("\nSaving document with all properties...")
    acad.save()


# Uncomment the test you want to run:
# test_general_properties()
# test_summary_properties()
# test_statistics()
# test_custom_properties()
# test_complete_workflow()
