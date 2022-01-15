# Class that controls the scoreboard.
from turtle import Turtle

# Class variables used
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("black")
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.pendown()
        self.write_score()

    def write_score(self):
        """Writes the score to the screen."""
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        """Updates the score by one."""
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        """Displays game over on screen."""
        self.penup()
        self.goto(0, 0)
        self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)
