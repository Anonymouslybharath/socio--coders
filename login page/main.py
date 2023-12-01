from tkinter import *
from tkinter import messagebox
import os
import pyttsx3

engine = pyttsx3.init()

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x300")
    register_screen.configure(bg="lightblue")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="lightblue", fg="navy", width=50, font=("Calibri", 15)).pack()
    Label(register_screen, text="").pack()
    username_label = Label(register_screen, text="Username * ", font=("Calibri", 12), bg="lightblue")
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(register_screen, text="Password * ", font=("Calibri", 12), bg="lightblue")
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=20, height=1, bg="navy", fg="white", font=("Calibri", 12), command=register_user).pack()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x300")
    login_screen.configure(bg="lightgreen")
    Label(login_screen, text="Please enter details below to login", bg="lightgreen", fg="darkgreen", width=50, font=("Calibri", 15)).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ", font=("Calibri", 12), bg="lightgreen").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ", font=("Calibri", 12), bg="lightgreen").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=20, height=1, bg="darkgreen", fg="white", font=("Calibri", 12), command=login_verify).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo("Success", "Registration Success")

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
            engine.say("Login successful")
            engine.runAndWait()
        else:
            password_not_recognised()
    else:
        user_not_found()

def login_success():
    messagebox.showinfo("Success", "Login successful")

def password_not_recognised():
    messagebox.showerror("Error", "Password incorrect")

def user_not_found():
    messagebox.showerror("Error", "User not found")

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("700x450")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="1", width="20", command=login, bg="navy", fg="white", font=("Calibri", 12)).pack()
    Label(text="").pack()
    Button(text="Register", height="1", width="20", command=register, bg="navy", fg="white", font=("Calibri", 12)).pack()

    main_screen.mainloop()

main_account_screen()
