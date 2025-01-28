from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.new_y = random.randint(-250, 250)
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.goto(320, self.new_y)
        self.color(random.choice(COLORS))
        self.setheading(180)

    def car_move(self, level):
        if level == 1:
            new_x = self.xcor() - STARTING_MOVE_DISTANCE
        else:
            new_x = self.xcor() - MOVE_INCREMENT * (level - 1)

        self.goto(new_x, self.new_y)

