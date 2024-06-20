import pygame
from pygame.math import Vector2
import math


class Tower(pygame.sprite.Sprite):

    def __init__(self, image, pos, damage, firerate, range):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 0
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.damage = damage
        self.firerate = firerate
        self.range = range
    

    def update(self, enemy):
        """
            Updates the tower angle if the enemy is in range.
        """
        distance = self.in_range(enemy)
        if distance is not False:
            self.rotate(distance)

        
    def in_range(self, enemy):
        distance = (Vector2(enemy.pos) - Vector2(self.pos))
        return distance if distance.length() <= self.range else False

    def rotate(self, distance):
        x, y = distance
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def fire(self, enemy):
        pass

    