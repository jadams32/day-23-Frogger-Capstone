from turtle import Turtle


class Lives:

    def __init__(self):
        self.lives_left = 3
        self.turtles_left = []

    def create_turtles(self):
        new_life = Turtle("turtle")
        new_life.color("green")
        new_life.setheading(90)
        new_life.penup()
        new_life.goto(140, 270)
        self.turtles_left.append(new_life)

    def display_turtles(self):
        for num in range(self.lives_left):
            self.create_turtles()

    def life_lost(self):
        self.lives_left -= 1


