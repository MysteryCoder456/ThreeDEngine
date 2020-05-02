import pyglet
from pyglet.gl import *
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
            if vertex.z >= Camera.pos.z + Options.render_dist[0] and vertex.z <= Camera.pos.z + Options.render_dist[1]:
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


    def render(self, color, outline):
        projections = self.get_projected_vertices()
        length = len(projections)
        c = []

        for i in range(length // 2):
            c.extend(color)
        
        vertex_list = pyglet.graphics.vertex_list(
            length // 2,
            ("v2f", projections),
            ("c3B", c)
        )

        if outline:
            glLineWidth(Options.stroke_width)
            vertex_list.draw(GL_LINE_LOOP)
        else:
            vertex_list.draw(GL_POLYGON)
