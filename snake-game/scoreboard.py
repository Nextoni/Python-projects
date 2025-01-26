from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 260)
        self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))

    def scored(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font= ('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font= ('Arial', 24, 'normal'))