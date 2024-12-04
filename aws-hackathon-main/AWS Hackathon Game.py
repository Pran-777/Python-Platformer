import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

from tutorial import PLAYER_VEL

pygame.init()
pygame.display.set_caption("Platformer")

BG_COLOR = (0, 255, 255)
WIDTH, HEIGHT = 800, 600
FPS = 144

PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.QUIT()
    quit()


window.fill(BG_COLOR)
pygame.display.update()

if __name__ == "__main__":
    main(window)