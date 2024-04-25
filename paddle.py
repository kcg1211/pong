from turtle import Turtle
STARTING_POS = [(350, 0), (-350, 0)]
UPPER_LIMIT = 240
LOWER_LIMIT = -240


class Paddle:

    def __init__(self):
        self.paddles = []
        self.creating_paddle()

    def creating_paddle(self):
        for starting_pos in STARTING_POS:
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.resizemode("user")
            paddle.shapesize(stretch_len=1, stretch_wid=5)
            paddle.penup()
            paddle.goto(starting_pos)
            self.paddles.append(paddle)

    def paddle1_up(self):
        if self.paddles[0].ycor() != UPPER_LIMIT:
            new_y = self.paddles[0].ycor() + 20
            self.paddles[0].goto(self.paddles[0].xcor(), new_y)

    def paddle1_down(self):
        if self.paddles[0].ycor() != LOWER_LIMIT:
            new_y = self.paddles[0].ycor() - 20
            self.paddles[0].goto(self.paddles[0].xcor(), new_y)

    def paddle2_up(self):
        if self.paddles[1].ycor() != UPPER_LIMIT:
            new_y = self.paddles[1].ycor() + 20
            self.paddles[1].goto(self.paddles[1].xcor(), new_y)

    def paddle2_down(self):
        if self.paddles[1].ycor() != LOWER_LIMIT:
            new_y = self.paddles[1].ycor() - 20
            self.paddles[1].goto(self.paddles[1].xcor(), new_y)


