import pygame as pg

LAND_RED = 2
LAND_GREEN = 79
LAND_BLUE = 22

LAND_COLOR = (LAND_RED, LAND_GREEN, LAND_BLUE)

class LandTile(pg.sprite.Sprite):
    def __init__(self, x ,y, size):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill((LAND_COLOR))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self, *args, **kwargs):
        pass