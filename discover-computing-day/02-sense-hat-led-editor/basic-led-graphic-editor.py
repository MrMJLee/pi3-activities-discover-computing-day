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

# colours are specified as [R,G,B], R - red, G - green, and B - blue
color={"red":[255,0,0],
        "blue":[0,0,248],
        "green":[0,255,0],
        "yellow":[255,255,0],  
        "cyan":[0,255,255],
        "white":[248,252,248],
        "black":[0,0,0],
        "off":[0,0,0],
        }

white = [200,200,200]
blank = [0,0,0]

'''
- Turn OFF the LED using current `x` and `y`
- If DOWN then add 1 to `y`
- If UP then subtract 1 from `y`
- If RIGHT then add 1 to `x`
- If LEFT then subtract 1 from `x`
- Turn ON the LED using updated `x` and `y`
'''

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
            elif event.key == K_RETURN: # This event occurs when you press the ENTER key
                sense.set_pixel(x,y,255,255,255)
                selected=True
            if not selected:
                if sense.get_pixel(x,y) == blank: 
                    sense.set_pixel(x, y, 200, 200, 200)
            
        if event.type == QUIT:
            running = False
            pygame.quit()
            sense.clear()
            print("BYE")
