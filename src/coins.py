import pygame

class Budget():
    coins = 10
    
    @classmethod
    def update(cls, screen, image):
        cls.coins += 0.001
        cls.show_image(screen, image)
        cls.show_coins(screen)

    @classmethod
    def add_coins(cls, amount):
        cls.coins += amount
    
    @classmethod
    def remove_coins(cls, amount):
        cls.coins -= amount

    @classmethod
    def enough_coins(cls, price):
        return True if cls.coins >= price else False
    
    @classmethod
    def show_coins(cls, surface):
        text_font = pygame.font.Font("../assets/fonts/FiraCode-SemiBold.ttf", 24)
        text_surface = text_font.render(f" | {round(cls.coins, 1)}", False, (255, 255, 255))
        surface.blit(text_surface, (765, 45))

    @classmethod
    def show_image(cls, surface, image):
        image = image
        rect = image.get_rect()
        rect.center = (750, 50)
        surface.blit(image, rect.center)
