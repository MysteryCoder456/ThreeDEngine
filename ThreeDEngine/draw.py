import pygame
from glm import vec3
from ThreeDEngine.options import Options
from ThreeDEngine.camera import Camera
from ThreeDEngine.face import Face

def cube(surface: pygame.Surface, pos: vec3, size: vec3, outline=False):
    """Draw a cube.

    Arguments:
        pos {vec3} -- position of top left front corner
        size {vec3} -- size of cube
    """

    size.z /= 10

    # Get postion of each vertex
    # Front vertices
    proj1 = vec3(pos.x, pos.y, pos.z) # top left
    proj2 = vec3((pos.x + size.x), pos.y, pos.z) # top right
    proj3 = vec3(pos.x, (pos.y + size.y), pos.z) # bottom left
    proj4 = vec3((pos.x + size.x), (pos.y + size.y), pos.z) # bottom right
    # Back vertices
    proj5 = vec3(pos.x, pos.y, (pos.z + size.z)) # top left
    proj6 = vec3((pos.x + size.x), pos.y, (pos.z + size.z)) # top right
    proj7 = vec3(pos.x, (pos.y + size.y), (pos.z + size.z)) # bottom left
    proj8 = vec3((pos.x + size.x), (pos.y + size.y), (pos.z + size.z))  # bottom right
    
    # Generate faces from vertices
    front_face = Face((proj1, proj2, proj4, proj3))
    left_face = Face((proj1, proj3, proj7, proj5))
    right_face = Face((proj2, proj4, proj8, proj6))
    back_face = Face((proj5, proj6, proj8, proj7))
    top_face = Face((proj1, proj2, proj6, proj5))
    bottom_face = Face((proj3, proj4, proj8, proj7))

    # Sort faces in list based on distance from camera revserse order
    faces = [front_face, left_face, right_face, back_face, top_face, bottom_face]
    faces.sort(key=lambda face: face.get_center_pos()[1], reverse=True)

    for face in faces:
        face.render(surface, outline)
