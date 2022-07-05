from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(height=600,width=800)
# screen.screensize(canvheight=600,canvwidth=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle=Paddle((360,0))
l_paddle=Paddle((-360,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(key="Up",fun=r_paddle.up)
screen.onkeypress(key="Down",fun=r_paddle.down)
screen.onkeypress(key="w",fun=l_paddle.up)
screen.onkeypress(key="s",fun=l_paddle.down)

is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update() 
    ball.move_ball()
    

    # collion on wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    # collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()

    # right paddle miss
    if ball.xcor()>380:
        scoreboard.l_point()
        ball.reset_ball()
    
    # left paddle miss
    if ball.xcor()<-380:
        scoreboard.r_point()
        ball.reset_ball()


screen.exitonclick()