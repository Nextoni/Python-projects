from tkinter import *

window = Tk()

window.title("Miles to Km Converter")
window.minsize(width= 7, height= 7)
window.config(padx= 30, pady= 30)

input = Entry(width= 10)
input.grid(column= 1, row= 0)

label1 = Label(text= "Miles")
label1.grid(column= 2, row= 0)

label2 = Label(text= "is equal to ")
label2.grid(column= 0, row= 1)

label3 = Label(text= "0")
label3.grid(column= 1, row= 1)

label4 = Label(text= "Kilometers")
label4.grid(column= 2, row= 1)

def button_clicked():
    kilometers = float(input.get()) * 1.609344
    label3.config(text = f"{round(kilometers, 2)}")

button = Button(text= "Calculate", command= button_clicked)
button.grid(column= 1, row= 2)

window.mainloop()