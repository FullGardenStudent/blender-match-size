
bl_info = {
    'name': 'Match Size Addon',
    'description': 'A poor implementation of Houdini\'s match size node'
    'author': 'FullGardenStudent'
    'version': (0, 6, 9),
    "blender": (3, 1, 0),
    'category': 'Object',
}


import bpy

from  bpy.types import Menu

addon_keymaps = []

class XMax(bpy.types.Operator):
    bl_idname = "x.max"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[0] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[1]
        print(v)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        n = co[0][0]
        for i in range(len(obj.data.vertices)):
            n = max(n,co[i][0])
        obj.location[0] -= n
        return { 'FINISHED' }

class XMin(bpy.types.Operator):
    bl_idname = "x.min"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[0] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[1]
        print(v)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        m = co[0][0]
        for i in range(len(obj.data.vertices)):
            m = min(m,co[i][0])
        obj.location[0] -= m
        return { 'FINISHED' }

class XCen(bpy.types.Operator):
    bl_idname = "x.cen"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[0] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[1]
        print(v)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        m = co[0][0]
        n = co[0][0]
        for i in range(len(obj.data.vertices)):
            m = min(m,co[i][0])
            n = max(n,co[i][0])
        obj.location[0] -= (m+n)/2
        return { 'FINISHED' }
#--------------------------------------------------------------------------------
class YMax(bpy.types.Operator):
    bl_idname = "y.max"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[1] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[1]
        print(v)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        n = co[0][1]
        for i in range(len(obj.data.vertices)):
            n = max(n,co[i][1])
        obj.location[1] -= n
        return { 'FINISHED' }

class YMin(bpy.types.Operator):
    bl_idname = "y.min"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[1] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[1]
        print(v)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        n = co[0][1]
        for i in range(len(obj.data.vertices)):
            n = min(n,co[i][1])
        obj.location[1] -= n
        return { 'FINISHED' }

class YCen(bpy.types.Operator):
    bl_idname = "y.cen"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[1] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[1]
        print(v)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        m = co[0][1]
        n = co[0][1]
        for i in range(len(obj.data.vertices)):
            n = min(n,co[i][1])
            m = max(m,co[i][1])
        obj.location[1] -= (m+n)/2
        return { 'FINISHED' }
#----------------------------------------------------------------------------------
class ZMax(bpy.types.Operator):
    bl_idname = "z.max"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[2] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[1]
        print(v)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        n = co[0][2]
        for i in range(len(obj.data.vertices)):
            n = max(n,co[i][2])
        obj.location[2] -= n
        return { 'FINISHED' }

class ZMin(bpy.types.Operator):
    bl_idname = "z.min"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[2] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[1]
        print(v)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        n = co[0][2]
        for i in range(len(obj.data.vertices)):
            n = min(n,co[i][2])
        obj.location[2] -= n
        return { 'FINISHED' }

class ZCen(bpy.types.Operator):
    bl_idname = "z.cen"
    bl_label = "matchsize"
    def execute(self, context):
        obj = bpy.context.active_object
        obj.location[2] = 0
        obj.data.update()
        bpy.context.view_layer.depsgraph.update()
        print(obj.location)
        v = obj.data.vertices[0]
        print(v.co)
        fc = obj.matrix_world @ v.co
        #print(fc)
        co = [(obj.matrix_world @v.co) for v in obj.data.vertices]
        k = len(obj.data.vertices)
        n = co[0][2]
        m = co[0][2]
        print(m)
        print(n)
        for i in range(len(obj.data.vertices)):
            n = min(n,co[i][2])
            m = max(m,co[i][2])
        print(m)
        print(n)
        obj.location[2] -= (m+n)/2
        return { 'FINISHED' }
#-----------------------------------------------------------------------------------
class FC_MT_SubMenuX(Menu):
    bl_label = 'X Axis position'
    def draw(self, context):
        layout = self.layout
        active_object = bpy.context.view_layer.objects.active
        pie = layout.menu_pie()
        if active_object:
            mode = active_object.mode
            if(mode=="OBJECT"):
                is_mesh = active_object.type
                if(is_mesh == "MESH"):
                    #print("Selected object is a mesh")
                    pie.operator("x.min", text="Minimum", icon="BLENDER")
                    pie.operator("x.max", text="Maximum", icon="BLENDER")
                    pie.operator("x.cen", text="Center", icon="BLENDER")
                else:
                    print("Please select a mesh")

class FC_MT_SubMenuY(Menu):
    bl_label = 'Y Axis position'
    def draw(self, context):
        layout = self.layout
        active_object = bpy.context.view_layer.objects.active
        pie = layout.menu_pie()
        if active_object:
            mode = active_object.mode
            if(mode=="OBJECT"):
                is_mesh = active_object.type
                if(is_mesh == "MESH"):
                    #print("Selected object is a mesh")
                    pie.operator("y.min", text="Minimum", icon="BLENDER")
                    pie.operator("y.max", text="Maximum", icon="BLENDER")
                    pie.operator("y.cen", text="Center", icon="BLENDER")
                else:
                    print("Please select a mesh")

class FC_MT_SubMenuZ(Menu):
    bl_label = 'Z Axis position'
    def draw(self, context):
        layout = self.layout
        active_object = bpy.context.view_layer.objects.active
        pie = layout.menu_pie()
        if active_object:
            mode = active_object.mode
            if(mode=="OBJECT"):
                is_mesh = active_object.type
                if(is_mesh == "MESH"):
                    #print("Selected object is a mesh")
                    pie.operator("z.min", text="Minimum", icon="BLENDER")
                    pie.operator("z.max", text="Maximum", icon="BLENDER")
                    pie.operator("z.cen", text="Center", icon="BLENDER")
                else:
                    print("Please select a mesh")

class FC_MT_Pie_menu(Menu):
    bl_label = "Axis Selection Menu"
    def draw(self, context):
        active_object = bpy.context.view_layer.objects.active
        print(active_object)
        layout = self.layout
        pie = layout.menu_pie()
        pie.operator("wm.call_menu_pie", text="X", icon="BLENDER").name="FC_MT_SubMenuX"
        pie.operator("wm.call_menu_pie", text="Y", icon="BLENDER").name="FC_MT_SubMenuY"
        pie.operator("wm.call_menu_pie", text="Z", icon="BLENDER").name="FC_MT_SubMenuZ"

def register():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type="EMPTY")
    kmi = km.keymap_items.new(ObjectCursorArray.bl_idname, 'V', 'PRESS')
    addon_keymaps.append((km, kmi))
    bpy.utils.register_class(FC_MT_Pie_menu)
    bpy.utils.register_class(FC_MT_SubMenuX)
    bpy.utils.register_class(FC_MT_SubMenuY)
    bpy.utils.register_class(FC_MT_SubMenuZ)
    bpy.utils.register_class(XMax)
    bpy.utils.register_class(XMin)
    bpy.utils.register_class(XCen)
    bpy.utils.register_class(YMax)
    bpy.utils.register_class(YMin)
    bpy.utils.register_class(YCen)
    bpy.utils.register_class(ZMax)
    bpy.utils.register_class(ZMin)
    bpy.utils.register_class(ZCen)

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(FC_MT_Pie_menu)
    bpy.utils.unregister_class(FC_MT_SubMenuX)
    bpy.utils.unregister_class(FC_MT_SubMenuY)
    bpy.utils.unregister_class(FC_MT_SubMenuZ)
    bpy.utils.unregister_class(XMax)
    bpy.utils.unregister_class(XMin)
    bpy.utils.unregister_class(XCen)
    bpy.utils.unregister_class(YMax)
    bpy.utils.unregister_class(YMin)
    bpy.utils.unregister_class(YCen)
    bpy.utils.unregister_class(ZMax)
    bpy.utils.unregister_class(ZMin)
    bpy.utils.unregister_class(ZCen)

if __name__ == "__main__":
    register()
    
    bpy.ops.wm.call_menu_pie(name="FC_MT_Pie_menu")





#----------------------------------------------------------------------------------------
