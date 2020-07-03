import pyglet
from pyglet.gl import *

from ThreeDEngine.options import Options
from ThreeDEngine.camera import Camera


class App(pyglet.window.Window):
    """
    The base class for all games and apps with the ThreeDEngine
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pyglet.clock.schedule_interval(self.schedule_callback, 1/Options.fps)
        glClearColor(*Options.background_color)
        pyglet.app.run()

    def schedule_callback(self, dt):
        self.update(dt)
        glClear(GL_COLOR_BUFFER_BIT)
        glLineWidth(Options.stroke_width)
        self.render()
