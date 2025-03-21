from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for letter in range(randint(8, 10))]

    password_list += [choice(symbols) for symbol in range(randint(2, 4))]

    password_list += [choice(numbers) for num in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    input_pass.delete(0, END)
    input_pass.insert(0, f"{password}")
    pyperclip.copy(password)


def save_to_file():

    website = input_website.get()
    email = input_email.get()
    password = input_pass.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title= "Oops", message= "Please fill in the boxes!")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent= 4)

        finally:
            input_website.delete(0, END)
            input_pass.delete(0, END)

def search():
    website = input_website.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title= "No data!", text= "No Data File Found.")

    else:
        if website in data:
            messagebox.showinfo(title= "Found a match", message= f"Website: {website}\n"
                                                                 f"Email: {data[website]["email"]}\n"
                                                                 f"Password: {data[website]["password"]}")
        else:
            messagebox.showinfo(title= "No match", message= f"No details for the {website} exists.")


window = Tk()
window.title("Password manager")
window.config(padx= 20, pady= 20)

canvas = Canvas(width= 200, height= 200)
img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= img)
canvas.grid(column= 1, row= 0)

website_label = Label(text= "Website:")
website_label.grid(column= 0, row= 1)

email_label = Label(text= "Email/Username:")
email_label.grid(column= 0, row= 2)

pass_label = Label(text= "Password:")
pass_label.grid(column= 0, row= 3)

input_website = Entry(width= 27)
input_website.grid(column= 1, row= 1)
input_website.focus()

input_email = Entry(width= 27)
input_email.grid(column= 1, row= 2)
input_email.insert(0, "some@gmail.com")

input_pass = Entry(width= 27)
input_pass.grid(column= 1, row= 3)

generate_pass_button = Button(text= "Generate Password", command= generate_password)
generate_pass_button.grid(column= 2, row= 3)

add_button = Button(text= "Add", width= 36, command= save_to_file)
add_button.grid(column= 1, row= 4, columnspan= 2)

search_button = Button(text= "Search", width= 14, command= search)
search_button.grid(column= 2, row= 1)

window.mainloop()