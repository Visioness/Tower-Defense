import pygame
from pygame.math import Vector2
import sys
from maps import Map
from buttons import Button
from enemies import Enemy
from towers import Tower
import random


def create_tower(tower_image, pos):
    """
    Creates tower at the given position.
    """
    tower = Tower(
        image=tower_image,
        pos=pos,
        damage=70,
        cooldown=2000,
        range = 150,
    )
    return tower


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
    level = 1
    ready_to_spawn = True
    game_over = False
    
    # Pygame initialization
    pygame.init()
    pygame.display.set_caption("Tower Defense")
    screen = pygame.display.set_mode(size=(900, 900))

    # Loads map and gets the waypoints for enemy path
    map = Map(SIZE, Map.MAP_A)
    waypoints = map.get_waypoints()

    # Enemy Group
    enemy_list = []
    last_enemy_spawn = pygame.time.get_ticks()
    spawn_cooldown = 2000

    enemy_image = pygame.image.load("../assets/enemy-01.png").convert_alpha()
    enemy_group = pygame.sprite.Group()
    
    # Tower Group
    tower_image = pygame.image.load("../assets/tower-02.png").convert_alpha()
    tower_group = pygame.sprite.Group()

    # Buttons
    buttons_image = pygame.image.load("../assets/buttons.png").convert_alpha()
    
    button_width = buttons_image.get_width() // 3
    button_height = buttons_image.get_height()

    build_button_rect = pygame.Rect(0, 0, button_width, button_height)
    upgrade_button_rect = pygame.Rect(button_width, 0, button_width, button_height)
    sell_button_rect = pygame.Rect(button_width * 2, 0, button_width, button_height)

    buttons = []
    base_selected = False
    selected_base_pos = None
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                # If any base clicked
                if base_selected:
                    # Buttons for the selected base
                    button_image_pos = (selected_base_pos[0], selected_base_pos[1])
                    
                    # Build Button
                    # Builds the tower on the clicked base
                    if build_button.draw(screen):
                        print("Build button clicked")
                        tower_pos = (base[0], base[1])
                        
                        # If there's no towers on the base
                        if tower_pos not in [each[0] for each in map.placed_towers]:
                            tower = create_tower(tower_image, tower_pos)
                            tower_group.add(tower)
                            map.placed_towers.append([tower_pos, tower]) 
                        
                        else:
                            print("There is already a Tower!")
                    
                    # Upgrade Button
                    # Upgrades the tower
                    elif upgrade_button.draw(screen):
                        print("Upgrade button clicked")
                        # Handle upgrade action here
                    
                    # Sell Button
                    # Sells the tower on the clicked base
                    elif sell_button.draw(screen):
                        print("Sell button clicked")
                        tower_pos_list = [each[0] for each in map.placed_towers]

                        # If there's a tower on the base
                        if (base[0], base[1]) in tower_pos_list:
                            index = tower_pos_list.index((base[0], base[1]))
                            
                            tower_to_kill = map.placed_towers.pop(index)[1]
                            tower_to_kill.kill()

                    # Sets variables to default values
                    base_selected = False
                    selected_base_pos = None
                    buttons = []

                else:
                    # Creates Button objects for the clicked base
                    for base in map.base_pos:
                        distance = (Vector2(base) - Vector2(mouse_pos)).length()
                        if distance < 17:
                            base_selected = True
                            selected_base_pos = base
                            button_image_pos = (base[0] - 56, base[1] + 30)
                            
                            build_button = Button(button_image_pos[0], button_image_pos[1], buttons_image, build_button_rect)
                            upgrade_button = Button(button_image_pos[0] + button_width, button_image_pos[1], buttons_image, upgrade_button_rect)
                            sell_button = Button(button_image_pos[0] + 2 * button_width, button_image_pos[1], buttons_image, sell_button_rect)
                            
                            buttons = [build_button, upgrade_button, sell_button]
                            break


        # Draws map
        map.draw_map(screen)
        # Draws tower bases where user can places towers
        map.draw_bases(screen)

        # If not leveled up
        if ready_to_spawn:
            # Creates enemy list to spawn
            if not enemy_list:          
                for enemy_type, enemy_count in Enemy.levels[level - 1].items():
                    for i in range(enemy_count):
                        enemy_list.append(enemy_type)
                # Shuffles enemy list
                random.shuffle(enemy_list)
            
            # Enemy spawn mechanism
            if pygame.time.get_ticks() - last_enemy_spawn > spawn_cooldown:
                # If any remaining enemy to spawn
                if enemy_list:
                    enemy = enemy_list.pop()
                    spawn_enemy(enemy_group, enemy_image, waypoints, Enemy.enemy_types[enemy][0], Enemy.enemy_types[enemy][1])
                    last_enemy_spawn = pygame.time.get_ticks()

                # If all enemies spawned in the list
                if not enemy_list:
                    ready_to_spawn = False


        # Enemy and Tower drawings
        enemy_group.draw(screen)
        tower_group.draw(screen)
        
        # Enemy and Tower updates
        enemy_group.update(screen)
        tower_group.update(enemy_group)
        
        # Leveling up mechanism
        if len(enemy_group) == 0 and ready_to_spawn == False and not enemy_list:
            # Checks if all levels are passed
            if level + 1 > len(Enemy.levels):
                print("All levels completed")
                game_over = True
                break
            
            print("Level up")
            level += 1
            ready_to_spawn = True

        # If any base selected draws buttons
        if base_selected:
            for button in buttons:
                button.draw(screen)

        # Updates the screen with the finished drawings
        pygame.display.flip()


if __name__ == "__main__":
    main()
