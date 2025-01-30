import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
writer = Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

score = 0
guessed_states = []
while guessed_states != states:
    answer_state = screen.textinput(title= f"{score}/50 States guessed", prompt= "What's another state's name?")
    answer_state = answer_state.title()
    location = data[data["state"] == answer_state]

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states and location["state"].item() not in guessed_states:

        writer.goto(float(location["x"].item()), float(location["y"].item()))
        writer.write(answer_state)
        guessed_states.append(location["state"].item())
        score += 1




