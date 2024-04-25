from turtle import Turtle
UPPER_LIMIT = 240
LOWER_LIMIT = -240


class Paddle(Turtle):

    def __init__(self, starting_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(starting_pos)

    def up(self):
        if self.ycor() != UPPER_LIMIT:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() != LOWER_LIMIT:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

