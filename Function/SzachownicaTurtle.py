import turtle

"""
setheading
0   - east
90  - north
180 - west
270 - south
"""
turtle.speed(0)

def move_up(steps=60):
    turtle.setheading(90)
    turtle.forward(steps)

def move_right(steps=60):
    turtle.setheading(0)
    turtle.forward(steps)

move_up()
move_right()

turtle.setheading(270)
turtle.forward(60)


turtle.setheading(180)
turtle.forward(60)


for i in range(20):
    move_up(60)
    move_right(60)
    turtle.setheading(270)
    turtle.forward(60)
    turtle.setheading(0)
    turtle.forward(1)


turtle.done()