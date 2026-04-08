"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 50
ground_depth = 50
ground_y_position = 0

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(0, ground_y_position, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# ---------------------------------------------------------------------------
building_width = 4
building_height = 6
building_depth = 4
building_x = -8
building_z = 5

building = cmds.polyCube(
    name="building_01",
    width=building_width,
    height=building_height,
    depth=building_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(building_x, building_height / 2.0, building_z, building)

ball_radius = 1
ball_x = 10
ball_z = -5
ball = cmds.polySphere(
    name="ball_01",
    radius=ball_radius,
)
# Raise the ball so it sits on the ground plane.
cmds.move(ball_x, ball_radius, ball_z, ball)

trunk_radius = 1
trunk_height = 8
trunk_x = 19
trunk_z = 15
trunk = cmds.polyCylinder(
    name="trunk_01",
    radius=trunk_radius,
    height=trunk_height,
)
# Raise the trunk so it sits on the ground plane.
cmds.move(trunk_x, trunk_height / 2.0, trunk_z, trunk)

leaves_radius = 4
leaves_x = trunk_x
leaves_z = trunk_z
leaves = cmds.polySphere(
    name="leaves_01",
    radius=leaves_radius,
)
# Position the leaves on top of the trunk.
cmds.move(leaves_x, trunk_height + leaves_radius, leaves_z, leaves)

ring_radius = 2
ring_section_radius = 0.5
ring_x = -15
ring_z = -10
ring_rotation_x = 90
ring = cmds.polyTorus(
    name="ring_01",
    radius=ring_radius,
    sectionRadius=ring_section_radius,
)
# Rotate the ring to stand upright
cmds.rotate(ring_rotation_x, 0, 0, ring)
# Raise the ring so it sits on the ground plane.
cmds.move(ring_x, ring_radius + ring_section_radius, ring_z, ring)

ring2_radius = 2
ring2_section_radius = 0.5
ring2_x = -15
ring2_z = -10
ring2_rotation_x = 90
ring2_rotation_y = 90
ring2 = cmds.polyTorus(
    name="ring_02",
    radius=ring2_radius,
    sectionRadius=ring2_section_radius,
)
# Rotate the second ring to stand upright and perpendicular to link in the first ring
cmds.rotate(ring2_rotation_x, ring2_rotation_y, 0, ring2)
# Raise the second ring so it sits above the ground plane and links with the first ring.
cmds.move(ring2_x, ring2_radius + ring2_section_radius + 3, ring2_z, ring2)

ring3_radius = 2
ring3_section_radius = 0.5
ring3_x = -15
ring3_z = -10
ring3_rotation_x = 90
ring3 = cmds.polyTorus(
    name="ring_03",
    radius=ring3_radius,
    sectionRadius=ring3_section_radius,
)
# Rotate the third ring to stand upright and perpendicular to link in the second ring
cmds.rotate(ring3_rotation_x, 0, 0, ring3)
# Raise the third ring so it sits above the ground plane and links with the second ring.
cmds.move(ring3_x, ring3_radius + ring3_section_radius + 6, ring3_z, ring3)
# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")