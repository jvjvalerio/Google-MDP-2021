# Initialized Variables
lineWidth = 6
small_lineWidth = False
med_lineWidth = False
large_lineWidth = False
start = False
red_color = False
green_color = False
black_color = False

# Setup for project space
def setup():
    size(1000, 1000)
    background(255)

# Draw function
def draw():
# Red Color Choice
    fill(255, 0, 0)
    rect(900, 900, 50, 50)
# Green Color Choice
    fill(0, 255, 0)
    rect(900, 825, 50, 50)
# Black Color Choice
    fill(0)
    rect(900, 750, 50, 50)
#Sample Line 6
    stroke(0)
    strokeWeight(6)
    line(900, 700, 950, 700)
# Sample Line 8
    stroke(0)
    strokeWeight(8)
    line(900, 650, 950, 650)
# Sample Line 10
    stroke(0)
    strokeWeight(10)
    line(900, 600, 950, 600)
# Modifications to lineWidth and Color
    if (start == True):
        strokeWeight(lineWidth)
        line(pmouseX, pmouseY, mouseX, mouseY)
    if (start == True and red_color == True):
        stroke(255, 0, 0)
        strokeWeight(lineWidth)
        line(pmouseX, pmouseY, mouseX, mouseY)
    if (start == True and green_color == True):
        stroke(0, 255, 0)
        strokeWeight(lineWidth)
        line(pmouseX, pmouseY, mouseX, mouseY)
    if (start == True and black_color == True):
        stroke(0)
        strokeWeight(lineWidth)
        line(pmouseX, pmouseY, mouseX, mouseY)
    if (start == True and small_lineWidth == True):
        strokeWeight(lineWidth)
    if (start == True and med_lineWidth == True):
        strokeWeight(lineWidth + 6)
    if (start == True and large_lineWidth == True):
        strokeWeight(lineWidth + 8)
        
# Start/Stop Drawing
def keyPressed():
    global start, refresh
    if ((key == 'a') or (key == 'A')):
        start = True
    if ((key == 's') or (key == 'S')):
        start = False

# Color and lineWidth Picker
def mousePressed():
    global start, red_color, green_color, black_color, lineWidth
    
# Color Picker
    if start == False and mouseButton == LEFT and 900 <= mouseX <= 950 and 750 <= mouseY <= 825:
        red_color = False
        green_color = False
        black_color = True
    if start == False and mouseButton == LEFT and 900 <= mouseX <= 950 and 825 < mouseY <= 900:
        green_color = True
        red_color = False
        black_color = False
    if start == False and mouseButton == LEFT and 900 <= mouseX <= 950 and 900 < mouseY <= 950:
        black_color = False
        red_color = True
        green_color = False
        
# LineWidth picker
    if start == False and mouseButton == LEFT and 900 <= mouseX <= 950 and 700 <= mouseY < 750:
        small_lineWidth = True
        med_lineWidth = False
        large_lineWidth = False
        lineWidth = 6
    if start == False and mouseButton == LEFT and 900 <= mouseX <= 950 and 650 <= mouseY < 700:
        small_lineWidth = False
        med_lineWidth = True
        large_lineWidth = False
        lineWidth = 6
        lineWidth += 2
    if start == False and mouseButton == LEFT and 900 <= mouseX <= 950 and 600 <= mouseY < 650:
        small_lineWidth = False
        med_lineWidth = False
        large_lineWidth = True
        lineWidth = 6
        lineWidth += 4

        

        
    
    
    

            
        



    
