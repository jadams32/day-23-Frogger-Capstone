from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("black")
        self.hideturtle()
        self.penup()
        self.goto(-400, 400)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
