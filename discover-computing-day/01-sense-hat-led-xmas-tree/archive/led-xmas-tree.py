'''
Discover Computing Day Activity

Given: A program that draws an undecorated green Christmas tree on the Sense HAT led matrix.
    This is the starting program for all tasks in this activity.
    Before starting any task, save it as a separate file as instructed to avoid overwriting this program.

Tasks:
(1) Run this program and study to understand the code.
(2) Decorate the Christmas tree by changing the colours of a few pixels on the tree - the top two pixels must be coloured white.
    Start with the program whole filename is "led-xmas-tree1.py";
(3) Starting again from the original program, modify the program to make the decorations randomly change their colours every half a second.
    This simulates Christmas tree lights. Start with the program whose filename is "led-xmas-tree2.py".
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
    time.sleep(8)

    # Start adding your code for Tasks 1 or 2 from here
    
    # Clear the LED matrix
    sense.clear()

# Run the program by calling the main() funtion
main()
    
