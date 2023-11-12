import pygame, sys, random
from pygame.locals import *
from pygame.math import *


class Explosion(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.particles = pygame.sprite.Group()

        # add ballong particle
        self.particles.add(BallongParticle(pos, Vector2(0,1.9)))

        # add explosion particles
        n = 7
        while n > 0:
            newPos = pos + ((random.random()-0.5)*95,(random.random()-0.5)*95)
            vel = ((random.random()-0.5)*0.5,(random.random()-0.3)*0.7)
            self.particles.add(ExplosionParticle(newPos, vel))
            n -= 1
        

    def move(self):
        if self.particles.__len__() == 0:
            self.kill()

        for p in self.particles:
            p.move()


    def draw(self, displaysurface):
        for p in self.particles:
            p.draw(displaysurface)
    

class ExplosionParticle(pygame.sprite.Sprite):

    def __init__(self, pos, vel):
        super().__init__()
        self.pos = pos
        self.vel = vel
        self.size = 155
        self.alpha = 255
        self.rotate = 0
        self.rotateStep = (random.random()-0.5)*0.2
        self.particleImage = pygame.image.load("pics/explosion.png") 

    def move(self):
        self.pos += self.vel
        self.particleImage.set_alpha(self.alpha)
        self.alpha -= 1
        if self.size < 256:
            self.size += 3
        if self.alpha == 0:
            self.kill()

    def draw(self, displaysurface):
        transformedImage = pygame.transform.rotate(self.particleImage, self.rotate)
        self.rotate = (self.rotate + self.rotateStep) % 365
        transformedImage = pygame.transform.scale(transformedImage, (self.size, self.size))
        displaysurface.blit(transformedImage, self.pos - (self.size/2, self.size/2))
        


class BallongParticle(pygame.sprite.Sprite):

    def __init__(self, pos, vel):
        super().__init__()
        self.pos = pos
        self.vel = vel
        self.alpha = 255
        self.rotate = 0
        self.rotateStep = 0.2
        self.particleImage = pygame.image.load("pics/ballongCrash.png") 

    def move(self):
        self.pos += self.vel
        self.particleImage.set_alpha(self.alpha)
        self.alpha -= 0.9
        if self.alpha == 0:
            self.kill()

    def draw(self, displaysurface):
        transformedImage = pygame.transform.rotate(self.particleImage, self.rotate)
        self.rotate = (self.rotate + self.rotateStep) % 365
        displaysurface.blit(transformedImage, self.pos - (transformedImage.get_width()/2, transformedImage.get_height()/2))
        