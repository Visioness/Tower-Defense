import pygame
import sys
from maps import Map
from enemies import Enemy


def main():

    SIZE = (900, 900)
    
    pygame.init()
    pygame.display.set_caption("Tower Defense")
    screen = pygame.display.set_mode(size=SIZE)

    screen.fill((170, 180, 170))

    map = Map(SIZE, Map.MAP_A)
    map.load_map(screen)

    enemy_image = pygame.image.load("../assets/enemy-01.png").convert_alpha()
    enemy_group = pygame.sprite.Group()

    enemy = Enemy(200, enemy_image, (200, 300))
    enemy_group.add(enemy)


    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #enemy_group.update()
        enemy_group.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
