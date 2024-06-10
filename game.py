import pygame
import sys


pygame.init()

pygame.display.set_caption("Tower Defense")
pygame.display.set_mode(size=(900, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()