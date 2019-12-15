bl_info = {
    "name": "GUI mood",
    "description": "",
    "author": "Arianna D'Alessandro",
    "version": (0, 0, 1),
    "blender": (2, 79, 0),
    "location": "3D View > Tools",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}

import bpy
import os


from bpy.props import (StringProperty,
                       BoolProperty,
                       EnumProperty,
                       PointerProperty
                       )
from bpy.types import (Panel,
                       Operator,
                       PropertyGroup,
                       )
# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------

class MySettings(PropertyGroup):

    mood = EnumProperty(
    	name="Mood",
    	items = [
	        ("Happy","Happy", "Happy", '', 0),
	        ("Sad", "Sad", "Sad", '', 1),
	     ],
	     default = "Happy"
	)   
    # sad = EnumProperty(
    #     name="Sad",
    #     description="",
    #     default = False
    #     )
    file = StringProperty(
        name="Json input",
        description="Specify the file with the extension",
        default="Json_interno.txt",
        maxlen=1024,
        )
# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class Generate(bpy.types.Operator):
    bl_idname = "wm.generate"
    bl_label = "Run"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        #gui_dir = "C:/Users/Giorgia/Desktop/Informatica grafica/Progetto/generate_scene.py"
        #exec(compile(open(gui_dir).read(), gui_dir, 'exec'))
        #text = bpy.data.texts.load('C:/Users/Giorgia/Desktop/Informatica grafica/Progetto/generate_scene.py')
        text = bpy.data.texts['Text.py']
        ctx = bpy.context.copy()
        ctx['edit_text'] = text
        bpy.ops.text.run_script(ctx)

        return {'FINISHED'}

# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------


class OBJECT_PT_CustomPanel(Panel):
    bl_idname = "object.custom_panel"
    bl_label = "Automatic scene generation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Auto Scene"

    @classmethod
    def poll(self,context):
        return context.scene is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "mood")
        layout.prop(mytool, "file")
        layout.operator("wm.generate")
        layout.separator()

# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

def register():
    bpy.utils.register_module(__name__)
    bpy.types.Scene.my_tool = PointerProperty(type=MySettings)

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()