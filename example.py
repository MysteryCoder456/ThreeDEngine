import sys
from random import randint

import pyglet
from pyglet.gl import *
from glm import vec3

from ThreeDEngine.options import Options
from ThreeDEngine.camera import Camera
from ThreeDEngine import draw


class App(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = [randint(50, 255) for i in range(3)]

        pyglet.clock.schedule_interval(self.schedule_callback, 1/Options.fps)
        pyglet.app.run()
        glClearColor(*Options.background_color)

    def schedule_callback(self, dt):
        self.update(dt)
        self.clear()
        glLineWidth(Options.stroke_width)
        self.render()

    def update(self, dt):
        Camera.pos.x += 100 * dt

    def render(self):
        Options.stroke_width = 5
        draw.cube(vec3(-500, 550, 400), vec3(300, 500, 300), self.color, True)

        draw.cube(vec3(400, -380, 150), vec3(300, 300, 300), self.color)


if __name__ == "__main__":
    window = App(*Options.window_size.to_tuple(), "3D iz kewl!")
