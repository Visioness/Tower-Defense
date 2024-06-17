import pygame


class Tower(pygame.sprite.Sprite):

    def __init__(self, image, pos, damage, firerate):
        pygame.sprite.Sprite.__init__(self)
        self.angle = 0
        self.original_image = image
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    