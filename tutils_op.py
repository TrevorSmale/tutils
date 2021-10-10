import bpy
from bpy.types import Operator

class tutils_pnl_apply_all_op(Operator):
    bl_idname = "Apply all operator of the active object"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return true

            return False

        def execute(self, context):
            
            #Apply all modifiers of active object
            active_obj = context.view_layer.objects.active

            for mod in active_obj.modifiers:
                bpy.ops.object.modifier_apply(modifier=mod.name)

