import pygame
pygame.init()


# Grid class
class Grid:
    def drawGrid(screen, width, height):
        tileSize = 32
        for x in range(0, width * tileSize, tileSize):
            for y in range(0, height * tileSize, tileSize):
                rect = pygame.Rect(x, y, tileSize, tileSize)
                pygame.draw.rect(screen, "grey", rect, 1)