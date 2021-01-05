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

    vehicleX = TILE_SIZE
    vehicleY = numOfYTiles / 2 * TILE_SIZE

    mapGenerator = MapGenerator(TILE_SIZE, numOfXTiles, numOfYTiles)
    roadTiles, landTiles = mapGenerator.generateMap()
    vehicle = Vehicle(vehicleX, vehicleY)

    mapSprites = pg.sprite.RenderPlain((roadTiles, landTiles))
    vehicleSprite = pg.sprite.RenderPlain((vehicle))

    gameIsRunning = True
    while(gameIsRunning):
        clock.tick(FRAMES_PER_SECOND)

        for event in pg.event.get():
            if(event.type == pg.QUIT):
                gameIsRunning = False
            elif(event.type == pg.KEYDOWN):
                if(event.key == pg.K_w):
                    vehicle.accelerationStatus = 'accelerate'
                elif(event.key == pg.K_s):
                    vehicle.accelerationStatus = 'reverse'
                elif (event.key == pg.K_d):
                    vehicle.turningStatus = 'right'
                elif (event.key == pg.K_a):
                    vehicle.turningStatus = 'left'
            elif(event.type == pg.KEYUP):
                if (event.key == pg.K_w):
                    vehicle.accelerationStatus = 'decelerate'
                elif (event.key == pg.K_s):
                    vehicle.accelerationStatus = 'decelerate'
                elif (event.key == pg.K_d):
                    vehicle.turningStatus = 'straight'
                elif (event.key == pg.K_a):
                    vehicle.turningStatus = 'straight'

        vehicleSprite.update()

        mapSprites.draw(screen)
        vehicleSprite.draw(screen)

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