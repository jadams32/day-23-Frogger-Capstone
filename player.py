# Class that controls the turtles movements
from turtle import Turtle

# Class variables Used
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.reset_player()

    def move(self):
        """Moves the turtle forward."""
        self.forward(20)

    def down(self):
        self.back(20)

    def reset_player(self):
        """Resets the turtle to the starting position."""
        self.goto(STARTING_POSITION)
