from vpython import canvas, box, cylinder, vector, color, rate

# Create a 3D canvas
scene = canvas(width=800, height=600, background=color.white)

# Define functions to draw and transform 3D objects
def draw_cuboid(pos, length, width, height, color):
    return box(pos=vector(*pos), length=length, width=width, height=height, color=color)

def draw_cylinder(pos, radius, height, color):
    return cylinder(pos=vector(*pos), radius=radius, height=height, color=color)

def transform(obj, pos_delta=(0,0,0), angle=0, axis=(0,0,1), scale_factors=(1,1,1)):
    obj.pos += vector(*pos_delta)
    obj.rotate(angle=angle, axis=vector(*axis))
    obj.size = vector(obj.size.x * scale_factors[0], obj.size.y * scale_factors[1], obj.size.z * scale_factors[2])

# Draw and transform a cuboid
cuboid = draw_cuboid((-2, 0, 0), 2, 2, 2, color.blue)
transform(cuboid, pos_delta=(4, 0, 0), angle=45, axis=(0, 1, 0), scale_factors=(1.5, 1.5, 1.5))

# Draw and transform a cylinder
cyl = draw_cylinder((2, 2, 0), 1, 10, color.red)
transform(cyl, pos_delta=(0, -2, 0), angle=30, axis=(1, 0, 0), scale_factors=(1.5, 1.5, 1.5))

# Keep the 3D scene interactive
while True:
    rate(30)  # Set the frame rate to 30 frames per second
