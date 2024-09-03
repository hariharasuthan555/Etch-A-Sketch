from turtle import Turtle,Screen


screen=Screen()
tim=Turtle()
tim.shape("turtle")
tim.color("green")
screen.listen()


def move_forward():
    tim.forward(100)


def move_backward():
    tim.backward(100)


def turn_clockwise():
    tim.setheading(tim.heading() - 20)


def turn_anticlockwise():
    tim.setheading(tim.heading() + 20)


def clear_turtle():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=turn_clockwise)
screen.onkey(key="a",fun=turn_anticlockwise)
screen.onkey(key="c",fun=clear_turtle)


screen.exitonclick()