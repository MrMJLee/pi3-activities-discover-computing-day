'''
Pixel Editor
    Given: Runs to navigate and turn pixel white on clicking
    (1) Modify to make pixel black or off when clicked
    (2) Add the new color, orange, to the color dictionary
    (3) Modify the program so that one navigates and change color though the sequence: white, blue, orange and then black/off when clicked
    (4) Challenge: Given the function hline(x1,y1, w2,y2), modify the program to draw horizontal lines.
    (5) Challenge: Write the function dline() to draw diagonal lines
'''

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

color={"red":[255,0,0],
        "blue":[0,0,255],
        "green":[0,255,0],
        "yellow":[255,255,0],
        "cyan":[0,255,255],
        "white":[255,255,255],
        "black":[0,0,0],
        "off":[0,0,0],
        }

white = [248,252,248]
blank = [0,0,0]
while running:
    for event in pygame.event.get():
        selected = False
        r = random.randint(0,255) # using the random number generator
        g = random.randint(0,255)
        b = random.randint(0,255)
        if event.type == KEYDOWN:
            if sense.get_pixel(x,y) == white:
                sense.set_pixel(x,y,0,0,0)

                setColor(x,y, color('white'))
                
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
                sense.set_pixel(x,y,255,255,255)
        print(event)
        
        if event.type == QUIT:
            running = False
            pygame.quit()
            sense.clear()
            print("BYE")


            
