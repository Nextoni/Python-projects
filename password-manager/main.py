from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


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

    if website and password and email:
        is_ok = messagebox.askokcancel(title= website, message= f"These are the details entered: \nEmail: {email} "
                                                        f"\n Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as d:
                d.write(f"{website} | {email} | {password}\n")
            input_website.delete(0, END)
            input_pass.delete(0, END)
    else:
        messagebox.showinfo(title= "Oops", message= "Please fill in the boxes!")


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

input_website = Entry(width= 46)
input_website.grid(column= 1, row= 1, columnspan= 2)
input_website.focus()

input_email = Entry(width= 46)
input_email.grid(column= 1, row= 2, columnspan= 2)
input_email.insert(0, "some@gmail.com")

input_pass = Entry(width= 27)
input_pass.grid(column= 1, row= 3)

generate_pass_button = Button(text= "Generate Password", command= generate_password)
generate_pass_button.grid(column= 2, row= 3)

add_button = Button(text= "Add", width= 36, command= save_to_file)
add_button.grid(column= 1, row= 4, columnspan= 2)

window.mainloop()