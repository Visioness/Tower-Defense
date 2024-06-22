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

        self.path = [(0, 6), (2, 6), (2, 8), (6, 8), (6, 4), (9, 4), (9, 1),
                     (13, 1), (13, 3), (12, 3), (12, 5), (16, 5), (16, 9), (9, 9),
                     (9, 12), (4, 12), (4, 14), (6, 14), (6, 15), (9, 15), (9, 16),
                     (14, 16), (14, 13), (17, 13), (17, 17), (19, 17)]

        self.base_cells = [(3, 7), (7, 5), (8, 3), (13, 4), (15, 8), (5, 13)]
        self.base_pos = [[(cell[1] + 0.5) * self.cell_size , (cell[0] + 0.5) * self.cell_size] for cell in self.base_cells]

        self.placed_towers = []

    def draw_map(self, screen):
        for row in range(self.map_height):
            for column in range(self.map_width):
                if self.game_map[row][column] is Map.X:
                    cell_color = (80, 90, 80) 
                
                else:
                    cell_color = (170, 180, 170)
                
                pygame.draw.rect(
                    surface=screen,
                    color=cell_color,
                    rect=(
                        self.start_x + column * self.cell_size,
                        self.start_y + row * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )
                )

    def draw_bases(self, screen):
        base_image = pygame.image.load("../assets/tower-base.png").convert_alpha()
        bases = [[(cell[1] + 0.5) * self.cell_size , (cell[0] + 0.5) * self.cell_size] for cell in self.base_cells]
        for base in bases:
            rect = base_image.get_rect()
            rect.center = base
            screen.blit(base_image, rect)

    def get_waypoints(self):
        waypoints = [[(cell[1] + 0.5) * self.cell_size , (cell[0] + 0.5) * self.cell_size] for cell in self.path]
        waypoints[0][1] = waypoints[0][1] - 100
        return waypoints
    