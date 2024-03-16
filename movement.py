import pygame
from settings import *

# Movement class for all playable units
class Movement:
    def __init__(self, unit, x: int, y: int):
        self.unit = unit
        self.x = x
        self.y = y
        self.selected = False

    def selected(self) -> bool:
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if self.unit.rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                return True
            
    def calculate_movement_radius(self) -> list:
        self.valid_positions: list = []
        for dx in range(-5, 6):
            for dy in range(-5, 6):
                grid_x = self.x + dx
                grid_y = self.y + dy
                if (0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT and abs(dx) + abs(dy) <= 5):
                    self.valid_positions.append((grid_x, grid_y))
                    return self.valid_positions
    
    def draw_movement_radius(self, screen):
        for pos in self.valid_positions:
            pixel_x = pos[0] * TILESIZE
            pixel_y = pos[1] * TILESIZE
            possible_moves = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
            possible_moves.fill((0, 255, 0, 128))
            screen.blit(possible_moves, (pixel_x, pixel_y))
    
    def move_to(self, x: int, y: int):
        if (x, y) in self.valid_positions:
            self.x = x
            self.y = y
            self.unit.rect.topleft = (x * TILESIZE, y * TILESIZE)
            self.selected = False

    def update(self):
        if self.selected == True:
            self.calculate_movement_radius()
            self.draw_movement_radius()
            self.move_to()
            self.selected = False