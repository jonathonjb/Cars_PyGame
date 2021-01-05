import pygame as pg
from mapGenerator import MapGenerator
from vehicle import Vehicle

FRAMES_PER_SECOND = 30
MIN_TILE_SIZE = 13
MAX_TILE_SIZE = 30

SCREEN_WIDTH_APPROX = 800
SCREEN_HEIGHT_APPROX = 600

def main():
    pg.init()
    pg.font.init()
    scoreFont = pg.font.SysFont(None, 100)

    clock = pg.time.Clock()

    currTileSize = MAX_TILE_SIZE + 1
    score = -1
    lives = 5
    gameIsRunning = True

    while(gameIsRunning):
        score += 1
        if(currTileSize != MIN_TILE_SIZE):
            currTileSize -=1

        numOfXTiles, numOfYTiles, screen = initializeScreen(currTileSize)
        vehicleStartX = currTileSize
        vehicleStartY = numOfYTiles / 2 * currTileSize

        mapGenerator = MapGenerator(currTileSize, numOfXTiles, numOfYTiles)
        roadTiles, landTiles, flag = mapGenerator.generateMap()
        vehicle = Vehicle(vehicleStartX, vehicleStartY)

        mapSprites = pg.sprite.RenderPlain((roadTiles, landTiles))
        vehicleSprite = pg.sprite.RenderPlain((vehicle))
        flagSprite = pg.sprite.RenderPlain((flag))

        scoreText = scoreFont.render(str(score), False, (0, 0, 255))

        roundIsRunning = True
        while(gameIsRunning and roundIsRunning):
            clock.tick(FRAMES_PER_SECOND)

            gameIsRunning = eventListener(gameIsRunning, vehicle)

            vehicleSprite.update()

            mapSprites.draw(screen)
            flagSprite.draw(screen)
            vehicleSprite.draw(screen)
            screen.blit(scoreText, (10, 10))

            livesText = scoreFont.render(str(lives), False, (0, 0, 255))
            screen.blit(livesText, (730, 10))

            if (pg.sprite.spritecollide(vehicle, flagSprite, True)):
                roundIsRunning = False
                for sprite in mapSprites:
                    sprite.kill()
                for sprite in flagSprite:
                    sprite.kill()

            if(pg.sprite.spritecollide(vehicle, landTiles, False) or
                    vehicle.rect.left < 0 or vehicle.rect.right > SCREEN_WIDTH_APPROX or
                    vehicle.rect.top < 0 or vehicle.rect.bottom > SCREEN_HEIGHT_APPROX):
                lives -= 1
                if(lives <= 0):
                    gameIsRunning = False
                    roundIsRunning = False
                else:
                    vehicle.restart()

            pg.display.flip()


def eventListener(gameIsRunning, vehicle):
    for event in pg.event.get():
        if (event.type == pg.QUIT):
            gameIsRunning = False
        elif (event.type == pg.KEYDOWN):
            if (event.key == pg.K_w):
                vehicle.accelerationStatus = 'accelerate'
            elif (event.key == pg.K_s):
                vehicle.accelerationStatus = 'reverse'
            elif (event.key == pg.K_d):
                vehicle.turningStatus = 'right'
            elif (event.key == pg.K_a):
                vehicle.turningStatus = 'left'
        elif (event.type == pg.KEYUP):
            if (event.key == pg.K_w):
                vehicle.accelerationStatus = 'decelerate'
            elif (event.key == pg.K_s):
                vehicle.accelerationStatus = 'decelerate'
            elif (event.key == pg.K_d):
                vehicle.turningStatus = 'straight'
            elif (event.key == pg.K_a):
                vehicle.turningStatus = 'straight'
    return gameIsRunning


def initializeScreen(tileSize):
    numOfXTiles = int(SCREEN_WIDTH_APPROX / tileSize)
    numOfYTiles = int(SCREEN_HEIGHT_APPROX / tileSize)
    screenWidth = tileSize * numOfXTiles
    screenHeight = tileSize * numOfYTiles
    screen = pg.display.set_mode((screenWidth, screenHeight))
    return numOfXTiles, numOfYTiles, screen


if __name__ == '__main__':
    main()