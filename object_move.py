import bpy

class ObjectMove(bpy.types.Operator):
    """My Object Moving Script"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.move"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Move object by one unit"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.
        # The original script
        scene = context.scene
        for obj in scene.objects:
            obj.location.y += 10.0

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.