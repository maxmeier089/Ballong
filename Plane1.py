import pygame, sys
from pygame.locals import *
from pygame.math import *

from Config import *

PLANE_1_WIDTH = 128
PLANE_1_HEIGHT = 64


class Plane1(pygame.sprite.Sprite):

    def __init__(self, pos, vel):
        super().__init__()
        self.pos = pos
        self.vel = vel
        self.rect = Rect(0, 0, 124, 50)
        self.image = pygame.image.load("pics/plane1.png")
        self.drawOffset = Vector2(PLANE_1_WIDTH/2, PLANE_1_HEIGHT/2) 
        self.sound = pygame.mixer.Sound("sound/plane1Motor.wav")
        self.sound.set_volume(0)
        self.sound.play(-1) 


    def move(self):
        
        # add velocity to position
        self.pos += self.vel

        # update bounding box position
        self.rect.center = self.pos

        # compute distance from center within [0, 1]
        distFromCenter = self.pos.x - (WIDTH / 2)
        distFromCenter = abs(distFromCenter)
        distFromCenter = min(WIDTH / 2, distFromCenter)
        distFromCenter = distFromCenter / (WIDTH / 2)

        # make sound louder the closer the plane is to the center
        self.sound.set_volume((1 - distFromCenter) * 0.5)

        # if plane exits screen on the left side, remove it
        if self.pos.x + PLANE_1_WIDTH < 0:
            self.kill()


    def draw(self, displaysurface):

        # draw bounding box
        #pygame.draw.rect(displaysurface, (255, 255, 255), self.rect)

        # draw plane
        displaysurface.blit(self.image, self.pos - self.drawOffset)


    # remove this plane from all groups
    def kill(self):
        pygame.mixer.Sound.stop(self.sound)   
        super().kill()