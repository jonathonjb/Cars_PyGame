import pygame as pg

ROAD_RED = 255
ROAD_GREEN = 156
ROAD_BLUE = 143

ROAD_COLOR = (ROAD_RED, ROAD_GREEN, ROAD_BLUE)

class RoadTile(pg.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pg.Surface((size, size))
        self.image.fill((ROAD_COLOR))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

    def update(self, *args, **kwargs):
        pass