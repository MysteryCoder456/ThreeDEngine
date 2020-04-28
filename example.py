import sys
import pygame
from glm import vec3
from ThreeDEngine.options import Options
from ThreeDEngine import draw


win = pygame.display.set_mode([int(x) for x in Options.window_size.to_tuple()])
pygame.display.set_caption("3D")

x = 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x -= 2

    win.fill(Options.background_color)

    Options.stroke_width = 7
    Options.stroke_color = (255, 0, 0)
    draw.cube(win, vec3(-1000, -700, 300), vec3(300, 300, 300), True)

    Options.stroke_color = (255, 255, 255)
    draw.cube(win, vec3(x, -150, 100), vec3(300, 300, 300), True)

    pygame.display.update()
