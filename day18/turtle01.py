from turtle import Turtle, Screen

DENGYIKANG = Turtle()

screen = Screen()

DENGYIKANG.shape("turtle")
for _ in range(4):
    DENGYIKANG.forward(100)
    DENGYIKANG.left(90)

screen.exitonclick()