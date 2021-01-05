import pygame as pg
from mapGenerator import MapGenerator
from vehicle import Vehicle

FRAMES_PER_SECOND = 30
TILE_SIZE = 20

SCREEN_WIDTH_APPROX = 800
SCREEN_HEIGHT_APPROX = 600

def main():
    pg.init()
    numOfXTiles, numOfYTiles, screen = initializeScreen()
    clock = pg.time.Clock()

    mapGenerator = MapGenerator(TILE_SIZE, numOfXTiles, numOfYTiles)
    roadTiles, landTiles = mapGenerator.generateMap()
    vehicle = Vehicle()

    sprites = pg.sprite.RenderPlain((roadTiles, landTiles, vehicle))

    gameIsRunning = True
    while(gameIsRunning):
        clock.tick(FRAMES_PER_SECOND)

        for event in pg.event.get():
            if(event.type == pg.QUIT):
                gameIsRunning = False

        sprites.draw(screen)

        pg.display.flip()


def initializeScreen():
    numOfXTiles = int(SCREEN_WIDTH_APPROX / TILE_SIZE)
    numOfYTiles = int(SCREEN_HEIGHT_APPROX / TILE_SIZE)
    screenWidth = TILE_SIZE * numOfXTiles
    screenHeight = TILE_SIZE * numOfYTiles
    screen = pg.display.set_mode((screenWidth, screenHeight))
    return numOfXTiles, numOfYTiles, screen


if __name__ == '__main__':
    main()