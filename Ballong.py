import pygame, sys
from pygame.locals import *
from pygame.math import *

from Config import *
from Player import *
from Plane1 import *
from Explosion import *
from Pattern import *


pygame.init()
 
clock = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ballong")


P1 = Player(K_SPACE)


background = pygame.image.load("pics/background.png")

# store all sprites here
allSprites = pygame.sprite.Group()
allSprites.add(P1)

# store enemies here
enemies = pygame.sprite.Group()

# fonts
bigFont = pygame.font.SysFont(None, 148)
font = pygame.font.SysFont(None, 48)

explosionSound = pygame.mixer.Sound("sound/explosion.wav")


# indicates if the game is in progress
running = True


def collision():
    global running
    
    P1.hit()

    pygame.mixer.Sound.play(explosionSound) 

    # game over
    running = False

    # remove all sprites
    for sprite in allSprites:
        sprite.kill()

    allSprites.add(Explosion(P1.pos))

 
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   	

    # draw background
    displaysurface.blit(background, (0, 0))


    if not running:
        # display game over text
        img = bigFont.render("GAME OVER", True, (255, 255, 255))
        displaysurface.blit(img, (640-(img.get_width() / 2), 440))

        img = font.render("press ENTER to play again", True, (255, 255, 255))
        displaysurface.blit(img, (640-(img.get_width() / 2), 540))

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_RETURN]:
            # restart
            P1.reset()
            allSprites.add(P1)
            running = True

    
    # randomly add enemy *patterns*
    if running and (enemies.sprites().__len__() == 0 or enemies.sprites()[-1].pos.x < 555):
        enemyPattern = createRandomPattern()
        enemies.add(enemyPattern)
        allSprites.add(enemyPattern)
        

    # move and draw all sprites
    for entity in allSprites:
        entity.move()
        entity.draw(displaysurface)


    # check for collision
    for enemy in enemies:

        if P1.rect.colliderect(enemy.rect):

            #collision!
            collision()

    if P1.crash:
        collision()
        P1.crash = False
  
 
    pygame.display.update()
    
    clock.tick(FPS)