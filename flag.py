import pygame as pg
import toolkit

class Flag(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image, self.rect = toolkit.load_image('flag.png', -1)
        self.rect.center = x, y