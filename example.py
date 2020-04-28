import sys
import pygame
from glm import vec3
from ThreeDEngine import options as opt, draw


win = pygame.display.set_mode([int(x) for x in opt.window_size.to_tuple()])
pygame.display.set_caption("3D")

x = 400

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x -= 2

    win.fill(opt.background_color)

    draw.cube(win, vec3(x, -150, 100), vec3(300, 300, 300), True)

    pygame.display.update()
