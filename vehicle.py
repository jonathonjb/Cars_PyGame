import pygame as pg
import toolkit
import math

MAX_SPEED = 7
REVERSE_MAX_SPEED = 2

ACCELERATION_SPEED_INCREASE = 1
REVERSE_SPEED_INCREASE = 0.5

DECELERATION_DECREASE = 0.95

TURN_SPEED = 2

class Vehicle(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.originalImage, self.rect = toolkit.load_image('car.png', -1)
        self.image = self.originalImage
        self.rect.center = x, y

        self.degrees = 0                        # current degrees of the image (0-359)
        self.speed = 0

        self.accelerationStatus = 'decelerate'  # accelerate, decelerate or reverse
        self.turningStatus = 'straight'         # straight, left, or right


    def update(self):
        if(self.accelerationStatus == 'accelerate'):
            self.accelerate()
        elif(self.accelerationStatus == 'decelerate'):
            self.decelerate()
        elif(self.accelerationStatus == 'reverse'):
            self.reverse()

        if(self.turningStatus == 'left'):
            self.turnLeft()
        elif(self.turningStatus == 'right'):
            self.turnRight()


        # self.image = pg.transform.rotate(self.image, self.degrees)            # Does some really fckn weird shit
        self.image = pg.transform.rotate(self.originalImage, self.degrees)
        xDiff = self.speed * math.cos(-math.radians(self.degrees ))
        yDiff = self.speed * math.sin(-math.radians(self.degrees))
        self.rect.move_ip(xDiff, yDiff)

    def accelerate(self):
        if(self.speed < MAX_SPEED):
            self.speed += ACCELERATION_SPEED_INCREASE

    def reverse(self):
        if (self.speed > -REVERSE_MAX_SPEED):
            self.speed -= REVERSE_SPEED_INCREASE

    def turnLeft(self):
        self.degrees = self.degrees + TURN_SPEED % 360

    def turnRight(self):
        self.degrees = self.degrees - TURN_SPEED % 360

    def decelerate(self):
        self.speed *= DECELERATION_DECREASE