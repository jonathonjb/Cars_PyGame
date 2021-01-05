import os
import pygame as pg
from pygame.compat import geterror

# functions to create our resources
def load_image(name, colorkey=None):
    try:
        image = pg.image.load(name)
    except pg.error:
        print("Cannot load image:", name)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()