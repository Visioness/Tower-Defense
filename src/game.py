import pygame
import sys
from maps import Map
from enemies import Enemy


def main():

    SIZE = (900, 900)
    
    pygame.init()
    pygame.display.set_caption("Tower Defense")
    screen = pygame.display.set_mode(size=SIZE)

    map = Map(SIZE, Map.MAP_A)
    waypoints = map.get_waypoints()

    enemy_image = pygame.image.load("../assets/enemy-01.png").convert_alpha()
    enemy_group = pygame.sprite.Group()

    enemy = Enemy(
        image=enemy_image, 
        waypoints=waypoints, 
        health=200, 
        speed=1
    )
    enemy_group.add(enemy)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        map.draw_map(screen)
        enemy_group.update()
        enemy_group.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
