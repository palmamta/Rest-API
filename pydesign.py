import turtle 

length = int(input('Enter length: '))
sides = int(input('Enter sides: '))

for i in range(0,sides):
    turtle.forward(length)
    turtle.left(360/sides)
    for i in range(0,sides):
        turtle.forward(length)
        turtle.right(360/sides)

turtle.exitonclick()