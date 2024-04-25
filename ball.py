from turtle import Turtle
import random

STARTING_POSITION = (0, 0)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.x_move = 6
        self.y_move = 6

    def moving_randomiser(self):
        self.x_move = random.randint(4, 7)
        self.y_move = random.randint(4, 7)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(STARTING_POSITION)
        self.bounce_x()