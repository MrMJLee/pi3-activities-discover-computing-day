'''
MASSEY UNIVERSITY

Discover Computing With the Raspberry Pi 3

Activity: 1

Date: 19 July 2016

Description:
    A program that runs on the Raspberry Pi 3 to
    draw the Christmas tree on the Sense HAT led matrix.

Task 2:
    Modify this program to decorate the Christmas tree by changing
    the colours of a selected few pixels on the tree. The decorations
    must be static and not be changing.
    The top two pixels must be coloured white - representing the
    white star at the top of the tree.
    Make use of the functions provided in this program.
    Write your code in the main() function.

'''

from sense_hat import SenseHat
import time
import random as rand

# Initialise the sense HAT
sense = SenseHat()

# Clours can be used to decorate Xmas tree
O = [0, 0, 0]       # no colour
b = [139,69,19]     # brown
d = [0,0,205]       # 
g = [34,139,34]     # green
r = [255,0,0]       # orange
w = [255, 255, 255] # white

# Array/list of colours to draw the Xmas tree on the 8 x 8 LED matrix:
# the undecorated tree
undecorated_tree = [
O, O, O, g, g, O, O, O,
O, O, g, g, g, g, O, O,
O, O, g, g, g, g, O, O,
O, g, g, g, g, g, g, O,
O, g, g, g, g, g, g, O,
g, g, g, g, g, g, g, g,
g, g, g, g, g, g, g, g,
O, O, b, b, b, b, O, O
]

# Function to draw the tree
def drawTree(tree):
    sense.set_pixels(tree)

# Function to pick a random colour
def getRandomColor():
    return rand.randrange(0,256, 5)

# Function to add decoration to tree by changing colour of pixel at (x,y) to a random colour
def addDeco(x,y):
    sense.set_pixel(x, y, getRandomColor(),getRandomColor(),getRandomColor())

# Function to add green pixel to tree by changing colour of pixel at (x,y) 
def addGreenDeco(x,y):
    sense.set_pixel(x,y,34,139,34)

# Function to switch "white star" to top of tree at (3,0) and (4,0)
def onWhiteStar():
    for i in range(3,5):
        sense.set_pixel(i, 0, 255, 255, 255)

# Function to switch off white star decoration
def offWhiteStar():
    for i in range(3,5):
        sense.set_pixel(i, 0, 34,139,34)
        
# Function to remove decorations from the tree by changing colour to green
def removeTreeDecos():
    onWhiteStar()
    addGreenDeco(3,1)
    addGreenDeco(5,1)
    addGreenDeco(2,3)
    addGreenDeco(5,3)
    addGreenDeco(0,5)
    addGreenDeco(2,5)
    addGreenDeco(4,5)
    addGreenDeco(6,5)

# Function to add decorations to the tree by changing colour to random colour
def addTreeDecos():
    onWhiteStar()
    addDeco(3, 1)
    addDeco(5, 1)
    addDeco(2, 3)
    addDeco(5, 3)
    addDeco(0, 5)
    addDeco(2, 5)
    addDeco(4, 5)
    addDeco(6, 5)

# Function specific colours to the tree as decorations
def addTreeDeco():
    onWhiteStar()
    sense.set_pixel(3, 1, 0,0,205)
    sense.set_pixel(5, 1, 0,0,205)
    sense.set_pixel(2, 3, 255,0,0)
    sense.set_pixel(5, 3, 255,0,0)
    sense.set_pixel(0, 5, 0,0,205)
    sense.set_pixel(2, 5, 255,0,0)
    sense.set_pixel(4, 5, 0,0,205)
    sense.set_pixel(6, 5, 255,0,0)
    
# Function to make the star at top of tree to twinkle
def twinkleStar():
    onWhiteStar()
    time.sleep(0.15)
    offWhiteStar()
    time.sleep(0.15)
    onWhiteStar()

def main():

    # Draw undocorated three
    drawTree(undecorated_tree)

    # Wait for 8 sec
    time.sleep(8)

    # Start adding your code for Tasks 2 from here
    
    # End by clearing the LED matrix
    sense.clear()

# Run the program by calling the main() funtion
main()
    
