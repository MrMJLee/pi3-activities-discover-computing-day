'''
#######################################################################
Discover Computing Day

Task 4
Given the functions hline(x1,y1, w2,y2) and vline(x1,y1, w2,y2),
modify the program to draw horizontal and vertical lines.

Core Algorithm Principles:
(1) We know (x,y) at any moment since this is being tracked
(2) When click is detected for 1st time, we store current (x,y) as (x1,y1)
(3) When click is detected for 2nd time, we store current (x,y) as (x2,y2)
(4) Check that (x1,y1) and (x1,y2) are on a horizontal line, i.e., y1==y2.
(5) Colour all pixels from x1 to x2 along y1(if y1==y2).
###########################################################################
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
cursor = [200,0,200]
blank = [0,0,0]

sense.set_pixel(x, y, cursor)

# The following code makes up solution to task (4)
count = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0

def hline(x1,y1,x2,y2,color):
    if (y1 == y2):
        for x in range(x1,x2+1):
            sense.set_pixel(x,y1,color)
            
def vline(x1,y1,x2,y2,color):
    if (x1==x2):
        for y in range(y1,y2+1):
            sense.set_pixel(x1,y,color)

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
        
# End solution to task (4)
        
color={"red":[255,0,0],
        "blue":[0,0,248],
        "green":[0,255,0],
        "yellow":[255,255,0],  # as [R,G,B]
        "cyan":[0,255,255],
        "white":[248,252,248],
        "black":[0,0,0],
        "off":[0,0,0],
        }



while running:    
    for event in pygame.event.get():
        selected=False
        if event.type == KEYDOWN:
            
            if sense.get_pixel(x,y) == cursor:
                sense.set_pixel(x, y, blank)  # Black 0,0,0 means OFF
                
            if event.key == K_DOWN and y < 7:
                y = y + 1
            elif event.key == K_UP and y > 0:
                y = y - 1
            elif event.key == K_RIGHT and x < 7:
                x = x + 1
            elif event.key == K_LEFT and x > 0:
                x = x - 1
            elif event.key == K_RETURN:

                ##########################################################
                # The following IF statements make up solution to task (4)    
                if count == 1:
                    x2 = x
                    y2 = y
                else:
                    x1 = x
                    y1 = y
                sense.set_pixel(x,y,color["white"])
                count +=1
                selected=True
                
            if count ==2:
                swapCordinates()
                hline(x1,y1,x2,y2,color["red"])
                vline(x1,y1,x2,y2,color["green"])
                count = 0
            # End solution to task (4)   
            ##############################################################
            
            if not selected:
                if sense.get_pixel(x,y) == blank: 
                    sense.set_pixel(x, y, cursor)
           

        if event.type == QUIT:
            running = False
            pygame.quit()
            sense.clear()
            print("BYE")



        
