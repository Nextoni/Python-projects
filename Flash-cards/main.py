from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient= "records")

else:
    to_learn = data.to_dict(orient= "records")

data_to_learn = pandas.DataFrame()



def correct():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index = False)

    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, fill= "black", text= "French")
    canvas.itemconfig(word_text, fill= "black", text= current_card["French"])
    canvas.itemconfig(card_background, image= card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, fill= "white", text= "English")
    canvas.itemconfig(word_text, fill= "white", text= current_card["English"])
    canvas.itemconfig(card_background, image= card_back)




window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file= "images/card_back.png")
canvas = Canvas(width= 800, height= 526, highlightthickness= 0)
card_background = canvas.create_image(400, 263, image= card_front)
canvas.config(background= BACKGROUND_COLOR)
title_text = canvas.create_text(400, 150, text= "", fill= "black", font= ("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text= "", fill= "black", font= ("Arial", 60, "bold"))
canvas.grid(column= 0, row= 0, columnspan= 2)

img_right = PhotoImage(file= "images/right.png")
button_right = Button(image= img_right, highlightthickness= 0, command= correct)
button_right.grid(column= 0, row= 1)

img_wrong = PhotoImage(file= "images/wrong.png")
button_wrong = Button(image= img_wrong, highlightthickness= 0, command= next_card)
button_wrong.grid(column= 1, row= 1)

next_card()

window.mainloop()