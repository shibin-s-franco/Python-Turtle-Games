from turtle import Turtle,Screen
import random

is_race_on=False
all_turtles=[]
colors=["red","orange","yellow","green","blue","purple"]
screen =Screen()
screen.setup(height=400,width=500)
user_bet=screen.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
y_axis=-70
for color in colors:
    turtle_color=color
    color=Turtle(shape="turtle")
    color.color(turtle_color)
    color.penup()
    color.goto(x=-230,y=y_axis)
    y_axis+=30
    all_turtles.append(color)


if user_bet:
    is_race_on=True

while is_race_on:
    for turtl in all_turtles:
        if turtl.xcor()>230:
            winning_color=turtl.pencolor()
            is_race_on=False
            
            if winning_color==user_bet:
                print(f"You have won!.The {winning_color} turtle is the winner ")
            else:
                 print(f"You have lost!.The {winning_color} turtle is the winner ")

        rand_distance=random.randint(0,10)
        turtl.forward(rand_distance)


screen.exitonclick()