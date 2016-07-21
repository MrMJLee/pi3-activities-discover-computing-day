import pygame

from pygame.locals import *
from sense_hat import SenseHat
import random # import module random to use the random number generator


pygame.init()
pygame.display.set_mode((320,240))

sense = SenseHat()
sense.clear()

running = True

x = 0
y = 0

sense.set_pixel(x,y,255,255,255)

white = [248,252,248]
blank = [0,0,0]

while running:
    for event in pygame.event.get():
        selected = False
        # Option is to use a few set of colours chosen by pressing down repeatedly the joystick
        r = random.randint(0,255) # using the random number generator
        g = random.randint(0,255)
        b = random.randint(0,255)
        if event.type == KEYDOWN:
            if sense.get_pixel(x,y) == white:
                sense.set_pixel(x,y,0,0,0)
            if event.key == K_DOWN and y <7:
                y = y+1
            elif event.key == K_UP and y>0:
                y = y-1
            elif event.key == K_RIGHT and x < 7:
                x = x+1
            elif event.key == K_LEFT and x > 0:
                x = x-1
            elif event.key == K_RETURN:
                sense.set_pixel(x,y,r,g,b)
                selected = True                
            if not selected:
                if sense.get_pixel(x,y) == blank: 
                    sense.set_pixel(x,y,255,255,255)
        print(event)
        
        if event.type == QUIT:
            running = False
            pygame.quit()
            sense.clear()
            print("BYE")
