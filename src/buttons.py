import pygame

class Button():
    def __init__(self, x, y, image, sub_rect):
        self.image = image
        self.sub_rect = sub_rect
        self.rect = pygame.Rect(x, y, sub_rect.width, sub_rect.height)

    def draw(self, surface):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True  # Indicates button click

        surface.blit(self.image, self.rect, self.sub_rect)
        return False  # No click