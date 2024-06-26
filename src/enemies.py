import pygame
from pygame.math import Vector2
import math
import random


def draw_health_bar(surf, pos, size, borderC, backC, healthC, progress):
    """
    Draws health bar with the given parameters.
    """
    pygame.draw.rect(surf, backC, (*pos, *size))
    pygame.draw.rect(surf, borderC, (*pos, *size), 1)
    innerPos = (pos[0] + 1, pos[1] + 1)
    outerPos = ((size[0] - 2) * progress, size[1] - 2)
    rect = (round(innerPos[0]), round(innerPos[1])), (round(outerPos[0]), round(outerPos[1]))
    pygame.draw.rect(surf, healthC, rect)


class Enemy(pygame.sprite.Sprite):
    """
    Enemy class to represent enemies as a pygame Sprite on the screen.
    """

    levels = [
        # Level 1
        {
            "weak": 6,
            "medium": 0,
            "strong": 0,
        },
        
        # Level 2
        {
            "weak": 8,
            "medium": 2,
            "strong": 0,
        },

        # Level 3
        {
            "weak": 6,
            "medium": 4,
            "strong": 0,
        },

        # Level 4
        {
            "weak": 7,
            "medium": 5,
            "strong": 2,
        },

        # Level 4
        {
            "weak": 5,
            "medium": 4,
            "strong": 5,
        },

        # Level 5
        {
            "weak": 4,
            "medium": 6,
            "strong": 6,
        },
    ]

    enemy_types = {
        "weak": (120, 0.24, 1.5),
        "medium": (280, 0.36, 2.5),
        "strong": (600, 0.28, 4.5),
    }

    def __init__(self, image, waypoints, health, speed, reward):
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
        self.reward = reward

    @classmethod
    def create_enemy_list(cls, level):
        """
        Creates enemy list to spawn depending on the level.
        """

        enemy_list = []
        for enemy_type, enemy_count in cls.levels[level - 1].items():
            for i in range(enemy_count):
                enemy_list.append(enemy_type)
        # Shuffles enemy list
        random.shuffle(enemy_list)
        return enemy_list

    def update(self, surface):
        self.draw_health(surface)
        self.move()
        self.rotate()

    def move(self):
        """
        Moves the enemy.
        """

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
        """
        Rotates enemy image depending on the facing direction.
        """

        distance = self.target_pos - self.pos
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def draw_health(self, surf):
        """
        Draws health of the enemy above.
        """

        health_rect = pygame.Rect(0, 0, self.original_image.get_width(), 7)
        health_rect.midbottom = self.rect.centerx, self.rect.top
        draw_health_bar(surf, health_rect.topleft, health_rect.size, (0, 0, 0), (255, 0, 0), (0, 255, 0), self.health / self.max_health)