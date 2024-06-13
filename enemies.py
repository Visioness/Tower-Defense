import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, health, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.health = health

    def update(self):
        self.move()

    def move(self):
        self.rect.x += 1
