import pygame


class Map():
    X = "X"
    O = " "

    MAP_A = [
        [X, X, X, X, X, X, O, X, X, X, X, X, X, X, X, X, X, X, X, X],
        [X, X, X, X, X, X, O, X, X, X, X, X, X, X, X, X, X, X, X, X],
        [X, X, X, X, X, X, O, O, O, X, X, X, X, X, X, X, X, X, X, X],
        [X, X, X, X, X, X, X, X, O, X, X, X, X, X, X, X, X, X, X, X],
        [X, X, X, X, X, X, X, X, O, X, X, X, O, O, O, X, X, X, X, X],
        [X, X, X, X, X, X, X, X, O, X, X, X, O, X, O, X, X, X, X, X],
        [X, X, X, X, O, O, O, O, O, X, X, X, O, X, O, O, X, X, X, X],
        [X, X, X, X, O, X, X, X, X, X, X, X, O, X, X, O, X, X, X, X],
        [X, X, X, X, O, X, X, X, X, X, X, X, O, X, X, O, X, X, X, X],
        [X, O, O, O, O, X, X, X, X, O, O, O, O, X, X, O, O, X, X, X],
        [X, O, X, X, X, X, X, X, X, O, X, X, X, X, X, X, O, X, X, X],
        [X, O, X, X, X, X, X, X, X, O, X, X, X, X, X, X, O, X, X, X],
        [X, O, X, O, O, O, X, X, X, O, X, X, X, X, X, X, O, X, X, X],
        [X, O, O, O, X, O, X, X, X, O, X, X, X, X, X, X, O, X, X, X],
        [X, X, X, X, X, O, X, X, X, O, X, X, X, O, O, O, O, X, X, X],
        [X, X, X, X, X, O, X, X, X, O, X, X, X, O, X, X, X, X, X, X],
        [X, X, X, X, X, O, O, O, O, O, X, X, X, O, X, X, X, X, X, X],
        [X, X, X, X, X, X, X, X, X, X, X, X, X, O, O, O, O, O, X, X],
        [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O, X, X],
        [X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, X, O, X, X],
    ]

    def __init__(self, size, game_map):
        self.width, self.height = size
        self.game_map = game_map
        self.map_width, self.map_height = len(game_map), len(game_map[0])
        self.cell_size = self.width / self.map_width
        self.start_x, self.start_y = (0, 0)

    def load_map(self, screen):
        for row in range(self.map_height):
            for column in range(self.map_width):
                if self.game_map[row][column] is Map.X:
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