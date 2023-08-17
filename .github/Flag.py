import sys

import pygame
import math
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((700, 700))
preto = (0, 0, 0)
branco = (255, 255, 255)


def draw_star(DISPLAYSURF, posição, tamanho):
    x, y = posição
    outer_radius = tamanho
    inner_radius = tamanho // 2

    pontos = []
    for i in range(5):
        angle_rad = math.radians(72 * i + 18)
        x_outer = x + outer_radius * math.cos(angle_rad)
        y_outer = y - outer_radius * math.sin(angle_rad)
        pontos.append((x_outer, y_outer))

        angle_rad = math.radians(72 * i + 54)
        x_inner = x + inner_radius * math.cos(angle_rad)
        y_inner = y - inner_radius * math.sin(angle_rad)
        pontos.append((x_inner, y_inner))

    pygame.draw.polygon(DISPLAYSURF, branco, pontos, 5)

 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    DISPLAYSURF.fill(preto)
    draw_star(DISPLAYSURF, (200, 200), 100)
    pygame.display.flip()

pygame.quit()