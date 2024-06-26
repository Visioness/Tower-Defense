import pygame

class Button():
    """
    Button class to represent buttons on the screen.
    """

    def __init__(self, x, y, image, sub_rect):
        self.image = image
        self.sub_rect = sub_rect
        self.rect = pygame.Rect(x, y, sub_rect.width, sub_rect.height)

    def draw(self, surface):
        """
        Draws the buttons on the given surface.
        """

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True

        surface.blit(self.image, self.rect, self.sub_rect)
        return False