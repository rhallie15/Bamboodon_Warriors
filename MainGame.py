import pygame, sys, time, random
from pygame.locals import *
from Tank import *
from ETank import*
from pandaAttack import*
#from alienattack import*
from SpriteManager import *
def DrawGame():
    playerTank.drawTank(screen)
    Enemy.drawTank(screen)

    #Displaying Variables on screen
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = BASICFONT.render('Move the Tank using A, W, D, S keys.', 1, BLACK)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, gameHeight - 25)

    #Scoring Variables
    score = 0
    scoreSurf = BASICFONT.render('Score: ' + str(score), 1, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (gameWidth/2, 10)

    #Show Health Variables
    hpSurf = BASICFONT.render('Health: ' + str(playerTank.getHP()), 1, BLACK)
    hpRect = scoreSurf.get_rect()
    hpRect.topleft = (0, 10)

    screen.blit(infoSurf,infoRect)
    screen.blit(scoreSurf,scoreRect)
    screen.blit(hpSurf,hpRect)

    pygame.display.update()

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
       pygame.quit()
       sys.exit()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        pygame.quit()
        sys.exit()
    return keyUpEvents[0].key
 #(^_^)  (=3=)  (~ =3=)~  L(T^T L)
#Game Starts
pygame.init()
pygame.display.set_caption('TANK FIGHT: GO!')
background = pygame.image.load('background.png')

#Set Game Variables
white = (255,64,64)
gameWidth = 1200
gameHeight = 600
FPSCLOCK = pygame.time.Clock()

DARKGRAY = ( 40, 40, 40)
BLACK = ( 0, 0, 0)

screen = pygame.display.set_mode((gameWidth,gameHeight))
screen.fill((white))
groundHeight = 400
playerTank = Tank(0,groundHeight,10)
Enemy = ETank(gameWidth*3/4,groundHeight)
Panda = pandaList(gameWidth*3/4, groundHeight-100)
spManager = SpriteManager(playerTank,Enemy,Panda)


#Here is the Main Loop for running the game
while True:
    screen.blit(background,(0,0))
    checkForKeyPress()
    playerTank.moveByKeyBoard(gameWidth,gameHeight)
    Enemy.moveTank(gameWidth,gameHeight)
    Panda.movePanda(gameWidth,gameHeight)
    #Alien.moveAlien(gameWidth, gameHeight)
    spManager.checkAllCollide()
    Panda.drawPanda(screen)
    #Alien.drawAlien(screen)
    
    pygame.display.set_caption("Health "+str(playerTank.getHP()))
    #screen.blit(playerTank.getImage(),(playerTank.getX(),playerTank.getY()))
    
    #########################Handles Draws for the Game ######################################
    DrawGame()
    pygame.display.update()
