# Imports libraries
import pygame
import sys
import random
import os

# Defines constants
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 50

# Initializes Pygame and creates window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


# Grid class
class Grid():
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(screen, ("white"), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(screen, ("white"), (0, y), (WIDTH, y))


# Creates player sprite class
# All sprites need to define init and update methods, and have an image and rect attribute
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "mage.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.dragging = False

    def update(self):
        if self.dragging:
            mouse_pos = pygame.mouse.get_pos()
            grid_x = round(mouse_pos[0] / TILESIZE) * TILESIZE
            grid_y = round(mouse_pos[1] / TILESIZE) * TILESIZE
            self.rect.topleft = (grid_x, grid_y)


# Adds player sprite to all_sprites group
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:

    # Gets mouse position, sets FPS
    pygame.mouse.get_pos()
    clock.tick(FPS)

    # Processes input (events)
    for event in pygame.event.get():

        # If X button is clicked, game loop stops running
        if event.type == pygame.QUIT:
            running = False

        # Allows player sprite to be dragged around screen with mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if player.rect.collidepoint(event.pos):
                player.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            player.dragging = False

    # Updates game state
    all_sprites.update()

    # Draws new game state
    screen.fill(("black"))
    all_sprites.draw(screen)
    Grid.draw(screen)

    # After drawing, flips display
    pygame.display.flip()

# If game loop stops running, closes game window
pygame.quit()
sys.exit()