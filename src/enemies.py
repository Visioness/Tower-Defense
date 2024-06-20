import pygame
from pygame.math import Vector2
import math


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, waypoints, health, speed):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 0
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target = 1

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.health = health
        self.speed = speed

    def update(self):
        self.move()
        self.rotate()

    def move(self):
        if self.target < len(self.waypoints):
            self.target_pos = Vector2(self.waypoints[self.target])
            self.movement = self.target_pos - self.pos
        else:
            self.kill()

        distance = self.movement.length()

        if distance >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if distance != 0:
                self.pos += self.movement.normalize() * distance
            
            self.target += 1

    def rotate(self):
        distance = self.target_pos - self.pos
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos