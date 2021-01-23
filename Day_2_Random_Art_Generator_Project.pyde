def setup ():
    size(800, 800)
    background(0, 0, 0)
    
def draw():
    delay(100)
    fill(random(255), 255, random(255))
    ellipse(random(800), random(800), 80, 30)
    circle(random(800), random(800), random(80))
    triangle(random(800.0),random(800.0),random(800.0),random(800.0),random(800.0),random(800.0))

    
