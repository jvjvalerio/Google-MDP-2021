size(1000, 750)
#background(255, 255, 255)
background(0, 0, 0)

#SUN
fill(255, 255, 0)
strokeWeight(4)
circle(0, 0, 500)

#TRANSLATION
translate(375, 375)

#MERCURY
noFill()
stroke(0, 0, 0)
fill(190, 190, 190)
ellipse(-150, -200, 50, 50)

#VENUS
fill(165, 42, 42)
ellipse(-135, -80, 70, 70)

#EARTH
fill(11, 182, 205)
ellipse(50, -200, 90, 90)

#MARS
fill(255, 0, 0)
ellipse(55, -50, 60, 60)

#JUPTIER
fill(255, 153, 0)
ellipse(-10, 100, 120, 120)

#SATURN
fill(255, 204, 0)
ellipse(300, 0, 120, 120)

#SATURNS_RING
stroke(105, 105, 105)
noFill()
ellipse(300, 10, 300, 50)

#COVER_URANUS'S RING
strokeWeight(8)
stroke(255, 204, 0)
noFill()
bezier(247, -13, 300, -16, 300, -16, 353, -13)

#URANUS
stroke(0, 0, 0)
fill(13, 152, 186)
ellipse(200, 200, 100, 100)

#URANUS'S_RING
strokeWeight(4)
stroke(105, 105, 105)
noFill()
ellipse(200, 200, 300, 50)

#COVER_URANUS'S RING
strokeWeight(8)
stroke(13, 152, 186)
noFill()
bezier(164, 176, 200, 174, 200, 174, 236, 176)

#NEPTUNE
stroke(0, 0, 0)
fill(0, 35, 102)
ellipse(400, 150, 90, 90)

#PLUTO
stroke (0, 0, 0)
fill(150, 75, 0)
ellipse(450, 300, 25, 25)
