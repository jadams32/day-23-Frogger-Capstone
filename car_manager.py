from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def make_new_car(self):
        random_chance = random.randint(1, 6)
        random_y = random.randint(-250, 260)
        if random_chance == 2:
            new = Turtle("square")
            new.turtlesize(stretch_len=2)
            new.color(random.choice(COLORS))
            new.penup()
            new.setheading(180)
            new.goto(300, random_y)
            self.all_cars.append(new)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def update_speed(self):
        self.move_speed += MOVE_INCREMENT

