import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

car_spawn_rate = 0
cars = []

game_is_on = True
while game_is_on:
    car_spawn_rate += 1

    if car_spawn_rate == 6:
        car = CarManager()
        cars.append(car)
        car_spawn_rate = 0

    for car in cars:
        car.car_move(level.level)
        if player.distance(car.pos()) < 30:
            level.game_over()
            game_is_on = False

    if player.ycor() >= 290:
        level.level_complete()
        player.player_reset()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()