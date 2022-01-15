# For day 23's capstone project I build a replica of the frogger game using the turtle module.
# The main goal of this project was to capitalize on the oop skills I have learned to create the game from scratch.
# Feel free to look around my code, and give the game a try!

# Importing all necessary modules.
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from lives import Lives

# Here the screen is initialized, size set, and animations turned off
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Frogger Replica")
screen.bgcolor("grey")
screen.tracer(0)

# Initialize the instances from each of the classes from other files.
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
lives_left = Lives()
lives_left.create_turtles()

# Listen to keystrokes from the up arrow on the keyboard and call the player move function when pressed.
screen.listen()
screen.onkey(fun=player.move, key="Up")

# While loop variable, used to determine when to exit loop
game_is_on = True
lives = 3

# Main Game loop
while game_is_on:

    # This causes the loop to pause, and then update the screen. Giving a break so the user does not have too
    # many cars to try and cross.
    time.sleep(0.1)
    screen.update()
    lives_left.display_turtles()

    # Here we create the group of cars and start moving them across the screen.
    car_manager.make_new_car()
    car_manager.move_cars()

    # Detecting collision with any of the cars on the screen
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            lives -= 1
            player.reset_player()
            if lives <= 0:
                scoreboard.game_over()
                game_is_on = False

    # Detecting if the user has crossed the road successfully, then level up the game.
    if player.ycor() > 300:
        scoreboard.update_score()
        player.reset_player()
        car_manager.update_speed()

# This exits the pop-up screen when the user clicks
screen.exitonclick()
