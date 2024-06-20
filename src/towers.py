import pygame
from pygame.math import Vector2
import math


class Tower(pygame.sprite.Sprite):

    def __init__(self, image, pos, damage, cooldown, range):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 0
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.damage = damage
        self.cooldown = cooldown
        self.range = range
        self.last_shot = 0

    def update(self, enemy):
        """
            Updates the tower angle and shoots the enemy if the enemy is in range.
        """

        distance = self.in_range(enemy)
        if distance is not False:
            self.rotate(distance)
        
            if pygame.time.get_ticks() - self.last_shot >= self.cooldown:
                self.fire(enemy)
                self.last_shot = pygame.time.get_ticks()
        
    def in_range(self, enemy):
        distance = (Vector2(enemy.pos) - Vector2(self.pos))
        return distance if distance.length() <= self.range else False

    def rotate(self, distance):
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def fire(self, enemy):
        print("boom")
        # TODO:
        # Animate bullet tracking
        
        enemy.health -= self.damage
        
        if enemy.health <= 0:
            enemy.kill()
