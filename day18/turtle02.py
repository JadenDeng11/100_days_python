from turtle import Turtle, Screen

T = Turtle()
screen = Screen()

for _ in range(10):
    T.forward(10)
    T.penup()
    T.forward(10)
    T.pendown()

screen.exitonclick()