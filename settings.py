import os
import pygame

pygame.init()
pygame.font.init()


# Defines constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
TILESIZE = 32
GRID_WIDTH = SCREEN_WIDTH / TILESIZE
GRID_HEIGHT = SCREEN_HEIGHT / TILESIZE
GAME_FOLDER = os.path.dirname(__file__)
IMG_FOLDER = os.path.join(GAME_FOLDER, "img")
MENU_FONT = pygame.font.Font("8-BIT WONDER.TTF", 50)