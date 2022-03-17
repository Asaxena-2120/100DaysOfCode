import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

carManager = CarManager()
scoreboard = Scoreboard()

# A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
screen.listen()
screen.onkey(fun=player.up,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # car manager creates a car every 0.1 sec
    carManager.create_car()
    carManager.move_cars()

    # Collision between turtle player and one of the car
    for car in carManager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Player turtle hits the top of the wall
    if player.is_at_finish_line():
        player.goto_start_position()
        scoreboard.increase_level()
        carManager.increase_cars_speed()

# pause game screen when game is over
screen.exitonclick()