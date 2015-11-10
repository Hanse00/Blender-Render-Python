import bpy
import bmesh

def _move_bmesh(mesh, x, y, z):
    for vertice in mesh.verts:
        vertice.co.x += x
        vertice.co.y += y
        vertice.co.z += z

    return mesh

def _move_bpy_obj(obj, x, y, z):
    bm = bmesh.new()
    bm.from_mesh(obj.data)

    new_mesh = _move_bmesh(bm, x, y, z)

    new_mesh.to_mesh(obj.data)
    obj.data.update()

def move(obj_name, x, y, z):
    try:
        obj = bpy.data.objects[obj_name]
        _move_bpy_obj(obj, x, y, z)
    except KeyError:
        print("Object {} couldn't be found".format(obj_name))

if __name__ == "__main__":
    move("Cube", 0, 0, 1)
