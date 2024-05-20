from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pone game")
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")

screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()
