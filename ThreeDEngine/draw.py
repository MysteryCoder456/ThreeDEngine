import pygame
from glm import vec2, vec3
from ThreeDEngine.options import Options
from ThreeDEngine.camera import Camera

def cube(surface: pygame.Surface, pos: vec3, size: vec3, outline = False):
    """Draw a cube.

    Arguments:
        pos {vec3} -- position of top left front corner
        size {vec3} -- size of cube
    """

    offset = vec2(Camera.pos.x + Options.window_size.x / 2, Camera.pos.y + Options.window_size.y / 2)
    fov = Camera.fov
    size.z /= 10

    # Front vertices
    proj1 = vec2(fov * pos.x / pos.z, fov * pos.y / pos.z) + offset # top left
    proj2 = vec2(fov * (pos.x + size.x) / pos.z, fov * pos.y / pos.z) + offset # top right
    proj3 = vec2(fov * pos.x / pos.z, fov * (pos.y + size.y) / pos.z) + offset # bottom left
    proj4 = vec2(fov * (pos.x + size.x) / pos.z, fov * (pos.y + size.y) / pos.z) + offset # bottom right
    
    # Back vertices
    proj5 = vec2(fov * pos.x / (pos.z + size.z), fov * pos.y / (pos.z + size.z)) + offset # top left
    proj6 = vec2(fov * (pos.x + size.x) / (pos.z + size.z), fov * pos.y / (pos.z + size.z)) + offset # top right
    proj7 = vec2(fov * pos.x / (pos.z + size.z), fov * (pos.y + size.y) / (pos.z + size.z)) + offset # bottom left
    proj8 = vec2(fov * (pos.x + size.x) / (pos.z + size.z), fov * (pos.y + size.y) / (pos.z + size.z)) + offset # bottom right
    
    front_face = (proj1, proj2, proj4, proj3)
    left_face = (proj1, proj3, proj7, proj5)
    right_face = (proj2, proj4, proj8, proj6)
    back_face = (proj5, proj6, proj8, proj7)

    sc = Options.stroke_color
    sw = round(Options.stroke_width / pos.z * fov)
    if outline:
        pygame.draw.polygon(surface, sc, back_face, sw)
        pygame.draw.polygon(surface, sc, left_face, sw)
        pygame.draw.polygon(surface, sc, right_face, sw)
        pygame.draw.polygon(surface, sc, front_face, sw)
    else:
        # TODO: Complete this code
        pygame.draw.polygon(surface, sc, back_face)
        pygame.draw.polygon(surface, sc, left_face)
        pygame.draw.polygon(surface, sc, right_face)
        pygame.draw.polygon(surface, sc, front_face)
