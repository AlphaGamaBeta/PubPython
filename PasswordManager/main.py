# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import tkinter
from tkinter import  messagebox
def genpass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = 5
    nr_symbols = 5
    nr_numbers = 5
    list1 = []
    list2 = []
    list3 = []
    password = []
    choice_list = []
    total = nr_letters + nr_numbers + nr_symbols
    for n in range(0, total):
        choice_list.append(n)
    for n1 in range(0, nr_letters):
        s = letters[random.randint(0, 27)]
        list1.append(s)
    for n2 in range(0, nr_symbols):
        s = symbols[random.randint(0, 8)]
        list2.append(s)
    for n3 in range(0, nr_numbers):
        s = numbers[random.randint(0, 9)]
        list3.append(s)
    all_list = []
    all_list.extend(list1)
    all_list.extend(list2)
    all_list.extend(list3)
    # randoming them
    for n in range(0, total):
        c = random.choice(choice_list)
        m = random.choice(all_list)
        password.insert(c, m)
        choice_list.remove(c)
        all_list.remove(m)
    final = ""
    for n in password:
        final += n
    website_Password_input.insert(0, final)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    usern = website_Username_input.get()
    em = website_Email_input.get()
    web = website_label_input.get()
    if usern == "" and em == "" and web == "":
        return
    if usern == "1" and em == "1" and web == "1" and website_Password_input.get() == "1":
        with open("Data.data", mode='r') as data:
            s = data.read().splitlines()
            screen.destroy()
            newscreen = tkinter.Tk()
            newscreen.minsize(width=600, height=500)
            newscreen.title("Your Saves")
            m = 1
            for n in s:
                value = tkinter.Label(text=f"{n}\n")
                value.grid(row=m, column=0)
                m += 1
            return
    website_Username_input.delete(0,'end')
    website_Email_input.delete(0,'end')
    website_label_input.delete(0,'end')
    website_Password_input.delete(0,'end')
    messagebox.showinfo(title="Done",message="It has been saved")


    with open("Data.data", mode='a') as data:
        data.write(f"Website:{web} |Username:{usern} |Email:{em} |Password:{website_Password_input.get()}\n")


# ---------------------------- UI SETUP ------------------------------- #


screen = tkinter.Tk()
screen.title("Password Manager")
screen.config(padx=40, pady=42)
logo = tkinter.Canvas(width=250, height=200)
img = tkinter.PhotoImage(file="logo.png")
logo.create_image(100, 100, image=img)
logo.grid(row=0, column=1)
website_label = tkinter.Label(text="Website")
website_Username = tkinter.Label(text="Username")
website_Email = tkinter.Label(text="Email")
website_Password = tkinter.Label(text="Password")
website_label.grid(row=1, column=0)
website_Username.grid(row=2, column=0)
website_Email.grid(row=3, column=0)
website_Password.grid(row=4, column=0)
GPassword = tkinter.Button(text="Generate Password", command=genpass)
GPassword.place(x=200, y=295)
addb = tkinter.Button(text="Add", width=10, command=add)
addb.place(x=40, y=295)
website_label_input = tkinter.Entry(width=30)
website_label_input.focus()
website_Username_input = tkinter.Entry(width=30)
website_Email_input = tkinter.Entry(width=30)
website_Password_input = tkinter.Entry(width=30)
website_label_input.grid(row=1, column=1)
website_Username_input.grid(row=2, column=1)
website_Email_input.grid(row=3, column=1)
website_Password_input.grid(row=4, column=1)

screen.mainloop()
