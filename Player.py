import pygame, sys
from pygame.locals import *
from pygame.math import *

from Config import *

PLAYER_SIZE = 128


class Player(pygame.sprite.Sprite):

    def __init__(self, burnKey):
        super().__init__() 
        self.drawOffset = Vector2(PLAYER_SIZE/2, PLAYER_SIZE/2)
        self.rect = Rect(0, 0, 100, 120)
        self.highestY = HEIGHT - (PLAYER_SIZE / 2) - 120
        self.burnKey = burnKey
        self.ballong = pygame.image.load("pics/ballong.png")
        self.ballongBurner = pygame.image.load("pics/ballongBurner.png")
        self.font = pygame.font.SysFont(None, 24)
        self.burnerSound = pygame.mixer.Sound("sound/burner.wav")
        self.pos = Vector2(640, self.highestY)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.burnerOn = False

        
    def move(self):
        
        pressed_keys = pygame.key.get_pressed()

        # gravity (accelerates downwards)
        self.acc = Vector2(0, 0.07)

        if pressed_keys[self.burnKey]:

            # add burner acceleration (upwards)
            # acceleration becomes smaller with increasing altitude
            self.acc -= Vector2(0, 0.06 + (0.06 * (1-self.altitude)) )

            if not self.burnerOn:
                # burner was not on before
                # turn it on
                self.burnerOn = True

                # turn burner sound on
                pygame.mixer.Sound.play(self.burnerSound, -1)    

        else:

            if self.burnerOn:
                # burner was on before
                # turn if off
                self.burnerOn = False

                # stop sound
                pygame.mixer.Sound.stop(self.burnerSound)

        # add acceleration to velocity
        self.vel += self.acc

        # limit velocity to a maximum value of -1
        self.vel.y = max(self.vel.y, -1)

        # add velocity to position
        self.pos += self.vel

        if self.pos.y > self.highestY:  
            # touched ground
            self.pos.y = self.highestY
            self.vel = Vector2(0,0)

        # compute altitude value within [0, 1.0] (0 lowest, 1 highest)
        self.altitude = min(1.0, (self.highestY - self.pos.y) / 700)
            
        # update bounding box position
        self.rect.center = self.pos

    
    def draw(self, displaysurface):

        # draw bounding box
        #pygame.draw.rect(displaysurface, (255, 255, 255), self.rect)

        # draw balloon
        if self.burnerOn:
            displaysurface.blit(self.ballongBurner, self.pos - self.drawOffset)
        else:
            displaysurface.blit(self.ballong, self.pos - self.drawOffset)

        # write height to upper left corner
        img = self.font.render("Height: " + str(round(self.altitude, 3)), True, (0,0,0))
        displaysurface.blit(img, (20, 20))

        # write speed to upper left corner
        img = self.font.render("Speed: " + str(round(self.vel.y, 3)), True, (0,0,0))
        displaysurface.blit(img, (20, 40))


    # balloon got hit :-(
    def hit(self):
        self.burnerOn = False
        pygame.mixer.Sound.stop(self.burnerSound)


    # reset balloon
    def reset(self):
        self.pos = Vector2(640, self.highestY)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.burnerOn = False

        
 
