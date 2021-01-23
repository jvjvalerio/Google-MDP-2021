# Global Variables we will be using for our functions
startX = 10
startY = 10
squareSize = 10
counter = 0

# Setup function of the space
def setup():
    size(800, 800)
    background(0)

# Drawing function to create our shape
def draw():
    global counter
    background(0)
    if counter == 1:
        circle(startX + 10, startY + 10, squareSize * 10)
    elif counter == 0:
        square(startX + 10, startY + 10, squareSize * 10)

# Where our shape is placed depending on mouse click   
def mousePressed():
    global startX, startY, counter
    startX = mouseX
    startY = mouseY
    fill(random(255), random(255), random(255))
    if counter == 1:
        counter -= 1
    else:
        counter += 1
    
# Increases in shape size upon keyboard press    
def keyPressed():
    global squareSize
    squareSize *= 2
    
# Decreases in shape size upon mouses wheel usage (An event is a polite interruption of the normal flow of a program)
def mouseWheel(event):
    global squareSize
    squareSize /= 2




    

    
    
    
