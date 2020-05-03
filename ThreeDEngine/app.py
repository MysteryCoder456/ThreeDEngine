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
        pyglet.app.run()
        glClearColor(*Options.background_color)

    def schedule_callback(self, dt):
        self.update(dt)
        self.clear()
        glLineWidth(Options.stroke_width)
        self.render()