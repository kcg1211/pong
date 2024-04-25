from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write_scoreboard()

    def write_scoreboard(self):
        self.setposition((-175, 180))
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.setposition((175, 180))
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_l_scoreboard(self):
        self.clear()
        self.l_score += 1
        self.write_scoreboard()

    def update_r_scoreboard(self):
        self.clear()
        self.r_score += 1
        self.write_scoreboard()
