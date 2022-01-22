# Importing the files needed.
from turtle import Turtle


class Lives:

    def __init__(self):
        self.lives_left = 3
        self.turtles_left = []

    def create_turtles(self, x_cord):
        """This creates turtles on the top portion of the screen."""
        new_life = Turtle("turtle")
        new_life.color("green")
        new_life.setheading(90)
        new_life.penup()
        new_life.goto(x_cord, 275)
        self.turtles_left.append(new_life)

    def display_turtles(self, x_cord):
        """Displays turtles depending on how many lives the user has left."""
        for num in range(self.lives_left):
            self.create_turtles(x_cord)
            x_cord += 40

    def life_lost(self):
        """When the user loses a life, decrement the lives counter."""
        self.lives_left -= 1
        for turtle in self.turtles_left:
            turtle.goto(1000, 1000)
        self.turtles_left.clear()

