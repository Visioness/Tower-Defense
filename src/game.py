import pygame
from pygame.math import Vector2
import sys
from maps import Map
from enemies import Enemy
from towers import Tower


def create_tower(tower_group, tower_image, pos):
    """
    Creates tower at the given position.
    """
    tower = Tower(
        image=tower_image,
        pos=pos,
        damage=100,
        firerate=0.5,
        range = 150,
    )
    tower_group.add(tower)

def main():
    # Screen Size
    SIZE = (900, 900)
    
    # Pygame initialization
    pygame.init()
    pygame.display.set_caption("Tower Defense")
    screen = pygame.display.set_mode(size=SIZE)

    # Loads map and gets the waypoints for enemy path
    map = Map(SIZE, Map.MAP_A)
    waypoints = map.get_waypoints()

    # Enemy Group
    enemy_image = pygame.image.load("../assets/enemy-01.png").convert_alpha()
    enemy_group = pygame.sprite.Group()

    # Tower Group
    tower_image = pygame.image.load("../assets/tower-02.png").convert_alpha()
    tower_group = pygame.sprite.Group()

    enemy = Enemy(
        image=enemy_image, 
        waypoints=waypoints, 
        health=200, 
        speed=0.15
    )
    enemy_group.add(enemy)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                for base in map.tower_pos:
                    distance = (Vector2(base) - Vector2(mouse_pos)).length()
                    if distance < 17:
                        create_tower(tower_group, tower_image, (base[0], base[1] - 6))                

        # Draws map
        map.draw_map(screen)
        # Draws tower bases where user can places towers
        map.draw_bases(screen)

        # Draws and updates enemy and tower groups
        enemy_group.update()
        enemy_group.draw(screen)
        
        tower_group.update(enemy)
        tower_group.draw(screen)

        
        # Updates the screen with the finished drawings
        pygame.display.flip()


if __name__ == "__main__":
    main()
