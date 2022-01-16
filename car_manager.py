# Class that controls the cars on the screen.
from turtle import Turtle
import random

# Class variables used
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):

        self.all_cars = []
        self.move_speed = .07

    def make_new_car(self):
        """Creates an individual car and stores it in a group(list)."""
        random_chance = random.randint(1, 4)
        y_locations_left = [-240, -160, -80, 0, 80, 160, 240]
        random_y_left = random.choice(y_locations_left)
        if random_chance == 2:
            new = Turtle("square")
            new.turtlesize(stretch_len=2)
            new.color(random.choice(COLORS))
            new.penup()
            new.setheading(180)
            new.goto(300, random_y_left)
            self.all_cars.append(new)

        y_locations_right = [-200, -120, -40, 40, 120, 200]
        random_y_right = random.choice(y_locations_right)

        if random_chance == 2:
            new = Turtle("square")
            new.turtlesize(stretch_len=2)
            new.color(random.choice(COLORS))
            new.penup()
            new.goto(-300, random_y_right)
            self.all_cars.append(new)

    def move_cars(self):
        """Moves all cars on the screen forward."""
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def update_speed(self):
        """Speeds up the cars when the user scores a point."""
        self.move_speed *= .5

