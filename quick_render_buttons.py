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
    "version": (0, 0, 2),
    "blender": (3, 0, 0),
    "location": "PROPERTIES WINDOW > Render > UI > Render Tab",
    "description": "Render buttons in the style of Blender 2.7 and earlier",
    "warning": "",
    "wiki_url": "",
    "category": "Interface",
    }

import bpy
import os

from bl_ui.utils import PresetPanel

from bpy.utils import register_class, unregister_class

from bpy.types import (
    Operator,
    Panel,Scene, PropertyGroup,Object,Menu, Panel, UIList
)
from bpy.props import (IntProperty,

                       PointerProperty,
                       )

#SETTINGS /////////////////////////////////////////////////////////////////////////////////////////////////////

#Camera Manager settings

class Renderbuttons_Settings(PropertyGroup):

    switchStillAnim_prop : bpy.props.BoolProperty(
        name="Animation",
        description="Activate Animation Rendering",
        default = False)

#UI Stuff /////////////////////////////////////////////////////////////////////////////////////////////////////

#Camera Manager Button UI (I modified the appearence of the button, removed the "RENDER_ANIMATION" switch and added rows for the Animation and Playblast buttons)

class Renderbuttons(Panel):
    bl_space_type  = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context     = "render"
    bl_label       = "Interface"
    bl_idname      = "QuickRenderButtons"
    bl_options     = {'HIDE_HEADER'}

    # Check if the addon "DuBlast"  is installed
    def isDuBlastEnabled(self):
        addons = bpy.context.preferences.addons
        for addon in addons:
            if addon.module == 'dublast':
                return True
        return False

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
            #row.operator("render.playblast", text="Playblast", icon='PLAY')

        if self.isDuBlastEnabled():
            row.operator("render.playblast", text="Playblast", icon='PLAY')
            

#Operators /////////////////////////////////////////////////////////////////////////////////////////////////////



def menu_func(self, context):
    self.layout.separator()
    self.layout.operator('render.playblast', icon= 'FILE_MOVIE')

# classes = (
#     DUBLAST_PT_settings,
#     DUBLAST_PT_playblast_settings,
#     DUBLAST_OT_playblast,
# )

#addon_keymaps = []


#Classes /////////////////////////////////////////////////////////////////////////////////////////////////////

classes = (Renderbuttons_Settings,
            Renderbuttons,
            )
    
#addon_keymaps = []

def register():
    for i in classes:
        register_class(i)
        
#    register_class(Renderbuttons)
#    Scene.RBTab_Settings = PointerProperty(type=Renderbuttons_Settings)


    Scene.RBTab_Settings = PointerProperty(type=Renderbuttons_Settings)
    
#     # New playblast attribute in the scenes
#     if not hasattr( bpy.types.Scene, 'playblast' ):
#         bpy.types.Scene.playblast = bpy.props.PointerProperty( type=DUBLAST_PT_settings )

#     # menus
#     bpy.types.VIEW3D_MT_view.append(menu_func)

#     # keymaps
#     kc = bpy.context.window_manager.keyconfigs.addon
#     if kc:
#         km = kc.keymaps.new(name='Playblast', space_type='VIEW_3D')
#         kmi = km.keymap_items.new('render.playblast', 'RET', 'PRESS', ctrl=True)
#         addon_keymaps.append((km, kmi))



def unregister():
    for i in classes:
        unregister_class(i)
        
#    unregister_class(Renderbuttons)
    del Scene.RBTab_Settings
    



 
    # menu
    # bpy.types.VIEW3D_MT_view.remove(menu_func)

#     # keymaps
#     for km, kmi in addon_keymaps:
#         km.keymap_items.remove(kmi)
#     addon_keymaps.clear()

#     # attributes
#     del bpy.types.Scene.playblast


if __name__ == "__main__":
    try:
        unregister()
    except:
        pass
    register()
