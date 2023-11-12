import pygame, sys
from pygame.locals import *
from pygame.math import *

from Config import *
from Player import *
from Plane1 import *

def createRandomPattern():
    n = random.randint(0, 7)

    if n == 0:
        return createPattern00()
    elif n == 1:
        return createPatternA()
    elif n == 2:
        return createPatternB()
    elif n == 3:
        return createPatternC()
    elif n == 4:
        return createPatternD()
    elif n == 5:
        return createPatternE()
    elif n == 6:
        return createPatternF()
    elif n == 7:
        return createPatternG()
    elif n == 8:
        return createPatternH()

def createPattern00():
    return [
        Plane1(Vector2(WIDTH + 128, 400), Vector2(-1, 0)),
        Plane1(Vector2(WIDTH + 128, 700), Vector2(-1.2, 0))
        ]

def createPatternA():
    return [
        Plane1(Vector2(WIDTH + 128, 200), Vector2(-1, 0)),
        Plane1(Vector2(WIDTH + 128, 500), Vector2(-1, 0))
        ]

def createPatternB():
    return [
        Plane1(Vector2(WIDTH + 128, 400), Vector2(-1, 0)),
        Plane1(Vector2(WIDTH + 128, 550), Vector2(-1.2, 0)),
        Plane1(Vector2(WIDTH + 128, 700), Vector2(-1.4, 0)),
        ]

def createPatternC():
    return [
        Plane1(Vector2(WIDTH + 128, 200), Vector2(-2.7, 0)),
        Plane1(Vector2(WIDTH + 128, 350), Vector2(-2.2, 0)),
        Plane1(Vector2(WIDTH + 128, 500), Vector2(-1.7, 0)),
        ]

def createPatternD():
    return [
        Plane1(Vector2(WIDTH + 128, random.randint(200, 400)), Vector2(-7.2, (random.random() * 4.0) - 2.0))
        ]

def createPatternE():
    return [
        Plane1(Vector2(WIDTH + 128, random.randint(200, 400)), Vector2(-7.2, (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 328, random.randint(200, 400)), Vector2(-7.2, (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 528, random.randint(200, 400)), Vector2(-7.2, (random.random() * 4.0) - 2.0))
        ]

def createPatternF():
    return [
        Plane1(Vector2(WIDTH + 428, random.randint(200, 400)), Vector2(-4.2, (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 528, random.randint(200, 400)), Vector2(-5.2, (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 628, random.randint(200, 400)), Vector2(-6.2, (random.random() * 4.0) - 2.0))
        ]

def createPatternG():
    return [
        Plane1(Vector2(WIDTH + 428, random.randint(100, 400)), Vector2(-4.2, (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 528, random.randint(100, 400)), Vector2(-5.2, (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 628, random.randint(100, 400)), Vector2(-6.2, (random.random() * 4.0) - 2.0))
        ]

def createPatternH():
    return [
        Plane1(Vector2(WIDTH + 128, random.randint(100, 500)), Vector2(-(random.random() * 7.0 + 4), (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 128, random.randint(100, 500)), Vector2(-(random.random() * 7.0 + 4), (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 128, random.randint(100, 500)), Vector2(-(random.random() * 7.0 + 4), (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 128, random.randint(100, 500)), Vector2(-(random.random() * 7.0 + 4), (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 128, random.randint(100, 500)), Vector2(-(random.random() * 7.0 + 4), (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 128, random.randint(100, 500)), Vector2(-(random.random() * 7.0 + 4), (random.random() * 4.0) - 2.0)),
        Plane1(Vector2(WIDTH + 128, random.randint(100, 500)), Vector2(-(random.random() * 7.0 + 4), (random.random() * 4.0) - 2.0)),
        ]
