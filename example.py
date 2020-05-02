from random import randint
from glm import vec3

from ThreeDEngine.app import App
from ThreeDEngine.options import Options
from ThreeDEngine.camera import Camera
from ThreeDEngine import draw


class Example(App):
    def __init__(self, *args, **kwargs):
        self.color = [randint(50, 255) for i in range(3)]
        # Declare your variables before super().__init__() is called
        
        super().__init__(*args, **kwargs)

    def update(self, dt):
        Camera.pos.x += 100 * dt

    def render(self):
        Options.stroke_width = 5
        draw.cube(vec3(-500, 550, 400), vec3(300, 500, 300), self.color, True)

        draw.cube(vec3(400, -380, 150), vec3(300, 300, 300), self.color)


if __name__ == "__main__":
    window = Example(*Options.window_size.to_tuple(), "3D iz kewl!")
