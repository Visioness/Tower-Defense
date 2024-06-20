import pygame
from pygame.math import Vector2
import math


def draw_health_bar(surf, pos, size, borderC, backC, healthC, progress):
    pygame.draw.rect(surf, backC, (*pos, *size))
    pygame.draw.rect(surf, borderC, (*pos, *size), 1)
    innerPos = (pos[0] + 1, pos[1] + 1)
    outerPos = ((size[0] - 2) * progress, size[1] - 2)
    rect = (round(innerPos[0]), round(innerPos[1])), (round(outerPos[0]), round(outerPos[1]))
    pygame.draw.rect(surf, healthC, rect)


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

        self.max_health = health
        self.health = health
        self.speed = speed

    def update(self, surface):
        self.draw_health(surface)
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

    def draw_health(self, surf):
        health_rect = pygame.Rect(0, 0, self.original_image.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        draw_health_bar(surf, health_rect.topleft, health_rect.size, (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / self.max_health)