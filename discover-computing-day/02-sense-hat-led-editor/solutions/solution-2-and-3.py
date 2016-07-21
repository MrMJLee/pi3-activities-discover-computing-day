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

# Use a nice pink colour for the cursor
sense.set_pixel(x, y, cursor)

# The following Dictionary makes up solution to task (2)
color={ "red":[255,0,0],
        "blue":[0,0,248],
        "green":[0,255,0],
        "yellow":[255,255,0],    # as [R,G,B]
        "cyan":[0,255,255],
        "white":[248,252,248],
        "black":[0,0,0],
        "off":[0,0,0],
        "orange":[248, 124, 0]   #[R-7,G-3,B-7]
        }
# End solution to task (2)

while running:    
    for event in pygame.event.get():
        selected=False
        if event.type == KEYDOWN:
            if sense.get_pixel(x,y) == cursor:
                sense.set_pixel(x, y, color['black'])  # Black 0,0,0 means OFF
                
            if event.key == K_DOWN and y < 7:
                y = y + 1
            elif event.key == K_UP and y > 0:
                y = y - 1
            elif event.key == K_RIGHT and x < 7:
                x = x + 1
            elif event.key == K_LEFT and x > 0:
                x = x - 1
            elif event.key == K_RETURN:
                ###########################################################
                # The following IF statements makes up solution to task (3)
                if sense.get_pixel(x,y) == color["white"]:
                    sense.set_pixel(x,y, color['blue'])

                elif sense.get_pixel(x,y) == color["blue"]:
                    sense.set_pixel(x,y, color["orange"])
                    
                elif sense.get_pixel(x,y) == color["orange"]:
                    sense.set_pixel(x,y, color["off"])

                else:
                    sense.set_pixel(x,y,color["white"])

                # End solution to task (3)
                ########################################################### 
                selected=True
            if not selected:
                if sense.get_pixel(x,y) == blank: 
                    sense.set_pixel(x, y, cursor)
            
        if event.type == QUIT:
            running = False
            pygame.quit()
            sense.clear()
            print("BYE")
