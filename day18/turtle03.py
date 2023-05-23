from turtle import Turtle, Screen

T = Turtle()
screen = Screen()
sides = 3
max_sides =10

for times in range(sides, max_sides):
    angle = 360 / times
    for _ in range(times):
        T.forward(100)
        T.right(angle)
        sides += 1


screen.exitonclick()