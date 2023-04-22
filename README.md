# GameMaker8-to-Godot

# POC (Proof of Conecpt)

Converts splitted gmk files (by gmksplitter) to a godot engine project.

## What does it convert?
  - All objects in rooms (no scripting nor drag&drop)
  - Rooms to scenes
## What it doesnt convert:
  - Everything else
  
# This tool will fail if you have multiple frames in a sprite

# Execute
  - Extract your gamemaker project file using GMKSplitter
  - Edit the prefix on line 9 to your folder that contains the splitted files
  - Run test.py 
