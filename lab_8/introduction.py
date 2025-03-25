import pygame
import sys
from pygame.locals import *
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exist()
    pygame.display.update()
    DISPLAYSURF=pygame.display.set_mode((300,300))
    color1=pygame.Color(0,0,0)#balck
    color2=pygame.Color(255,255,255)#white
    color3=pygame.Color(128,128,128)#grey
    color4=pygame.Color(255,0,0)#red
    FPS=pygame.time.Clock()
    FPS.tick(45)
    object1=pygame.React((20,50),(50,100))
    object2=pygame.React((10,10),(100,100))
    print(object1.colliderect(object2))
    
    
    