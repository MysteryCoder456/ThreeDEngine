import sys
import pyglet
from glm import vec3
from ThreeDEngine.options import Options
from ThreeDEngine.camera import Camera
from ThreeDEngine import draw


class App(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_draw(self):
        # Camera.pos.x += 3

        Options.stroke_width = 1
        Options.stroke_color = (255, 0, 0)
        draw.cube(vec3(-150 + -500, 250, 500), vec3(300, 500, 300), True)

        Options.stroke_color = (255, 255, 255)
        draw.cube(vec3(300, -180, 100), vec3(300, 300, 300))


if __name__ == "__main__":
    window = App(*Options.window_size.to_tuple(), "3D iz kewl!")
    pyglet.app.run()
