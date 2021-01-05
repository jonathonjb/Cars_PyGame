import pygame as pg
import random

from roadTile import RoadTile
from landTile import LandTile

LIKELIHOOD_OF_TURNS = .5
MIN_TILES_BETWEEN_TURNS =10

class MapGenerator:
    def __init__(self, tileSize, numOfTilesX, numOfTilesY):
        self.tileSize = tileSize
        self.numOfTilesX = numOfTilesX
        self.numOfTilesY = numOfTilesY
        screen = pg.display.get_surface()
        screenWidth, screenHeight = screen.get_size()

    def generateMap(self, roadWidth=4):
        # Checks whether each (x, y) coordinates were already added to the map
        tilesAdded = set()

        roadTiles = pg.sprite.Group()
        landTiles = pg.sprite.Group()

        self.generateRoadTiles(roadTiles, roadWidth, tilesAdded)
        self.generateLandTiles(landTiles, tilesAdded)

        return roadTiles, landTiles

    def generateRoadTiles(self, roadTiles, roadWidth, tilesAdded):
        # The ith tile, NOT USING PIXELS. So 3 means 3rd tile of TILE_SIZE
        xTileCurr = 0
        yTileCurr = int(self.numOfTilesY / 2) - (roadWidth / 2)
        xTileChange = 1
        yTileChange = 0
        tilesSinceTurn = 0
        while True:
            for j in range(roadWidth):
                xthTile = xTileCurr + (-yTileChange * j)
                ythTile = yTileCurr + (xTileChange * j)
                x, y = xthTile * self.tileSize, ythTile * self.tileSize
                roadTiles.add(RoadTile(x, y, self.tileSize))
                tilesAdded.add((xthTile, ythTile))
            xTileCurr += xTileChange
            yTileCurr += yTileChange

            tilesSinceTurn += 1
            if (tilesSinceTurn >= MIN_TILES_BETWEEN_TURNS):
                randNum = random.random()
                if (randNum >= 1 - (LIKELIHOOD_OF_TURNS / 2)):
                    # Turning right
                    newXTileChange = -yTileChange
                    newYTileChange = xTileChange

                    xTileChange = newXTileChange
                    yTileChange = newYTileChange

                elif (randNum >= 1 - LIKELIHOOD_OF_TURNS):
                    # Turning left
                    xTileCurr -= (xTileChange * roadWidth)
                    yTileCurr -= (yTileChange * roadWidth)

                    newXTileChange = yTileChange
                    newYTileChange = -xTileChange

                    xTileChange = newXTileChange
                    yTileChange = newYTileChange
                tilesSinceTurn = 0
            if (xTileCurr < 0 or xTileCurr > self.numOfTilesX or yTileCurr < 0 or yTileCurr > self.numOfTilesY):
                break

    def generateLandTiles(self, landTiles, tilesAdded):
        # Creates land on non-road tiles
        for xTile in range(self.numOfTilesX):
            for yTile in range(self.numOfTilesY):
                if ((xTile, yTile) not in tilesAdded):
                    x, y = xTile * self.tileSize, yTile * self.tileSize
                    landTiles.add(LandTile(x, y, self.tileSize))
