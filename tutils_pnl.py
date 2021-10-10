import bpy

from bpy.types import Panel

class JMU_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Modifier operations"
    bl_category = "tutils"

    def draw(self, context):

        layout = self.layout

        # 2 Columns with buttons
        row = layout.row()
        col = row.column()
        col.ooperator("object.apply_all_mods", text="Apply all")

        col = row.column()
        col.operator("object.cancel_all_mods", text="Cancel all")
