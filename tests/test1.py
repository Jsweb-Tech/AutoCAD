from AutoCAD import AutoCAD

template_path = "Template.dwg"
new_file_path = "new.dwg"

acad = AutoCAD()
acad.open_file(template_path)
# Both blocks variable return the blocks in template.dwg - used to verify block existence
block_refs = list(acad.iter_objects("AcDbBlockReference"))
# print("Block References:", [b.Name for b in block_refs])

user_blocks = acad.get_user_defined_blocks()
print("User Defined Blocks:", user_blocks)

try:
    acad.export_blocks_to_file(['Back_Contact1', 'Loc_Sig_Proving', 'Relay_Coil_ACI', 'Supply'], new_file_path)
except Exception as e:
    print("Export failed:", e)
