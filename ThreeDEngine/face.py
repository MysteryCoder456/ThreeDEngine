import pyglet
from pyglet.gl import GL_POLYGON, GL_LINES
from glm import vec2

from ThreeDEngine.util import *
from ThreeDEngine.camera import Camera
from ThreeDEngine.options import Options


class Face:
    """
    Class for making your own 3D surfaces or faces of 3D shapes.

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
        offset = vec2(Options.window_size.x / 2, Options.window_size.y / 2)
        projections = []
        for vertex in self.vertices:
            if vertex.z >= Camera.pos.z:
                try:
                    projection = vec2(
                        fov * (vertex.x - Camera.pos.x) / (vertex.z - Camera.pos.z),
                        fov * (vertex.y - Camera.pos.y) / (vertex.z - Camera.pos.z)
                    ) + offset
                except ZeroDivisionError:
                    projection = vec2(
                        fov * (vertex.x - Camera.pos.x),
                        fov * (vertex.y - Camera.pos.y)
                    ) + offset
            
                projections.append(projection.x)
                projections.append(projection.y)

        return projections


    def render(self, outline=False):
        projections = self.get_projected_vertices()
        length = len(projections)

        if length > 4:
            if outline:
                pyglet.graphics.draw(
                    length // 2,
                    GL_LINES,
                    ('v2f', projections)
                )
            else:
                pyglet.graphics.draw(
                    length // 2,
                    GL_POLYGON,
                    ('v2f', projections)
                )
