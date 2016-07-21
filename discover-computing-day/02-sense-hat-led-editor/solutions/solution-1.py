import pygame

from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((320, 240))

sense = SenseHat()
sense.clear()

running = True

x = 0
y = 0
sense.set_pixel(x, y, 200, 200, 200)

white = [200,200,200]
blank = [0,0,0]

while running:    
    for event in pygame.event.get():
        selected=False
        if event.type == KEYDOWN:
            if sense.get_pixel(x,y) == white:
                sense.set_pixel(x, y, 0, 0, 0)  # Black 0,0,0 means OFF
            if event.key == K_DOWN and y < 7:
                y = y + 1
            elif event.key == K_UP and y > 0:
                y = y - 1
            elif event.key == K_RIGHT and x < 7:
                x = x + 1
            elif event.key == K_LEFT and x > 0:
                x = x - 1
            elif event.key == K_RETURN:
                # The following IF statement make up solution to task (1)
                if sense.get_pixel(x,y) != blank:
                    sense.set_pixel(x,y,0,0,0)
                else:
                    sense.set_pixel(x,y,255,255,255)
                # End solution to Task (1)
                selected=True
            if not selected:
                if sense.get_pixel(x,y) == blank: 
                    sense.set_pixel(x, y, 200, 200, 200)
            
        if event.type == QUIT:
            running = False
            pygame.quit()
            sense.clear()
            print("BYE")
