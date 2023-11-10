import pygame, sys
from pygame.locals import *
from pygame.math import *

from Config import *
from Player import Player
from Plane1 import Plane1


pygame.init()
 
clock = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ballong")

#pygame.mixer.music.load("music/Kristallo.wav")
#pygame.mixer.music.play(-1)


P1 = Player(K_SPACE)


background = pygame.image.load("pics/background.png")

# store all sprites here
allSprites = pygame.sprite.Group()
allSprites.add(P1)

# store enemies here
enemies = pygame.sprite.Group()


bigFont = pygame.font.SysFont(None, 148)
font = pygame.font.SysFont(None, 48)


# indicates if the game is in progress
running = True

 
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


    # randomly add enemies
    if random.randint(0, 200) == 0 and running:
        
        yPos = random.randint(55, 555)

        tooClose = False

        # check if another plane has a similar height already
        for enemy in enemies:
            if abs(enemy.pos.x - WIDTH) < 150 and abs(enemy.pos.y - yPos) < 100:
                tooClose = True
                break

        #if not tooClose:
            # add enemy plane
            enemy = Plane1(yPos)
            enemies.add(enemy)
            allSprites.add(enemy)


    # move and draw all sprites
    for entity in allSprites:
        entity.move()
        entity.draw(displaysurface)


    # check for collision
    for enemy in enemies:

        if P1.rect.colliderect(enemy.rect):

            #collision!
            P1.hit()

            # game over
            running = False

            # remove all sprites
            for sprite in allSprites:
                sprite.kill()
  
 
    pygame.display.update()
    
    clock.tick(FPS)