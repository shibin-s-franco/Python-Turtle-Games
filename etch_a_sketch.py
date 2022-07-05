from turtle import Turtle,Screen

jude=Turtle()
screen=Screen()

def move_forward():
    jude.forward(10)

def move_backward():
    jude.backward(10)

def counter_clockwise():
    jude.left(10)

def clockwise():
    jude.right(10)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear_screen)

screen.exitonclick()