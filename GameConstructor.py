import pygame
from pygame import *
"""
 _____                        _____                 _                   _             
|  __ \                      /  __ \               | |                 | |            
| |  \/ __ _ _ __ ___   ___  | /  \/ ___  _ __  ___| |_ _ __ _   _  ___| |_ ___  _ __ 
| | __ / _` | '_ ` _ \ / _ \ | |    / _ \| '_ \/ __| __| '__| | | |/ __| __/ _ \| '__|
| |_\ \ (_| | | | | | |  __/ | \__/\ (_) | | | \__ \ |_| |  | |_| | (__| || (_) | |   
 \____/\__,_|_| |_| |_|\___|  \____/\___/|_| |_|___/\__|_|   \__,_|\___|\__\___/|_|  
V0.01
______         _                       _____ 
| ___ \       | |                     |_   _|
| |_/ /_   _  | |    _   _  ___ __ _    | |  
| ___ \ | | | | |   | | | |/ __/ _` |   | |  
| |_/ / |_| | | |___| |_| | (_| (_| |   | |_ 
\____/ \__, | \_____/\__,_|\___\__,_|   \_(_)
        __/ |                                
       |___/     

"""
scrollx = 0.0
scrolly = 0.0
screen = ''
bgcolor = (255,255,255)

def UpdateScreen():
    pygame.display.update()

def ClearScreen():
    global screen, bgcolor
    screen.fill(bgcolor)

def BackgroundColor(Red, Green, Blue):
    global screen, bgcolor
    screen.fill((Red,Green,Blue))
    bgcolor = (Red,Green,Blue)

def QuitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def setupPygame(colorRGB,sizeX,sizeY,title):
    global screen
    pygame.init()
    screen = pygame.display.set_mode((sizeX, sizeY))
    screen.fill(colorRGB)
    pygame.display.set_caption(str(title))
    pygame.display.update()



class Sprite():
    def __init__(self,imagePath,imageWidth,imageHeight,hazardous,collidable,hitbox_X,hitbox_Y,hitbox_origin_X,hitbox_origin_Y,origin_point_X,origin_point_y):
        self.width = imageWidth
        self.height = imageHeight
        self.image = pygame.image.load(imagePath)
        self.hazard = hazardous
        self.collidable = collidable
        self.hitX = hitbox_X
        self.hitY = hitbox_Y
        self.hitOriginX = hitbox_origin_X
        self.hitOriginY = hitbox_origin_Y
        self.originX = origin_point_X
        self.originY = origin_point_y
    def moveX(self,starting_X,moving_to_X,time_taking,animation):
        self.originX = starting_X
        self.movX = moving_to_X
        self.movetime = time_taking
        self.anim = animation
    def moveY(self,starting_Y,moving_to_Y,time_taking,animation):
        self.originY = starting_Y
        self.movY = moving_to_Y
        self.movetime = time_taking
        self.anim = animation
    def draw(self,position_X,position_Y,centerBased):
        global screen
        if centerBased:
            screen.blit(self.image,(position_X-(self.width/2),position_Y-(self.height/2)))
        elif not centerBased:
            screen.blit(self.image,(position_X-self.originX,position_Y-self.originY))



class DetailSprite():
    def __init__(self,imagePath,imageWidth,imageHeight,origin_point_X,origin_point_y):
        self.width = imageWidth
        self.height = imageHeight
        self.originX = origin_point_X
        self.originY = origin_point_y
        self.image = pygame.image.load(imagePath)
    def moveX(self,starting_X,moving_to_X,time_taking,animation):
        self.originX = starting_X
        self.movX = moving_to_X
        self.movetime = time_taking
        self.anim = animation
    def moveY(self,starting_Y,moving_to_Y,time_taking,animation):
        self.originY = starting_Y
        self.movY = moving_to_Y
        self.movetime = time_taking
        self.anim = animation
    def draw(self,position_X,position_Y,centerBased):
        global screen
        if centerBased:
            screen.blit(self.image,(position_X-(self.width/2),position_Y-(self.height/2)))
        elif not centerBased:
            screen.blit(self.image,(position_X-self.originX,position_Y-self.originY))
