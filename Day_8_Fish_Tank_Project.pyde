def setup():
    size(600, 600)
    background(0, 0, 255)
    
# Parameters for the drawFish() function
    fishRed = random(255)
    fishGreen = random(255)
    fishBlue = random(255)
    fishWidth = 150
    fishHeight = 75
    drawFish(fishRed, fishGreen, fishBlue, fishWidth, fishHeight)
    
# Parameters for the drawOtherFish() function
    otherfishRed = random(255)
    otherfishGreen = random(255)
    otherfishBlue = random(255)
    otherfishWidth = 100
    otherfishHeight = 25
    drawOtherFish(otherfishRed, otherfishGreen, otherfishBlue, otherfishWidth, otherfishHeight)
    
# Parameters for drawOtherThing() function
    seaweedcolorRed = random(255)
    seaweedcolorGreen = random(255)
    seaweedcolorBlue = random(255)
 
def drawFish(fishRed, fishGreen, fishBlue, fishWidth, fishHeight):
# Code to draw a fish.
# Don't forget to use parameters to make it customizable.
    fill(fishRed, fishGreen, fishBlue)
    ellipse(300, 200, fishWidth, fishHeight)
    fill(fishRed, fishGreen, fishBlue)
    triangle(400, 150, 375, 200, 400, 250)
 
def drawOtherFish(otherfishRed, otherfishGreen, otherfishBlue, otherfishWidth, otherfishHeight):
# Code to draw a different fish.
    fill(otherfishRed, otherfishGreen, otherfishBlue)
    ellipse(500, 400, otherfishWidth, otherfishHeight)
    triangle(575, 350, 550, 400, 575, 450)
    
    
