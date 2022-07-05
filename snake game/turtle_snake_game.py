from turtle import Screen
from food import Food
from scoreboard import ScoreBoard 
from snake import Snake 
import time
 
screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snak=Snake()
scoreboard=ScoreBoard()
food=Food()
screen.listen()
screen.onkey(fun=snak.up,key="Up")
screen.onkey(fun=snak.down,key="Down")
screen.onkey(fun=snak.right,key="Right")
screen.onkey(fun=snak.left,key="Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snak.move()

    #Collision with food
    if snak.head.distance(food)<15:
        food.refresh()
        snak.extend_snake()
        scoreboard.change_score()

    # Collision with wall
    if snak.head.xcor()>280 or snak.head.xcor()<-280 or snak.head.ycor()>280 or snak.head.ycor()<-280:
        snak.reset()
        scoreboard.reset()

    # Collision with tail
    for segment in snak.segments[2:]:
        if snak.head.distance(segment)<10:
            snak.reset()
            scoreboard.reset()







screen.exitonclick()