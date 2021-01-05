import pygame as pg
import toolkit

class Vehicle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image, self.rect = toolkit.load_image('car.png', -1)

    def update(self):
        pass