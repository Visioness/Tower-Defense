import pygame
import sys
from maps import Map
from enemies import Enemy
from towers import Tower


def create_tower(tower_group, tower_image):
    mouse_pos = pygame.mouse.get_pos()
    tower = Tower(
        image=tower_image,
        pos=mouse_pos,
        damage=100,
        firerate=0.5
    )
    tower_group.add(tower)

def main():

    SIZE = (900, 900)
    
    pygame.init()
    pygame.display.set_caption("Tower Defense")
    screen = pygame.display.set_mode(size=SIZE)

    map = Map(SIZE, Map.MAP_A)
    waypoints = map.get_waypoints()

    
    pygame.display.flip()

    # Enemy
    enemy_image = pygame.image.load("../assets/enemy-01.png").convert_alpha()
    enemy_group = pygame.sprite.Group()

    enemy = Enemy(
        image=enemy_image, 
        waypoints=waypoints, 
        health=200, 
        speed=1
    )
    enemy_group.add(enemy)


    # tower
    tower_image = pygame.image.load("../assets/tower-02.png").convert_alpha()
    tower_group = pygame.sprite.Group()

    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                create_tower(tower_group, tower_image)                

        map.draw_map(screen)
        map.draw_bases(screen)
        enemy_group.update()
        enemy_group.draw(screen)
        tower_group.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
