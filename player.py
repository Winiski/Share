import pygame
import os
from settings import *
from movement import Movement

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
        self.movement = Movement(self, x, y)


    def update(self):
        self.movement.update()