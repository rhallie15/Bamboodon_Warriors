import pygame, sys , math
from pygame.locals import *
from Tank import *

class ETank(pygame.sprite.Sprite):

    def __init__(self,X,Y):
        self.posX = X
        self.posY = Y
        self.tankw =168
        self.tankh = 71
        self.reloadTime = 30
        self.tankList =[Tank(X,Y,self.reloadTime)]
        self.tankImages = [pygame.image.load('tanks/p2tank-str0.png'),pygame.image.load('tanks/p2tank-med0.png'),pygame.image.load('tanks/p2tank-high0.png')]
        self.attackImages = [pygame.image.load('tanks/p2tank-str1.png'),pygame.image.load('tanks/p2tank-med1.png'),pygame.image.load('tanks/p2tank-high1.png')]
        self.tankList[0].setImages(self.tankImages,self.attackImages)
        self.clock = 0
        self.moveX = 0
        self.moveY = 3
        self.limit = 5
        self.spawnTime = 60


    def getX(self):
        return self.posX

    def getList(self):
        return self.tankList
        
    def getY(self):
        return self.posY
    
    def moveTank(self,maxX,maxY):
        self.clock += 1
        if self.clock > self.spawnTime and len(self.tankList) < self.limit :
            self.clock = 0
            self.tankList.append(Tank(self.posX,self.posY,self.reloadTime))
            self.tankList[len(self.tankList)-1].setImages(self.tankImages,self.attackImages)  
        
        
        for i in range(0,len(self.tankList)-1):
            self.tankList[i].moveAI(maxX,maxY,self.moveX,self.moveY)


    def getCount(self):
        return len(self.tankList)-1
        
    def destroyTank(self):
        for i in range(0, len(self.tankList)-1):
            if self.tankList[i].getHP() <= 0:
                self.tankList.pop(i) 

    def drawTank(self,screen):
        for i in range(0,len(self.tankList)-1):
            screen.blit(self.tankList[i].getImage(),(self.tankList[i].getX(),self.tankList[i].getY()))  
        pygame.display.update()    

