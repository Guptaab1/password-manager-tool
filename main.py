import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

COLOR = "#CFFDE1"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
               'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_number + password_symbol + password_letters
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    print(f"Your password is: {password}")
    print(len(password))


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password_1 = password_entry.get()

    if len(website) == 0 or len(password_1) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password_1} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password_1}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=150, pady=150, bg=COLOR)
canvas = tkinter.Canvas(width=200, height=200, bg=COLOR, highlightthickness=0)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(85, 85, image=logo_image)
canvas.grid(column=1, row=0)

# Website_text
website_text = tkinter.Label(text="Website:", bg=COLOR, highlightthickness=0, font=("Mute", 10, "bold"))
website_text.grid(column=0, row=1)

# Website_entry
website_entry = tkinter.Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
website_entry.get()

# Email_text
email_text = tkinter.Label(text="Email/Username:", bg=COLOR, highlightthickness=0, font=("Mute", 10, "bold"))
email_text.grid(column=0, row=2)

# Email_entry
email_entry = tkinter.Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "abhishek@email.com")
email_entry.get()

# Password_text
password_text = tkinter.Label(text="Password:", bg=COLOR, highlightthickness=0, font=("Mute", 10, "bold"))
password_text.grid(column=0, row=3)

# Password_entry
password_entry = tkinter.Entry(width=18)
password_entry.grid(column=1, row=3)

# Generate password Button
generate_password_button = tkinter.Button(text="Generate Password", bg=COLOR, highlightthickness=0, font=("Mute", 10, "bold"), command=generate_password)
generate_password_button.grid(column=2, row=3)

# Add Button
add_button = tkinter.Button(text="Add", bg=COLOR, highlightthickness=0, font=("Mute", 10, "bold"), width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
