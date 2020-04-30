from ThreeDEngine.util import *
from ThreeDEngine.camera import Camera
from ThreeDEngine.options import Options

from pygame.draw import polygon
from glm import vec2


class Face:
    """
    Class for making a 3D surface or face.

    Arguments:
        vertices {list/tuple} -- list or tuple of the vertices of the face
    """
    
    def __init__(self, vertices):
        self.vertices = vertices
    
    def get_center_pos(self):
        x = []
        y = []
        z = []

        for vertex in self.vertices:
            x.append(vertex.x)
            y.append(vertex.y)
            z.append(vertex.z)

        center = vec3(average(x), average(y), average(z))
        distance = dist3d(center, Camera.pos)

        return center, distance
    
    def get_projected_vertices(self):
        fov = Camera.fov
        offset = vec2(Camera.pos.x + Options.window_size.x / 2, Camera.pos.y + Options.window_size.y / 2)
        return [vec2(fov * vertex.x / vertex.z, fov * vertex.y / vertex.z) + offset for vertex in self.vertices]

    def render(self, surface, outline=False):
        if outline:
            polygon(surface, Options.stroke_color, self.get_projected_vertices(), Options.stroke_width)
        else:
            polygon(surface, Options.stroke_color, self.get_projected_vertices())
