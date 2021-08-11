import turtle

house = turtle.Turtle()

house.begin_fill()
house.color("blue")

for i in range(4):
 house.forward(100)
 house.left(90)

house.left(90)
house.forward(100)
house.end_fill()


#roof
house.begin_fill()
house.color("orange")

house.right(30)
house.forward(100)
house.right(120)
house.forward(100)

house.end_fill()

turtle.done()