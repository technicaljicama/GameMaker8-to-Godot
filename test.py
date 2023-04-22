from godot_project_lib import godot
import untangle
import shutil
import os
from distutils.dir_util import copy_tree

handler = godot.Godot()

prefix = "tut"
project_prefix = "Tutorial"

sprites = []
rids = []
rids2 = []

def parse_sprite_list():
    o = untangle.parse(f"{prefix}/Sprites/_resources.list.xml")
    for s in o.resources.resource:
        sp = s["name"]
        
        print(f"Found sprite: {sp}")
        
        os.mkdir(f"{project_prefix}/{sp}")
        copy_tree(f"{prefix}/Sprites/{sp}.images/", f"{project_prefix}/{sp}")
        sprites.append(sp)
       
def parse_room_list():
    o = untangle.parse(f"{prefix}/Rooms/_resources.list.xml")
    for s in o.resources.resource:
        sp = s["name"]
        
        print(f"Found room: {sp}")
        handler.create_scene(sp)
        
        o = untangle.parse(f"{prefix}/Rooms/{sp}.xml")

        for obj in rids:
            rid = handler.add_resource(f"{obj[1]}/image 0.png")
            rids2.append([rid, obj[0]])
            
        handler.add_node("main", 0, 0, 0, godot.Nodes.Node2D)
        for i in o.room.instances.instance:
            x = i.position["x"]
            y = i.position["y"]
            
            for idx in rids2:
                if i.object.cdata == idx[1]:
                    handler.add_node(idx[1], idx[0], x, y, godot.Nodes.Sprite)
        rids2.clear()
        
def parse_object_list():
    o = untangle.parse(f"{prefix}/Objects/_resources.list.xml")
    for s in o.resources.resource:
        sp = s["name"]
        
        print(f"Found object: {sp}")
        o = untangle.parse(f"{prefix}/Objects/{sp}.xml")

        rids.append([sp, o.object.sprite.cdata])

    
if __name__ == "__main__":
    handler.create_project(project_prefix)
    parse_sprite_list()
    parse_object_list()
    parse_room_list()
