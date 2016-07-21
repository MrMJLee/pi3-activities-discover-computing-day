'''
Discover Computing Day

Task 4
Given the functions hline(x1,y1, w2,y2) and vline(x1,y1, w2,y2),
modify the program to draw horizontal and vertical lines.Description:
    

Core Algorithm Principles from drawing a line:
(1) We know (x,y) at any moment since this is being tracked
(2) When click is detected for 1st time, we store current (x,y) as (x1,y1)
(3) When click is detected for 2nd time, we store current (x,y) as (x2,y2)
(4) Check that (x1,y1) and (x1,y2) are on a horizontal line, i.e., y1==y2.
(5) Colour all pixels from x1 to x2 along y1(if y1==y2).
'''

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

# Your code for the solution for Task 4 comes bellow here 

def hline(x1,y1,x2,y2,color):
    # add code for this function - delete the "pass" statement
    pass
    
    
def vline(x1,y1,x2,y2,color):
    # add code for this function - delete the "pass" statement
     pass

# End solution to task (4)

def swap():
    global x1,y1,x2,y2
    tempX = x1
    tempY = y1    
    x1 = x2
    x2 = tempX
    y1 = y2
    y2 = tempY    

def swapCordinates():
    if (x1>x2 or (y1>y2)):
        swap()

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
Basic Navigation around the LED natrix using JoyStick or Arrow Keys
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

                # Code for Task (4) starts here -
                # Re-use with modification of the code below and add any other statements
                # that may be necessary
                
                sense.set_pixel(x,y,255,255,255)
                selected=True
                
                # End solution to task (4) 
                
            if not selected:
                if sense.get_pixel(x,y) == blank: 
                    sense.set_pixel(x, y, 200, 200, 200)
            
        if event.type == QUIT:
            running = False
            pygame.quit()
            sense.clear()
            print("BYE")
