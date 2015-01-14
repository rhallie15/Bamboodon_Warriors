import pygame, sys
from pygame.locals import *
pygame.init()

pygame.display.set_caption('TANK FIGHT: GO!')
background = pygame.image.load('background.png')
tank = pygame.image.load('tank.png')

white = (255,64,64)
w = 1200
h = 600
screen = pygame.display.set_mode((w, h))
screen.fill((white))
tankPosX = 50
tankPoxY = 100

while True: # main game loop
        screen.fill((white))
        screen.blit(background,(0,0))
        screen.blit(tank,(tankPosX,tankPoxY))
        for event in pygame.event.get():
               #if event.type == QUIT:
                # pygame.quit()
                # sys.exit()
                if event.type == KEYDOWN:
                        if event.key == K_a:
                                tankPosX = tankPosX - 10
				elif event.key == K_d:
                                tankPosX = tankPosY + 10
        pygame.display.update()
