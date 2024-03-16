import pygame
from settings import *
from player import *
from grid import Grid
import os
import random

# ____ Quick Notes ____
# Load images with: pygame.image.load(os.path.join(img_folder, "<name.png>"))

# Game loop
class Game:
    def __init__(self):
        # Initialize pygame/mixer/font, create screen, set caption, create clock
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Necromancer")
        self.clock = pygame.time.Clock()
        # Creates "all sprites" folder and places player sprite in it
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self, 10, 10)
        self.all_sprites.add(self.player)

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
            # check for closing windowmouse
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.update()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def draw(self):
        # Game Loop - Draw
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        Grid.draw_grid(self)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.running()