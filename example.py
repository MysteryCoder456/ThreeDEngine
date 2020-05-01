import sys
import pygame
from glm import vec3
from ThreeDEngine.options import Options
from ThreeDEngine.camera import Camera
from ThreeDEngine import draw

win = pygame.display.set_mode([int(x) for x in Options.window_size.to_tuple()])
pygame.display.set_caption("3D")
clock = pygame.time.Clock()

x = 500

while True:
    clock.tick(Options.fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x -= 2

    Camera.pos.x += 60 * clock.get_time() / 1000

    win.fill(Options.background_color)

    Options.stroke_width = 1
    Options.stroke_color = (255, 0, 0)
    draw.cube(win, vec3(-150 + -500, 250, 500), vec3(300, 500, 300), True)

    Options.stroke_color = (255, 255, 255)
    draw.cube(win, vec3(300, -180, 100), vec3(300, 300, 300))

    pygame.display.update()
