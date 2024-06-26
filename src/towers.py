import pygame
from pygame.math import Vector2
import math


class Tower(pygame.sprite.Sprite):
    """
    Tower class to represent towers as a pygame Sprite on the screen.
    """

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
        self.level = 1

        self.last_shot = 0
        self.selected_enemy = None

        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        
        pygame.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(30)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

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

    def upgrade_tower(self, tower_level):
        """
        Upgrades the tower.
        """

        self.damage += 0.4
        self.cooldown -= 10
        self.range += 30
        self.level = tower_level

        self.range_image = pygame.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        
        pygame.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(30)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center
        

    def show_range(self, surface):
        """
        Shows the range of the Tower.
        """

        surface.blit(self.range_image, self.range_rect)
        
    def select_enemy(self, enemy_group):
        """
        Selects the enemy to fire.
        """
        
        for each in enemy_group:
            self.selected_enemy = each
            if self.in_range():
                return
        self.selected_enemy = None

    def in_range(self):
        """
        Checks if enemy is in range.
        """

        distance = (Vector2(self.selected_enemy.pos) - Vector2(self.pos))
        return distance if distance.length() <= self.range else False

    def rotate(self, distance):
        """
        Rotates the image of the tower depending on the enemy movement.
        """

        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def fire(self, budget):
        """
        If enemy is in range, shoots at the enemy
        """
        
        if self.in_range():
            self.selected_enemy.health -= self.damage
        
            if self.selected_enemy.health <= 0:
                budget.add_coins(self.selected_enemy.reward)
                
                self.selected_enemy.kill()
                self.selected_enemy = None
