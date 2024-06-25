import pygame
from pygame.math import Vector2
import math


class Tower(pygame.sprite.Sprite):

    def __init__(self, image, pos, damage, cooldown, range, price):
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
        self.price = price

        self.last_shot = 0
        self.selected_enemy = None

    def update(self, enemy_group, budget):
        """
            Updates the tower angle and shoots the enemy if the enemy is in range.
        """
        if self.selected_enemy is None or self.in_range() is False:
            self.select_enemy(enemy_group)
        
        if self.selected_enemy is not None:
            distance = self.in_range()
            if distance is not False:
                self.rotate(distance)
            
                if pygame.time.get_ticks() - self.last_shot >= self.cooldown:
                    self.fire(budget)
                    self.last_shot = pygame.time.get_ticks()
        
    def select_enemy(self, enemy_group):
        for each in enemy_group:
            self.selected_enemy = each
            if self.in_range():
                return
        self.selected_enemy = None

    def in_range(self):
        distance = (Vector2(self.selected_enemy.pos) - Vector2(self.pos))
        return distance if distance.length() <= self.range else False

    def rotate(self, distance):
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def fire(self, budget):
        # TODO:
        # Animate bullet tracking
        
        if self.in_range():
            self.selected_enemy.health -= self.damage
        
            if self.selected_enemy.health <= 0:
                budget.add_coins(self.selected_enemy.reward)
                
                self.selected_enemy.kill()
                self.selected_enemy = None
                
