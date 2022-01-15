import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.make_new_car()
    car_manager.move_cars()

    # if player.distance(car_manager.all_cars) > 20:
    #     car_manager.move_cars()

    if player.ycor() > 300:
        scoreboard.update_score()
        player.reset_player()
        car_manager.update_speed()

    # if player.distance(car_manager.all_cars) < 20:
    #     scoreboard.game_over()


