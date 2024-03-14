import pygame
import os
from settings import *

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(IMG_FOLDER, "mage.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.all_sprites = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.game = game
        self.x = x
        self.y = y
        self.selected = False

    def movement_radius(self):
        valid_positions = []
        if self.selected:
            for dx in range(-5, 6):
                for dy in range(-5, 6):
                    # calculate grid position
                    grid_x = self.x + dx
                    grid_y = self.y + dy
                    # check if grid position is within the screen and within the diamond-shaped radius
                    if (0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT and abs(dx) + abs(dy) <= 5):
                        valid_positions.append((grid_x, grid_y))
                        # calculate pixel position
                        pixel_x = grid_x * TILESIZE
                        pixel_y = grid_y * TILESIZE
                        # create a new surface with alpha channel
                        s = pygame.Surface((TILESIZE, TILESIZE), pygame.SRCALPHA)
                        # draw a semi-transparent square on the surface
                        s.fill((0, 255, 0, 128))  # RGBA
                        # blit the surface onto the screen
                        self.game.screen.blit(s, (pixel_x, pixel_y))
        return valid_positions
        
    def move_to(self, x, y):
        self.x = x
        self.y = y
        

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.selected = True
            elif self.selected:
                grid_x = mouse_pos[0] // TILESIZE
                grid_y = mouse_pos[1] // TILESIZE
                self.move_to(grid_x, grid_y)
                self.selected = False
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE