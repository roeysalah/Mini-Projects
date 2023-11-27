import bcrypt
from tkinter import *


def validate(password,hashed_password):
    password = bytes(password,encoding = 'utf-8')
    if bcrypt.checkpw(password, hashed_password):
        print("Login Successful")
    else:
        print("Invalid password")

    pass







# implementing password hashing in python
password_input = input("Please Choose a Password:")
password_input= bytes(password_input,encoding = 'utf-8')
hashed = bcrypt.hashpw(password_input,bcrypt.gensalt())


root = Tk()
root.title("Password Validator")
root.geometry("400x400")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="Validate",command=lambda:validate(password_entry.get(),hashed))
button.pack()

root.mainloop()





