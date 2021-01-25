circleSize = 255
color = 0

def setup():
    size(800, 600)
    background(255)

def draw():
    global circleSize, color
    if color <= 255:
        stroke(color)
        circle(400, 300, circleSize)
        circle(200, 150, circleSize)
        color += 1
        if circleSize <= 255:
            circleSize -= 1
        
