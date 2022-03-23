# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENCE BLOCK #####


bl_info = {
    "name": "Quick Render Buttons",
    "author": "Thane5",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "PROPERTIES WINDOW > Render > UI > Render Tab",
    "description": "Render buttons in the style of Blender 2.7 and earlier",
    "warning": "",
    "wiki_url": "",
    "category": "Interface",
    }


import bpy
import os


from bpy.utils import register_class, unregister_class

from bpy.types import (
    Operator,
    Panel,Scene, PropertyGroup,Object,Menu, Panel, UIList
)


# UI BUTTONS /////////////////////////////////////////////////////////////////////////////////////////////////////

class Renderbuttons(Panel):
    bl_space_type  = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context     = "render"
    bl_label       = "Interface"
    bl_idname      = "QUICKRENDERBUTTONS_PT_buttons"
    bl_options     = {'HIDE_HEADER'}


    # Check if the addon "DuBlast"  is installed
    def isDuBlastEnabled(self):
        addons = bpy.context.preferences.addons
        for addon in addons:
            if addon.module == 'dublast':
                return True
        return False


    # Add the Buttons to the Render Panel
    def draw(self, context):
        scene  = context.scene
        rd     = context.scene.render

        layout = self.layout
        split  = layout.split()

        layout.use_property_split    = True
        layout.use_property_decorate = False

        row = layout.row(align=True)
        row.scale_y = 1

        if (context.active_object is not None) and (context.active_object.mode !='OBJECT'):
            row.enabled = False

        else:
            row.operator("render.render", text="Render", icon='RENDER_STILL')
            row.operator("render.render", text="Animation", icon='RENDER_ANIMATION').animation = True
        
        
        # Only Add the Playblast Button if "DuBlast" is installed
        if self.isDuBlastEnabled():
            row.operator("render.playblast", text="Playblast", icon='PLAY')
            


# REGISTER THINGS //////////////////////////////////////////////////////////////////////////////////////

classes = (Renderbuttons,
            )


def register():
    for i in classes:
        register_class(i)
        

def unregister():
    for i in classes:
        unregister_class(i)
        

if __name__ == "__main__":
    try:
        unregister()
    except:
        pass
    register()
