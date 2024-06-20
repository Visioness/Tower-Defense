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
        damage=20,
        cooldown=2000,
        range = 250,
    )
    tower_group.add(tower)


def spawn_enemy(enemy_group, enemy_image, waypoints, health, speed):
    enemy = Enemy(
        image=enemy_image, 
        waypoints=waypoints, 
        health=health, 
        speed=speed,
    )
    enemy_group.add(enemy)


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

    spawn_enemy(enemy_group, enemy_image, waypoints, 200, 0.12)
    spawn_enemy(enemy_group, enemy_image, waypoints, 200, 0.14)
    spawn_enemy(enemy_group, enemy_image, waypoints, 200, 0.16)
    spawn_enemy(enemy_group, enemy_image, waypoints, 200, 0.18)
    spawn_enemy(enemy_group, enemy_image, waypoints, 200, 0.20)
    spawn_enemy(enemy_group, enemy_image, waypoints, 200, 0.22)
    spawn_enemy(enemy_group, enemy_image, waypoints, 200, 0.24)
    
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
        enemy_group.update(screen)
        enemy_group.draw(screen)
        
        for enemy in enemy_group:
            tower_group.update(enemy)
        tower_group.draw(screen)

        
        # Updates the screen with the finished drawings
        pygame.display.flip()


if __name__ == "__main__":
    main()
