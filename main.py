import bpy
from object_move import ObjectMove

bl_info = {
    "name": "My Addon",
    "blender": (3, 0, 0),
    "category": "Object",
}

def menu_func(self, context):
    self.layout.operator(ObjectMove.bl_idname)

def register():
    bpy.utils.register_class(ObjectMove)
    bpy.types.VIEW3D_MT_object.append(menu_func)

    print("my addon registered.")

def unregister():
    bpy.utils.unregister_class(ObjectMove)
    print("my addon unregister")
