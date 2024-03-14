import pygame
from settings import *
from player import *
import os
import random

# ____ Quick Notes ____
# Load images with: pygame.image.load(os.path.join(img_folder, "<name.png>"))

# Game loop
class Game:
    def __init__(self):
        # Initialize game
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Necromancer")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self, 10, 10)
        self.all_sprites.add(self.player)

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(self.screen, "grey", (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, "grey", (0, y), (SCREEN_WIDTH, y))

    def running(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - Events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            # check for mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                grid_x = mouse_pos[0] // TILESIZE
                grid_y = mouse_pos[1] // TILESIZE
                # if the player is clicked, select it and calculate valid positions
                if self.player.rect.collidepoint(mouse_pos):
                    self.player.selected = True
                    self.valid_positions = self.player.movement_radius()
                    if self.player.selected:
                        if (grid_x, grid_y) in self.valid_positions:
                            self.player.move_to(grid_x, grid_y)
                    self.player.selected = False

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        self.player.movement_radius()
        pygame.display.flip()

game = Game()
game.running()
