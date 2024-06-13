import pygame
import sys
from maps import X, O, MAP_A


class Map():
    def __init__(self, size, game_map):
        self.width, self.height = size
        self.game_map = game_map
        self.map_width, self.map_height = len(game_map), len(game_map[0])
        self.cell_size = self.width / self.map_width
        self.start_x, self.start_y = (0, 0)
        
    def load_map(self, screen):
        for row in range(self.map_height):
            for column in range(self.map_width):
                if self.game_map[row][column] is X:
                    pygame.draw.rect(
                        surface=screen,
                        color=(60, 60, 60),
                        rect=(
                            self.start_x + column * self.cell_size,
                            self.start_y + row * self.cell_size,
                            self.cell_size,
                            self.cell_size
                        )
                    )


def main():
    SIZE = (900, 900)
    pygame.init()
    pygame.display.set_caption("Tower Defense")
    screen = pygame.display.set_mode(size=SIZE)

    screen.fill((170, 180, 170))

    map = Map(SIZE, MAP_A)
    map.load_map(screen)
    
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
