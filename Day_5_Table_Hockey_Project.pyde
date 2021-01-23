def setup():
    size(400, 600)
    background(255)
    global speedX, speedY, X, Y, puckRadius, puckInPlay 
    speedX = 0
    speedY = 0
    puckInPlay = False
    X = 100
    Y = 100
    puckRadius = 25
 
# Draws the one sided playing table with slot/goal on the top. No need to modify
# this unless you want to tinker with the look.
def drawTable():
    fill(0, 220, 255)
    circle(200, 0, 150)
    fill(255, 0, 0)
    circle(200, 300, 100)
    fill(255, 255, 255)
    circle(200, 300, 90)
    fill(255, 0, 0)
    circle(200, 300, 10)
    rect(0, 300, 150, 2)
    rect(250, 300, 150, 2)    
 
# Majority of the logic goes in this function.
def draw():
    global speedX, speedY, X, Y, puckRadius, puckInPlay
    background(255)
 
    # Draw background of the playing field. [Don't modify unless you aren't 
    # using a 400x600 playing field.
    drawTable()
 
     # [INSERT CODE] Move puck (hint: use speedX / speedY)
 
    # Initial starting state where the puck follows the mouse above the paddle.
    # Understand how this works so we can utilize this logic in mousePressed()
    # below.
    if not puckInPlay:
        X = mouseX
        Y = 580 - puckRadius
 
    # Draw puck & paddle. Here's the puck & paddle to get you started.
    fill(255, 0, 0)
    ellipse(speedX, speedY, puckRadius * 2, puckRadius * 2)  # Puck
    fill(237, 131, 50)
    rect(mouseX - 50, 580, 100, 20)  # Paddle
 
    # [INSERT CODE] Bounce puck off left and right side of screen
 
    # [INSERT CODE] Detect if puck is off the bottom of the screen
 
    # [INSERT CODE] Detect if puck crosses through the slot up top or needs to bounce off the top
 
def mousePressed():
    global speedX, speedY, puckInPlay
    if mousePressed == LEFT and puckInPlay == False:
        speedX += random(speedX)
        speedY += random(speedY)
        puckInPlay == True
    print("Pressed")  # Just a print debug statement.
    # Logic to launch puck if we have the puck resting on the paddle.
    # If we're not in play, we should set speedX and speedY variables as
    # well as enable puckInPlay.
    if puckInPlay == False:
      # Add code here for getting the puck going. Remove the pass statement as
      # that's just here so the code can run without any statements.
      pass     
