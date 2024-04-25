from turtle import Turtle, Screen
from paddle2 import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()

ball = Ball()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect when paddle misses the ball and send new ball to opponent
    if ball.xcor() > 450:
        ball.reset_pos()
        scoreboard.update_l_scoreboard()

    if ball.xcor() < -450:
        ball.reset_pos()
        scoreboard.update_r_scoreboard()

        # ball.moving_randomiser()






    print(ball.xcor())

screen.exitonclick()