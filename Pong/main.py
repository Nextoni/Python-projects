from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
score = Scoreboard()

screen.listen()

screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.restart()
        score.l_point()

    if ball.xcor() < -380:
        ball.restart()
        score.r_point()

    time.sleep(ball.ball_speed)

    screen.update()

screen.exitonclick()